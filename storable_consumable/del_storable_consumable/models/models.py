from odoo import api, fields, models

class ProductProduct(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    @api.onchange('detailed_type')
    def _onchange_detailed_type_method(self):
        if self.detailed_type == 'consu':
            print("Yes")
            self.detailed_type = 'product'