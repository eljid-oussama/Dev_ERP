# -*- coding: utf-8 -*- 
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TestAbstract(models.AbstractModel):
    _name = 'test_abstract'
    _description = ' description de mon abstract model'

    # creation d'une fonction qui permet d'ajouter un suffixe au nom chaque qu'il est changé
    @api.onchange('name')
    def change_my_name(self):
        self.name = self.name + "un suffixe"


class Carpooling(models.Model):
    _name = 'carpooling.carpooling'  # nom de notre classe
    _description = """this a model for carpooling """  # description de la classe
    # mail.thread permet d'heriter du model responsable du mail
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Name', required=True)
    taken_seats = fields.Integer(string="Taken Seats", tracking=True)
    time_of_departure = fields.Float(string="Departue time")
    departure_date = fields.Date(string="Departure date")
    note = fields.Text('note')
    is_free = fields.Boolean('Est disponible')
    states = [('new', 'New'), ('available', 'Has seats available'), ('full', 'Full')]
    state = fields.Selection(selection=states, default='new')

    departure_city = fields.Char(string="Departure city")
    destination_city = fields.Char(string="Destination city")

    # fields.Many2one  représente une relation "many-to-one" avec un autre modèle. Dans ce cas, il fait référence au modèle res.currency, qui est le modèle des devises dans Odoo.
    # 'res.currency' : Indique que ce champ est une clé étrangère pointant vers le modèle res.currency.
    # string="Currency" : Définit l'étiquette (label) qui sera affichée dans l'interface utilisateur pour ce champ.
    # compute="_compute_company_currency" : Spécifie que la valeur de ce champ est calculée par une méthode, _compute_company_currency.
    # store=True : Indique que la valeur calculée de ce champ doit être stockée dans la base de données. Cela permet de réduire les calculs répétés et d'améliorer les performances lors des lectures de ce champ.
    company_currency = fields.Many2one('res.currency', string="Currency", compute="_compute_company_currency",store=True)

    # fields.Monetary est un type de champ qui représente un montant monétaire. Il est similaire à un champ Float, mais avec une fonctionnalité supplémentaire pour gérer les devises
    # string="Amount per km" : Définit l'étiquette qui sera affichée dans l'interface utilisateur pour ce champ.
    # currency_field="company_currency" : Spécifie que ce champ monétaire doit utiliser la devise définie dans le champ company_currency. Cela permet à Odoo d'afficher correctement les valeurs monétaires avec le symbole et le format de la devise appropriée.
    amount_per_km = fields.Monetary(string="Amount per km", currency_field="company_currency")

    # champ acceptant de l'html
    resume = fields.Html("Resume")

    # Ajout d'une image
    image = fields.Binary(string="Image")

    # Usage de Many2one
    car_id = fields.Many2one('car.car', string="Car")
    # Utilsation de related
    brand = fields.Char(string="Marque", related="car_id.brand")

    # Un champ de tag pour indiquer si un champ est court/long ou à l'étranger (Utilisation de Many2Many)
    tags_id = fields.Many2many('tag.tag', string="Tags")

    # Utilisation de << compute >> pour calculer le cout à la somme des kms

    km = fields.Float(string="KM")
    cost = fields.Monetary(string="Cost", currency_field="company_currency", compute="_compute_cost")

    def _compute_company_currency(self):
        for rec in self:
            rec.company_currency = self.env.company.currency_id.id

    # utilisation des constarins pour afficher des boites de dialoges d'erreurs
    @api.constrains('km')
    def _check_km(self):
        for rec in self:
            if rec.km < 0:
                raise ValidationError('You cannot add a negative km')

    # A cahque changement de depature_date le fct onchange s'active
    @api.onchange('departure_date')
    def onchange_time(self):
        self.increment_departure_time()

    @api.onchange('car_id')
    def onchange_car_id(self):
        # fait gaffe à ce que le search cherche direct depuis la db , laors que filtered chaerche dans la liste qu'on a retourné
        # c pour filtrer la liste : filtered(lambda car: "Voiture" in car.name)
        cars = self.env['car.car'].search([]).filtered(lambda car: "Voiture" in car.name).sorted(key=lambda car: car.name)
        # print(cars)
        # for car in cars:
        #   print(car.name)
        print(cars.mapped('brand'))

    @api.depends('km', 'amount_per_km')
    def _compute_cost(self):
        for rec in self:
            rec.cost = rec.amount_per_km * rec.km

    def increment_departure_time(self):
        for rec in self:
            rec.time_of_departure += 1
