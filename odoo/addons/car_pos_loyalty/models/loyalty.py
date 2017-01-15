# -*- coding: utf-8 -*-
# Copyright 2016 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, fields, models


_logger = logging.getLogger(__name__)

class LoyaltyProgram(models.Model):
    _name = 'loyalty.program'
    
    name = fields.Char('Loyalty Program Name', size=32, required=True)
    pp_currency = fields.Float('Points per currency')
    pp_product = fields.Float('Points per product')
    pp_order = fields.Float('Points per order')
    rounding = fields.Float('Points Rounding', default=1)
    rule_ids = fields.One2many('loyalty.rule', 'loyalty_program_id', 'Rules')
    reward_ids = fields.One2many('loyalty.reward', 'loyalty_program_id', 'Rewards')


class LoyaltyRule(models.Model):
    _name = 'loyalty.rule'
    
    name = fields.Char('Loyalty Program Name', size=32, required=True)
    loyalty_program_id = fields.Many2one('loyalty.program', 'Loyalty Program')
    type = fields.Selection([('product', 'Product'), ('category', 'Category')], 'Type', default='product')
    product_id = fields.Many2one('product.product', 'Target Product')
    category_id = fields.Many2one('pos.category', 'Target Category')
    cumulative = fields.Boolean('Cumulative')
    pp_product = fields.Float('Points per product')
    pp_currency = fields.Float('Points per currency')


class LoyaltyReward(models.Model):
    _name = 'loyalty.reward'
    
    name = fields.Char('Name', size=32, required=True, help='An internal identification for this loyalty reward')
    loyalty_program_id = fields.Many2one('loyalty.program', 'Loyalty Program', help='The Loyalty Program this reward belongs to')
    minimum_points = fields.Float('Minimum Points', help='The minimum amount of points the customer must have to qualify for this reward')
    type = fields.Selection((('gift','Gift'),('discount','Discount'),('resale','Resale')), 'Type', required=True, help='The type of the reward')
    gift_product_id = fields.Many2one('product.product','Gift Product', help='The product given as a reward')
    point_cost = fields.Float('Point Cost', help='The cost of the reward')
    discount_product_id = fields.Many2one('product.product','Discount Product', help='The product used to apply discounts')
    discount = fields.Float('Discount',help='The discount percentage')
    point_product_id = fields.Many2one('product.product', 'Point Product', help='The product that represents a point that is sold by the customer')
    
    @api.constrains('type', 'gift_product_id')
    @api.multi
    def _check_gift_product(self):
        for reward in self:
            if reward.type == 'gift':
                return bool(reward.gift_product_id)
            else:
                return True

    @api.constrains('type', 'discount_product_id')
    @api.multi
    def _check_discount_product(self):
        for reward in self:
            if reward.type == 'discount':
                return bool(reward.discount_product_id)
            else:
                return True
    
    @api.constrains('type', 'discount_product_id')
    @api.multi
    def _check_point_product(self):
        for reward in self:
            if reward.type == 'resale':
                return bool(reward.point_product_id)
            else:
                return True


class PosConfig(models.Model):
    _inherit = 'pos.config'
    
    loyalty_id = fields.Many2one('loyalty.program','Loyalty Program', help='The loyalty program used by this point_of_sale')


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    loyalty_points = fields.Float('Loyalty Points', help='The loyalty points the user won as part of a Loyalty Program')


class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    loyalty_points = fields.Float('Loyalty Points', help='The amount of Loyalty points the customer won or lost with this order')

    @api.model
    def _order_fields(self, ui_order):
        fields = super(PosOrder,self)._order_fields(ui_order)
        fields['loyalty_points'] = ui_order.get('loyalty_points',0)
        return fields

    @api.model
    def create_from_ui(self, orders):
        ids = super(PosOrder,self).create_from_ui(orders)
        for order in orders:
            if order['data']['loyalty_points'] != 0 and order['data']['partner_id']:
                partner = self.env['res.partner'].browse(order['data']['partner_id'])
                partner.write({'loyalty_points': partner['loyalty_points'] + order['data']['loyalty_points']})

        return ids
            
             
    
