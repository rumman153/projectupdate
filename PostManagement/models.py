from django.db import models
from ManageVisitor.models import Visitor


from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    RATING_OPTIONS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rating = models.CharField(max_length=10, choices = RATING_OPTIONS, default='4')
    comment = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.rating



class Post(models.Model):
    Post_title = models.CharField(max_length=200)
    Post_location = models.CharField(max_length=50)
    Post_catagory = models.CharField(max_length=50,
                                     choices=(('Regions','Regions'),
                                              ('Popular Places', 'Popular Places'),
                                              ('Blog', 'Blog')),
                                     default='Blog')
    Post_tags = models.CharField(max_length=200)
    Post_image= models.ImageField(null='true')
    Post_description = models.TextField(max_length=100000)

    User = models.ForeignKey(User, on_delete=models.CASCADE,null='true')
    #reviews = models.ManyToManyField(Review)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reviews = None

    def __str__(self):
        return self.Post_title

# operationalerror no such table
# python manage.py migrate --run-syncdb

