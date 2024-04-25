from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SrodekTransportuAddForm(forms.Form):
    nazwa = forms.CharField(
        label="Nazwa",
        max_length=100,
        required=True
    )
    
    typ = forms.CharField(
        label="Typ",
        max_length=100,
        required=True
    )
    
    droga_przewozu = forms.ChoiceField(
        label="Droga przewozu",
        choices=( ("Ld","Lądowa"),("Mr","Morska"),("Pw","Powietrzna") ),
        required=True
    )
    
    przewoznik = forms.CharField(
        label="Przewoznik",
        max_length=100,
        required=True
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'SrodekTransportuAddId'
        self.helper.form_class = 'SrodekTransportuAddClass'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))
        
    
    def clean_nazwa(self):
        nazwa = self.cleaned_data['nazwa'] 
        return nazwa
    def clean_typ(self):
        typ = self.cleaned_data['typ'] 
        return typ
    def clean_droga_przewozu(self):
        droga_przewozu = self.cleaned_data['droga_przewozu'] 
        return droga_przewozu
    def clean_przewoznik(self):
        przewoznik = self.cleaned_data['przewoznik'] 
        return przewoznik