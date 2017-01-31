# -*- coding: utf-8 -*-
# Copyright 2016 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Car All',
    'description': """
        All Dependencies""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Denis Roussel',
    'depends': ['sale',
                'purchase',
                'point_of_sale',
                'account',
                'account_accountant',
                'car_pos_loyalty',
                'pos_cache',
                'car_pos',
                'web_environment_ribbon',
                # Server tools
                'auto_backup',
                'server_environment_files',
                'server_environment',
                'server_environment_ir_config_parameter',
                'web_responsive',
                'base_technical_features',
    ],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': False
}
