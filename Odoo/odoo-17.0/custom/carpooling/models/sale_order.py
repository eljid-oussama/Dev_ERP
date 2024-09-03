# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo.exceptions import UserError
import logging



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    agency_id = fields.Many2one('res.partner', 'Agences' , readonly=True)
    #s represente le sale_order
    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['agency_id'] = "s.agency_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
          s.agency_id"""
        return res
