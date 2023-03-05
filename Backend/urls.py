from django.urls import path,include
from accounts import views

urlpatterns = [
    path('',include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('activate/<str:uid>/<str:token>',views.UserActivationView),
    path('chat/',include('Chat.urls')),
    path("admin/",include('Admin.urls')),
              
]


# urlpatterns+= [re_path('',TemplateView.as_view(template_name = 'index.html'))]