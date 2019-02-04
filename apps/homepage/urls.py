from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^menu$', views.menu, name="menu"),
    url(r'^menu_images$', views.menu_images, name="menu_images"),
    url(r'^about$', views.about_us, name="about_us"),
    url(r'^contact_us$', views.contact_us, name="contact_us"),
    url(r'^careers$', views.careers, name="careers"),

    url(r'^closing_soon$', views.closing_soon),

    url(r'^login$', views.login),
    url(r'^login_process$', views.login_process),
    url(r'^logout$', views.logout),
    url(r'^admin$', views.admin),

    url(r'^admin/menu/add$', views.menu_add),
    url(r'^admin/menu/add_process$', views.menu_add_process),
    url(r'^admin/menu/(?P<item_id>\d+)/modify$', views.menu_modify),
    url(r'^admin/menu/(?P<item_id>\d+)/modify_process$', views.menu_modify_process),
    url(r'^admin/menu/(?P<item_id>\d+)/delete_process$', views.menu_delete_process),
    url(r'^admin/menu/(?P<item_id>\d+)/add_image$', views.menu_add_image),
    url(r'^admin/menu/(?P<item_id>\d+)/add_image_process$', views.menu_add_image_process),
]
