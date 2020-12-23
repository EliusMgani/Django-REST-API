from django.contrib import admin
from django.urls import path
from snippets import views, viewsapi_view, viewsAPIView, viewsMixin, viewsGeneric
from rest_framework.urlpatterns import format_suffix_patterns


# APIendpoints
urlpatterns = [
    path('list1', views.list1, name="List1"),
    path('detail1/<int:pk>/', views.detail1, name="Detail1"),

    path('list2', viewsapi_view.list2, name="List2"),
    path('detail2/<int:pk>/', viewsapi_view.detail2, name="Detail2"),

    path('list3', viewsAPIView.List3.as_view(), name="List3"),
    path('detail3/<int:pk>/', viewsAPIView.Detail3.as_view(), name="Detail3"),

    path('list4', viewsMixin.List4.as_view(), name="List4"),
    path('detail4/<int:pk>/', viewsMixin.Detail4.as_view(), name="Detail4"),

    path('list5', viewsGeneric.List5.as_view(), name="List5"),
    path('detail5/<int:pk>/', viewsGeneric.Detail5.as_view(), name="Detail5"),

    path('userlist', viewsGeneric.UserList.as_view(), name="UserList"),
    path('userdetail/<int:pk>/', viewsGeneric.UserDetail.as_view(), name="UserDetail"),

    path('', viewsGeneric.api_root, name="API_Root"),
    path('snippets/<int:pk>/highlight/', viewsGeneric.SnippetHighlight, name="SnippetHighlight")
]

urlpatterns = format_suffix_patterns(urlpatterns)