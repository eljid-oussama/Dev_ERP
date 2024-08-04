
from odoo import models , fields , api

class Tag(models.Model):
    _name = 'tag.tag'
    name = fields.Char(string="Tagy")
