from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.forms import formset_factory

from fides.models.project import (Project, ProjectPage, )
from fides.forms.project.wizard_forms import (WizardBasicDetails, ProjectPagePrevisualAssesmentForm, )


@login_required
def wizard_project_basic_site_details(request):
    form = WizardBasicDetails()

    if request.method == 'POST':
        form = WizardBasicDetails(request.POST)

        if form.is_valid():
            project = form.save()

            return redirect(reverse('wizard-project-scrape-site', kwargs={ 'project_codename': project.codename }))    

    return render(request, 'project/wizard/basic_site_details.html', {
        'form': form,
    })


@login_required
def wizard_project_scrape_site(request, project_codename):
    project = get_object_or_404(Project, codename=project_codename)

    return render(request, 'project/wizard/scrape_site.html', {
        'project': project,
    })


@login_required
def wizard_project_add_pages(request, project_codename):
    project = get_object_or_404(Project, codename=project_codename)

    if request.method == 'POST':
        urls = request.POST.get('urls')

        project.bulk_add_pages(urls)

        return redirect(reverse('wizard-project-visual-assesment', kwargs={ 'project_codename': project.codename }))    
    
    return render(request, 'project/wizard/add_pages.html', {
    })


@login_required
def wizard_project_visual_assesment(request, project_codename):
    project = get_object_or_404(Project, codename=project_codename)
    previsual_assesment_formset = formset_factory(ProjectPagePrevisualAssesmentForm)

    if request.method == 'POST':
        previsual_assesment_formset = previsual_assesment_formset(request.POST)
        if previsual_assesment_formset.is_valid():
            for form in previsual_assesment_formset:
                previsual_assesment = form.save()
                previsual_assesment.project = project
                previsual_assesment.save()

            return redirect(reverse('wizard-project-build-dataset'))  

    return render(request, 'project/wizard/visual_assesment.html', {
        'previsual_assesment_formset': previsual_assesment_formset,
    })


@login_required
def wizard_project_build_dataset(request):

    return render(request, 'project/wizard/build_dataset.html', {
    })


@login_required
def delete_page(request):
    comma_separated_page_ids = request.GET.get('page_ids')
    page_ids = comma_separated_page_ids.split(',')
    pages = ProjectPage.objects.filter(id__in=page_ids)
    project = pages[0].project

    pages.delete()

    return redirect(reverse('wizard-project-scrape-site', kwargs={ 'project_codename': project.codename }))