from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import Person, Award
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse

import random
import json

from tablib import Dataset
from import_export import resources

from django.core import serializers

# not available
def simple_upload(request):
    if request.method == 'POST':
        person_resource = resources.modelresource_factory(model=Person)()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'lottery/import.html')


def index(request):
	award_list = Award.objects.exclude(award_id=0)
	awards_not_done = Award.objects.filter(is_done=False)
	current_award = None
	if (awards_not_done):
		current_award = awards_not_done.last()
	
	person_list = Person.objects.filter(award=None)
	

	

	context = {
		'award_list': award_list,
		'person_list': person_list,
		'current_award': current_award,
	}
	
	return render(request, 'lottery/index.html', context)

def resetAward(request,award_id):
	current_award = Award.objects.get(award_id=award_id)
	current_award.is_done = False

	end= len(current_award.person_set.all())
	start = end -current_award.first_selection
	
	last_added_person_set = current_award.person_set.all()[start:end]
	for p in last_added_person_set:
		current_award.person_set.remove(p)


	current_award.save()
	return HttpResponseRedirect(reverse('lottery:index'))

def reloadPage(request):
	return HttpResponseRedirect(reverse('lottery:index'))

def doLottery(request, award_id):

	current_award = Award.objects.get(award_id=award_id)
	
	if not current_award :
		return

	award_num_diff = (current_award.award_amount-len(current_award.person_set.all()))
	if award_num_diff < current_award.first_selection : 
		current_award.first_selection = award_num_diff
		print(current_award.first_selection)

	p_list_all = list(Person.objects.filter(award=None).filter(is_attend=True))
	p_list_first_select =[]


	
	random_list = random.sample(range(len(p_list_all)),min(len(p_list_all),current_award.first_selection))


	for i in random_list:
		p_list_first_select.append(p_list_all[i])

	for p in p_list_first_select:
		p.award.add(current_award)
		p.save()
	
	award_num_diff = (current_award.award_amount-len(current_award.person_set.all()))
	if(award_num_diff==0):
		current_award.is_done = True

	current_award.save()

	end = len(current_award.person_set.all())
	start = end - current_award.first_selection
	
	serialized_qs = serializers.serialize('json', current_award.person_set.all()[start:end])
	data = { "queryset" : serialized_qs}
	return JsonResponse(data)
	#return HttpResponseRedirect(reverse('lottery:index'))