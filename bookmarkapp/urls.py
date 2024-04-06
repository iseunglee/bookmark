from django.urls import path
from . import views

app_name = 'bookmark'

urlpatterns = [
    path("", views.BookmarkLV.as_view(), name='index'),

    path("<int:pk>/", views.BookmarkDV.as_view(), name='detail')
]

'''
클래스형 뷰가 간단한 경우는 views.py에 코딩할 필요없이 URLconf에서 뷰 및 뷰 처리에 필요한 파라미터를 모두 지정할 수 있다.
하지만 향후 확장성이나 임포트 관계를 단순하게 유지하기 위해 views.py에 작성하는 것이 좋다

즉, 아래와 같이 코딩할 수 있다.
urlpatterns = [
    path('', ListView.as_view(model=Bookmark), name='index')
    path('<int:pk>/', DetailView.as_view(model=Bookmark), name='detail')
]

다음과 같이 코드를 작성하면 views.py에 코드를 작성할 필요없이 urls.py에서 처리가 가능하다.
'''