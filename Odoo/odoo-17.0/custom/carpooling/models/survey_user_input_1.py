# -*- coding: utf-8 -*-
from odoo import models, fields , api

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    def _mark_done(self):
        res = super(SurveyUserInput, self)._mark_done()
        for rec in self.filtered(lambda k: k.survey_id.is_creating_lead):
            lead = self.env['crm.lead'].create({
                'email_form': rec.email,
                'name' : rec.survey_id.title + '' + rec.email,
                'survey_id': rec.survey_id.id,
                'campaign_id': rec.survey_id.campaign_id.id,
                'website': rec.survey_id.website_survey_id.name,
                'type': 'lead',
            })
            note = '<p>'
            for line in rec.user_input_line_ids:
                note += line.question_id.display_name + ':' + line.display_name + '<br />'
            note += '</p>'
            lead.description = note