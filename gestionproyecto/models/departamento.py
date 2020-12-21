# -*- coding: utf-8 -*-

from odoo import models, fields, api

class departamento(models.Model):
     _name ='departamento.general'
     name= fields.Char(string="Nombre", required=True)
     direccion=fields.Char(string="Direccion", required=True)
     email=fields.Char(string="Email", required=True)
     celu = fields.Integer(string="Teléfono")
     departamento_ids= fields.One2many('proyecto.personas', 'departamento_id')
