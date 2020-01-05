from django.shortcuts import render
from .models import Contact_us

# Create your views here.
def contacts_view(request):
	if request.method == "POST":
		New_name = request.POST.get('Name')
		New_email = request.POST.get('Email')
		New_contact = request.POST.get('Contact_no')
		New_message = request.POST.get('Message')
		print(New_name)
		Contact_us.objects.create(Name= New_name,Email= New_email,Contact_no= New_contact,Message= New_message)

	contact = Contact_us.objects.all()
	return render(request, "contacts/contacts.html", {"contact": contact})