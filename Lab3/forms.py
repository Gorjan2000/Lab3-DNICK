from django import forms

from Lab3.models import Blog


class BlogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Blog
        exclude = ("avtor",)