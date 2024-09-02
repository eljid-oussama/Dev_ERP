# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for rec in self :
            lines = rec.order_line.filtered(lambda x: rec.partner_id.id in x.product_id.blacklist_contacts_ids.ids or rec.partner_id.id in x.product_id.blacklist_countries_ids.ids)
            if lines:
                raise UserError("You cannot confirm this sale order because you have blacklisted the following contacts or countries")
            return res

