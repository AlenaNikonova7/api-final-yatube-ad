from django.contrib import admin
from .models import Post, Comment, Follow, Group

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    search_fields = ('text', 'author__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'post', 'created')
    list_filter = ('author', 'post', 'created')
    search_fields = ('text', 'author__username')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {'slug': ('title',)}