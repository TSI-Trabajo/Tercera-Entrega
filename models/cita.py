from odoo import models, fields, api


class Cita(models.Model):
     _name = 'upobarber.cita'
     _description = 'Citas de la peluqueria'

     name = fields.Integer(string="ID de la Cita",required=True)
     confirmada = fields.Boolean(string="¿Cita Confirmada?",default=True)
     pagado = fields.Boolean(string="¿Pagado?",default=False)
     nombre_del_cliente = fields.Char(related='cliente_id.nombre', string='Nombre del Cliente', readonly=True)

     horario_id = fields.One2many("upobarber.horario","cita_ids","Horario de la Cita")
     cliente_id = fields.Many2one("upobarber.cliente",'Dni Cliente')
     reserva_id = fields.Many2one("upobarber.reserva",'Reserva')
     #horario_ids = fields.One2many("upobarber.horario",'cita_id',"horario")
     #tipo_Servicio = fields.Many2one ("Upobarber.servicio", 'Nombre del Servicio')
     #pago_id  = fields.One2one ("upobarber.pago",'Pago')
     #reseña_ids = fields.Many2one ("upobarber.reseña",'Reseña')
     
     
     