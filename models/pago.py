# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pago(models.Model):
    _name = 'upobarber.pago'
    _description = 'upobarber Pago'

    _rec_name = 'concepto'

    name = fields.Char(string="Id pago", required=True, index=True)
    pagado = fields.Boolean(string="Pagado", default=False)
    
    boolean_pagado_contar = fields.Integer(string="Estado de los pagos", compute='_compute_contar_pagado', store=True)
    
    concepto = fields.Char(string="Concepto del pago", required=True)

    metodo_id = fields.Many2one('upobarber.metodopago',string="Metodo Pago")
    #cita_id = fields.Many2one('upobarber.cita', string="Pago de la Cita")
    compra_id = fields.Many2one('upobarber.compra', string="Compra")

    string_poner_pagado = fields.Char(string="Estado de los pagos para imprimir", compute='_compute_poner_pagado', store=True)
    
    @api.depends('pagado')
    def _compute_poner_pagado(self):
        for record in self:
            if(record.pagado):
                record.string_poner_pagado = "Pagado"
            else:
                record.string_poner_pagado = "No Pagado"  

    @api.depends('pagado')
    def _compute_contar_pagado(self):
        for record in self:
            record.boolean_pagado_contar = self.search_count([('pagado','=',True)])

    sql_constraints = [
        ('name_uniq',
        'UNIQUE (name)',
        'El id del pago debe ser único.')
    ]

    def btn_generate_report(self):
          return self.env.ref('upobarber.upobarber_pago_report').report_action(self)