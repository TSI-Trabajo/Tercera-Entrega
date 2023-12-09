from odoo import models, fields, api
from datetime import datetime

class Cita(models.Model):
      _name = 'upobarber.cita'
      _description = 'Citas de la peluqueria'

      name = fields.Char(string='ID de la Cita', required=True)
      confirmada = fields.Boolean(string="¿Cita Confirmada?",default=True)
      pagado = fields.Boolean(string="¿Pagado?",default=False)
     
      start_date = fields.Datetime(related='horario_id.horarioInicio', string = 'Hora de Inicio', readonly=True)
      end_date = fields.Datetime(related='horario_id.horarioFin', string = 'Hora de Fin', readonly=True)
     
      cliente_id = fields.Many2one("upobarber.cliente",'Dni Cliente')
      reserva_id = fields.Many2one("upobarber.reserva",'Reserva')
      horario_id = fields.One2many("upobarber.horario",'cita_id','Horario')
      pago_id  = fields.One2many("upobarber.pago",'cita_id','Pago')
      #tipo_Servicio = fields.Many2one ("Upobarber.servicio", 'Nombre del Servicio')
      #reseña_ids = fields.Many2one ("upobarber.reseña",'Reseña')
     
      _sql_constraints = [('cita_id_unico', 'UNIQUE (name)', 'El ID de la Cita debe ser único.')]

      def btn_confimarCita(self):
            citas_pagadas = self.env['upobarber.cita'].search([('cliente_id', '=', self.id), ('pagado', '=', True)])
           