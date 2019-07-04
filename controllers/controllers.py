# -*- coding: utf-8 -*-
from odoo import http

# class SabaPickings(http.Controller):
#     @http.route('/saba_pickings/saba_pickings/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saba_pickings/saba_pickings/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saba_pickings.listing', {
#             'root': '/saba_pickings/saba_pickings',
#             'objects': http.request.env['saba_pickings.saba_pickings'].search([]),
#         })

#     @http.route('/saba_pickings/saba_pickings/objects/<model("saba_pickings.saba_pickings"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saba_pickings.object', {
#             'object': obj
#         })