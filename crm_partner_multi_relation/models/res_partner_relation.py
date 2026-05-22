# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResPartnerRelation(models.Model):
    _inherit = "res.partner.relation"

    lead_ids = fields.Many2many(
        comodel_name="crm.lead",
        relation="crm_lead_res_partner_relation",
        column1="relation_id",
        column2="lead_id",
        string="CRM Lead",
    )
