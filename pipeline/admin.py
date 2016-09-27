from django.contrib import admin
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from .models import Consult

# Register your models here.
admin.site.register(Consult)
