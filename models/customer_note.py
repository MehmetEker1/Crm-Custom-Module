from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CustomerNote(models.Model):
    _name = 'customer.note'
    _description = 'Müşteri Notları'

    customer_id = fields.Many2one('res.partner', string='Müşteri', required=True)
    note_text = fields.Text(string='Not')
    created_by = fields.Many2one('res.users', string='Oluşturan', default=lambda self: self.env.user)
    date = fields.Datetime(string='Oluşturulma Tarihi', default=fields.Datetime.now)
