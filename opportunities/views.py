from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.urls import reverse

from .models import Opportunity

class OpportunityListView(ListView):
	model = Opportunity
	context_object_name = 'opportunities'
	template_name = 'opportunities_list.html'
	
class OpportunityDetailView(DetailView):
	model = Opportunity
	template_name = 'opportunity_details.html'

# def opportunity_details(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'opportunity_details.html', {'Opportunity': Opportunity})