from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .forms import Create_Form

# from .models import Site, Interface, Element, State, Notification, Temperature, CDR, Help

from .models import *

from django.conf import settings
from .forms import InterfaceForm
from .forms import ElementForm, UpdateSoftwareForm
from .interface import form_interfaces
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import json
from .models import User
from hashlib import sha256
import crypt
@login_required(login_url='login')
def create(request):
    if request.method == 'GET':
        create_form = Create_Form()
        return render(request,'create.html',{'form':create_form})
    if request.method == 'POST':
        form = Create_Form(request.POST)
        if form.is_valid():
            hash_string = form.cleaned_data['password']
            form.cleaned_data['password'] = form.encrypt_string(hash_string)
            form.save()
        return HttpResponse('User Created')


@login_required(login_url='login')
def index(request):
    site = Site.objects.get(pk=1)
    interfaces = Interface.objects.all()
    context = {'site': site, 'interfaces': interfaces,
               'device': settings.DEVICE_TYPE}
    return render(request, 'index.html', context=context)


@login_required(login_url='login')
def interfaces(request):
    site = Site.objects.get(pk=1)
    interfaces = Interface.objects.all()
    context = {'site': site, 'interfaces': interfaces,
               'device': settings.DEVICE_TYPE}
    return render(request, 'interfaces.html', context=context)


@login_required(login_url='login')
def element(request, interface):
    if request.method == 'POST':
        # print(request.POST['id'], request.POST['status'])
        element = Element.objects.get(pk=request.POST['id'])
        element.status = request.POST['status']
        # Start extraction of extra information from the request #
        try:
            misc_extra = json.loads(element.configuration)
        except ValueError as ve:
            misc_extra = {}

        key = request.POST['interface']

        if 'extras' in form_interfaces[key]:

            extras = form_interfaces[key]['extras']
            for extra in extras:
                extra_value = request.POST[extra['name']]
                misc_extra[extra['name']] = extra_value

            element.configuration = json.dumps(misc_extra)
            # End of extraction of extra information fromt the request #

        element.save()
        return HttpResponseRedirect(reverse("ems_interfaces"))

    else:

        site = Site.objects.first()
        interface = Interface.objects.get(pk=interface)
        elementals = []
        key = interface.name.lower()
        options = form_interfaces.get(key, None)
        if options:
            for element in interface.elements.all():

                try:
                    element.configuration = json.loads(element.configuration)
                except ValueError as ve:
                    element.configuration = {}

                form = ElementForm()
                form.configure(options, element)
                elementals.append(form)

        return render(request, 'former.html', context={'interface': key, 'elementals': elementals})

        form = InterfaceForm()
        options = {}
        elements = [(element.id, element)
                    for element in interface.elements.all()]  # List Comprehension to collect all element as list

        options['e1'] = {'value': 'E1 Status',
                         'type': 'select', 'choices': elements}

        options['status'] = {'value': 'Status', 'type': 'select', 'choices': [('enable', 'Enable'),
                                                                              ('disable',
                                                                               'Disable'),
                                                                              ('unplugged', 'Unplugged')]}

        form.add_form_element(options)

        context = {'site': site, 'interface': interface,
                   'device': settings.DEVICE_TYPE, 'form': form}

        return render(request, 'interface.html', context=context)


@login_required(login_url='login')
def ems_logs(request):
    return HttpResponse('EMS Logs')


"""
Alarms records
Returns:
    [type] -- [description]
"""
@login_required
def ems_alarms(request):
    alarms = Notification.objects.filter(
        of_type=0).filter(is_active=1).all()
    return render(request, 'alarms.html', {'alarms': alarms})


"""
Events records
Returns:
    [type] -- [description]
"""
@login_required
def ems_events(request):
    events = Notification.objects.filter(of_type=1).all()
    {'events': events}
    return render(request, 'events.html', {'events': events})


"""
Call details records
Returns:
    [type] -- [description]
"""
@login_required(login_url='login')
def ems_cdr(request):
    cdrs = CDR.objects.order_by('-is_active').all()
    return render(request, 'cdr.html', {'cdrs': cdrs})


@login_required(login_url='login')
def ems_temperature(request):
    temperature = Temperature.objects.all()
    context = {'temperature': temperature}
    return render(request, 'temperature.html', context=context)


"""
To provide the update functionalilty for the system

Returns:
    render html or redirect

"""
@login_required(login_url='login')
def ems_update_software(request):
    if request.method == 'POST':
        form = UpdateSoftwareForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_software = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(uploaded_software.name, uploaded_software)
            uploaded_software_file = fs.url(filename)
            messages.add_message(
                request, messages.SUCCESS, 'New Update Uploaded, will be updating software shortly')

        return HttpResponseRedirect(reverse('homepage'))

    if request.method == 'GET':
        form = UpdateSoftwareForm()
        return render(request, 'update_software.html', {'form': form})


"""
Customary Help Topics to handle ems
Returns:
    html -- [description]
"""
@login_required
def help(request):
    helps = Help.objects.all()
    return render(request, 'help.html', {'helps': helps})


@login_required
def ems_import(request):
    return HttpResponse('Import Settings to the database TBD')


@login_required
def ems_export(request):
    return HttpResponse("Export Settings TDB")
