from django.shortcuts import render,HttpResponse
from .Form import BasicDetailForm,Education,Language,TechnologyForm,WorkForm,RefranceForm,PreferenceForm
from django.http import JsonResponse,QueryDict
from .models import StateMaster,CityMaster,BasicDetails,Languages,LanguageMaster,TechnologyMaster,WorkExperiences
# Create your views here.
import math


def BasicForm(request):

    form=BasicDetailForm(request.POST or None)
    userLang=LanguageMaster.objects.all()
    userTech=TechnologyMaster.objects.all()
    
    education_part=Education(request.POST or None)
    language_part=Language(request.POST or None)
    technology_part=TechnologyForm(request.POST or None)
    work_part=WorkForm(request.POST or None)
    refrance_part=RefranceForm(request.POST or None)
    preferance_part=PreferenceForm(request.POST or None)
    # print(work_part)
    


    formResponse=dict(request.POST)
    # print(formResponse,"data")


    # print(request.POST.get('course_name'),"course name")
    # print(request.POST.get('board_name'),"board name")
    # print(request.POST.get('passing_year'),"passing year")
    # print(request.POST.get('percentage'),"percentage")
    # print(request.POST)

    


  
    if form.is_valid() :
        
          

        formObject=  form.save()


        for i in range(len(formResponse['board_name']))    :
            exec_quer=QueryDict(
                f"course_name={formResponse['course_name'][i]}&board_name={formResponse['board_name'][i]}&passing_year={formResponse['passing_year'][i]}&percentage={formResponse['percentage'][i]}")          
            educationresponse=Education(exec_quer)

            if educationresponse.is_valid():
                eduSave = educationresponse.save(commit=False)
                eduSave.student_id=formObject

        #         # print(formObject)
                educationresponse.save()
            else:
                print(educationresponse.errors) 


        for i in range(len(formResponse['language'])) :

            langFun=f"language={formResponse['language'][i]}"
            if 'read_status' in formResponse:
                if formResponse['language'][i] in formResponse['read_status']:
                  langFun+=f"&read_status={1}"
                  
            if 'write_status' in formResponse:
                      
                if formResponse['language'][i] in formResponse['write_status']:
                       langFun+=f"&write_status={1}"
                          

                      
            if 'speak_status' in formResponse:
                if formResponse['language'][i] in formResponse['speak_status']:
                               langFun+=f"&speak_status={1}"
                               
            exec_lang=QueryDict(langFun)
                        


            
            languageresponse=Language(exec_lang)
            print(exec_lang,"lasdasldak")
            if languageresponse.is_valid():
                langSave=languageresponse.save(commit=False)
                langSave.student_id=formObject
                languageresponse.save()
            else:
                print(languageresponse.errors)
            


        for i in range(len(formResponse['tech_name'])):
            techFun=f"tech_name={formResponse['tech_name'][i]}"
            tech_name=formResponse['tech_name'][i]

            if tech_name in formResponse: 
              print(formResponse[tech_name][0])
              techFun+=f"&star={formResponse[tech_name][0]}"

            print(techFun)
            exec_tech=QueryDict(techFun)
            technologyresponse=TechnologyForm(exec_tech)
            print(exec_tech,"techdata")
#         print(exec_lang,"lasdasldak")

            if technologyresponse.is_valid():
                techSave=technologyresponse.save(commit=False)
                techSave.student_id=formObject
                technologyresponse.save()
            else:
                print(technologyresponse.errors)



        for i in  range(len(formResponse['company_name'])):
            exec_quer=QueryDict(
            f"company_name={formResponse['company_name'][i]}&designation={formResponse['designation'][i]}&start_date={formResponse['start_date'][i]}&end_date={formResponse['end_date'][i]}")          
            workresponse=WorkForm(exec_quer)
            if workresponse.is_valid():
                workSave = workresponse.save(commit=False)
                workSave.student_id=formObject

                
                workresponse.save()
            else:
                print( workresponse.errors) 
              
        for i in range(len(formResponse['ref_name'])) :
            exec_quer=QueryDict(
            f"ref_name={formResponse['ref_name'][i]}&ref_contact={formResponse['ref_contact'][i]}&relation={formResponse['relation'][i]}")     
            refresponse=RefranceForm(exec_quer)

            if refresponse.is_valid():
                refSave = refresponse.save(commit=False)
                refSave.student_id=formObject

                
                refresponse.save()
            else:
                print( refresponse.errors)
      
          
        preferenceresponse=PreferenceForm(request.POST)

        prefSave = preferenceresponse.save(commit=False)
        prefSave.student_id=formObject
        if preferenceresponse.is_valid():
                prefSave = preferenceresponse.save(commit=False)
                prefSave.student_id=formObject

            
                preferenceresponse.save()
        else:
                print(preferenceresponse.errors) 
   

    else:
        print(form.errors)
      
    return render(request,'jobForm.html',{'form': BasicDetailForm,'education': education_part,'userlang':userLang,'usertech':userTech,'work_part':work_part,'refrances':refrance_part,'preferance':preferance_part})


def get(request,state):

    
 
     queryset=CityMaster.objects.filter(stateID=state).values_list('city_name',flat=True)

     city_option=''
     for i in queryset:
         city_option+='<option value="{}" >{}</option>'.format(i,i)
     
     cityData={}
     cityData['city']=city_option
 
     return JsonResponse(cityData)
     



def showData(request):
     id=request.GET.get('pageId',1)
     flag=request.GET.get('ajax',1)
     sort=request.GET.get('sort','id')
     print(flag,"falg")

     
     
     limit=1
     
     offset=(int(id)-1)*limit 
     print(offset,'offset')
    #  if flag:
          
     totalDataCount=BasicDetails.objects.all().count()
     pageno=math.ceil(int(totalDataCount/limit))
     print(pageno,"page no")
     print(type(pageno),"page no")

     
          

     all_Data=BasicDetails.objects.all().order_by(sort  )[offset:offset+limit].values('id','firstname','lastname','designation1','email','city','dob','state','gender')
     print(all_Data,"Dataset")
     data1=list(all_Data)

     for i in all_Data:
          stateId=i['state']
          statename=StateMaster.objects.filter(id=stateId).values_list('state_name',flat=True)

          i['state']=list(statename)[0]


     
    #  print(list(all_Data),"DataList")
     if flag==1:
        print("dfhbsdjhfbdf")
     

        return render(request,'viewForm.html',{"data":all_Data,'range': range(1,pageno+1)})
     else:
          print("draqweqweqwe")
          return JsonResponse({'all_data':list(all_Data)})
    
     
     


def deleteData(request):
     deleteId=request.GET.get('id')
     print('deleteId',deleteId)

     member = BasicDetails.objects.get(id=int(deleteId))
     member.delete()
     return HttpResponseRedirect(reversed('viewForm.html'))
    
     

    #  if flag:
    #       offset=(id-1)*limit |0

    

          

          
     