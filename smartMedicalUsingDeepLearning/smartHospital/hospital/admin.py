from django.contrib import admin
from . import models


admin.site.site_header = 'AI Hospital Administration'
admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.Appointment)
admin.site.register(models.Disease)
