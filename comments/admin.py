from django.contrib import admin
from .forms import CommentForm
from .models import Comment

admin.site.register(Comment)
