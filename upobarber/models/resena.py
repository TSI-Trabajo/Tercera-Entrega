from odoo import models, fields, api
import uuid


class resena(models.Model):
    _name = 'upobarber.resena'
    _description = 'resenas Upobarber'

    resena_id = fields.Char(string="ID de la resena", readonly=True)
    puntuacion = fields.Selection(
        [('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Puntuacion',
        required=True
    )
    comentarios = fields.Char(string="Comentarios", required=False)

    def btn_generar_report(self):
        return self.env.ref('upobarber.upobarber_resena_template').report_action(self)

    @api.model
    def create(self, vals):
        if vals.get('resena_id', 'New') == 'New':
            vals['resena_id'] = str(uuid.uuid4())[:8]
        return super(resena, self).create(vals)
