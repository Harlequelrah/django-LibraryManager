from django import forms
class BookForm(forms.Forms):
    title=forms.CharField(max_length=30,label='Titre',widget=forms.TextInput(attrs={'class':'book--input'}))
    description=forms.CharField(max_length=100,label='description',widget=forms.Textarea(attrs={'class':'book--input'}))
    title = forms.CharField(
        max_length=30, label="Titre", widget=forms.TextInput(attrs={"class": "input"})
    )
