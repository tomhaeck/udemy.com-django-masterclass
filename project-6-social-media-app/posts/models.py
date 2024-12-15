from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/%y/%m/%d')
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateField(auto_now=True)

    liked_by = models.ManyToManyField(User,
                                      related_name='posts_liked',
                                      blank=True)

    def __str__(self):
        return self.title

    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*arg, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')

    body = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now=True)

    posted_by = models.CharField(max_length=200)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.body
