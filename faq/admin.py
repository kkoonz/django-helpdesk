from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Answer

admin.site.register(Answer, MarkdownxModelAdmin)