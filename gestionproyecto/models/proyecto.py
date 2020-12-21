# -*- coding: utf-8 -*-

from odoo import models, fields, api


    
#class proyecto(models.Model):
#     _name = 'proyecto.general'
#     name = fields.Char(string="Nombre proyecto", required=True)
#     
#     encargado = fields.Char(string="Encargado", required=True)
#     date_contract = fields.Date(string="Fecha de Inicio")
#     date_contract = fields.Date("Fecha de Termino")
     
     
class proyecto(models.Model):
     _name = 'proyecto.general'
     name = fields.Char(string="Nombre proyecto", required=True)
     encargado_id = fields.Many2one('proyecto.personas', string="Encargado")
     fecha_inicio= fields.Date(string="Fecha de Inicio")
     fecha_termino=fields.Date(string="Fecha de termino")
     
     miembros_ids = fields.One2many('proyecto.miembros', 'miembros_id', string="Miembros del equipo")
class personas(models.Model):
     _name ='proyecto.personas'
     name= fields.Char(String="Nombre", required=True)
     apellidos=fields.Char(String="Apellidos", required=True)
     encargado_ids=fields.One2many('proyecto.general', 'encargado_id')
     miembro_ids=fields.One2many('proyecto.miembros','miembro_id')
     
     
class rol(models.Model):
     _name = 'proyecto.roles'
     name=fields.Char(String="Rol", required=True)
     descripcion=fields.Char(String="Descripción")
     rol_ids= fields.One2many('proyecto.miembros', 'rol_id')
     
class detalleMiembros(models.Model):
     _name ='proyecto.miembros'
     miembros_id= fields.Many2one('proyecto.general', string="Miembro del equipo")
     miembro_id= fields.Many2one('proyecto.personas', string="Miembro del equipo")

     rol_id= fields.Many2one('proyecto.roles', string="Rol")
     
     