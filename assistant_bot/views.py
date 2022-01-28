from django.shortcuts import render
from .models import AddressBook
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import TemplateView, CreateView, ListView, UpdateView


class HomePage(TemplateView):
    template_name = "homepage.html"


class AddressBookCreate(CreateView):
    model = AddressBook
    fields = "__all__"
    template_name = "addressbook_add.html"
    success_url = reverse_lazy("homepage")


class AddressBookView(ListView):
    model = AddressBook
    template_name = "addressbook_listview.html"
    context_object_name = "contacts"


def delete_addressbook(response, pk):
    model = AddressBook.objects.filter(id=pk)
    model.delete()
    return render(
        response, "addressbook_listview.html", {"contacts": AddressBook.objects.all()}
    )
