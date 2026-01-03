from django import forms

class AadharForm(forms.Form):
    AadharNumber = forms.CharField(max_length=14, min_length=12)
    FullName = forms.CharField(max_length=10)
    PhoneNumber=forms.CharField(max_length=10,min_length=10)
    Date_Of_Birth = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2026)))
    Gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    Address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
    Email = forms.EmailField()
    Image = forms.ImageField(required=False)
    Created_at=forms.DateTimeField(widget=forms.HiddenInput(),required=False)

    def __str__(self):
        return f"{self.FullName} - {self.AadharNumber}"
    