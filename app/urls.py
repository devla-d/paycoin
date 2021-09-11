from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_view, name="home"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('transaction-history/', views.history_view, name="history"),
    path('sell-coin/', views.sell_coin_view, name="sell_coin"),
    path('buy-coin/', views.buy_coin_view, name="buy_coin"),
    path('verify-payment/', views.verify_payment_view, name="verify_payment"),
    path('account/', views.account_view, name="account"),
    path('login/', views.login_view, name="login"),
    path('account-settings/', views.account_setting_view, name="settings"),
    path('register/', views.register_view, name="register"),
    path('change-password/', views.user_paswordchange_view, name="user_paswordchange"),
    path('change-profile/', views.profile_info_view, name="profile_info"),
    path('change-profile-info/', views.user_profile_info_view, name="user_profile_info"),
    path('logout/', views.logout_view, name="logout"),
    path('helpdesk/', views.helpdesk_view, name="helpdesk"),
    path('contact/', views.contact_view, name="contact"),
    path('faq/', views.faq_view, name="faq"),
    path('about/', views.about_us_view, name="about"),
    path('team/', views.team_view, name="team"),
    path('career/', views.carer_view, name="career"),
    path('wallet/', views.wallet_view, name="wallet"),
    path('price/', views.price_view, name="price"),
    


]
