# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CRMead(models.Model):
    _inherit = "crm.lead"

    relation_ids = fields.Many2many(
        comodel_name="res.partner.relation",
        relation="crm_lead_res_partner_relation",
        column1="lead_id",
        column2="relation_id",
        string="Partner Relations",
    )
