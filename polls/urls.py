from django.urls import path
# is this necssary?
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('deepthought/list/', views.detail, name='detail'),
    path('deepthought/<int:DeepThought_id>/', views.viewDeepThought, name='viewDeepThought'),

    # this one is where you subjit a deep thought
    path('deepthought/', views.SubmitDeepThought, name='SubmitDeepThought')
    
]