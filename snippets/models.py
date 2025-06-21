from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Tag(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, related_name="tags", on_delete=models.CASCADE)
    
class Snippet(models.Model):
    LANDUAGE_CHOICES = [
       ('python', 'Python'),
        ('js', 'JavaScript'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('java', 'Java'),
        ('c', 'C'),
        ('cpp', 'C++'),
    ]
    id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField(Tag)
    share_uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    title = models.CharField(max_length=100, blank=True, default="UNNAMED")
    language = models.CharField(max_length=30, choices=LANDUAGE_CHOICES)
    code = models.TextField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    user = models.ForeignKey(User, related_name="snippets", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class HighlightedSnippet(models.Model):
    snippet = models.OneToOneField(Snippet, on_delete=models.CASCADE, related_name="highlighted")
    highlighted_code = models.TextField()
