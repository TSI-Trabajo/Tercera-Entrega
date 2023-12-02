# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MetodoPago(models.Model):
    _name = 'upobarber.metodopago'
    _description = 'upobarber MetodoPago'

    name = fields.Char(string="Title",required=True, help="Dame el metodo de pago")
    pago_ids = fields.One2many("upobarber.pago", 'metodo_id', 'Metodo Pago')

    #pago_id = fields.Many2One("upobarber.pago", string="Pago")