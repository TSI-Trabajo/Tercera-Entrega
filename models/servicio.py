from odoo import models, fields, api

class Servicio(models.Model):
    _name = 'upobarber.servicio'
    _description = 'Servicios Upobarber'

    nombre_servicio = fields.Char(string="Nombre")
    tipos_servicio_ids = fields.Many2many('upobarber.tiposervicio', string='Tipos de Servicio')

    @api.onchange('tipos_servicio_ids')
    def _onchange_tipos_servicio_ids(self):
        # Aggiorna il display_name del campo tipos_servicio_ids
        for servicio in self:
            servicio.tipos_servicio_ids = servicio.tipos_servicio_ids


    @api.depends('tipos_servicio_ids.precio')
    def _compute_total_precio(self):
        for servicio in self:
            servicio.precio_total = sum(servicio.tipos_servicio_ids.mapped('precio'))

    @api.depends('tipos_servicio_ids.tiempo')
    def _compute_total_tiempo(self):
        for servicio in self:
            servicio.tiempo_total = sum(servicio.tipos_servicio_ids.mapped('tiempo'))

    precio_total = fields.Float(string="Precio", compute='_compute_total_precio')
    tiempo_total = fields.Float(string="Tiempo", compute='_compute_total_tiempo')