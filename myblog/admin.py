from django.contrib import admin
from .models import Article, Category, Tag, ExampleModel

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ExampleModel)

