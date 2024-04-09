from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager # 태그 추가
# Create your models here.
# id, title, slug, description, content, create_df, modify_df

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField(verbose_name='SLUG', unique=True, allow_unicode=True, help_text="one word for title alias.")
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True) # 태그 추가

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts' # 만들어지는 테이블 이름을 지정할 수 있다.
        ordering = ('-modify_dt',) # 최신내용을 먼저 출력하도록 - 붙임

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt() # 날짜, 시간 필드와 관련되어서 자동으로 생성되는 함수를 사용

    def get_next(self):
        return self.get_next_by_modify_dt() # get_previous_by_modify_dt와 마찬가지
'''
# 댓글 관련 테이블
# Question, Choice 구조와 같다.
class Comment(models.Model):
    # user
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    # date ...
'''