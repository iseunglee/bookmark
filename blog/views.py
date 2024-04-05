from django.shortcuts import render
from django.views.generic import ListView, DeleteView, ArchiveIndexView,  YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from .models import Post

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 디폴트로 생성되는 이름을 사용하지 않고, 사용할 이름을 정하겠다
    context_object_name = 'posts'
    paginate_by = 1 # 페이지 생성을 위한 변수, 2개씩 1페이지 구성

class PostDV(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'

#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive.html"

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    template_name = "blog/post_archive_year.html"

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_month.html"

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_day.html"

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_day.html"