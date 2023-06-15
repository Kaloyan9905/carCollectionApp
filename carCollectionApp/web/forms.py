from django import forms
from carCollectionApp.web.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {'password': forms.PasswordInput}


class ProfileCreateForm(ProfileBaseForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    pass


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].disabled = True
        self.fields['model'].disabled = True
        self.fields['year'].disabled = True
        self.fields['image_url'].disabled = True
        self.fields['price'].disabled = True
