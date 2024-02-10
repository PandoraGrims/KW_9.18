from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Advertisement, Comment
from .forms import AdvertisementForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'crud/index.html'
    context_object_name = 'advertisements'
    paginate_by = 6
    paginate_orphans = 3
    ordering = ('-published_at',)


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'crud/advertisement_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


#
# class AdvertisementCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'advertisement_create.html'
#     model = Advertisement
#     form_class = AdvertisementForm
#
#     def form_valid(self, form):
#         advertisement = form.save(commit=False)
#         advertisement.author = self.request.user
#         advertisement.save()
#         form.save_m2m()
#         return redirect('webapp:advertisement_detail', pk=advertisement.pk)


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'crud/advertisement_create.html'
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertisementUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'crud/advertisement_edit.html'
    success_url = reverse_lazy('webapp:index')


# class AdvertisementDeleteView(LoginRequiredMixin, DeleteView):   Обычное удаление, оставил специально
#     model = Advertisement
#     template_name = 'crud/advertisement_delete.html'
#     success_url = reverse_lazy('webapp:index')

class AdvertisementDeleteView(UpdateView):
    model = Advertisement
    fields = []
    template_name = 'crud/advertisement_delete.html'
    success_url = reverse_lazy('webapp:index')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.status = 'deleted'
        return super().form_valid(form)


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
