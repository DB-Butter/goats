from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.urls import reverse
# import models
from .models import Goat, Expertise, CustomGoat
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customgoats"] = CustomGoat.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class GoatsList(TemplateView):
    template_name = "goats_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["goats"] = Goat.objects.filter(name__icontains=name, user=self.request.user)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["goats"] = Goat.objects.filter(user=self.request.user)
            # default header for not searching 
            context["header"] = "The Goats"
        return context

class GoatCreate(CreateView):
    model = Goat
    fields = ['name', 'img', 'bio']
    template_name = "goat_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GoatCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('goat_detail', kwargs={'pk': self.object.pk})

class GoatDetail(DetailView):
    model = Goat
    template_name = "goat_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customgoats"] = CustomGoat.objects.all()
        return context

class GoatUpdate(UpdateView):
    model = Goat
    fields = ['name', 'img', 'bio']
    template_name = "goat_update.html"
    success_url = "/allgoats/"

    def get_success_url(self):
        return reverse('goat_detail', kwargs={'pk': self.object.pk})

class GoatDelete(DeleteView):
    model = Goat
    template_name = "goat_delete_confirmation.html"
    success_url = "/allgoats/"

class ExpertiseCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        strength = request.POST.get("strength")
        goat = Goat.objects.get(pk=pk)
        Expertise.objects.create(title=title, strength=strength, goat=goat)
        return redirect('goat_detail', pk=pk)

class CustomGoatExpertiseAssoc(View):

    def get(self, request, pk, expertise_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            CustomGoat.objects.get(pk=pk).expertises.remove(expertise_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            CustomGoat.objects.get(pk=pk).expertises.add(expertise_pk)
        return redirect('/')

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("goats_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

