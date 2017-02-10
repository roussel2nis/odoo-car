# -*- coding: utf-8 -*-
# Copyright 2016 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Car Pos',
    'description': """
        Add POS Customization""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Denis Roussel',
    'depends': ['point_of_sale',
                'product_print_labels',
    ],
    'data': [
        'views/product_label_sheet.xml',
    ],
    'demo': [
    ],
    'qweb': ['static/src/xml/pos.xml'],
    'application': False,
    'installable': True,
}
