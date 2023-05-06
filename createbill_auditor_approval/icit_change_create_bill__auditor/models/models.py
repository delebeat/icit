# -*- coding: utf-8 -*-
from odoo import models
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # @api.multi
    def action_invoice_create(self):
        # Change the name of the button in the view
        self.env['ir.actions.act_window'].search([('name', '=', 'Create Bill')]).name = 'Audit Approval'

        # Call the original method to create the invoice
        res = super(PurchaseOrder, self).action_invoice_create()

        return res
