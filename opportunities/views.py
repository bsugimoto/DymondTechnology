from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.utils import timezone
from django.urls import reverse

from .models import Opportunity

class OpportunityListView(ListView):
	model = Opportunity
	context_object_name = 'opportunities'
	template_name = 'opportunities_list.html'