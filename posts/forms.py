from django import forms
from posts.models import Category

class PostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()

    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if title.lower and description and title.lower() == description.lower():
            raise forms.ValidationError("error")
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data["title"]
        if "python" in title.lower():
            raise forms.ValidationError("error")
        return title



class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "search", 'class': 'form-control'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )


    orderings = {
        ("created_at", "created_at"),
        ("updated_at", "updated_at"),
        ("rate", "rate"),
        ("-created_at", "-created_at"),
        ("-updated_at", "-updated_at"),
        ("-rate", "-rate"),
        }
    
    ordering = forms.ChoiceField(
        choices=orderings, required=False, widget=forms.Select(attrs={"class": "form-control"})
    )
