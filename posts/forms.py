from django import forms

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


        