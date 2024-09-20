from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='blog_home'),
    path('about/',views.about,name='blog_about'),
    path('contact/',views.contact,name='blog_contact'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail,name='blog_post'),
    path('post/<int:post_id>/comment',views.post_comment,name='post_comment'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    
