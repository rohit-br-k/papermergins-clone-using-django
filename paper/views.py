from django.shortcuts import get_object_or_404, render,redirect
from .models import Bookmark, Folder,Files
from .forms import FilesForm
from django.conf import settings
import os
from django.http import HttpResponse,Http404
# Create your views here.


def index(request):
    folder = Folder.objects.all()
    if request.method == 'POST':
        name = request.POST['folder']
        folder=Folder(name=name)
        folder.save()
        return redirect('paper:home')
    context={
        "folder":folder,
    }
    return render(request,'index.html',context)


def folder(request,id):
    folder = Folder.objects.get(pk=id)
    files = folder.files_set.all()
    if request.method == 'POST':
        fileName = request.POST['fileName']
        data = request.FILES['data']
        allData = Files(folder=Folder.objects.get(pk=id),fileName=fileName,data=data)
        allData.save()
        return redirect('paper:folder',id)
    
    context={
        'files':files,
    }

    return render(request,'folder.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
    results = Files.objects.filter(fileName__icontains=keyword)
    context={
        "result":results,
    }
    return render(request,'search.html',context)

def bookmark_view(request):
    bookmarked_files = Bookmark.objects.all()
    context={
        'bookmark':bookmarked_files,
    }
    return render(request,'bookmark.html',context)

def bookmark(request,id):
    # allFiles =
    file = get_object_or_404(Files,pk=id)
    saved = Bookmark.objects.create(name=file.fileName,files=file)
    saved.save()
    context={
        'bookmark':saved,
    }
    return redirect('paper:folder',id)

def bookmark_remove(request,id):
    get_bookmarked_file = Bookmark.objects.get(pk=id)
    get_bookmarked_file.delete()
    return redirect('paper:bookmark_view')