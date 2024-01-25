from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Company, Director
from django.shortcuts import render, get_object_or_404
from .forms import DirectorForm, CompanyForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'cportal/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'cportal/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

def d(request):
    form = AuthenticationForm()
    return render(request, 'cportal/dashboard.html', {'form': form})

@login_required
def dashboard(request):
    comp_ls = Company.objects.filter(owner=request.user)
    return render(request, 'cportal/dashboard.html', {'comp_data': comp_ls})

@login_required
def companydetail(request, id):
    comp = get_object_or_404(Company, pk=id)
    return render(request, 'cportal/detail.html', {'comp': comp})

@login_required
def add_company(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST, prefix='company')
        director_form = DirectorForm(request.POST, prefix='director')
        if all([company_form.is_valid(), director_form.is_valid()]):
            company = company_form.save()
            director = director_form.save(commit=False)
            director.save()

            director.company.set([company])   

    else:

        company_form = CompanyForm(prefix='company')
        director_form = DirectorForm(prefix='director')

    return render(request, 'cportal/add_company.html', {'company_form': company_form, 'director_form': director_form})