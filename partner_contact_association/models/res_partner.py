import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"
    _rec_names_search = ["complete_name", "email", "ref", "vat", "company_registry", "association_name"]

    association_id = fields.Many2one("res.association")
    association_name = fields.Char(related="association_id.name", string="Assocation Name", store=True)

    def _get_complete_name(self):
        name = super()._get_complete_name()
        if self.association_id:
            name = f"{self.name} ({self.association_id.name})"
        return name
