from django.shortcuts import render, get_object_or_404
from .models import Country, Profile

# Create your views here.

def home(request):
	country = Country.objects.all()
	context = {'countries':country}
	return render(request, "profiles/home.htm", context)

def countries(request):
	country = Country.objects.all()
	context = {'countries':country}
	return render(request, "profiles/countries.htm", context)


def country_detail(request, id):
	country = Country.objects.get(pk=id)
	countries = Country.objects.all()
	print(country)
	context = {'country':country, 'countries':countries}
	return render(request, "profiles/country_detail.htm", context)

def country_gender(request, id, idm):
	men_or_women = ''
	if idm == 1:	
		profile = Profile.objects.filter(country=id,  gender='male')
		men_or_women = 'Men'
	elif idm == 2:
		profile = Profile.objects.filter(country=id,  gender='female')
		men_or_women = 'Women'
	
	country_id = Country.objects.get(pk=id)
	
	context = {'profiles':profile, 'country':country_id, 'men_or_women':men_or_women}
	return render(request, "profiles/profiles_list.htm", context)

def profile(request, id):
	profile = Profile.objects.get(pk=id)
	context = {'profile':profile}
	return render(request, "profiles/profile.htm", context)


def profiles(request):
    
    return render(request, "profiles/profiles.htm", {})

def jobs(request):
    
	return render(request, "profiles/jobs.htm", {})

def contact_us(request):
    
	return render(request, "profiles/contact-us.htm", {})

def about_us(request):
   
	return render(request, "profiles/about-us.htm", {})

