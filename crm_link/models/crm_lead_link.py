# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CRMLeadLink(models.Model):
    _name = "crm.lead.link"
    _description = "Opportunity Link"

    label_id = fields.Many2one("res.partner.link.label", help="Label for the link.")
    lead_id = fields.Many2one("crm.lead", string="Opportunity", required=True, help="Link points to this opportunity.")
    comment = fields.Char(help="Optional comment for the link.")

    source_lead_id = fields.Many2one("crm.lead", string="Contact", help="The link originates from this opportunity.")

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.lead_id.name} ({rec.label_id.name})"
