from odoo import models, fields, api


class Cita(models.Model):
     _name = 'upobarber.cita'
     _description = 'Citas de la peluqueria'

     name = fields.Integer (string="ID de la Cita", index=True, required=True)
     confirmada = fields.Boolean(string="¿Cita Confirmada?", default=True)
     pagado = fields.Boolean(string="¿Pagado?", default=False)

     
     horario_id = fields.One2many("upobarber.horario","cita_ids","Horario de la Cita")
     cliente_id = fields.Many2one("upobarber.cliente",'Cliente')
     reserva_id = fields.Many2one("upobarber.reserva",'Reserva')
     #pago_id  = fields.One2one ("upobarber.pago",'Pago')
     #reseña_id = fields.Many2one ("upobarber.reseña",'Reseña')
     #tipo_Servicio = fields.Many2one ("Upobarber.servicio",stirng = " Nombre del Servicio")
     
     
     