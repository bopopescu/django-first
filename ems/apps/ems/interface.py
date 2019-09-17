"""
Interface Configuration Status Choice File
"""

form_interfaces = {}

form_interfaces['e1'] = {

    'type': 'select',
    'default': 'disabled',
    'help_text': 'Please choose the status of the Port',
    'status': [
        ('', "Select Port"),
        ('active', "Active"),
        ('disabled', "Disable"),
        ('unplugged', "Unplugged"),
    ],

    'extras': [
        {
            'name': 'ip_allocation',
            'type': 'select',
            'default': 'dhcp',
            'help_text': 'Please choose the status of the Port',
            'status': [
                ('', "Select Ip Allocation"),
                ('dhcp', "DHCP"),
                ('static', "Static"),
            ]
        },

        {
            'name': 'ip-address',
            'type': 'text',
            'default': '0.0.0.0',
            'help_text': 'Enter the ip',
        },
        {
            'name': 'netmask',
            'type': 'text',
            'default': '0.0.0.0',
            'help_text': 'Enter the gateway',
        },

    ]
}

form_interfaces['e3'] = {
    'type': 'select',
    'default': 'disabled',
    'help_text': 'Please choose the status of the Port',
    'status': [
        ('', "Select Port"),
        ('active', "Active"),
        ('disabled', "Disable"),
        ('unplugged', "Unplugged"),
    ],
    'extras': [
        {
            'name': 'Ip Allocation',
            'type': 'select',
            'default': 'dhcp',
            'help_text': 'Please choose the status of the Port',
            'status': [
                ('', "Select Ip Allocation"),
                ('dhcp', "DHCP"),
                ('static', "Static"),
            ]
        },

        {
            'name': 'ip-address',
            'type': 'text',
            'default': '0.0.0.0',
            'help_text': 'Enter the ip',
        },
    ]
}

form_interfaces['eth'] = {
    'type': 'select',
    'default': 'disabled',
    'help_text': 'Please choose the status of the Port',
    'status': [
        ('', "Select Status"),
        ('active', "Active"),
        ('disabled', "Disable"),
        ('unplugged', "Unplugged"),
    ],
    # 'extras': [
    #     {
    #         'name': 'Ip Allocation',
    #         'type': 'select',
    #         'default': 'dhcp',
    #         'help_text': 'Please choose the status of the Port',
    #         'status': [
    #             ('', "Select Ip Allocation"),
    #             ('dhcp', "DHCP"),
    #             ('static', "Static"),
    #         ]
    #     },
    # ]
}

form_interfaces['rotator'] = {
    'type': 'text',
    'default': '0',
    'help_text': 'Please enter the angle you want to rotate',
}
