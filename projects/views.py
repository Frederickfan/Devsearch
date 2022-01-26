from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerce website.'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'This is the project for the portfolio website.'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'This is the project for the social network.'
    },
]

# Create your views here.
def projects(request):
    page = 'project'
    number = 2
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, './projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for project in projectsList:
        if int(project['id']) == int(pk):
            projectObj = project
    return render(request, 'projects/single-project.html', {'project': projectObj})
