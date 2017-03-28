from django.conf.urls import url

from bookine import views

app_name = 'website'

urlpatterns = [
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^signin_user/$', views.sign_in_user, name='signin_user'),
    url(r'^signin_staff/$', views.sign_in_staff, name='signin_staff'),
    url(r'^signin_manager/$', views.sign_in_manage, name='signin_manager'),
    url(r'^list_book/$', views.get_all_book, name='list_book'),
    url(r'^detail_book/(?P<id>[0-9]+)/$', views.detail_book, name='detail_book'),
    url(r'^add_cart/$', views.add_cart, name='add_cart'),
    url(r'^get_cart/$', views.get_cart, name='get_cart'),


    # url(r'^profile/$', views.profile, name='profile'),
    # url(r'^logout/$', views.log_out, name='logout'),
]
