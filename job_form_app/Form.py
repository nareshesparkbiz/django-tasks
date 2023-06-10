from django import forms
from .models import BasicDetails,StateMaster,CityMaster,EducationDetail,OptionMaster,WorkExperiences,LanguageMaster,Languages,Technologies,RefranceContact,Preference

class BasicDetailForm(forms.ModelForm):
    class Meta:
      
      model=BasicDetails
      fields='__all__'
      labels={
         'designation1':'Designation',
      }
      
      widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'lastname': forms.TextInput(
                attrs={'placeholder': 'Enter Last Name'}),
            'designation1': forms.TextInput(attrs={'placeholder': 'Enter Designation'}),
             'address1': forms.TextInput(attrs={'placeholder': 'Address 1'}),
             'address2': forms.TextInput(attrs={'placeholder': 'Address 2'}),
             'email': forms.TextInput(attrs={'placeholder': ' Enter Email'}),
             'zipcode': forms.TextInput(attrs={'placeholder': 'Pincode'}),
           'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={ 'placeholder':'Select a date', 'type':'date'}),
             
             'city':forms.Select(),
             'state':forms.Select( attrs={'onchange' : "changeState(this.value);"}),
             'course_name':forms.Select()
 

             


        }
      

 


class Education(forms.ModelForm):
      class Meta:
        def __init__(self, *args, **kwargs):
          pass
        model=EducationDetail
      #   widgets={
      #      'course'
      #   }
       
        exclude=['student_id']


      course_name=forms.ModelChoiceField(
         queryset=OptionMaster.objects.filter(selectId=5).values_list('option_value',flat=True),
          empty_label='None',
          required=False, widget=forms.Select(),to_field_name="option_value"
      )
        
      


class WorkForm(forms.ModelForm):
   class Meta:
    
      model=WorkExperiences
      exclude=['student_id']
   widgets={
           'start_date':forms.DateInput()


   }
   # start_date:forms.DateField()
   start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
   end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))



class Language(forms.ModelForm):
   # data=LanguageMaster.objects.all().values_list('lang_name', flat=True)                                                                                                                                                                                                                                                                                                          

   class Meta:

  
      
      model=Languages
      exclude=['student_id']
      # widgets={
      #    'read_status': forms.BooleanField(attrs={'class': 'required checkbox form-control'}),
      #    'write_status': forms.BooleanField(attrs={'class': 'required checkbox form-control'}),
      #    'speak_status': forms.BooleanField(attrs={'class': 'required checkbox form-control'}),
      # }

     
      labels={
         'read_status':'Read',
         'write_status':'Write',
         'speak_status':'Speak'
      }

    
      






class TechnologyForm(forms.ModelForm):
   CHOICES=OptionMaster.objects.filter(selectId=7).values_list('option_value',flat=True)

  
   # tech_name=forms.ChoiceField(choices=[(value['id'],value['option_value']) for value in OptionMaster.objects.filter(selectId=7).values('id','option_value')],widget=forms.CheckboxSelectMultiple(attrs={'onchange':'check_validate_tech(this)','oninput':'allValidate()'}))  


   class Meta:
      
   
      model=Technologies
      exclude=['student_id']

   # widgets={
         
   #    'tech_name':forms.CheckboxSelectMultiple(attrs={'class': 'required checkbox' ,'onchange':'check_validate_tech(this)','oninput':'allValidate()'})
   # }


class RefranceForm(forms.ModelForm):
   class Meta:
      model=RefranceContact
      exclude=['student_id']

      labels={
         'ref_name':'Name',
         'ref_contact':'Contact',
         'relation':'Relation'
      }


class PreferenceForm(forms.ModelForm):
   class Meta:
      model=Preference
      exclude=['student_id']

   
   prefered_location=forms.ModelChoiceField(
      queryset=OptionMaster.objects.filter(selectId=11).values_list('option_value',flat=True),
         empty_label='None',
         required=False, widget=forms.Select(),to_field_name="option_value"
   )

   department=forms.ModelChoiceField(
   queryset=OptionMaster.objects.filter(selectId=12).values_list('option_value',flat=True),
      empty_label='None',
      required=False, widget=forms.Select(),to_field_name="option_value"
)

   

