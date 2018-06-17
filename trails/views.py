from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models

class TrailCreateView(LoginRequiredMixin, CreateView):
	model = models.Trail
	template_name = 'trail_new.html'
	fields = ['title', 'about', 'image', 'difficulty']
	login_url = 'login'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class TrailListView(ListView):
	model = models.Trail
	template_name = 'trail_list.html'

	# queryset = Trail.objects.all().order_by('date')

	# def get_queryset(self):
	# 	return Trail.objects.all()

class TrailDetailView(DetailView):
	model = models.Trail
	template_name = 'trail_detail.html'

class TrailUpdateView(LoginRequiredMixin, UpdateView):
	model = models.Trail
	fields = ['title', 'about', 'image',]
	template_name = 'trail_edit.html'
	login_url = 'login'

class TrailDeleteView(LoginRequiredMixin, DeleteView):
	model = models.Trail
	template_name = 'trail_delete.html'
	login_url = 'login'
	success_url = reverse_lazy('trail_list')

success_url = reverse_lazy('trail_list')

# class AboutUsView(DetailView):
# 	template_name = 'about_us.html'