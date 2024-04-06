from django.contrib import admin
from bookmarkapp.models import Bookmark
# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

'''
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

admin.site.register(Bookmark, BookmrkAdmin)

데코레이터를 사용하지 않고 다음과 같이 admin 사이트에 테이블을 반영할 수 있다.
'''