# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CRMLead(models.Model):
    _inherit = "crm.lead"

    link_ids = fields.One2many(
        "res.partner.link", "source_lead_id", domain=[("partner_id", "!=", False)], help="Link partners."
    )
    lead_link_ids = fields.One2many(
        "res.partner.link", "source_lead_id", domain=[("lead_id", "!=", False)], help="Link opportunities."
    )
    source_lead_link_ids = fields.One2many(
        "res.partner.link", "lead_id", domain=[("source_lead_id", "!=", False)], help="Backlinks from opportunities."
    )
