from Home.models import RegisterUser, SurveyPost , Workshop,ShortCourse,Feedback
from django import forms
from django.forms import DateField


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = RegisterUser
        fields = ['name', 'userName', 'email', 'password']


class SurveyPostForm(forms.ModelForm):

            class Meta:
                model = SurveyPost
                fields = ['title','description','link']


class WorkshopForm(forms.ModelForm):

    class Meta:
        model = Workshop
        fields = ['title', 'description','SDate','time','duration','fee','venue','instructor', 'status']


class ShortCourseForm(forms.ModelForm):
    class Meta:
        model = ShortCourse
        fields = ['title', 'description','SDate','time','duration','fee','venue','instructor']



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'postTitle','email','message']
