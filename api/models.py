from django.db import models
import numpy as np

def random_prT():
        return "T_" + str(np.random.randint(1,1000)) 
def random_prAc():
        return "AC_" + str(np.random.randint(1,1000)) 
def random_prS():
        return "S_" + str(np.random.randint(1,1000))
def random_prSu():
        return "Su_" + str(np.random.randint(1,1000))
def random_prSc():
        return "Sc_" + str(np.random.randint(1,1000))
def random_room_name():
        return "room_name" + str(np.random.randint(1,1000))
def random_prA():
    return np.random.choice(["M","P","PRI","R"])
def random_prD():
        return "D_" + str(np.random.randint(1,1000))

class admin(models.Model):
    Admin_id = models.CharField(max_length = 25,null = False,primary_key = True,default=random_prA)
    Name = models.CharField(max_length = 100,null = False)
    T_id =  models.CharField(max_length=255,null=False)
    S_id = models.CharField(max_length = 100,null = False,default=random_prS)
    class Meta:
        db_table = 'Admin'
    def __str__(self) :
        return self.Name
    
class Disability(models.Model):
    def random_prD():
        return "D_" + str(np.random.randint(1,1000))
    Desability_id = models.CharField(max_length=255,primary_key=True,default=random_prD)
    Category = models.CharField(max_length=255,null = False)
    Disabilitys = models.CharField(max_length=255,null=False)
    class Meta:
        db_table = "Disability"
    def _str_(self):
        return self.Disabilitys
    
class student(models.Model):
    def FileName(instance,filename):
        return '/'.join(['images',str(instance.Name),filename])
    S_id = models.CharField(max_length = 255,null = False,primary_key = True,default=random_prS)
    Name = models.CharField(max_length = 255,null = False)
    Admin_id = models.CharField(max_length = 100,null = False,default=random_prA)
    T_id = models.CharField(max_length = 100,null = True,default=random_prT)
    Subject_id =models.CharField(max_length = 100,null = True,default=random_prT)
    Desability_id = models.ForeignKey(Disability,on_delete=models.CASCADE)
    Gender = models.CharField(max_length = 255,null = False)
    Education_level = models.CharField(max_length=255,null=True)
    Date_of_Birth = models.DateField()
    ProfilePic = models.ImageField(upload_to=FileName,null=True)
    class Meta:
        db_table = 'Student'
    def __str__(self) :
        return self.Name
    
class gardian(models.Model):
    S_id = models.ForeignKey(student,on_delete=models.CASCADE)
    G_Name = models.CharField(max_length = 100,null = False)
    contact_number = models.CharField(max_length = 13,null = False)
    Relationship = models.CharField(max_length=255)
    Gender = models.CharField(max_length = 25)
    Addresse = models.CharField(max_length=255,null = False)
    gmail = models.EmailField(max_length=255,unique=True)
    class Meta:
        db_table = 'Gardian'
    def __str__(self) :
        return self.Name

class subject(models.Model):
    Subject_id = models.CharField(max_length = 25,null = False,primary_key = True,default=random_prSu)
    Name = models.CharField(max_length = 100,null = False)
    T_id = models.CharField(max_length = 100,null = False,default=random_prT)
    S_id =  models.CharField(max_length = 100,null = False,default=random_prS)
    class Meta:
        db_table = 'Subject'
    def __str__(self) :
        return self.Name
    

class schedule(models.Model):
    Schedle_id = models.CharField(max_length = 25,null = False,primary_key = True,default=random_prSc)
    Name = models.CharField(max_length = 100,null = False)
    T_id =  models.CharField(max_length = 100,null = False)
    S_id = models.CharField(max_length = 100,null = False)
    Date = models.DateField()
    Time = models.DateField()
    
    class Meta:
        db_table = 'Schedule'
    def __str__(self) :
        return self.Name

class teacher(models.Model):
    def FileName(instance,filename):
        return '/'.join(['images',str(instance.Name),filename])
    T_id = models.CharField(max_length = 255,null = False,primary_key = True,default = random_prT)
    Name = models.CharField(max_length = 255,null = False)
    Email = models.EmailField(max_length=225,unique=True)
    Admin_id = models.CharField(max_length = 100,null = True,default=random_prA)
    S_id = models.CharField(max_length = 100,null = True,default=random_prS)
    Subject_id = models.CharField(max_length = 100,null = True,default=random_prSu)
    Schedule_id = models.CharField(max_length = 100,null = True,default=random_prSc)
    Gender = models.CharField(max_length = 255,null = True)
    Experience = models.CharField(max_length=255,null = True)
    Date_of_Birth = models.DateField(null = True)
    Addrese = models.CharField(max_length=255,unique=True,null = True)
    Expert_IN = models.CharField(max_length=255)
    Review = models.IntegerField(null=True,blank=True)
    certificate = models.ImageField(upload_to=FileName)
    Goverment_id = models.ImageField(upload_to=FileName)
    Photo = models.ImageField(upload_to=FileName)
    Signature = models.ImageField(upload_to=FileName)
    Payment = models.IntegerField(null=True,blank=True,default=0)
    class Meta:
        db_table = 'Teacher'
    def __str__(self) :
        return self.Name

class Attendence(models.Model):
    def FileName(instance,filename):
        return '/'.join(['FingerPrints',str(instance.T_id),filename])
    T_id = models.ForeignKey(teacher,on_delete=models.CASCADE)
    Fingerprint = models.ImageField(upload_to=FileName)
    Date = models.DateField()
    Start_time = models.TimeField()
    End_time = models.TimeField()
    class Meta:
        db_table = "Attendence"
    def _str_(self):
        return self.Date    


class Request(models.Model):
     Accept_id =  models.CharField(max_length = 25,null = False,primary_key = True,default=random_prAc)
     S_id = models.ForeignKey(student,on_delete=models.CASCADE)
     T_id = models.ForeignKey(teacher,on_delete=models.CASCADE)
     Message = models.CharField(max_length=255,null=False,default="I want help")
     class Meta:
        db_table = "Join_Request"
     def _str_(self):
        return self.S_id
     
class Accept(models.Model):
     Accept_id = models.ForeignKey(Request,on_delete=models.CASCADE)
     room_name=models.CharField(max_length=255,default=random_room_name,null=False)
     is_accepted = models.BooleanField(default=0)   
     class Meta:
          db_table = 'Room_name'
     def _str_(self):
        return self.room_name
