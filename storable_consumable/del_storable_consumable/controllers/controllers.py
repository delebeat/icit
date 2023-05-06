# -*- coding: utf-8 -*-
# from odoo import http


# class DelStorableConsumable(http.Controller):
#     @http.route('/del__storable_consumable/del__storable_consumable', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/del__storable_consumable/del__storable_consumable/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('del__storable_consumable.listing', {
#             'root': '/del__storable_consumable/del__storable_consumable',
#             'objects': http.request.env['del__storable_consumable.del__storable_consumable'].search([]),
#         })

#     @http.route('/del__storable_consumable/del__storable_consumable/objects/<model("del__storable_consumable.del__storable_consumable"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('del__storable_consumable.object', {
#             'object': obj
#         })
