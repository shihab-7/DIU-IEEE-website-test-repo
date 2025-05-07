from django.shortcuts import render, redirect, get_object_or_404
from .models import MemberProfile, Projects
from .forms import MemberProfileForm, ProjectForm, CustomUserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def profile_view(request):
    if request.user.is_superuser:
        try:
            profile = request.user.profile
        except MemberProfile.DoesNotExist:
            profile = None
    else:
        profile, created = MemberProfile.objects.get_or_create(user=request.user)
    projects = Projects.objects.filter(user=request.user)
    return render(request, 'profile.html', {'profile': profile, 'projects': projects})


@login_required
def edit_profile(request):
    profile = get_object_or_404(MemberProfile, user=request.user)
    user_instance = request.user

    if request.method == 'POST':
        profile_form = MemberProfileForm(request.POST, request.FILES, instance=profile)
        user_form = CustomUserEditForm(request.POST, instance=user_instance)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile_view')
    else:
        profile_form = MemberProfileForm(instance=profile)
        user_form = CustomUserEditForm(instance=user_instance)
    return render(request, 'edit_profile.html', {'profile_form': profile_form, 'user_form': user_form})


@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, 'Project added successfully!')
            return redirect('profile_view')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Projects, id=project_id, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('profile_view')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form, 'project': project})


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Projects, id=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('profile_view')
    return render(request, 'delete_project.html', {'project': project})