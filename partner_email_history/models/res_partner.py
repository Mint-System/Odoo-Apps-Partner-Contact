import logging

from odoo import models

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    def action_show_message_history(self):
        self.ensure_one()
        action = self.env.ref("partner_email_history.action_view_mail_message_list").read()[0]
        subtype_id = self.env.ref("mail.mt_comment")
        message_types = ["email", "comment"]

        action["domain"] = [
            "&",
            "|",
            ("subtype_id", "=", subtype_id.id),
            ("message_type", "in", message_types),
            "|",
            ("author_id", "=", self.id),
            "|",
            ("email_from", "ilike", self.email),
            "&",
            ("model", "=", "res.partner"),
            ("res_id", "=", self.id),
        ]

        return action

    def action_show_mail_history(self):
        self.ensure_one()
        action = self.env.ref("partner_email_history.action_view_mail_mail_list").read()[0]

        action["domain"] = [
            "|",
            ("email_from", "ilike", self.email),
            "|",
            ("email_to", "ilike", self.email),
            ("recipient_ids", "in", self.id),
        ]

        return action
