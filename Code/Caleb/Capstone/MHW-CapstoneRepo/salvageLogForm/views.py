from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonalInfo
import json


# Create your views here.
def salvageLogForm(request):
    if request.method == "POST":
        print(request.body)
        print('***'*25)
        data = json.loads(request.body)
        print(data)
        print('***'*25)
        pinfo = PersonalInfo(
            name=data['Name'],
            phone=data['Phone'],
            address_ln1=data['Address'],
            address_ln2=data['Address2'],
            city=data['City'],
            zip=data['Zip'],
            email=data['Email'],
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
    return render(request, 'logs/base.html')