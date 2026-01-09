from django.shortcuts import render

def home(request):
    context = {'title': 'Home - Profile Saya', 'page': 'home'}
    return render(request, 'profile/home.html', context)

def about(request):
    context = {'title': 'About Me - Riwayat Pendidikan', 'page': 'about'}
    return render(request, 'profile/about.html', context)

def gallery(request):
    context = {'title': 'Gallery - Kegiatan Saya', 'page': 'gallery'}
    return render(request, 'profile/gallery.html', context)
