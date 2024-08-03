from odoo import api, fields, models

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Master'

    name = fields.Char(string="name",required=True)
    date_of_birth = fields.Date(string="Merza")