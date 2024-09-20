from django.db import models
from PIL import Image
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.
def validate_image_dimensions(image):
    min_width=1000
    min_height=500
    img = Image.open(image)
    width, height = img.size

    if width < min_width or height < min_height: 
                raise ValidationError(f"The image_dimensions must be at least {min_width}px and {min_height}px tall.")
    
class PageBase(models.Model):
    
    title=models.CharField(max_length=150)
    sub_title=models.CharField(max_length=250)
    bg_image=models.ImageField(upload_to='images/%y/%m/%d',validators=[validate_image_dimensions])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
          abstract=True

    def __str__(self):

        return self.title
    
class HomePage(PageBase):
    
    pass

class AboutPage(PageBase):
      
    description=models.TextField(null=True,blank=True)
    
class ContactPage(PageBase):
    description=models.TextField(null=True,blank=True)

class Post(models.Model):
     
    class Status(models.TextChoices):
          DRAFT=('DF','Draft')
          PUBLISHED=('PB','Published')

    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    bg_image=models.ImageField(upload_to="images/%y/%m/%d/background_images")
    post_image=models.ImageField(upload_to="images/%y/%m/%d/post_images")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

    class Meta:
        ordering=['-publish']
        indexes=[
             models.Index(fields=['publish'])
        ]
    def __str__(self):
          return self.title
    

    def get_absolute_url(self):
         
         return reverse('blog_post',args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
         ])
    
class Comment(models.Model):
     
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name=models.CharField(max_length=150)
    email=models.EmailField()
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=False)

    class Meta:
        ordering=['-created_at']
        indexes=[
             models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return self.name