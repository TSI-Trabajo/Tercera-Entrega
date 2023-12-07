# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Compra(models.Model):
    _name = 'upobarber.compra'
    _description = 'upobarber Compra'

    name = fields.Char(string="idCompra", index=True, required=True)
    importe = fields.Float(string="Importe", required=True)
    fechaCompra = fields.Datetime(
        string='Fecha de la compra',
        widget='datetime',
        options={'format': 'YYYY-MM-DD HH:mm:ss'},
    )

    pago_id = fields.Many2one('upobarber.pago', string="Concepto del pago")
    #cliente_id = fields.Many2one('upobarber.cliente', string="Cliente")
    articulo_id = fields.One2many('upobarber.articulo', 'compra_id', "Artículo")

    @api.constrains('importe')
    def _check_importe_valido(self):
        if self.importe <= 0:
            raise models.ValidationError('El importe debe ser un importe válido!!')
     
    @api.constrains('fechaCompra')
    def _chech_fecha_valida(self):
        if self.fechaCompra > datetime.now():
            raise models.ValidationError('La fecha debe ser una fecha válida!! No puede ser una fecha más tarde de la actual')

    sql_constraints = [
        ('name_uniq',
        'UNIQUE (name)',
        'El id de la compra debe ser único.')
    ]

    def btn_generate_report(self):
          return self.env.ref('upobarber.upobarber_compra_report').report_action(self)
