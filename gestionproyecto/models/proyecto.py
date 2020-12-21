# -*- coding: utf-8 -*-

from odoo import models, fields, api


     
class proyecto(models.Model):
     _name = 'proyecto.general'
     name = fields.Char(string="Nombre proyecto", required=True)
     encargado_id = fields.Many2one('proyecto.personas', string="Encargado")
     fecha_inicio= fields.Date(string="Fecha de Inicio")
     fecha_termino=fields.Date(string="Fecha de termino")
     estado=fields.Selection([('Activo','Activo'),('Pendiente','Pendiente'),('Inactivo','Inactivo')])
          
          
     miembros_ids = fields.One2many('proyecto.miembros', 'miembros_id', string="Miembros del equipo")

     
class detalleMiembros(models.Model):
     _name ='proyecto.miembros'
     miembros_id= fields.Many2one('proyecto.general', string="Miembros del equipo")
     miembro_id= fields.Many2one('proyecto.personas', string="Nombre")

     rol_id= fields.Many2one('proyecto.roles', string="Rol")
     
     