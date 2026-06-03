from django import forms

from .models import Domain,Duration_add,Intership_mode

from django import forms


from .models import StudentIntern, Payment


class StudentInternForm(forms.ModelForm):

    class Meta:

        model = StudentIntern

        exclude = ['Intern_amount', 'status','referenceid','fees']

                      
                      
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),

            'contact_No': forms.TextInput(attrs={'class': 'form-control'}),

            'whatsapp_no': forms.TextInput(attrs={'class': 'form-control'}),

            'email': forms.EmailInput(attrs={'class': 'form-control'}),

            'college_name': forms.TextInput(attrs={'class': 'form-control'}),

            'degree': forms.TextInput(attrs={'class': 'form-control'}),

            'department_name': forms.TextInput(attrs={'class': 'form-control'}),

            'join_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'end_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'duration': forms.Select(attrs={'class': 'form-select'}),

            'domain': forms.Select(attrs={'class': 'form-select'}),

       
            'intership_mode': forms.Select(attrs={'class': 'form-select'}),
            
        }
    def __init__(self, *args, **kwargs):

                super().__init__(*args, **kwargs)

                self.fields['duration'].empty_label = "Select Duration"

                self.fields['domain'].empty_label = "Select Domain"

                self.fields['intership_mode'].empty_label = "Select Internship Mode"
                    
   
    


class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = ['amount', 'payment_mode']

        widgets={
            
            'amount':forms.TextInput(
                attrs={
                   
                    'class': 'form-control'
                }
            
            ),
            'payment_mode': forms.Select(attrs={'class': 'form-select'}),
        }

class Domainform(forms.ModelForm):

    class Meta:
        model = Domain

        fields = '__all__'

        widgets = {

            'Domain_name': forms.TextInput(attrs={'class': 'form-control'}),

        }
        
class Durationform(forms.ModelForm):

    class Meta:
        model = Duration_add

        fields = '__all__'

        widgets = {

            'mode_name': forms.TextInput(attrs={'class': 'form-control'}),

        }



class modeform(forms.ModelForm):

    class Meta:
        model = Intership_mode

        fields = '__all__'

        widgets = {

            'add_mode': forms.TextInput(attrs={'class': 'form-control'}),

        }    



