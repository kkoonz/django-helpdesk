from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Answer(models.Model):
    title = models.CharField(max_length=500)
    text = MarkdownxField()
    #text = models.TextField()
    photo = models.FileField(blank=True)
    attach = models.FileField(blank=True)
    is_display = models.BooleanField(default=0)
    view_cnt = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.text)