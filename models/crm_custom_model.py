from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    satisfaction_score = fields.Selection(
        [
            ('1', 'Very Dissatisfied'),
            ('2', 'Dissatisfied'),
            ('3', 'Neutral'),
            ('4', 'Satisfied'),
            ('5', 'Very Satisfied'),
        ],
        string='Customer Satisfaction'
    )
