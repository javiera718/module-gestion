# -*- coding: utf-8 -*-
{
    'name': "gestionproyecto",

    'summary': """
      modulo gestion de proyecto""",

    'description': """
        sistema que permite visualizar la organización del personal
    """,

    'author': "javiera",
    'website': "http://www.modulogestion.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
      'security/ir.model.access.csv',
        'views/view_proyecto.xml',
        'views/view_persona.xml',
        'views/view_roles.xml',
        'views/view_especialidad.xml',
        'views/view_departamento.xml'
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
  #  'demo': [
   #     'demo/demo.xml',
    #],
}