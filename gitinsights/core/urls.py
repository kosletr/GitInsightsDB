from django.urls import path
from . import views


urlpatterns = [

    path('users/', views.usersView.get, name='usersUrl'),
    path('users/search', views.usersView.search, name='usersSearchUrl'),
    path('users/<str:username>/', views.usersView.selected, name="selectedUserUrl"),


    path('repos/', views.reposView.get, name='reposUrl'),
    path('repos/search', views.reposView.search, name='reposSearchUrl'),
    path('repos/<int:id>/', views.reposView.selected, name="selectedRepoUrl"),
    path('repos/<int:id>/commits/<str:hash>',
         views.commitView.get, name="selectedRepoCommitUrl"),
    path('repos/<int:id>/issues/',
         views.reposView.issues, name="repoIssuesUrl"),
    path('repos/<int:id>/issues/<str:title>',
         views.reposView.issueSelected, name="selectedRepoIssueUrl"),
    path('repos/<int:id>/commits/<str:hash>/files/<str:filename>',
         views.commitView.commitSelected, name="selectedRepoCommitFileUrl"),


    path('orgs/', views.orgsView.get, name='orgsUrl'),
    path('orgs/search', views.orgsView.search, name='orgsSearchUrl'),
    path('orgs/<str:org_name>/', views.orgsView.selected, name="selectedOrgUrl"),
    path('orgs/<str:org_name>/teams/', views.orgsView.teams, name='orgTeamsUrl'),
    path('orgs/<str:org_name>/teams/<str:team_name>',
         views.orgsView.teamSelected, name="selectedOrgTeamUrl"),


    path('', views.indexView.index, name='indexUrl'),
    path('contact/', views.contactView.contact, name='contactUrl'),
    path('stats/', views.statsView.get, name='statsUrl')

]
