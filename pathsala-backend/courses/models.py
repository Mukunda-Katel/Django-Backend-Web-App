from django.db import models

# Create your models here.
class Categorys(models.Model):
    category_title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return f"category-{self.category_title}"
class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categorys,on_delete=models.CASCADE)
    duration = models.CharField(max_length=100,default=2)

    def __str__(self):
        return self.title

class Weeks(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='weeks')
    number = models.PositiveIntegerField() 
    title = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('course', 'number')
        ordering = ['number']

    def __str__(self):
        return f"Week {self.number} - {self.title or ''}"

class Videos(models.Model):
    videos_url = models.URLField()
class Lessons(models.Model):
    week = models.ForeignKey(Weeks, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # video_url = models.URLField()
    video = models.ManyToManyField(Videos,related_name='videos')
    order = models.PositiveIntegerField()  

    class Meta:
        unique_together = ('week', 'order')
        ordering = ['order']

    def __str__(self):
        return self.title

