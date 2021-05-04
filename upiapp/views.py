from django.shortcuts import render


def home(request):
	if request.method == "POST":
		#write the logic to save the data in db
	return render(request,'home.html')

