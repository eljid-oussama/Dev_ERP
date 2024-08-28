# -*- coding: utf-8 -*-
from odoo import models, api
from odoo.exceptions import UserError


class CarpoolingReport(models.AbstractModel):
    # l'idee est de creer un model abstrait pour controller l'impression des rapports
    _name = 'report.carpooling.template_car_travelling'
    _description = 'Carpooling Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['carpooling.carpooling'].browse(docids) #les objets carpoolings
        #la lgne en bas pr testeer si un carpool n'a pas de departure date
        if not  all(d.departure_date for d in docs):
            raise UserError('Please set a departure date on all carpooling records.')
        return {
            'doc_ids': docids,
            'doc_model': 'carpooling.carpooling',
            'docs': docs,
            'data': data,
        }
