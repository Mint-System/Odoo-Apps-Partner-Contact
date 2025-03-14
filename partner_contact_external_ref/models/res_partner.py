import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    ref_external = fields.Char(string="External Reference")
