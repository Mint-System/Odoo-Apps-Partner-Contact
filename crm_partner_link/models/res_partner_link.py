# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner.link"

    source_lead_id = fields.Many2one("crm.lead", string="Opportunity", help="Link originates from this opportunity.")
    lead_id = fields.Many2one("crm.lead", string="Opportunity")
