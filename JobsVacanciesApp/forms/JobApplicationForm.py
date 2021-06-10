from django import forms


from JobsVacanciesApp.models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        fields = ["pay_claim", "last_education", "experience"]
        widgets = {
            'experience': forms.Textarea(attrs={'rows': 4}),
        }