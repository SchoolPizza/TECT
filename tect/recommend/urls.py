from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search/', views.SearchFormView.as_view(), name = 'search'),
    path('important/dbinstall/', views.dbinstall, name = 'dbinstall'),
    path('important/dbdelete/', views.dbdelete, name = 'dbdelete'),
	path('<int:book_id>/', views.details, name ='details'),
]
