from django.contrib import admin
from django.urls import path, include

from carCollectionApp.web.views import index, catalogue, create_profile, details_profile, edit_profile, delete_profile, \
    create_car, details_car, edit_car, delete_car

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:car_id>/details/', details_car, name='details car'),
        path('<int:car_id>/edit/', edit_car, name='edit car'),
        path('<int:car_id>/delete/', delete_car, name='delete car'),
    ])),
)
