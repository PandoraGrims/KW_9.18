from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from .models import Advertisement

from django.http import JsonResponse


def approve_ad(request):
    if request.method == 'POST' and request.is_ajax():
        ad_id = request.POST.get('ad_id')
        advertisement = Advertisement.objects.get(pk=ad_id)
        advertisement.status = 'published'
        advertisement.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def reject_ad(request):
    if request.method == 'POST' and request.is_ajax():
        ad_id = request.POST.get('ad_id')
        advertisement = Advertisement.objects.get(pk=ad_id)
        advertisement.status = 'rejected'
        advertisement.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@user_passes_test(lambda u: u.is_staff)
def new_advertisements(request):
    new_ads = Advertisement.objects.filter(status='moderation')
    return render(request, 'new_advertisements.html', {'new_ads': new_ads})
