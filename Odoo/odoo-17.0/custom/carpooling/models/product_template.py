# -*- coding: utf-8 -*-
from odoo import models, fields, api
from random import randint

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    blacklist_countries_ids = fields.Many2many('res.country', string="Blacklist Countries")
    blacklist_contacts_ids = fields.Many2many('res.partner', string="Blacklist Contacts")

#fonction appele a la creation d'un produit , il genere un numero random qui sera le code barre
    def _create_new_barcode(self):
        current_seq = str(randint(1, 9999999999999)).zfill(13)
        #la on essaye d'ajouter des conditions sur le codebare (ici on l'oblge de commence par 4)
        while current_seq[0] != '4' and self.env['product.template'].search([('barcode', '=' , current_seq)]):
            current_seq = str(randint(1, 9999999999999)).zfill(13)
        self.barcode = current_seq

    @api.model_create_multi
    def create(self, vals_list):
        recs = super().create(vals_list)
        for rec in recs:
            if not rec.barcode:
                rec._create_new_barcode()
        return recs

