from django import forms
class PollsterForm(forms.ModelForm):
    class Meta: #inner Class / container
        fields=[
            "title",
            "description",
            'price',
        ]