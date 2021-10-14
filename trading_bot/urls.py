from django.urls import path, re_path
from . import views

app_name = 'trading_bot'

urlpatterns = [
    path('trading/start/', views.start_trading, name='start_trading'),
    path('trading/end/', views.end_trading, name='end_trading'),
    path('trading/requirements/<username>/', views.get_trading_requirements, name='username'),
    path('trading/userlist/', views.get_trading_user_list, name='get_user_list'),
]

