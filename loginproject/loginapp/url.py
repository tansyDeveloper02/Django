from django.conf.urls import url
from loginapp import views

app_name = "loginapp"

urlpatterns = [

    url(r'^register/$',views.register,name='register'),
    url(r'^login/',views.user_login, name="user_login")

]
