from pyexpat import model
from django.db import models
from django.forms import CharField
from pyparsing import Char

class posts(models.posts):
    
    title = models.CharField(max_length= 150)
    content = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add= True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.titolo

