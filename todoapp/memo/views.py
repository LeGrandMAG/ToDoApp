from django.shortcuts import redirect, render
from .forms import MemoForm
from .models import Memo 
from django.shortcuts import render, get_object_or_404
# Create your views here.

def DisplayMemo(request):
    memos = Memo.objects.all()
    if request.method == 'POST':
        form = MemoForm(request.POST)
        
        if form.is_valid():
            title = request.POST['title']
            description = request.POST['description']
            completed = True
            memo = Memo.objects.create(title=title, description=description,completed=completed)
            return redirect('/todo/')
    else:
        form = MemoForm()
    context = {'form':form, 'memos':memos }
    return render(request, 'memo/todo.html', context)

def MemoView(request):
    memos = Memo.objects.all()
    return render(request, 'memo/todo.html', {'memos':memos})
    
    
def deleteMemo(request, pk):
    bye = Memo.objects.get(id = pk)

    if request.method == 'POST':
        bye.delete()
        return redirect('/todo/')
    return render(request, 'memo/todo.html', {'object': bye})