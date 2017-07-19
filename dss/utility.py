from .models import Viral
from django.apps import apps

def getListFromString(slist):
	if slist:
		alist = slist.split("'")
		alist.remove('[')
		alist.remove(']')
		return list(filter(lambda a: a != ', ', alist))
	else:
		return []
			

def getColumnData(col,table):
	model = apps.get_model('dss', table)
	kw =col+'__isnull'
	query_set = model.objects.filter(**{kw: False}).values_list(col, flat=True).distinct()
	data = []
	for query in query_set:
		data.append({'value': query, 'label': query})
	return data
def getOrganismForTable(table):
	model = apps.get_model('dss', table)
	query_set = model.objects.filter(type_of_organisms__isnull=False).values_list('type_of_organisms', flat=True).distinct()
	return query_set

def findTable(types):
	for table in ["Bacterial", "Viral", "Genetic", "NonInfectious", "Parasitic", "VitaminMinerals"]:
		if types in getOrganismForTable(table):
			return table

def allorganisms():
	orglist = []
	for table in ["Bacterial", "Viral", "Genetic", "NonInfectious", "Parasitic", "VitaminMinerals"]:
		for item in getOrganismForTable(table):
			orglist.append(item)
	return orglist


# find decision using naive bayes algorithm.
def naive(dic):
	model = apps.get_model('dss', dic['table'])
	diseases = model.objects.filter(disease_condition__isnull=False).values_list('disease_condition', flat=True).distinct()
	final_disease_prob = 0.0
	final_disease = ""
	for disease in diseases:
		p1=probc("system_affected", dic, "disease_condition", disease, model)
		p2=probc("organ_affected", dic, "disease_condition", disease, model)
		p3=probc("age_group", dic, "disease_condition", disease, model)
		p4=probc("am_findings", dic, "disease_condition", disease, model)
		p5=proba("disease_condition", disease, model)

		prob = p1*p2*p3*p4*p5

		if final_disease_prob < prob:
			final_disease_prob = prob
			final_disease = disease
		print ("  ")
		print ("Probability of disease_condition = "+disease+" is "+str(prob))
		print ("  ")
	print ("  ")
	print ("###   FINAL DECISION IS Disease_condition = "+final_disease+" with probability "+str(final_disease_prob)+"    ###")
	print ("  ")
	print ("  ")

	am_decisions = model.objects.filter(am_decision__isnull=False).values_list('am_decision', flat=True).distinct()
	final_amd_prob = 0.0
	final_amd = ""
	for am_d in am_decisions:
		p1=probc("system_affected", dic ,"am_decision", am_d, model)
		p2=probc("organ_affected", dic ,"am", am_d, model)
		p3=probc("age_group", dic ,"am_decision", am_d, model)
		p4=probc("disease_condition", dic ,"am_decision", am_d, model)
		p5=probc("type_of_organisms", dic ,"am_decision", am_d, model)
		p6=probc("causative_agent", dic ,"am_decision", am_d, model)
		p7=probc("am_findings", dic ,"am", am_d, model)
		p8=proba("am_decision",am_d, model)

		prob = p1*p2*p3*p4*p5*p6*p7*p8

		if final_amd_prob < prob:
			final_amd_prob = prob
			final_amd = am_d
		print ("  ")
		print ("Probability of Antimortem Decision = "+am_d+" is "+str(prob))
		print ("  ")

	print ("  ")
	print ("  ")
	print ("######    FINAL DECISION IS Antimortem Decision = "+final_amd+" with probability "+str(final_amd_prob)+"  #######")

	return {"disease" : final_disease, "am_dec" : final_amd}

# sum all the probabilities if the column have multiple items for specific decision column 
def probc(colname, dic, decision, decvalue, model):
	sum = 0.0
	for colvalue in dic[colname]:
		i = probb(colname, colvalue, decision, decvalue, model)
		print ("Probability of "+ colname +" = "+ colvalue +" | "+ decision +" = "+decvalue+" is "+str(i))
		if i:
			sum += i
		else:
			sum += 0.0

	if sum == 0.0:
		sum = 0.00001

	return sum


# find probability of a=x given b=y
def probb(a,x,b,y, model):
	# SELECT COUNT(*) FROM Viral WHERE a IS x AND b IS y;
	# SELECT COUNT(*) FROM Viral WHERE b IS y;
	fe = model.objects.filter(**{a: x, b: y}).count()
	te = model.objects.filter(**{b: y}).count()

	if te != 0:
		prob = fe/float(te)
	else:
		prob = 0.0
	
	return prob


# find probalility of a=x.
def proba(a,x,model):
	kw =a+'__isnull'
	fe = model.objects.filter(**{a: x}).count()
	te = model.objects.exclude(**{kw: True}).count()
	if te != 0:
		prob = fe/float(te)
	else:
		prob = 0.0
	
	return prob

	