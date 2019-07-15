from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from halls import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Auth
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Hall
    path('halloffame/create/', views.CreateHall.as_view(), name='create_hall'),
    path('halloffame/<int:pk>/', views.DetailHall.as_view(), name='detail_hall'),
    path('halloffame/<int:pk>/update/', views.UpdateHall.as_view(), name='update_hall'),
    path('halloffame/<int:pk>/delete/', views.DeleteHall.as_view(), name='delete_hall'),
    # Video
    path('halloffame/<int:pk>/addvideo/', views.add_video, name='add_video'),
    path('video/search/', views.video_search, name='video_search'),
    path('video/<int:pk>/delete/', views.DeleteVideo.as_view(), name='delete_video'),
]
urlpatterns += static(settings.STATIC_URL, dcocument_url=settings.STATIC_ROOT)
