from django.template.response import TemplateResponse
from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect


def get_username(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/index/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = index()

    return render(request, 'index.html', {'form': form})


class indexView():

    def index(request):
        return TemplateResponse(request, 'index.html')


class commitView():

    def addCommit(request):
        return TemplateResponse(request, 'addCommit.html')

    def searchCommit(request):
        return TemplateResponse(request, 'searchCommit.html')


class issueView():
    def addIssue(request):
        return TemplateResponse(request, 'addIssue.html')

    def searchIssue(request):
         return TemplateResponse(request, 'searchIssue.html')


class organizationView():

    def addOrganization(request):
        return TemplateResponse(request, 'addOrganization.html')

    def searchOrganization(request):
        return TemplateResponse(request, 'searchOrganization.html')


class repoView():
    def addRepo(request):
        return TemplateResponse(request, 'addRepo.html')

    def searchRepo(request):
        return TemplateResponse(request, 'searchRepo.html')


class teamView():
    def addTeam(request):
        return TemplateResponse(request, 'addTeam.html')

    def searchTeam(request):
        return TemplateResponse(request, 'searchTeam.html')


class userView():
    def addUser(request):
        return TemplateResponse(request, 'addUser.html')

    def searchUser(request):
         return TemplateResponse(request, 'searchUser.html')


class contactView():

    def contact(request):
        return TemplateResponse(request, 'contact.html')
