# -*- coding: utf-8 -*-
# from odoo import http


# class Upobarber(http.Controller):
#     @http.route('/megamarket/megamarket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upobarber/upobarber/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upobarber.listing', {
#             'root': '/upobarber/upobarber',
#             'objects': http.request.env['upobarber.upobarber'].search([]),
#         })

#     @http.route('/upobarber/upobarber/objects/<model("upobarber.upobarber"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upobarber.object', {
#             'object': obj
#         })
