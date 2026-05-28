# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    link_ids = fields.One2many("res.partner.link", "source_partner_id", help="Link partners.")
    source_partner_link_ids = fields.One2many(
        "res.partner.link", "partner_id", domain=[("source_partner_id", "!=", False)], help="Backlinks from contacts."
    )
