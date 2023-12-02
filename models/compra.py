# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Compra(models.Model):
    _name = 'upobarber.compra'
    _description = 'upobarber Compra'

    #compra_id = fields.Integer(string="idCompra")
    importe = fields.Float(string="Importe")
    fechaCompra = fields.Datetime(string="Fecha Compra")

    #pago_id = fields.related('upobarber.Pago', string="Pago")
    #cliente_id = fields.One2many('upobarber.cliente', 'dniCliente', "Cliente")