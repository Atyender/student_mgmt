from django import forms
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders for date fields
        self.fields['date_of_birth'].widget.attrs.update({
            'placeholder': 'YYYY-MM-DD'
        })
        self.fields['enrollment_date'].widget.attrs.update({
            'placeholder': 'YYYY-MM-DD'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        student_id = self.instance.pk
        if Student.objects.filter(email=email).exclude(pk=student_id).exists():
            raise forms.ValidationError('A student with this email already exists.')
        return email

    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if grade < 1 or grade > 12:
            raise forms.ValidationError('Grade must be between 1 and 12.')
        return grade
