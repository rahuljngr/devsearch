from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import Project, Tag 
from .forms import ProjectForm , ReviewForm
from django.contrib import messages
from .utils import searchProjects , paginationProjects


def projects(request):

    projects,search_query = searchProjects(request)
    custom_range, projects = paginationProjects(request,projects,6)    

    context = {'projects': projects,
     'search_query': search_query,'custom_range': custom_range}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm() 

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        
        projectObj.getVoteCount

        messages.success(request,'Your review was successfully submitted!')
        return redirect('project', pk=projectObj.id)
           
    context = {'project': projectObj, 'form':form}
    return render(request,'projects/single-projects.html',context)

@login_required(login_url='login')
def CreateProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method =='POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project =  form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tag.add(tag)

                
            return redirect('account')


    context = {'form':form}
    return render(request, 'projects/project_form.html',context)

@login_required(login_url='login')
def UpdateProject(request,pk):
    profile = request.user.profile
    projectt = profile.project_set.get(id = pk)
    form = ProjectForm(instance=projectt)

    if request.method =='POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        
        form = ProjectForm(request.POST,request.FILES, instance = projectt)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tag.add(tag)
                
            messages.success(request,'skill was updated successfully!')
            return redirect('account')


    context = {'form':form,'project': projectt}
    return render(request, 'projects/project_form.html',context)

@login_required(login_url='login')
def DeleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id = pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request,'skill was deleted successfully!')
        return redirect('account')
    context = {'object': project}
    return render(request,'delete_template.html',context)