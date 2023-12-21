# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tiposervicio(models.Model):
    _name = 'upobarber.tiposervicio'
    _description = 'Tipo de Servicio'

    
    tipo_servicio = fields.Char(string="Tipo Servicio", required=True, index=True)
    descripcion = fields.Char(string="descripcion", required=True)
    precio = fields.Float(string="Precio", required=True)
    tiempo = fields.Float(string="Tiempo", required=True)

    @api.depends('precio', 'tiempo')
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.tipo_servicio))
        return result

    def btn_generar_report(self):
        return self.env.ref('upobarber.upobarber_tiposervicio_template').report_action(self)
