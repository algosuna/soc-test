import csv

from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class UploadForm(forms.Form):

    upload = forms.FileField()

    def clean_upload(self):
        ''' Check that the uploaded file IS indeed a .csv '''
        upload = self.cleaned_data['upload']
        file_name = str(upload)

        if not file_name.endswith('.csv'):
            raise ValidationError('Please upload a CSV file.')

        return upload

    def save(self):
        '''
        It makes a dictionary of the CSV file, then it iterates it's rows and
        makes a dictionary of info per row. It creates a Contact if it
        doesn't already exist.
        Note: If an imported contact was modified it will import it again.
        '''
        upload = self.clean_upload()
        file_dialect = csv.Sniffer().sniff(upload.read(1024))
        csv_file = csv.DictReader(upload, dialect=file_dialect)

        for row in csv_file:
            values = {}

            for key, value in row.iteritems():
                values[key] = value

            obj, created = Contact.objects.get_or_create(**values)

        return


class ContactUpdateForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = []
