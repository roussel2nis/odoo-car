# -*- coding: utf-8 -*-
# Copyright 2017 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ProductLabelSheetTemplate(models.Model):

    _name = 'product.label.sheet.template'
    _description = 'Product Label Sheet Template'

    name = fields.Char()
    paperformat_id = fields.Many2one('report.paperformat',
                                     required=True)
    
    nb_col = fields.Integer('Columns number')
    nb_row = fields.Integer('Rows Number')

    print_logo = fields.Boolean('Print logo')
    print_barcode = fields.Boolean('Print Barcode')
    
    barcode_field = fields.Many2one('ir.model.field','Barcode Field',
                                     domain=[('model', '=', 'product.product')])