from django.contrib import admin
from core.models import User, Post, Like, Follows


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('author', 'title', 'text_body', 'url', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}


# class UserAdmin(admin.ModelAdmin):
#     model = User
#     list_display = (User)

admin.site.register(Post, PostAdmin)
