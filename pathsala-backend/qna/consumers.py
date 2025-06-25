import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Comment, Vote
from courses.models import Lessons
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.video_id = self.scope["url_route"]["kwargs"]["video_id"]
        self.room_group_name = f"comment_video_{self.video_id}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json.get("type")
        
        if message_type == "comment":
            comment = text_data_json.get("comment")
            video_id = text_data_json.get("video_id")
            parent_id = text_data_json.get("parent_id", None)
            user_id = self.scope["user"].id
            
            # Save comment to database
            saved_comment = await self.save_comment(user_id, video_id, comment, parent_id)
            
            # Send comment to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "comment_message",
                    "comment": comment,
                    "user_id": user_id,
                    "comment_id": saved_comment.id,
                    "video_id": video_id,
                    "parent_id": parent_id,
                    "username": self.scope["user"].username,
                }
            )
        
        elif message_type == "vote":
            comment_id = text_data_json.get("comment_id")
            vote_value = text_data_json.get("vote_value")  # 1 for upvote, -1 for downvote
            user_id = self.scope["user"].id
            
            # Toggle vote in database
            vote_count = await self.toggle_vote(user_id, comment_id, vote_value)
            
            # Send vote update to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "vote_message",
                    "comment_id": comment_id,
                    "vote_count": vote_count,
                }
            )

    async def comment_message(self, event):
        # Send comment to WebSocket
        await self.send(text_data=json.dumps({
            "type": "comment",
            "comment": event["comment"],
            "user_id": event["user_id"],
            "comment_id": event["comment_id"],
            "video_id": event["video_id"],
            "parent_id": event["parent_id"],
            "username": event["username"],
        }))

    async def vote_message(self, event):
        # Send vote update to WebSocket
        await self.send(text_data=json.dumps({
            "type": "vote",
            "comment_id": event["comment_id"],
            "vote_count": event["vote_count"],
        }))

    @database_sync_to_async
    def save_comment(self, user_id, video_id, content, parent_id=None):
        user = User.objects.get(id=user_id)
        video = Lessons.objects.get(id=video_id)
        parent = None
        if parent_id:
            parent = Comment.objects.get(id=parent_id)
        
        comment = Comment.objects.create(
            user=user,
            video=video,
            content=content,
            parent=parent
        )
        return comment

    @database_sync_to_async
    def toggle_vote(self, user_id, comment_id, vote_value):
        user = User.objects.get(id=user_id)
        comment = Comment.objects.get(id=comment_id)
        
        # Check if user already voted on this comment
        existing_vote = Vote.objects.filter(user=user, comment=comment).first()
        
        if existing_vote:
            if existing_vote.vote_value == vote_value:
                # Same vote, remove it
                existing_vote.delete()
            else:
                # Different vote, update it
                existing_vote.vote_value = vote_value
                existing_vote.save()
        else:
            # New vote
            Vote.objects.create(user=user, comment=comment, vote_value=vote_value)
        
        # Calculate total vote count
        total_votes = comment.votes.aggregate(
            total=models.Sum('vote_value')
        )['total'] or 0
        
        return total_votes 