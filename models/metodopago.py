# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MetodoPago(models.Model):
    _name = 'upobarber.metodopago'
    _description = 'upobarber MetodoPago'

    name = fields.Char(string="Id método pago", required=True)

    metodos = fields.Char(string="Método del Pago", required=True)
    pago_ids = fields.One2many('upobarber.pago', 'metodo_id', "Metodo Pago")

    sql_constraints = [
        ('name_uniq',
        'UNIQUE (name)',
        'El id del método de pago debe ser único.')
    ]