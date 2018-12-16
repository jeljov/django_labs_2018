from django.contrib import admin

from .models import Audiobook, Review

admin.site.register(Audiobook)
admin.site.register(Review)