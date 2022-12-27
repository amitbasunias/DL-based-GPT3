from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from django.conf.urls import include
from . import views
import uniai

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard),
    path('login/', views.loginview),
    path('register/', views.register),
    path('write/', views.write),
    path('create/', views.create, name='create'),
    path('history/', views.history),
    path('package/', views.package),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    path('profile/', views.profile),
    path('getresult/', views.get_result),
    path('notes/<int:notes_id>/', views.notes_view, name='notes_view'),
    path('checkout/<int:packages_id>/', views.checkout, name='checkout_view'),
    path('dashboard/<str:package_key>/<str:packages_id>/',views.package_purchase),
 #   path('blog/', views.blog),
    path('logout/', LogoutView.as_view(), {'next_page': uniai.settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset/', views.password_reset),

]


