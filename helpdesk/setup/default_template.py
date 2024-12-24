import frappe

from helpdesk.consts import DEFAULT_TICKET_TEMPLATE


def create_default_template():
    existing_template = frappe.db.exists(
        "HD Ticket Template", {"template_name": DEFAULT_TICKET_TEMPLATE}
    )
    if not existing_template:
        doc = {
            "doctype": "HD Ticket Template",
            "template_name": DEFAULT_TICKET_TEMPLATE,
        }
        frappe.get_doc(doc).save()
