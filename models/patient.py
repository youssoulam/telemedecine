# -*- coding: utf-8 -*-


from odoo import models, fields

class Patients(models.Model):
    _name = 'telemedecine.patient'
    _description = 'Liste des Patients'
    
    name = fields.Char(string='Référence du client', required=True, index=True)
    prenom = fields.Char(string='Prénom', required=True)
    nom_famille = fields.Char(string='Nom de famille', required=True)
    sexe = fields.Selection([('h',"Homme"),('f',"Femme"),('a',"Autres")], 
        string='Sexe')
    date_naissance = fields.Date(string="Date de Naissance")
    securite_sociale = fields.Char(string="N° Sécurité Sociale (NIR)")
    mutuelle = fields.Char(string="Mutuelle")
    telephone = fields.Char(string="Téléphone", placeholder="+33 690 20 30")
    email = fields.Char(string="Email", placeholder="exemple@yopmail.com")
    ald = fields.Boolean(string="Affection de longue durée")
    allergie = fields.Text(string="Allergie")














