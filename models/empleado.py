from odoo import models, fields, api


class Empleado(models.Model):
     _name = 'upobarber.empleado'
     _description = 'empleados'

     name = fields.Char(string="Dni Empleado" ,required=True)

     nombre = fields.Char(string="Nombre", size=60, required=True, help="Nombre del empleado")
     apellidos = fields.Char(string="Apellidos", size=60, required=True, help="Apellidos del empleado")
     telefono = fields.Char(string="Telefono", size=10, required=True, help="Telefono del Empleado")
     correoElectronico = fields.Char(string="Correo Electronico", size=50, required=True, help="Correo electronico del Empleado")
     numeroCuenta = fields.Char(string="Numero de Cuenta", size=50, required=True, help="Numero de cuenta del empleado")

     horario_id = fields.One2many("upobarber.horario","empleado_dnis","Horarios Empleado")

     '''@api.onchange('name')
     def onchange_empleado(self):
          resultado = {}
          if len(self.name) != 9:
               resultado = {
                    'value': {'name:' "00000000K"},
                    'warning': {
                         'title':'Longitud incorrecta',
                         'message':'El dni debe tener 9 caracteres'
                    }
               }
          return resultado'''
     
     def btn_eliminar_horarios(self):
          self.write({'horario_id':[(5,)]})