from odoo import models, fields, api


class Horario(models.Model):
     _name = 'upobarber.horario'
     _description = 'horario'

     name = fields.Integer(string="ID del horario", required=True, index=True)
     
     horarioInicio = fields.Datetime(required=True, string = "Horario Inicio")
     horarioFin = fields.Datetime(required=True, string = "Horario Fin")
     disponible = fields.Boolean(string="¿Disponible?")

     empleado_dnis = fields.Many2one("upobarber.empleado", string="Empleados")
     cita_id = fields.Many2one("upobarber.cita", string="Citas")

     @api.onchange('horarioFin')
     def onchange_empleado(self):
               resultado = {}
               if self.horarioFin < self.horarioInicio:
                    resultado = {
                         'value': {'horarioFin': self.horarioInicio},  # Corregir la cadena cerrando comillas
                         'warning': {
                              'title': 'Horario Incorrecto',
                              'message': 'El horario de fin no puede ser antes que el de inicio'
                         }
                    }
               return resultado
     
     def btn_ocupar_horario(self):
          self.write({'disponible':True})

     def btn_desocupar_horario(self):
          self.write({'disponible':False})
