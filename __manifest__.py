# -*- coding: utf-8 -*-
{
    'name': "upobarber",

    'summary': """ Gestion de una peluquería""",

    'description': """ Gestion de clientes, reservas y venta de productos """,

    'author': "Carlos Marchante",
    'website': "https://www.upo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/cliente_report.xml',
        'views/cliente_views.xml',
        'views/cita_views.xml',
        'views/reserva_views.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/upobarber.cliente.csv',
        'demo/upobarber.reserva.csv',
        'demo/upobarber.cita.csv'
    ],
    'application': True,
}
