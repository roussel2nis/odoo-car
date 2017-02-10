# -*- coding: utf-8 -*-
# Copyright 2017 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ProductLabelSheet(models.Model):

    _name = 'product.label.sheet'
    _description = 'Product Label Sheet'

    name = fields.Char()
    product_ids = fields.Many2many('product.product',
                                   'label_sheet_product_product_rel',
                                   'label_id',
                                   'product_id',
                                   'Products')
    
