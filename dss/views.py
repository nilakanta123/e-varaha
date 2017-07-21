from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from .models import Viral
from .forms import InputForm
from .utility import naive, getColumnData, getListFromString, allorganisms, findTable
import json

def home_view(request):

	if request.method == 'POST':
		
		form = InputForm(request.POST)

		if form.is_valid():
			type_of_organisms = form.cleaned_data['type_of_organisms']
			age_group = form.cleaned_data['age_group']
			system_affected = form.cleaned_data['system_affected']
			organ_affected = form.cleaned_data['organ_affected']
			causative_agent = form.cleaned_data['causative_agent']
			disease_condition = form.cleaned_data['disease_condition']
			am_findings = form.cleaned_data['am_findings']
			pm_findings = form.cleaned_data['pm_findings']

			table = findTable(type_of_organisms)

			result_dict = naive({"system_affected":[system_affected], "organ_affected":getListFromString(organ_affected),
			"age_group":[age_group], "disease_condition":[disease_condition],
			"type_of_organisms":[type_of_organisms], "causative_agent":[causative_agent],
			"am_findings":getListFromString(am_findings), "pm_findings":getListFromString(pm_findings), "table":table})

			return render(request, 'result.html', {'result': result_dict})


	else:
		form = InputForm()


	return render(request, 'home.html', {'form': form })

@csrf_exempt
def ajax_request(request):
    if request.method == 'POST' and request.is_ajax():
    	response_data = {}
    	if request.POST.get('post_table') == "":
    		response_data['table'] = "None Selected!!"
    	else:
    		table = findTable(request.POST.get('post_table'))
	    	response_data['table'] = table
	    	response_data['age'] = getColumnData('age_group',table)
	    	response_data['system'] = getColumnData('system_affected',table)
	    	response_data['organ'] = getColumnData('organ_affected',table)
	    	response_data['agent'] = getColumnData('causative_agent',table)
	    	response_data['disease'] = getColumnData('disease_condition',table)
	    	response_data['am'] = getColumnData('am_findings',table)
	    	response_data['pm'] = getColumnData('pm_findings',table)

    	return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
    	return render_to_response("home.html", locals())