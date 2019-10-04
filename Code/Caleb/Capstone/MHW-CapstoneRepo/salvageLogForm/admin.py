from django.contrib import admin
from .models import PersonalInfo, SalvageLogInfo

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(SalvageLogInfo)