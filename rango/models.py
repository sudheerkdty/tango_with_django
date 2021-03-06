from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    """docstring for Category"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def  __unicode__(self):
        return self.name

class Page(models.Model):
    """docstring for Page"""

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def  __unicode__(self):
        return self.title
