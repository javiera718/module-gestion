# -*- coding: utf-8 -*-
from odoo import http

# class Ejemplo(http.Controller):
#     @http.route('/ejemplo/ejemplo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo/ejemplo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo.listing', {
#             'root': '/ejemplo/ejemplo',
#             'objects': http.request.env['ejemplo.ejemplo'].search([]),
#         })

#     @http.route('/ejemplo/ejemplo/objects/<model("ejemplo.ejemplo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo.object', {
#             'object': obj
#         })