from django.urls import path
from CPRapp import views
from django.contrib.auth import views as ad
urlpatterns = [
path('',views.home,name="hm"),
path('about/',views.about,name="about"),
path('contact/',views.contact,name="contact"),
path('reg/',views.register,name="reg"),
path('lg/',ad.LoginView.as_view(template_name='html/ulogin.html'),name="ulog"),
path('alg/',ad.LoginView.as_view(template_name='html/alogin.html'),name="alog"),
path('rst/',ad.PasswordResetView.as_view(template_name="html/resetpassword.html"),name="rt"),
path('rst_done/',ad.PasswordResetDoneView.as_view(template_name="html/resetpassworddone.html"),name="password_reset_done"),
path('rst_cf/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name="html/resetpasswordconfirm.html"),name="password_reset_confirm"),
path('rst_cmplt/',ad.PasswordResetCompleteView.as_view(template_name="html/resetpasswordcomplete.html"),name="password_reset_complete"),
path('dash/',views.dashboard,name="dash"),
path('logo/',ad.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
path('pro/',views.profile,name="profile"),
path('updf/',views.updpf,name="upf"),
path('addpro/',views.addpro,name="addpro"),
path('pns/',views.pns,name="pns"),
path('contview/',views.contview,name="contview"),
path('uview/',views.userview,name="userview"),
path('more/<int:id>/',views.more,name='more'),
path('del/<int:id>/',views.dlt,name='dlt'),
]