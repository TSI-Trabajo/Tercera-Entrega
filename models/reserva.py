from odoo import models, fields, api

class Reserva(models.Model):
     _name = 'upobarber.reserva'
     _description = 'Reservas de la peluquería.'

     name = fields.Integer(string="IdReserva", required=True, help="ID de la reserva")
     telefonoContacto = fields.Integer(string="Telefono",default='123456789', help = "Telefono MOVIL de la peluquería",readonly=True)
     fechaReserva = fields.Date(string="Fecha Reserva", required=True,help = "Fecha en la que se hizo la Reserva", index=True, default=fields.Date.today())
     clienteReservante = fields.Char(related='cliente_id.nombre',string="Cliente Reservante", readonly=True)
     pagada = fields.Boolean(related='cita_id.pagado', string='Cita de la Reserva', readonly=True)
     
     cita_id = fields.One2many("upobarber.cita",'reserva_id',string="Citas de la reserva")
     cliente_id = fields.Many2one("upobarber.cliente",'DNI Cliente Reservante')
     
     def obtener_nombre_cliente(self):
          if self.cita_id:
               cita_pagada = self.cita_id.pagado
               # Hacer algo con el nombre del cliente
          else:
               # Manejar el caso cuando no hay una cita asociada
               cita_pagada
               
     _sql_constraints = [('reserva_id_unico', 'UNIQUE (name)', 'El ID de la Reserva debe ser único.')]
     
     def btn_eliminarCitas(self):
          self.write({'cita_id':[(5,)]})
          
     def btn_eliminarCitasNoPagadas(self):
          if(self.pagada == False):
                    self.write({'cita_id':[(5,)]})