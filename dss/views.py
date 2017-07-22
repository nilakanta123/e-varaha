from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from .models import Viral
from .forms import InputForm
from .utility import naive, naiveForDisease, naiveForAntimortem, naiveForPostmortem, getColumnData, getListFromString, allorganisms, findTable
import json

def home_view(request):

	if request.method == 'POST':
		
		form = InputForm(request.POST)

		if form.is_valid():
			decision_switch = request.POST.get('decision_switch')
			type_of_organisms = form.cleaned_data['type_of_organisms']
			age_group = form.cleaned_data['age_group']
			system_affected = form.cleaned_data['system_affected']
			organ_affected = form.cleaned_data['organ_affected']
			causative_agent = form.cleaned_data['causative_agent']
			disease_condition = form.cleaned_data['disease_condition']
			am_findings = form.cleaned_data['am_findings']
			pm_findings = form.cleaned_data['pm_findings']

			table = findTable(type_of_organisms)

			dic = {"system_affected":[system_affected], "organ_affected":getListFromString(organ_affected),
			"age_group":[age_group], "disease_condition":[disease_condition],
			"type_of_organisms":[type_of_organisms], "causative_agent":[causative_agent],
			"am_findings":getListFromString(am_findings), "pm_findings":getListFromString(pm_findings), "table":table}
			decision =""
			if decision_switch:
				decision_type = "antimortem"
				justment = naiveForAntimortem(dic)
			else:
				decision_type = "postmortem"
				justment = naiveForPostmortem(dic)
			disease =naiveForDisease(dic)

			result = []
			result.append({"disease": disease[0]['disease'], "disease_prob": disease[0]['prob'],
				"justment": justment[0]['decision'], "justment_prob": justment[0]['prob']})
			result.append({"disease": disease[1]['disease'], "disease_prob": disease[1]['prob'],
				"justment": justment[1]['decision'], "justment_prob": justment[1]['prob']})
			result.append({"disease": disease[2]['disease'], "disease_prob": disease[2]['prob'],
				"justment": justment[2]['decision'], "justment_prob": justment[2]['prob']})
			result.append({"disease": disease[3]['disease'], "disease_prob": disease[3]['prob'],
				"justment": justment[3]['decision'], "justment_prob": justment[3]['prob']})
			
			return render(request, 'result.html', {'decision_type': decision_type, "result": result})


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