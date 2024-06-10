# -*- coding: utf-8 -*-
{
    'name': 'Oxp',
    'version': '17.0.1.0',
    'description': """ Oxp Description """,
    'summary': """ Oxp Summary """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web'],
    "data": [
        "views/templates.xml"
    ],'assets': {
            'web.assets_backend': [
                'oxp/static/src/**/*'
            ],
        },
    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
