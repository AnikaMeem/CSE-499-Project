from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("",views.home_page,name = "homepage"),
    path("aboutus/",views.aboutus,name = "aboutus"),
    path("patientlogin/",views.PatientLogin.as_view(),name = "patientlogin"),
    path("doctorlogin/",views.doctorlogin,name = "doctorlogin"),
    path("doctorSignin/",views.doctorSignin,name="doctorSignin"),
    path("patientSignin/",views.patientSignin,name="patientSignin"),
    path('contactus/',views.contactUs,name = "contactus"),
    path("doctorDash/",views.DoctorDash.as_view(),name = "doctorDash"),
    path("patientDash/",views.PatientDash.as_view(),name = "patientDash"),
    path("diseasePrediction/",views.DiseasePrediction.as_view(),name = "diseasePrediction"),
    path("appointment/",views.MakeAppointments.as_view(),name = "appointment"),
    path("success/",views.success,name="success")
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)