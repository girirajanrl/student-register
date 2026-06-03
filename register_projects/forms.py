from django import forms

from django.forms import modelformset_factory

from .models import StudentProject, TeamMember, Payment


class StudentProjectForm(forms.ModelForm):

    class Meta:

        model = StudentProject

        exclude = ['project_amount', 'status','reference_no']

        widgets = {

            'project_title': forms.TextInput(attrs={'class': 'form-control'}),

            'college_name': forms.TextInput(attrs={'class': 'form-control'}),

            'department': forms.TextInput(attrs={'class': 'form-control'}),

            'domain': forms.TextInput(attrs={'class': 'form-control'}),

            'team_members': forms.TextInput(attrs={'class': 'form-control'}),

        }
        


class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = ['paid_amount', 'payment_mode']

        widgets={
            
            'paid_amount': forms.TextInput(
                attrs={
                    
                    'class': 'form-control'
                }
            
            ),
            'payment_mode': forms.Select(attrs={'class': 'form-select'}),
        }

TeamMemberFormSet = modelformset_factory(
    
    TeamMember,
    fields=(
        'member_name',
        'member_contact',
        'member_email',
        
    ),
    extra=0
    
)