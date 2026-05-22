# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    lead_relation_ids = fields.Many2many(
        comodel_name="res.partner.relation",
        compute="_compute_lead_relation_ids",
        string="CRM Lead",
    )

    def _compute_lead_relation_ids(self):
        for partner_id in self:
            partner_id.lead_relation_ids = self.env["res.partner.relation"].search(
                [("lead_ids", "!=", False), ("right_partner_id", "=", partner_id.id)]
            )
