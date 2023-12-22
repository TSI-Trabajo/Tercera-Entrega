# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Articulo(models.Model):
    _name = 'upobarber.articulo'
    _description = 'Articulos Upobarber'
    
    name = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio", required=True)
    stock = fields.Integer(string="Stock", required=True)

    producto_id = fields.Many2one('upobarber.producto', string='Producto Relacionado')
    compra_id = fields.Many2many('upobarber.compra', string="Compras")

    
    _sql_constraints = [('articulo_name_unique','UNIQUE (name)','El Nombre del artículo ya existe')]

    @api.onchange('precio')
    def onchange_precio(self):
        resultado = {}
        if self.precio < 0:
            resultado = {
                'value': {'precio': 0},
                'warning': {
                        'title':'Precio incorrecto',
                        'message':'El precio no puede ser negativo'
                }
            }
            return resultado
        
    @api.onchange('stock')
    def onchange_stock(self):
        resultado = {}
        if self.stock < 0:
            resultado = {
                'value': {'stock': 0},
                'warning': {
                        'title':'Stock incorrecto',
                        'message':'El stock no puede ser negativo'
                }
            }
            return resultado 
        
    def btn_generate_report(self):
          return self.env.ref('upobarber.report_articulos').report_action(self)
      
    def btn_generate_report_graph(self):
          return self.env.ref('upobarber.report_articulos_graph').report_action(self)