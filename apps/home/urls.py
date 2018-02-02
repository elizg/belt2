from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^add/item/$', add_item, name='add'),
    url(r'^wish/(?P<wish_id>\d+)$', add_wish, name='wish'),
    url(r'^unwish/(?P<wish_id>\d+)$', remove_wish, name='unwish'),
    url(r'^item/(?P<item_id>\d+)$', item, name='item'),
    url(r'^delete(?P<item_id>\d+)$', delete, name='delete')
]
