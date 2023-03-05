from django.urls import path
import Admin.views as views


urlpatterns = [
  path('help/',views.HelpView.as_view()),
  path('help/res',views.helpres)
]