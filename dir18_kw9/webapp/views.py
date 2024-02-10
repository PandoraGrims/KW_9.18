from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Advertisement, Comment
from .forms import AdvertisementForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'index.html'
    context_object_name = 'advertisements'
    paginate_by = 6
    paginate_orphans = 3
    ordering = ('-published_at',)


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'advertisement_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisement_create.html'
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertisementUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'advertisement_edit.html'
    success_url = reverse_lazy('webapp:index')


class AdvertisementDeleteView(LoginRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'advertisement_delete.html'
    success_url = reverse_lazy('webapp:index')


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.advertisement = Advertisement.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:advertisement_detail', kwargs={'pk': self.kwargs['pk']})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('webapp:advertisement_detail', kwargs={'pk': self.object.advertisement.pk})
