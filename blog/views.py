from django.shortcuts import render
from django.views.generic import ListView, DeleteView, ArchiveIndexView,  YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView, TemplateView
from .models import Post
from django.conf import settings # disqus 내용을 위한 라이브러리 추가
# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 디폴트로 생성되는 이름을 사용하지 않고, 사용할 이름을 정하겠다
    context_object_name = 'posts'
    paginate_by = 1 # 페이지 생성을 위한 변수, 2개씩 1페이지 구성

'''
제네릭 뷰를 사용하지 않을 시
def dummy_post(request):
    objects = Post.objects.all()
    context = {
        'posts' : objects
    }
    return render(request, 'blog/post_all.html', context)
PostLV는 위와 같은 내용을 담고있다. 즉 제네릭뷰를 사용하냐 안하냐의 차이
'''

class PostDV(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    # disqus 관련 내용 추가
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context

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

# 태그관련 뷰 클래스 추가
class TagCloudTV(TemplateView):
    template_name="taggit/taggit_cloud.html"

class TaggedObjectLV(ListView):
    template_name='taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
    '''
    context = {
        post_list : ... ,
        tagname : ... , 
        # context 변수에 기본적으로 추가되는 post_list를 제외하고 다른 내용을 추가하기 위해 상단의 get_context_date()메서드를 통해 추가한다.
    }
    '''

# 폼 활용 - 뷰 재활용
from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form:any):
        # 검색어 확인
        searchWord = form.cleaned_data['search_word']
        # Q를 통해 검색하고
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()
        # 결과를 담아
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        # 페이지에 전달
        return render(self.request, self.template_name, context)