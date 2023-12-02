from odoo import models, fields, api

class Cliente(models.Model):
     _name = 'upobarber.cliente'
     _description = 'Clientes de la peluquería.'

     name = fields.Char(String = "DNI" , required=True, help="DNI del cliente ; FORMATO = 'IIIIIIII-S'")
     nombre = fields.Char(string="Nombre", size=50, required=True, help="Nombre del cliente")
     apellidos = fields.Char(string="Apellidos", size=50, required=True, help="Primer y Segundo apellidos del cliente")
     telefono = fields.Integer(string="Telefono",size = 9, required=True, help = "Telefono MOVIL del cliente")
     correoElectronico = fields.Char(string="Correo",size = 50, required=True, help="Correo Electronico del cliente")
     foto=fields.Binary('Photo')
     
     cita_id = fields.One2many("upobarber.cita",'cliente_id',string="ID de la cita")
     #compra_id = fields.Many2one("upobarber.citas",string="Confirmar cita")
     
