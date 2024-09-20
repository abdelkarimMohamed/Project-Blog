from django.contrib import admin
from .models import HomePage, AboutPage, ContactPage,Post,Comment
# Register your models here.

admin.site.register(HomePage)
admin.site.register(AboutPage)
admin.site.register(ContactPage)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','created_at','slug','status']
    list_filter=['publish','created_at','author','status']
    search_fields=['title','body']
    raw_id_fields=['author']
    prepopulated_fields={'slug':('title', )}
    date_hierarchy='publish'
    ordering=['status','publish']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','created_at','active','body']
    list_filter=['active','created_at','active']
    search_fields=['name','body']
