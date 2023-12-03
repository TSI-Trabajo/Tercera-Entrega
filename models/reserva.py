from odoo import models, fields, api

class Reserva(models.Model):
     _name = 'upobarber.reserva'
     _description = 'Reservas de la peluquería.'

     name = fields.Char(string="IdReserva", size=60, required=True, help="Nombre del cliente")
     telefonoContacto = fields.Integer(string="Telefono",size = 9, help = "Telefono MOVIL de la peluquería")
     fechaReserva = fields.Date(string="Fecha Reserva", required=True, index=True, default=fields.Date.today())
     
     cita_id = fields.One2many("upobarber.cita",'reserva_id',string="Citas de la reserva")
     cliente_id = fields.Many2one("upobarber.cliente",'Cliente Reservante')