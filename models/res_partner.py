from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_tax_id = fields.Char(string='Tax ID')
    x_extra_info = fields.Text(string='Extra Information')
    x_phone2 = fields.Char(string='Secondary Phone')
