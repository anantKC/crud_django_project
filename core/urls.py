from django.urls import path
from .views import *

urlpatterns = [
    path('',list_asset, name='home'),
    path('add',add_assets,name='add'),
    path('edit',edit_asset,name='edit'),
    path('update/<str:id>',update_asset,name='update'),
    path('delete/<str:id>',delete_asset,name='delete'),


]