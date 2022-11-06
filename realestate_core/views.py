from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm, CreateUserForm, CreateRealtorForm, CreateRealestateForm, RealtorForm, RealestateForm, \
     SellBuyForm
from .models import Realtor, Realestate, RealestateType


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            us = form.cleaned_data['username']
            pd = form.cleaned_data['password']
            user = authenticate(username=us, password=pd)
            if user is None:
                return render(request, 'form.html', {'form': form, 'message': "Niepoprawne dane"})
            else:
                login(request, user)
                url = request.GET.get('next', 'index')
                return redirect(url)
        return render(request, 'form.html', {'form': form, 'message': "Niepoprawne dane"})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class CreateUserView(View):

    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('create_user')
        return render(request, 'form.html', {'form': form})


class CreateRealtorView(LoginRequiredMixin, View):

    def get(self, request):
        form = CreateRealtorForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateRealtorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_realtor')
        return render(request, 'form.html', {'form': form})


class CreateRealestateView(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_authenticated

    def get(self, request):
        form = CreateRealestateForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateRealestateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_realestate')
        return render(request, 'form.html', {'form': form})


class RealtorListView(View):

    def get(self, request):
        realtors = Realtor.objects.order_by('title')
        return render(request, 'realtor_list.html', {'realtors': realtors})


class AllRealestatesView(View):

    def get(self, request):
        realestates = Realestate.objects.all()
        return render(request, 'realestate_list.html', {'realestates': realestates})


class EditRealtorView(LoginRequiredMixin, View):

    def get(self, request, id):
        realtor = Realtor.objects.get(pk=id)
        form = RealtorForm(instance=realtor)

        header = f"Edit Realtor {realtor.user}"
        return render(request, 'form.html', {'form': form, 'header': header})

    def post(self, request, id):
        realtor = Realtor.objects.get(pk=id)
        form = RealtorForm(request.POST, instance=realtor)
        if form.is_valid():
            form.save()
            return redirect('realtors')
        else:
            header = f"Edit Realtor {realtor.user}"
            return render(request, 'form.html', {'form': form, 'header': header})

class DeleteRealtorView(LoginRequiredMixin, View):

    def get(self, request, id):
        realtor = Realtor.objects.get(pk=id)
        realtor.delete()
        return redirect('realtor_list')


class EditRealestateView(LoginRequiredMixin, View):

        def get(self, request, id):
            realestate = Realestate.objects.get(pk=id)
            form = RealestateForm(instance=realestate)

            header = f"Edit Realestate {realestate.price}"
            return render(request, 'form.html', {'form': form, 'header': header})

        def post(self, request, id):
            realestate = Realestate.objects.get(pk=id)
            form = RealestateForm(request.POST, instance=realestate)
            if form.is_valid():
                form.save()
                return redirect('realestate_list')
            else:
                header = f"Edit Realestate {realestate.price}"
                return render(request, 'form.html', {'form': form, 'header': header})


class DeleteRealestateView(LoginRequiredMixin, View):

        def get(self, request, id):
            realestate = Realestate.objects.get(pk=id)
            realestate.delete()
            return redirect('realestate_list')


class SellBuyView(View):

    def get(self, request):
        sellbuy = RealestateType.objects.all()
        form = SellBuyForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = SellBuyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Sell_Buy')
        return render(request, 'form.html', {'form': form})

class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')