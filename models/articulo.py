# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Articulo(models.Model):
    _name = 'upobarber.articulo'
    _description = 'Articulos Upobarber'
    
    name = fields.Char(string="Nombre", required=True)
    precio = fields.Float(string="Precio", required=True)
    stock = fields.Integer(string="Stock", required=True)

    producto_id = fields.Many2one('upobarber.producto', string='Producto Relacionado')

