# -*- coding: utf-8 -*-
# from odoo import http


# class IcitChangeCreateBillAuditor(http.Controller):
#     @http.route('/icit_change_create_bill__auditor/icit_change_create_bill__auditor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/icit_change_create_bill__auditor/icit_change_create_bill__auditor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('icit_change_create_bill__auditor.listing', {
#             'root': '/icit_change_create_bill__auditor/icit_change_create_bill__auditor',
#             'objects': http.request.env['icit_change_create_bill__auditor.icit_change_create_bill__auditor'].search([]),
#         })

#     @http.route('/icit_change_create_bill__auditor/icit_change_create_bill__auditor/objects/<model("icit_change_create_bill__auditor.icit_change_create_bill__auditor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('icit_change_create_bill__auditor.object', {
#             'object': obj
#         })
