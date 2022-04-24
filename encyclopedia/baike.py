from django.urls import path

from baike import views
app_name = 'baike'
urlpatterns = [
    path('entry/', views.baike_entry, name='add'),
    path('list/', views.baike_list, name='list'),
]