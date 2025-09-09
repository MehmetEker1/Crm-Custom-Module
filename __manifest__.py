{
    'name': 'New CRM',
    'version': '1.4',
    'summary': 'CRM modülüne özel alanlar ve otomasyonlar eklemektedir.',
    'author': 'Mehmet Eker',
    'category': 'Sales',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
        'views/res_partner_views.xml',

    ],
    'images': ['static/description/icon.png'],  # <- icon pathi buraya eklendi
    'installable': True,
    'application': True,
    'auto_install': False,
}
