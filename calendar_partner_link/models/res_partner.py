# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    source_event_link_ids = fields.One2many(
        "res.partner.link", "partner_id", domain=[("source_event_id", "!=", False)], help="Backlinks from evens."
    )
