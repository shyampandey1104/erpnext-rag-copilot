# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "copilot"
app_title = "Erpnext Rag Copilot"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Rag Copilot - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/copilot/css/copilot.bundle.css"
app_include_js = "/assets/copilot/js/copilot.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Rag Copilot Entry": {
        "validate": "copilot.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "copilot.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "copilot.tasks.hourly_sync"
    ],
    "daily": [
        "copilot.tasks.daily_reconciliation"
    ],
    "weekly": [
        "copilot.tasks.weekly_digest"
    ]
}
