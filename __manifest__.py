# -*- coding: utf-8 -*-
{
    'name': "upobarber",

    'summary': """Gestion del modulo upobarber""",

    'description': """Gestion de peluqueria.""",

    'author': "TSI - UPO",
    'website': "https://www.upo.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        #cargar reports
        'reports/reports.xml',
        'reports/empleado_report.xml',
        'reports/cliente_report.xml',
        'views/horario_views.xml',
        'views/cita_views.xml',
        'views/empleado_views.xml',
        'views/cliente_views.xml',
        'views/reserva_views.xml',
        'views/articulo_views.xml',
        'views/producto_views.xml',
        'views/tipoproducto_views.xml',
        'views/pago_views.xml',
        'views/metodopago_views.xml',
        'views/compra_views.xml',
        'views/menu.xml', 
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/upobarber.cliente.csv',
        'demo/upobarber.empleado.csv',
        'demo/upobarber.tipoproducto.csv',
        'demo/upobarber.producto.csv',
        'demo/upobarber.reserva.csv',
        'demo/upobarber.cita.csv',
        'demo/upobarber.horario.csv',
        'demo/upobarber.articulo.csv',    
    ],
    'assets':{
    	'web.assets_backend': [
            'gym/static/src/components/*/*.js',
            'gym/static/src/components/*/*.xml',
            'gym/static/src/components/*/*.scss',
    	],
    },
    'application': True,
}
