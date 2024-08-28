# -*- coding: utf-8 -*-
from odoo import models, fields, api
class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_driver = fields.Boolean(string="Conducteur")

    #ici on a modifie le cham email pour devenir Adresse email
    email = fields.Char(string="Adresse email")



    #ici en bas , on modifie le compute en ajoutant à la definition de base d'autres conditions
    @api.depends_context('lang')
    @api.depends('display_name')
    def _compute_display_name(self):
        super()._compute_display_name()
        for rec in self :
            if rec.is_driver:
                rec.display_name = rec.display_name + "Conducteur" if "Conducteur" not in rec.display_name  else rec.display_name
            else:
                rec.display_name =  rec.display_name.replace("Conducteur", "") if "Conducteur" not in rec.display_name  else rec.display_name