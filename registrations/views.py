from django.shortcuts import render

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
    
    context = {
        'page': page,
        'page_title': page_title
    }
    
    return render(request, 'registrations/form.html', context)

def registerStep2(request):
    page  = 'register_step2'
    page_title = 'Register'
    
    context = {
        'page': page,
        'page_title': page_title
    }
    
    return render(request, 'registrations/form.html', context)

def registerStep3(request):
    page  = 'register_step3'
    page_title = 'Register'
    
    context = {
        'page': page,
        'page_title': page_title
    }
    
    return render(request, 'registrations/form.html', context)

def registerStep4(request):
    page  = 'register_step4'
    page_title = 'Register'
    
    context = {
        'page': page,
        'page_title': page_title
    }
    
    return render(request, 'registrations/form.html', context)

def registerStep5(request):
    page  = 'register_step5'
    page_title = 'Register'
    
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