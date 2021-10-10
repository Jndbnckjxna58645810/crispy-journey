from django.urls import path
from .views import index, by_rubric, by_salesman, BbCreateView
urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path ('salesman/<int:salesman_id>/', by_salesman, name="by_salesman"),
    path ('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
]