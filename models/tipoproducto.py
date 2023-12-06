# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoProducto(models.Model):
    _name = 'upobarber.tipoproducto'
    _description = 'Tipo de Producto'

    name = fields.Char(string="Tipo Producto", required=True, index=True)
    nombre = fields.Char(string="Nombre", required=True)

    producto_ids = fields.One2many('upobarber.producto', 'tipoproducto_id', string="Producto")
    
    _sql_constraints = [('tipoproducto_name_unique','UNIQUE (name)','El Tipo de producto ya existe')]
    
    def btn_eliminarProductos(self):
          self.write({'producto_ids':[(5,)]})
          
    def btn_generate_report(self):
          return self.env.ref('upobarber.report_tipoproductos').report_action(self)