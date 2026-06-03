from django import forms

from register_projects.models import Payment,StudentProject



class AdminLoginForm(forms.Form):

    username = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput)





class AddPaymentForm(forms.ModelForm):

    class Meta:

        model =StudentProject 

        fields = [
            'project_amount',
            'status',
        ]