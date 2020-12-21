# -*- coding: utf-8 -*-
from odoo import http

# class Gestionproyecto(http.Controller):
#     @http.route('/gestionproyecto/gestionproyecto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestionproyecto/gestionproyecto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestionproyecto.listing', {
#             'root': '/gestionproyecto/gestionproyecto',
#             'objects': http.request.env['gestionproyecto.gestionproyecto'].search([]),
#         })

#     @http.route('/gestionproyecto/gestionproyecto/objects/<model("gestionproyecto.gestionproyecto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestionproyecto.object', {
#             'object': obj
#         })