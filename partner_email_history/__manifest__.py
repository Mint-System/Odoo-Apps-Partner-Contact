{
    "name": "Partner Email History",
    "summary": """
        Show history of messages sent and received to a partner.
    """,
    "author": "Mint System GmbH",
    "website": "https://www.mint-system.ch/",
    "category": "Productivity",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["contacts"],
    "data": [
        "views/res_partner_views.xml",
        "views/mail_message_views.xml",
        "views/mail_mail_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
