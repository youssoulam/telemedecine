# -*- coding: utf-8 -*-
{
    'name': 'Télémedecine',
    'version': '18.0.1.0.0',
    'category': 'tp',
    'summary': "Ce module a été développé lors du séminaire Odoo",
    'description': """
        Module prend en charges les demandes de consultation à distance
        dont les fonctionnalités sont les suivantes :
        - Medecins
        - Patients 
        - Consultation ou Rendez-vous
        - Ordonnance

    """,
    'author': 'Youssoupha',
    'website': 'https://www.votre-universite.fr',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/telemedecine_security.xml',
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/medecin_views.xml',
        'views/consultation_views.xml',
        'views/menu.xml',
    ],
    #'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
