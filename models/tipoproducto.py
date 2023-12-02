# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoProducto(models.Model):
    _name = 'upobarber.tipoproducto'
    _description = 'Tipo de Producto'

    name = fields.Char(string="Tipo Producto", required=True, index=True)
    nombre = fields.Char(string="Nombre", required=True)

    producto_ids = fields.One2many('upobarber.producto', 'tipoproducto_id', string="Producto")