from urllib import response

import pytest
from django.test import Client
from django.urls import reverse
from .forms import CreateRealtorForm, RealtorForm, CreateRealestateForm, RealestateForm
from realestate_core.forms import CreateRealtorForm
from realestate_core.models import Realtor, Realestate


# Create your tests here.
def test_index():
    client = Client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200
    assert 'Login' in str(response.content)


@pytest.mark.django_db
def test_login_post(user):
    client = Client()
    url = reverse('login')
    data = {
        'username': user.username,
        'password': 'jakub'
    }
    response = client.post(url, data)
    assert response.status_code == 302

@pytest.mark.django_db
def test_logout(user):
    client = Client()
    client.force_login(user)
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.django_db
def test_create_realtor_get(user):
    client = Client()
    client.force_login(user)
    url = reverse('create_realtor')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, CreateRealtorForm)

@pytest.mark.django_db
def test_create_realtor_post(user):
    client = Client()
    client.force_login(user)
    url = reverse('create_realtor')
    data = {
        'user': user.id,
        'bio': 'asdf',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(url)
    assert Realtor.objects.get(user__username='jakub')

@pytest.mark.django_db
def test_edit_realtor_get(user, realtor):
    client = Client()
    client.force_login(user)
    url = reverse('edit_realtor', args=(realtor.id,))
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, RealtorForm)



@pytest.mark.django_db
def test_edit_realtor_post(user, realtor):
    client = Client()
    client.force_login(user)
    url = reverse('edit_realtor', args=(realtor.id,))
    data = {
        'bio': 'yyy',
    }
    response = client.post(url, data)
    assert response.status_code == 200
    assert Realtor.objects.get(bio=realtor.bio)
    url = reverse('realtor_list')


@pytest.mark.django_db
def test_delete_realtor_get(user, realtor):
    client = Client()
    client.force_login(user)
    url = reverse('delete_realtor', args=(realtor.id,))
    response = client.get(url)
    assert realtor.delete()
    assert response.status_code == 302

@pytest.mark.django_db
def test_realtor_list_get(user):
    client = Client()
    client.force_login(user)
    url = reverse('realtor_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_realestate_get(user):
    client = Client()
    client.force_login(user)
    url = reverse('create_realestate')
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, CreateRealestateForm)


@pytest.mark.django_db
def test_create_realestate_post(user):
    client = Client()
    client.force_login(user)
    url = reverse('create_realestate')
    data = {
        'price': 300000,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(url)
    assert Realestate.objects.get()


@pytest.mark.django_db
def test_edit_realestate_get(user, realestate):
    client = Client()
    client.force_login(user)
    url = reverse('edit_realestate', args=(realestate.id,))
    response = client.get(url)
    assert response.status_code == 200
    form_in_view = response.context['form']
    assert isinstance(form_in_view, RealestateForm)

@pytest.mark.django_db
def test_edit_realestate_post(user, realestate):
    client = Client()
    client.force_login(user)
    url = reverse('edit_realestate', args=(realestate.id,))
    data = {
        'price': 400000,
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Realestate.objects.get()
    url = reverse('realestate_list')



@pytest.mark.django_db
def test_delete_realestate_get(user, realestate):
    client = Client()
    client.force_login(user)
    url = reverse('delete_realestate', args=(realestate.id,))
    response = client.get(url)
    assert realestate.delete()
    assert response.status_code == 302

@pytest.mark.django_db
def test_realestate_list_get(user):
    client = Client()
    url = reverse('realestate_list')
    response = client.get(url)
    assert response.status_code == 200

