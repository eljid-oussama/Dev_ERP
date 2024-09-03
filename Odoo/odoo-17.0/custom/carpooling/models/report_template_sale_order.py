# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class ReportTemplateSaleOrder(models.AbstractModel):
    _name = 'report.sale.report_saleorder'  #le nom de cet abstract model sera report.lenom du module.le nom del'action generante le rapport

    @api.model
    def _get_report_values (self, docids, data = None):
        #cette fonction ne fait que genere un message d'erreur pour les sales n'ayant pas de tags lors de la generation du rapport
        report = self.env['ir.actions.report']._get_report_from_name("sale. report_saleorder")
        for ele in docids:
            sale_order = self.env['sale.order'].browse(ele)  #docids est l'enselble dees docs avec leurs ids
            if not sale_order.tag_ids:
                raise UserError("You must set a tag on the sale order before printing")
        return {
            'doc ids': docids,
            'doc_model': report.model,
            'docs': self.env[report.model].browse(docids),
        }
