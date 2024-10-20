from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one('hospital.patient',string="Patient")
    data_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")
