# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tiposervicio(models.Model):
    _name = 'upobarber.tiposervicio'
    _description = 'Tipo de Servicio'


    tipo_servicio = fields.Char(string="Tipo Servicio", required=True, index=True)
    descripcion = fields.Char(string="descripcion", required=True)
    precio = fields.Float(string="Precio", required=True)
    tiempo = fields.Float(string="Tiempo", required=True)

    @api.depends('precio', 'tiempo')
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.tipo_servicio))
        return result

    def btn_generar_report(self):
        # Fetch data for the report
        data = {
            'docs': self  # Pass the current recordset to the template
        }

        # Render the report template using qweb rendering engine
        template = self.env.ref('upobarber.upobarber_tiposervicio_template')
        report_html = template.render(data)

        # Generate PDF using qweb rendering engine
        pdf = self.env['report'].qweb_pdf(report_html)

        # Return the report as a downloadable file
        return {
            'name': 'Tipo_Servicio_Report.pdf',
            'type': 'ir.actions.act_url',
            'url': '/web/content/?model=upobarber.tiposervicio&id=%s&field=pdf_report&download=true' % self.id,
            'target': 'new',
        }