from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutor_list/', views.TutorListView.as_view(), name='tutor_list'),
    path('tutor_detail/<int:pk>', views.TutorDetailView.as_view(), name='tutor_detail'),
#    path('session/create/', views.SessionCreate.as_view(), name='session_create'),
#    path('session/<int:pk>/update/', views.SessionUpdate.as_view(), name='session_update'),
#    path('session/<int:pk>/delete/', views.SessionDelete.as_view(), name='session_delete'),
    path('my_sessions/', views.MySessionsByStudentListView.as_view(), name='my_sessions'),
]
