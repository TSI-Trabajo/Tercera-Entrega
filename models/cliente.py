from ctypes import sizeof
from odoo import models, fields, api
import re

class Cliente(models.Model):
     _name = 'upobarber.cliente'
     _description = 'Clientes de la peluquería'

     name = fields.Char(String = "DNI" ,size = 9, required=True, help="DNI del cliente ; FORMATO = 'IIIIIIII-S'")
     nombre = fields.Char(string="Nombre", size=50, required=True, help="Nombre del cliente")
     apellidos = fields.Char(string="Apellidos", size=50, required=True, help="Primer y Segundo apellidos del cliente")
     telefono = fields.Integer(string="Telefono",size = 9, required=True, help = "Telefono MOVIL del cliente")
     correoElectronico = fields.Char(string="Correo",size = 50, required=True, help="Correo Electronico del cliente")
     foto=fields.Binary('Photo')
     
     cita_id = fields.One2many("upobarber.cita",'cliente_id',string="Citas del Cliente")
     reserva_id = fields.One2many("upobarber.reserva",'cliente_id',string="Reservas del Cliente")
     #compra_id = fields.Many2one("upobarber.citas",string="Confirmar cita")
     
     _sql_constraints = [('cliente_name_unico','UNIQUE (name)','El DNI ya está registrado en nuestros datos')]
     _sql_constraints = [('cliente_telefono_unico','UNIQUE (telefono)','El telefono ya está registrado en nuestros datos')]
     _sql_constraints = [('cliente_correoElectronico_unico','UNIQUE (correoElectronico)','El correoElectronico ya está registrado en nuestros datos')]
     
     def btn_verCitasPagadas(self):
          citas_no_pagadas = self.env['upobarber.cita'].search([('cliente_id', '=', self.id), ('pagado', '=', False)])
          citas_no_pagadas.unlink()
     
     def btn_generar_report(self):
          return self.env.ref('upobarber.upobarber_cliente_template').report_action(self)
     
     @api.onchange('name')
     def _onchange_dni(self):
        if self.name and not self._validar_dni():
          resultado = {  'value': {'name':''}, 
                                   'warning': { 'title':'Valores incorrectos', 'message':'El DNI debe tener 8 digitos y un caracter en MAYUSCULA.'}
                    }
          return resultado
     
     def _validar_dni(self):
        return bool(re.match(r'^\d{8}[A-Z]$', self.name))
     
     
     @api.onchange('nombre')
     def onchange_cliente(self):
          resultado = {}
          if self.nombre and not self.nombre[0].isupper():
               resultado = {  'value': {'nombre':' '}, 
                              'warning': { 'title':'Valores incorrectos', 'message':'El primer carácter del nombre debe ser una letra en mayúscula.'}
               }
               return resultado             
    


     
