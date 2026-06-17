# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CRMLead(models.Model):
    _inherit = "crm.lead"

    source_event_link_ids = fields.One2many(
        "crm.lead.link", "lead_id", domain=[("source_event_id", "!=", False)], help="Backlinks from events."
    )
