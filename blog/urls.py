from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # http://localhost:8000/blog/
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('tag/<int:blog_tag_pk>', views.blogs_with_tag, name="blogs_with_tag"),
    path('date/<int:year>/<int:month>', views.blogs_with_date, name="blogs_with_date"),
    path('share', views.blog_share, name='share_list'),
    path('timer', views.blog_timer, name='timer_list'),
]