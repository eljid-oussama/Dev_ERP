# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Car(models.Model):
    _name ='car.car'
    name = fields.Char(string="Marque")

    #avec one2many ce champ sert à lier une voiture à toutes les trajets qu'il avait effectué liaison via le champ car_id(Car)
    carpoolong_ids = fields.One2many('carpooling.carpooling', 'car_id' ,string="Carpoolings")

    brand = fields.Char(string="Marques")

