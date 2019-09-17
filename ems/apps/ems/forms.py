from django import forms
from .models import User
import json

CHOICES = [('select1', 'Label 1'),
           ('select2', 'Label 2')]
           
class UpdateSoftwareForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': False}))

class ElementForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    name = forms.CharField(max_length=30, widget=forms.TextInput
                           (attrs={'class': 'form-control', 'readonly': True}))
    status = forms.ChoiceField(choices=[('', "Select Status"), ], widget=forms.Select(
        attrs={'class': 'form-control'}))

    def clean_name(self):
        return self.cleaned_data['name']

    def clean_id(self):
        return self.cleaned_data['id']

    def clean_status(self):
        return self.cleaned_data['status']

    # def clean(self):
    #     super().clean()

    # def is_valid():

    def configure(self, options, element):

        self.fields["id"].initial = element.id
        self.fields["name"].initial = element

        if 'type' in options:
            if options['type'] == 'text':
                self.fields['status'] = forms.CharField(
                    max_length=30,
                    help_text=options['help_text'],
                    widget=forms.TextInput(attrs={'class': 'form-control'})
                )
            if options['type'] == 'select':
                self.fields['status'].choices = options['status']

            self.fields["status"].initial = element.status if element.status else options['default']
        if 'extras' in options:
            for extra in options['extras']:
                if extra['type'] == 'text':
                    self.fields[extra['name']] = forms.CharField(max_length=30, widget=forms.TextInput
                                                                 (attrs={'class': 'form-control'}))

                    if extra['name'] in element.configuration:
                        self.fields[extra['name']
                                    ].initial = element.configuration[extra['name']]

                if extra['type'] == 'select':
                    self.fields[extra['name']] = forms.ChoiceField(choices=[('', "Select Status"), ], widget=forms.Select(
                        attrs={'class': 'form-control'}))

                    self.fields[extra['name']].choices = extra['status']
                    if extra['name'] in element.configuration:
                        self.fields[extra['name']
                                    ].initial = element.configuration[extra['name']]

            # def is_valid(self):
            #     return True


class InterfaceForm(forms.Form):
    # name = forms.CharField(max_length=30, help_text='Interface name', widget=forms.TextInput
    #                        (attrs={'class': 'form-control'}))
    # self.status = forms.ChoiceField(
    #     choices=CHOICES, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(InterfaceForm, self).__init__(*args, **kwargs)

    def add_form_element(self, tags=None):
        pass
        if tags:
            # tags = json.loads(options)

            for field in tags:
                item = tags[field]
                if item['type'] == 'text':
                    pass

                if item['type'] == 'select':
                    self.fields[field] = forms.ChoiceField(
                        label=item['value'], choices=item['choices'], widget=forms.Select(
                            attrs={'class': 'form-control'}),
                    )

                if item['type'] == 'radio':
                    pass

                if item['type'] == 'check':
                    pass
                # question = 'hello'
                # self.fields[question] = forms.ChoiceField(
                #     label=question, choices=CHOICES, widget=forms.RadioSelect)

    def clean(self):
        cleaned_data = super(InterfaceForm, self).clean()
        name = cleaned_data.get('name')
        status = cleaned_data.get('status')

        if not name:
            raise forms.ValidationError('You have to write something!')


class Create_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def encrypt_string(hash_string):
        sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
        return sha_signature
