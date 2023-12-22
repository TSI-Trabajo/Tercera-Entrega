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
        'views/articulo_views.xml',
        'views/producto_views.xml',
        'views/tipoproducto_views.xml',
        'views/menus.xml',
        'reports/compra_report.xml',
        'reports/pago_report.xml',
        'reports/producto_report.xml',
        'reports/articulo_report.xml',
        'reports/tipoproducto_report.xml',
        'reports/reports.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/upobarber.metodopago.csv',
        'demo/upobarber.pago.csv',
        'demo/upobarber.compra.csv',
        'demo/upobarber.tipoproducto.csv',
        'demo/upobarber.producto.csv',
        'demo/upobarber.articulo.csv',  
    ],
    'assets':{
        'web.assets_backend': [
            'upobarber/static/src/components/*/*.js',
            'upobarber/static/src/components/*/*.xml',
            'upobarber/static/src/components/*/*.scss',
    	],
    },
    'aplication': True,
}
