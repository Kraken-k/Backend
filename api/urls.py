from django.urls import path
import api.views as views
from . import Student_Views , Teacher_view , Admin_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # path('Gardian/',views.Gardian),
    # path('Student/',views.Student),
    # path('Teacher/',views.Teacher),
    path('Admin/',views.Admin),
    path('Subject/',views.Subject),
    path('Schedule/',views.Schedule),
    path("Teachers/Registration",Teacher_view.T_Registration.as_view()),
    path("Teacher/id/get",Student_Views.TGET),
    path("Student/Registration",Student_Views.S_Registration.as_view()),
    path("Gardian/Registration",Student_Views.G_Registration.as_view()),
    path("Student/id/get",Teacher_view.SGET),
    path("Student/id",Student_Views.getid),
    path("Teacher/Request",Teacher_view.request_GET),
    path('Student/Disabilitys',views.Disabilitys),
    path('Teacher/Attendence',Student_Views.T_Attendence.as_view()),
    path('Student/Request',Student_Views.Student_Request),
    path('Student/<str:S_id>/UplodePic',Student_Views.Uplode_ProfilePic.as_view()),
    path("Teacher/id",Teacher_view.get_id)
                       
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)