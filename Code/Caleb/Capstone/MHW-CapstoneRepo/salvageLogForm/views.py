from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import PersonalInfo, SalvageLogInfo
import json


# Create your views here.
def salvageLogForm(request):
    if request.method == "POST":
        print(request.body)
        print('***'*25)
        data = json.loads(request.body)
        print(data)
        print('***'*25)
        log_data = SalvageLogInfo(
            log_species=data['Species'],
            trunk_diameter=data['LogDiameter'],
            trunk_crotch_height=data['TrunkHeight'],
            address_ln1=data['Address'],
            address_ln2=data['Address2'],
            city=data['City'],
            zip=data['Zip'],
            state=data['State']
        )
        post = log_data
        print(post)
        print('***'*25)
        # post.author = request.user
        # post.published_date = timezone.now()
        post.save()
        # if pinfo.SalvageLogInquiryCheck:
        #     return render(request, 'logs/salvageLogForm.html')
        # else:
        #     return render(request, 'logs/personalInfoForm.html')
        return HttpResponse('Success')
    return render(request, 'ContactUsforms/salvageLogForm.html')

    # Create your views here.
def contactUsForm(request):
    if request.method == "POST":
        print(request.body)
        print('***'*25)
        data = json.loads(request.body)
        print(data)
        print('***'*25)
        pinfo = PersonalInfo(
            name=data['Name'],
            phone=data['Phone'],
            email=data['Email'],
            address_ln1=data['Address'],
            address_ln2=data['Address2'],
            city=data['City'],
            zip=data['Zip'],
            state=data['State'],
            SalvageLogInquiryCheck=data['SalvageLogInquiryCheck'],
            MillingKilnInquiryCheck=data['MillingKilnInquiryCheck'],
            LumberyardInquiryCheck=data['LumberyardInquiryCheck']
        )
        post = pinfo
        print(post)
        print('***'*25)
        # post.author = request.user
        # post.published_date = timezone.now()
        post.save()
        # if pinfo.SalvageLogInquiryCheck:
        #     return render(request, 'logs/salvageLogForm.html')
        # else:
        #     return render(request, 'logs/personalInfoForm.html')
    return render(request, 'ContactUsforms/personalInfoForm.html')

def form_view(request):
    return render(request, 'ContactUsforms/personalInfoForm.html')