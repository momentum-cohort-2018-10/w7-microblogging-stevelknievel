from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text_body = models.CharField(max_length=280)
    url = models.URLField(max_length=400, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=250)
    # favorited_by = models.ManyToManyField(User, through='Favorite', related_name='favorite_posts')
    # liked_by = models.ManyToManyField(User, through='Like', related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follows(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='is_following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='followed_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            'following',
            'followed',
            )


class Like(models.Model):
    liked = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






# class Post_from_users():


# class Post_from_followed_users():



# """CLINTON EXAMPLE FROM SNOWDAY VIDEO LECTURE"""

# class User (go into settings and change AUTH_USER_MODEL, then register in apps/admin.py) 

# class User(AbstractUser):
#     pass

# class Book(models.Model):
#     owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="books")
#     title = models.CharField(max_length=255)
#     authors = models.CharField(max_length=255, null=True, blank=True
#     status = models.ChoiceField(
#         max_length = 20,
#         choices=(
#             ("want_to_read", "Want to Read"),
#             ("reading", "Currently Reading"),
#             ("read", "Have Read"),
#         )
#     )
#     create_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_add=True)

# class BookNote(models.Model):
#     book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="notes")
#     body = models.TextField()
#     page_number = models.PositiveIntegerField(null=True, blank=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_add=True)
