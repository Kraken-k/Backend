
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gardian/',views.getdata),
        # path('addgardian/',views.addItem),
    path('Student/',views.getdata1),
         path('addStudent/',views.addItem1),
    path('Teacher/',views.getdata2),
         path('addTeacher/',views.addItem2),
    path('Admin/',views.getdata3),
         path('addAdmin/',views.addItem3),
    path('Subject/',views.getdata4),
         path('addSubject/',views.addItem4),
    path('Schedule/',views.getdata5),
         path('addSchedule/',views.addItem5)
                       
]
