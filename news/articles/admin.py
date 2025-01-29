from django.contrib import admin
from .models import Article, Comment


# inlines which displays foreign key relationships in a visual way.
# We can use two main inline views used
# - Tubarline: all model fields appear on one line
# - StackedInline: each field has its own line


# Basically we used the 'Comment' model, and used StackedInline
# , then we created another class where we put those comments or the class 'CommentInline',
# "in a line", 'inlines', of the article
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
