from django import forms
from .models import Mystickynote

class MystickynoteForm(forms.Modelform):
    class Meta:
        model = Mystickynote
        fields = [
            'title',
            'description',
            'is_completed', 
            'created_by']                  
                  
    