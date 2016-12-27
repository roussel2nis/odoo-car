# -*- coding: utf-8 -*-
# Copyright 2016 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Car Pos Loyalty',
    'description': """
        Add POS Loyalty Management""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Denis Roussel',
    'depends': ['point_of_sale'
    ],
    'data': ['security/ir.model.access.csv',
             'views/views.xml',
             'views/templates.xml'
    ],
    'demo': [
    ],
    'qweb': ['static/src/xml/loyalty.xml'],
    'application': False,
    'installable': True,
}
