from typing import DefaultDict
from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
 #  models.
   
@python_2_unicode_compatible
class Blogpost(models.Model):
        STATUS_CHOICES = (       
            ('draft', 'Draft'),        
            ('published', 'Published'),    
)    
        title = models.CharField(max_length=250)    
        slug = models.SlugField(max_length=250,      
                       unique_for_date='publish')
        author = models.ForeignKey(User,
                                on_delete=models.CASCADE)
        body = models.TextField() 
        publish = models.DateTimeField(default=timezone.now)    
        published_date = models.DateTimeField(auto_now_add=True)    
        updated = models.DateTimeField(auto_now=True)   
        status = models.CharField(max_length=10,                               
                           choices=STATUS_CHOICES,                              
                             default='draft')
        thumbnail = models.ImageField()
        tags = TaggableManager()

        def get_absolute_url(self):
            return reverse("Blogpost:post_detail", kwargs={'pk':self.id})
 

        class Meta:
                ordering = ('-publish',)


        def __str__(self):        
            return self.title



class Comment(models.Model):    
    post = models.ForeignKey(Blogpost, 
                                on_delete=models.CASCADE,
                                 related_name='comments')    
    name = models.CharField(max_length=80)    
    email = models.EmailField()    
    body = models.TextField()    
    created = models.DateTimeField(auto_now_add=True)    
    updated = models.DateTimeField(auto_now=True)    
    active = models.BooleanField(default=True)



    class Meta:        
        ordering = ('created',)



    def __str__(self):        
        return 'Comment by {} on {}'.format(self.name, self.post) 


class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)



