from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
     path('home/',views.home,name='home'),
    path('courses/',views.courses,name='courses'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('about/',views.about,name='about'),  
    path('trainers/',views.trainers,name='trainers'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout')

]
