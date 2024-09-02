# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_hidden = fields.Boolean(string="Est cachée")

    def _prepare_invoice_line(self,**optional_values):
        res= super()._prepare_invoice_line(**optional_values)
        res.update({'is_hidden': self.is_hidden})
        return res

