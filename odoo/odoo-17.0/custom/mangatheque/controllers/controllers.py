# -*- coding: utf-8 -*-
# from odoo import http


# class Mangatheque(http.Controller):
#     @http.route('/mangatheque/mangatheque', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mangatheque/mangatheque/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mangatheque.listing', {
#             'root': '/mangatheque/mangatheque',
#             'objects': http.request.env['mangatheque.mangatheque'].search([]),
#         })

#     @http.route('/mangatheque/mangatheque/objects/<model("mangatheque.mangatheque"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mangatheque.object', {
#             'object': obj
#         })

