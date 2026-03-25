# -*- coding: utf-8 -*-


from odoo import models, fields

class Medecins(models.Model):
    _name = 'telemedecine.medecin'
    _description = 'Liste des Medecins'
    
    name = fields.Char(string='Référence', required=True, index=True)
    prenom = fields.Char(string='Prénom', required=True)
    nom_famille = fields.Char(string='Nom de famille', required=True)
    rpps = fields.Char(string="N° RPPS * (11 chiffres)", placeholder="12345678901")
    adeli = fields.Char(string="N° ADELI)")
    specialite = fields.Selection(
        [
        ('generaliste',"Médecin Généraliste"),
        ('cardio',"Cardiologue"),
        ('dermato',"Dermatologue"),
        ('pediatre',"Pédiatre"),
        ('psychatre',"Psychatre")], 
        string='Spécialité du Médecin', default='generaliste')
    secteur = fields.Selection([
        ('secteur1',"Secteur 1 (Conventionné)"),
        ('secteur2',"Secteur 2 (Horaires libres)"),
        ('optam',"OPTAM")], string="Secteur de conventionnement")
    tarif = fields.Integer(string="Tarif consultation (€)")
    mode_consultation = fields.Selection([
        ('video_telephone',"Vidéo et Téléphone"),
        ('video_unique',"Vidéo uniquement"),
        ('telephone_unique',"Téléphone uniquement")],
        string="Mode de consultation")
    telephone = fields.Char(string="Téléphone", placeholder="+33 690 20 30")
    email = fields.Char(string="Email", placeholder="exemple@yopmail.com")














