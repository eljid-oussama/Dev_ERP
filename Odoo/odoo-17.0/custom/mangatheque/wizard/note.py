from odoo import models , fields

class DonnerNote(models.TransientModel):
    _name="donner.note"
    _description = "Pour donner une note"

    note = fields.Integer("Note (sur 10)")
    def donner_note(self):
        Manga = self.env['manga']
        manga_id = Manga.browse(self.env.context['manga_id'])
        manga_id.note = self.note

