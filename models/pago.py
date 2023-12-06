# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pago(models.Model):
    _name = 'upobarber.pago'
    _description = 'upobarber Pago'

    #pago_id = fields.Integer(string="Id pago")
    importe = fields.Float(string="Importe total del pago")
    pagado = fields.Boolean(string="Pagado", default=False)

    metodo_id = fields.Many2one('upobarber.metodopago',string="Metodo Pago")
    #cita_id = fields.related('upobarber.cita', string="Cita")
    #compra_id = fields.Many2one('upobarber.compra', "Compra")