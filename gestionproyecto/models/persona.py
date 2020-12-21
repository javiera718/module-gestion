# -*- coding: utf-8 -*-

from odoo import models, fields, api

class persona(models.Model):
     _name ='proyecto.personas'
     name= fields.Char(String="Nombre", required=True)
     apellidos=fields.Char(String="Apellidos", required=True)
     encargado_ids=fields.One2many('proyecto.general', 'encargado_id')
     miembro_ids=fields.One2many('proyecto.miembros','miembro_id')
     
     ##
class rol(models.Model):
     _name = 'proyecto.roles'
     name=fields.Char(String="Rol", required=True)
     descripcion=fields.Char(String="Descripción")
     atributos=fields.Char(String="Atributos")
     rol_ids= fields.One2many('proyecto.miembros', 'rol_id')
     
