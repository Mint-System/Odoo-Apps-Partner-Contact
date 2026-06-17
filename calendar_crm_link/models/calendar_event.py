# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    lead_link_ids = fields.One2many("crm.lead.link", "source_event_id", help="Link opportunities.")
