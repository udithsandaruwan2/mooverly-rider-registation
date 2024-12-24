from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application

def index(request):
    page = 'index'
    page_title = 'Home'
    
    context = {
        'page': page,
        'page_title': page_title
    }
    
    return render(request, 'registrations/index.html', context)

def registerStep1(request):
    page  = 'register_step1'
    page_title = 'Register'
    
    form = ApplicationForm()
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        
        if form.is_valid():
            form.save()
            form_uuid = form.instance.uuid
            request.session['form_uuid'] = str(form_uuid)
            return redirect('registerStep2')
    
    context = {
        'page': page,
        'page_title': page_title,
        'form': form
    }
    
    return render(request, 'registrations/form.html', context)

def registerStep2(request):
    page = 'register_step2'
    page_title = 'Register'
    
    # Initialize an empty form or bind it with POST data
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
    else:
        form = ApplicationForm()
    
    # Handle form submission
    if request.method == 'POST' and form.is_valid():
        form_uuid = request.session.get('form_uuid')
        if not form_uuid:
            # Handle missing form UUID in session
            return redirect('error_page')  # Replace 'error_page' with your error-handling view
        
        # Retrieve the application object
        try:
            application = Application.objects.get(uuid=form_uuid)
        except Application.DoesNotExist:
            return redirect('error_page')  # Replace with your error-handling view
        
        # Update application with validated form data
        application.address_line_1 = form.cleaned_data.get('address_line_1')
        application.address_line_2 = form.cleaned_data.get('address_line_2')
        application.address_line_3 = form.cleaned_data.get('address_line_3')
        application.description = form.cleaned_data.get('description')
        application.working_type = form.cleaned_data.get('working_type')
        application.possible_working_hours = form.cleaned_data.get('possible_working_hours')
        application.save()
        request.session['form_uuid'] = str(application.uuid)
        
        return redirect('registerStep3')  # Proceed to the next step
    
    # Render the form with the template
    context = {
        'page': page,
        'page_title': page_title,
        'form': form
    }
    return render(request, 'registrations/form.html', context)


def registerStep3(request):
    page  = 'register_step3'
    page_title = 'Register'
    
    # Initialize an empty form or bind it with POST data
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
    else:
        form = ApplicationForm()
    
    # Handle form submission
    if request.method == 'POST' and form.is_valid():
        form_uuid = request.session.get('form_uuid')
        if not form_uuid:
            # Handle missing form UUID in session
            return redirect('error_page')  # Replace 'error_page' with your error-handling view
        
        # Retrieve the application object
        try:
            application = Application.objects.get(uuid=form_uuid)
        except Application.DoesNotExist:
            return redirect('error_page')  # Replace with your error-handling view
        
        # Update application with validated form data
        application.verification_type = form.cleaned_data.get('verification_type')
        application.verification_document_number = form.cleaned_data.get('verification_document_number')
        application.front_side_document = form.cleaned_data.get('front_side_document')
        application.back_side_document = form.cleaned_data.get('back_side_document')
        application.save()
        
        return redirect('registerSuccess')  # Proceed to the next step
    
    context = {
        'page': page,
        'page_title': page_title,
        'form':form
    }
    
    return render(request, 'registrations/form.html', context)

def registerStep4(request):
    page  = 'register_step4'
    page_title = 'Register'
    
    if request.method == 'POST':
        return redirect('registerSuccess')
    
    context = {
        'page': page,
        'page_title': page_title
    }
    
    return render(request, 'registrations/form.html', context)

def registerSuccess(request):
    page  = 'register_success'
    page_title = 'Register'
    
    context = {
        'page': page,
        'page_title': page_title
    }
    
    return render(request, 'registrations/success.html', context)