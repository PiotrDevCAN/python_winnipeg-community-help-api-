from django import forms

class VolunteerForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")
    phone_number = forms.CharField(max_length=15, label="Phone Number")
    availability = forms.ChoiceField(
        choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')],
        label="Availability"
    )
    start_date = forms.DateField(widget=forms.SelectDateWidget, label="Start Date")
