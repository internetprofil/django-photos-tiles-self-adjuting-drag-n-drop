from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline
from .models import Story, PhotosStory


class Photos(SortableTabularInline):
    fields = ('template', 'imageField1', 'imageField2', 'imageField3')
    model = PhotosStory
    extra = 1

class StoryAdmin(SortableAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (Photos,)

admin.site.register(Story, StoryAdmin)
