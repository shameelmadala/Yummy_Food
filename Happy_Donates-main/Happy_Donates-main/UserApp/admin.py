from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserDataModel)
admin.site.register(UserPostModel)
admin.site.register(UserDonationModel)
admin.site.register(UserImageModel)