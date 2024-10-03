from django.shortcuts import render, redirect, get_object_or_404
from .models import Mystickynote
from .forms import MystickynoteForm

def create (request):
    if request.method == 'POST':
        form = MystickynoteForm(request.POST)
        
        if form.is_valid():
            Mystickynote= form.save(commit=False)
            Mystickynote.save()
            return redirect('Mystickynote')
        
        else:
            form = MystickynoteForm()
            
            return render (request, 'Mystickynoteform.html',['form: form'])
        
        def get_all (request):
            Mystickynote=Mystickynote.object.all()
            
            context= {
            'Mystickynote': Mystickynote,
            'page_title': 'Show all Notes'
        }
            
            return render(request, 'allnotes.html,', context=context)
        
        def get(request, pk):
            Mystickynote= get_list_or_404(Mystickynote, pk=pk)
            
            return render (request, 'Mystickynote.html', context=context)
        
        def update(request, pk):
            Mystickynote = get_object_or_404 (Mystickynote, pk=pk)
            
            if request.method=='POST':
                form =MystickynoteForm(request.POST, instance=Mystickynote)
                
                if form.is_valid():
                    Mystickynote = form.saved(commit=False)
                    Mystickynote.save()
                    return redirect('Mystickynote')
                
                else:
                    form = Mystickynoteform()
                    
                    return render (request, 'Mystickynoteform.html',{'form:form'} )
                
                def delete(request, pk):
                    Mystickynote = get_object_or_404 (Mystickynote, pk=pk)
                    Mystickynote.delete()
                    return redirect('Mystickynote')