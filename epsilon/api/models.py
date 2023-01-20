from django.db import models


# Create your models here.
class Item(models.Model):
    G_id = models.CharField(max_length = 25,null = False,primary_key = True)
    Name = models.CharField(max_length = 100,null = False)
    contact_number = models.CharField(max_length = 13,null = False)
    Relationship = models.CharField(max_length=255)
    Gender = models.CharField(max_length = 25,null = False)
    S_id = models.CharField(max_length = 25,null = False)
    Addresse = models.CharField(max_length=255,null = False)
    class Meta:
        db_table = 'gardian'
    def __str__(self) :
        return self.Name
    

class Item1(models.Model):
    S_id = models.CharField(max_length = 255,null = False,primary_key = True)
    Name = models.CharField(max_length = 255,null = False)
    Admin_id = models.CharField(max_length = 255,null = False)
    T_id = models.CharField(max_length = 255,null = False)
    Subject_id = models.CharField(max_length = 255,null = False)
    Desability_id = models.CharField(max_length=255,null = False)
    Gender = models.CharField(max_length = 255,null = False)
    Education_level = models.CharField(max_length=255)
    Date_of_Birth = models.DateField()
    class Meta:
        db_table = 'Student'
    def __str__(self) :
        return self.Name
    

class Item2(models.Model):
    T_id = models.CharField(max_length = 255,null = False,primary_key = True)
    Name = models.CharField(max_length = 255,null = False)
    Email = models.CharField(max_length=255)
    Admin_id = models.CharField(max_length = 255,null = False)
    S_id = models.CharField(max_length = 255,null = False)
    Subject_id = models.CharField(max_length = 255,null = False)
    Schedule_id = models.CharField(max_length=255,null = False)
    Gender = models.CharField(max_length = 255,null = False)
    Experience = models.CharField(max_length=255)
    Date_of_Birth = models.DateField()
    Adrese = models.CharField(max_length=255)
    certificate = models.JSONField()
    Goverment_id = models.JSONField()
    Photo = models.JSONField()
    Signature = models.JSONField()
    class Meta:
        db_table = 'Teacher'
    def __str__(self) :
        return self.Name
    


class Item3(models.Model):
    Admin_id = models.CharField(max_length = 25,null = False,primary_key = True)
    Name = models.CharField(max_length = 100,null = False)
    T_id =  models.CharField(max_length = 100,null = False)
    S_id = models.CharField(max_length = 100,null = False)
    class Meta:
        db_table = 'Admin'
    def __str__(self) :
        return self.Name
    


class Item4(models.Model):
    Subject_id = models.CharField(max_length = 25,null = False,primary_key = True)
    Name = models.CharField(max_length = 100,null = False)
    T_id =  models.CharField(max_length = 100,null = False)
    S_id = models.CharField(max_length = 100,null = False)
    class Meta:
        db_table = 'Subject'
    def __str__(self) :
        return self.Name
    

class Item5(models.Model):
    Schedle_id = models.CharField(max_length = 25,null = False,primary_key = True)
    Name = models.CharField(max_length = 100,null = False)
    T_id =  models.CharField(max_length = 100,null = False)
    S_id = models.CharField(max_length = 100,null = False)
    Date = models.DateField()
    Time = models.DateField()
    
    class Meta:
        db_table = 'Schedule'
    def __str__(self) :
        return self.Name
    


    