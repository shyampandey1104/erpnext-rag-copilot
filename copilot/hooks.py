# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "copilot"
app_title = "Erpnext Rag Copilot"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Rag Copilot for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/copilot/css/copilot.bundle.css"
app_include_js = "/assets/copilot/js/copilot.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "copilot.engine.on_document_submit",
        "on_cancel": "copilot.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "copilot.engine.daily_scheduled_sync"
    ]
}
