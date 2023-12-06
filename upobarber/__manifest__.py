# -*- coding: utf-8 -*-
{
    'name': "upobarber",

    'summary': """Gestion del modulo upobarber""",

    'description': """Gestion del pago, metodo de pago, compra""",

    'author': "joseAntonioOrozcoRodriguez",
    'website': "https://www.upobarber.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/compra_view.xml',
        'views/pago_view.xml',
        'views/metodopago_view.xml',
        'views/menus.xml',
        'reports/compra_report.xml',
        'reports/pago_report.xml',
        'reports/reports.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/upobarber.metodopago.csv',
        'demo/upobarber.pago.csv',
        'demo/upobarber.compra.csv',
    ],
    'aplication': True,
}