from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmarkapp.models import Bookmark
# Create your views here.

class BookmarkLV(ListView):
    model = Bookmark # ListView를 상속받았기 때문에 template과 context 이름을 따로 지정해주지 않아도 저장되어 있다.
    # template_name = "bookmarkapp/bookmark_list.html" # appname/model_name_list.html
    # context_object_name = "object_list" # object_list

class BookmarkDV(DetailView):
    model = Bookmark
    # template_name = "bookmarkapp/bookmark_detail.html" # appname/model_name_list.html
    # context_object_name = "object" # object