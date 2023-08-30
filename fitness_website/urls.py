from django.contrib import admin
from django.urls import path
from fitness_app import views
from django.conf import settings  
from django.conf.urls.static import static  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('customer_signup/', views.customer_signup, name='customer_signup'),
    path('trainer_signup/', views.trainer_signup, name='trainer_signup'),
    path('book_sessions/', views.book_sessions, name='book_sessions'),
    path('history_page/', views.history_page, name='history_page'),
    path('trainer_page/', views.trainer_page, name='trainer_page'),
    path('profile/', views.profile_page, name='profile_page'),
    path('video-call/<str:customer_username>-<str:trainer_username>/', views.video_call, name='video_call'),
    #path('save-booking/', views.save_booking, name='save_booking'),

]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)