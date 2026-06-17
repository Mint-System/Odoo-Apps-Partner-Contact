# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CRMLeadLink(models.Model):
    _inherit = "crm.lead.link"

    source_event_id = fields.Many2one("calendar.event", string="Event", help="Link originates from this event.")
