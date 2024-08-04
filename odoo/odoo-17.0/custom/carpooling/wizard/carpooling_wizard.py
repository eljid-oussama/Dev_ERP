from odoo import models , fields
from odoo.exceptions import ValidationError

class CarpoolingWizard(models.TransientModel):
    _name= 'carpooling_wizard'
    _description = 'Crapooling wizard'

   #!!! La on est train de creer un wizard qui cherche des trajets
    departure = fields.Char(string='Departure City')
    destination =fields.Char(string='Destination City')
    departure_date = fields.Date(string='Departure date')

    def search_trip(self):
        carpool = self.env['carpooling.carpooling'].search([
            ('departure_city', '=', self.departure),
            ('destination_city', '=', self.destination),
            ('departure_date', '=', self.departure_date)
        ])

        if carpool:
            raise ValidationError(f'Un carpool correspondant à votre demande existe. Carpool id {carpool.id}')
        else:
            raise ValidationError(f'Pas de carpool correspondant à votre demande existe.')
