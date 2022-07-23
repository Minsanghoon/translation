from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload menu board', views.upload_menu_board, name='upload menu board'),
    path('Local food recommend', views.Local_food_recommend, name='Local food recommend'),
    path('taste setting', views.taste_setting, name='taste setting'),
    path('Allergy setting', views.Allergy_set, name='Allergy setting'),
]
