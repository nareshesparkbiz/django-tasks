from django.db import models

# Create your models here.

relation_choices=(
    ('married','Married'),
    ('unmarried','UnMarried')
)

gender_choices=(
    ('male','Male'),
    ('female','Female'),
    ('others','Other'),
)



class StateMaster(models.Model):
    state_name=models.CharField(max_length=50)

    def __str__(self):
        return self.state_name



class CityMaster(models.Model):
    
    stateID = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.city_name
    


class SelectMaster(models.Model):
    select_name = models.CharField(max_length=50)
    select_key = models.CharField(max_length=50)
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.select_name

class OptionMaster(models.Model):
    
    option_value=models.CharField(max_length=100)
    selectId=models.ForeignKey(SelectMaster, on_delete=models.CASCADE)


class TechnologyMaster(models.Model):
    techName=models.CharField(max_length=100)
    def __str__(self):

        return self.techName
    

class LanguageMaster(models.Model):
    lang_name = models.CharField(max_length=100)

    def __str__(self):

        return self.lang_name






class BasicDetails(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    designation1 = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    email = models.EmailField(max_length=90)
    city = models.CharField(max_length=50)
    state=models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, choices=gender_choices)
    zipcode = models.CharField(max_length=10)
    relation_status = models.CharField(max_length=50,choices=relation_choices)
    dob=models.DateField()

    def __str__(self):
        a=str(self.id)
        return a

    

    



    

class EducationDetail(models.Model):
    student_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=200)
    board_name = models.CharField(max_length=100,null=True)
    passing_year=models.CharField(max_length=20,null=True)
    percentage=models.FloatField(default=0)

class WorkExperiences(models.Model):
    student_id = models.ForeignKey(BasicDetails,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Languages(models.Model):
    student_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    language=models.CharField(max_length=100)
    read_status=models.BooleanField()
    write_status=models.BooleanField()
    speak_status=models.BooleanField()

class Technologies(models.Model):
    student_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    tech_name = models.CharField(max_length=100)
    star=models.CharField(max_length=100)

class RefranceContact(models.Model):
    student_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    ref_name = models.CharField(max_length=100)
    ref_contact = models.CharField(max_length=100)
    relation=models.CharField(max_length=50)

class Preference(models.Model):
    student_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    prefered_location=models.CharField(max_length=100 )
    expected_ctc=models.CharField(max_length=100)
    current_ctc=models.CharField(max_length=100)
    notice_period=models.CharField(max_length=10)
    department=models.CharField(max_length=100)



