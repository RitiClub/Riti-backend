from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for Riti model
  
    path('riti/', views.RitiListView.as_view(), name='riti-list'),

    # Endpoint for Members model
    path('members/', views.MembersListView.as_view(), name='members-list'),

    # Endpoint for Carsol model
    path('carsol/', views.CarsolListView.as_view(), name='carsol-list'),

    # Endpoint for Logo model
    path('logo/', views.LogoListView.as_view(), name='logo-list'),

    # Endpoint for Recruitment model
    path('recruitment/', views.RecruitmentListView.as_view(), name='recruitment-list'),

    # Endpoint for Team model
    path('team/', views.TeamListView.as_view(), name='team-list'),

    # Endpoint for TeamImages model
    path('teamimages/', views.TeamImagesListView.as_view(), name='team-images-list'),

    # Endpoint for Magzine model
    path('magzine/', views.MagzineListView.as_view(), name='magzine-list'),

    # Endpoint for MagImages model
    path('magimages/', views.MagImagesListView.as_view(), name='mag-images-list'),
]
