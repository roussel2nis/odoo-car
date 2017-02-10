# -*- coding: utf-8 -*-
# Copyright 2017 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Product Print Labels',
    'description': """
        Adds label printing support""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Denis Roussel',
    'depends': ['report'
    ],
    'data': [
        'security/product_label_sheet_template.xml',
        'views/product_label_sheet_template.xml',
        'security/product_label_sheet.xml',
        'views/product_label_sheet.xml',
    ],
    'demo': [
        'demo/product_label_sheet_template.xml',
        'demo/product_label_sheet.xml',
    ],
}
