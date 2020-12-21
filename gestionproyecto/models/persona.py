# -*- coding: utf-8 -*-

from odoo import models, fields, api

class persona(models.Model):
     _name ='proyecto.personas'
     name= fields.Char(string="Nombre", required=True)
     apellidos=fields.Char(string="Apellidos", required=True)
     fecha_ingreso=fields.Date(string="Fecha de ingreso", required=True)
     encargado_ids=fields.One2many('proyecto.general', 'encargado_id')
     miembro_ids=fields.One2many('proyecto.miembros','miembro_id')
     especialidad_id = fields.Many2one('persona.especialidad', string="Especialidad")
     departamento_id = fields.Many2one('departamento.general', string="Departamento")
     rut= fields.Char(string="Rut", required=True, )
     direccion=fields.Char(string="Dirección")
     fecha_nac=fields.Date(string="Fecha de nacimiento")

     ##
class rol(models.Model):
     _name = 'proyecto.roles'
     name=fields.Char(string="Rol", required=True)
     descripcion=fields.Char(string="Descripción")
     atributos=fields.Char(string="Atributos")
     rol_ids= fields.One2many('proyecto.miembros', 'rol_id')
     
class especialidad(models.Model):
     _name = 'persona.especialidad'
     name= fields.Char(string="Especialidad", required=True)
     descripcion=fields.Char()
     especialidad_ids = fields.One2many('proyecto.personas', 'especialidad_id')
     