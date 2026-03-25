# -*- coding: utf-8 -*-


from odoo import models, fields

class Consultations(models.Model):
    _name = 'telemedecine.consultation'
    _description = 'Consultations'
    
    name = fields.Char(string='Référence', required=True, index=True)
    patient_id = fields.Many2one('telemedecine.patient',  
        string="Liste des patients")
    medecin_id = fields.Many2one('telemedecine.medecin',  
        string="Liste des médecins")
    date_debut = fields.Datetime("Début de consultation")
    date_fin = fields.Datetime("Fin de la consultation")
    # durée
    type_consultation = fields.Selection([
        ('premier',"Primiére consultation"),
        ('deuxieme',"Suivi"),
        ('troisieme',"Urgente"),
        ('quatrieme',"Renouvellement ordonnance")], 
        string='Type de consultation')
    mode_consultation = fields.Selection([
        ('video',"Vidéo"),
        ('telephone',"Téléphone"),
        ('messagerie',"Messagerie")], 
        string='Mode de consultation')
    motif = fields.Text(string="Motif (déclaré par le patient)")













