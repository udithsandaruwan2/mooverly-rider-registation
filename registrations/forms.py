from django.forms import ModelForm
from .models import Application
from django import forms

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        
        widgets = {
            'birth_day': forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'Udith', 'required': 'required'}
        )
        
        self.fields['middle_name'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'Sandaruwan', 'required': 'required'}
        )
        
        self.fields['last_name'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'Konara', 'required': 'required'}
        )
        
        self.fields['full_name'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'K M Udith Sandaruwan Konara', 'required': 'required'}
        )
        
        self.fields['nic'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': '123456789V', 'required': 'required'}
        )
        
        self.fields['birth_day'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': '1990-01-01', 'required': 'required'}
        )
        
        self.fields['gender'].widget.attrs.update(
            {'class': "form-control custom-input", 'required': 'required'}
        )
        
        self.fields['mobile_number_1'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': '+94771234567', 'required': 'required'}
        )
        
        self.fields['mobile_number_2'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': '+94771234567', 'required': 'required'}
        )
        
        self.fields['whatsapp_number'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': '+94771234567', 'required': 'required'}
        )
        
        self.fields['verification_type'].widget.attrs.update(
            {'class': "form-control custom-input", 'name': 'verification_type', 'required': 'required'}
        )
        
        self.fields['verification_document_number'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': '123456789', 'name': 'verification_document_number', 'required': 'required'}
        )
        self.fields['address_line_1'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'No 123', 'name': 'address_line_1', 'required': 'required'}
        )
        
        self.fields['address_line_2'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'Main Street', 'name': 'address_line_2', 'required': 'required'}
        )
        
        self.fields['address_line_3'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'Colombo', 'name': 'address_line_3', 'required': 'required'}
        )
        
        self.fields['description'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'Description', 'rows': 6, 'name': 'description', 'required': 'required'}
        )
        
        self.fields['working_type'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': 'Full Time', 'name': 'working_type', 'required': 'required'}
        )
        
        self.fields['possible_working_hours'].widget.attrs.update(
            {'class': "form-control custom-input", 'placeholder': '9am - 5pm', 'name': 'possible_working_hours', 'required': 'required'}
        )
        
        self.fields['front_side_document'].widget.attrs.update(
            {'class': "form-control custom-input", 'name': 'front_side_document', 'required': 'required'}
        )
        
        self.fields['back_side_document'].widget.attrs.update(
            {'class': "form-control custom-input", 'name': 'back_side_document', 'required': 'required'}
        )
        
        self.fields['video'].widget.attrs.update(
            {'class': "form-control custom-input", 'type': 'file', 'id': 'video-input', 'name': 'video', 'accept': 'video/webm', 'hidden': 'hidden', 'required': 'required'}
        )
