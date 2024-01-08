from django.shortcuts import render, get_object_or_404
from .models import Crud
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

# display function
def crud(request):
    crud_data = Crud.objects.all()
    paginator = Paginator(crud_data, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'display.html', {'page_obj': page_obj})

# Adding function
def insert_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mobno = request.POST.get('mobno')
        email = request.POST.get('email')
        Crud.objects.create(firstname=firstname, lastname=lastname, mobno=mobno, email=email)
        messages.success(request, 'User created successfully!')
        return HttpResponseRedirect('/display/')  # Redirect to display page
    return render(request, 'create.html')

# Update function
def edit_view(request, id):
    instance = get_object_or_404(Crud, id=id)
    if request.method == 'POST':
        # Update the data
        instance.firstname = request.POST.get('firstname')
        instance.lastname = request.POST.get('lastname')
        instance.mobno = request.POST.get('mobno')
        instance.email = request.POST.get('email')
        instance.save()
        return HttpResponseRedirect('/display/')  # Redirect to display page
    return render(request, 'edit.html', {'instance': instance})

# Delete function
def delete_view(request, id):
    instance = get_object_or_404(Crud, id=id)
    instance.delete()
    return HttpResponseRedirect('/display/')  # Redirect to display page
