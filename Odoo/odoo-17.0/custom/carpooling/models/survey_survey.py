# -*- coding: utf-8 -*-
from odoo import models, fields , api

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    campaign_id = fields.Many2one('utm.campaign', string='Campaign', help="The campaign this survey is linked to.")
    website_survey_id = fields.Many2one('website','Website', help="The website this survey is linked to.")
    is_creating_lead = fields.Boolean("Crée un lead")

