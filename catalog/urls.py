from django.urls import path
from . import views

#app_name = "catalog"  # added, is this needed?

urlpatterns = [
    path('', views.index, name='index'),
    path('my_session/', views.MySessionsByStudentListView.as_view(), name='my_session'),
    path('tutor_list/', views.TutorListView.as_view(), name='tutor_list'),
    path('tutor_detail/<int:pk>', views.TutorDetailView.as_view(), name='tutor_detail'),
    # path('<int:pk>/', views.TutorDetailView.as_view(), name='tutor_detail'),
    # path('session/create/', views.SessionCreate.as_view(), name='session_create'),
    # path('session/<int:pk>/update/', views.SessionUpdate.as_view(), name='session_update'),
    # path('session/<int:pk>/delete/', views.SessionDelete.as_view(), name='session_delete'),
    path('billing_details/<int:pk>', views.BillDetailView.as_view(), name='billing_details'),
    path('payment_create/', views.PaymentCreate.as_view(), name='payment_create'),
]
