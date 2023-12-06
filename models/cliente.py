from ctypes import sizeof
from odoo import models, fields, api

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
           citas_pagadas = self.env['upobarber.cita'].search([('cliente_id', '=', self.id), ('pagado', '=', True)])
     
     
     @api.onchange('name')
     def onchange_cliente(self):
          resultado = {}
          if self.name:
               if len(self.name) != 9:
                    resultado = {  'value': {'name':''}, 
                                   'warning': { 'title':'Valores incorrectos', 'message':'El DNI debe tener 8 digitos y un caracter.'}
                    }
                    return resultado
               if not self.name[:8].isdigit():
                    resultado = {  'value': {'name':''}, 
                                   'warning': { 'title':'Valores incorrectos', 'message':'El DNI debe comenzar por 8 números.'}
                    }
                    return resultado 
               if not self.name[8].isalpha() or not self.name[8].isupper():
                    resultado = {  'value': {'name':''}, 
                                   'warning': { 'title':'Valores incorrectos', 'message':'El último carácter del DNI debe ser una letra en mayúscula.'}                              
                    }
                    return resultado
          return resultado
     
     @api.onchange('nombre')
     def onchange_cliente(self):
          resultado = {}
          if self.nombre and not self.nombre[0].isupper():
               resultado = {  'value': {'nombre':' '}, 
                              'warning': { 'title':'Valores incorrectos', 'message':'El primer carácter del nombre debe ser una letra en mayúscula.'}
               }
               return resultado             
    
     @api.onchange('telefono')
     def onchange_cliente(self):
          resultado = {}
          if self.telefono.isdigit() or len(self.telefono) != 9:
               resultado = {  'value': {'telefono':''}, 
                              'warning': { 'title':'Valores incorrectos', 'message':'El telefono debe ser 9 números.'}
               } 
               return resultado

     
