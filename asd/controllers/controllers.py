# -*- coding: utf-8 -*-
from odoo import http

# class Asd(http.Controller):
#     @http.route('/asd/asd/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asd/asd/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('asd.listing', {
#             'root': '/asd/asd',
#             'objects': http.request.env['asd.asd'].search([]),
#         })

#     @http.route('/asd/asd/objects/<model("asd.asd"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asd.object', {
#             'object': obj
#         })