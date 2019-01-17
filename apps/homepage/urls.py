from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^menu$', views.menu),
    url(r'^menu_test$', views.menu_test),
    url(r'^about$', views.about_us),
    url(r'^contact_us$', views.contact_us),
    url(r'^careers$', views.careers),

    url(r'^closing_soon$', views.closing_soon),

    url(r'^login$', views.login),
    url(r'^login_process$', views.login_process),
    url(r'^logout$', views.logout),
    url(r'^admin$', views.admin),

    url(r'^admin/menu/add$', views.menu_add),
    url(r'^admin/menu/add_process$', views.menu_add_process),
    # url(r'^admin/menu/(?P<menu_id>\d+)/modify$', views.menu_modify),
    # url(r'^admin/menu/(?P<menu_id>\d+)/modify_process$', views.menu_modify_process),
    # url(r'^admin/menu/delete_process$', views.menu_delete_process),
    url(r'^admin/menu/(?P<menu_id>\d+)/add_image$', views.menu_add_image),
    url(r'^admin/menu/(?P<menu_id>\d+)/add_image_process$', views.menu_add_image_process),
]
