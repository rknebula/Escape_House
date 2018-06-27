from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game$', views.game, name='game'),
    url(r'^move/(?P<location_id>\d+)$', views.move, name='move'),
    url(r'^look/(?P<item_id>\d+)$', views.look, name='look'),
    # url(r'^fight$', views.fight, name='fight'),

    url(r'^admin$', views.admin, name='admin'),
]
