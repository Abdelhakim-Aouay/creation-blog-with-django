from django.contrib import admin

from .models import Post, Category, UserProfile, Comments

admin.site.register(Post),
admin.site.register(Category),
admin.site.register(UserProfile),
admin.site.register(Comments),
