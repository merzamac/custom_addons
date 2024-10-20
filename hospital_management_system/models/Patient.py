from odoo import api, fields, models


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Patient Master'

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="Birth",tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
