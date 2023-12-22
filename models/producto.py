# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Producto(models.Model):
    _name = 'upobarber.producto'
    _description = 'Productos de UpoBarber'

    name = fields.Char(string="ID Producto", required=True, index=True)

    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Modelo", required=True)
    foto = fields.Binary('Foto')
    
    tipoproducto_id = fields.Many2one('upobarber.tipoproducto', string="Tipo de Producto")
    articulo_ids = fields.One2many('upobarber.articulo', 'producto_id', "Articulo")
    
    _sql_constraints = [('producto_name_unique','UNIQUE (name)','El ID del producto ya existe')]
    
    def btn_generate_report(self):
          return self.env.ref('upobarber.report_productos').report_action(self)
    