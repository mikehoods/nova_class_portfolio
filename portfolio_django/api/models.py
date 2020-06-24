from django.db import models
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=400)
    deployment = models.CharField(max_length=400)
    image = models.CharField(max_length=400)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '%s %s %s %s' % (self.title, self.code, self.deployment, self.image)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        return super(Project, self).save(*args, **kwargs)


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.title, self.body)
