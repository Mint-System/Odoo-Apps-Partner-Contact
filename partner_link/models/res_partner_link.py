# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartnerLink(models.Model):
    _name = "res.partner.link"
    _description = "Partner Link"

    label_id = fields.Many2one("res.partner.link.label", help="Label for the link.")
    partner_id = fields.Many2one("res.partner", string="Contact", help="Link points to this partner.")
    comment = fields.Char(help="Optional comment for the link.")

    source_partner_id = fields.Many2one("res.partner", string="Contact", help="The link originates from this partner.")

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.partner_id.name} ({rec.label_id.name})"
