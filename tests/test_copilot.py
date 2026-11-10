"""Unit tests for Copilot IntentRouter."""

from copilot.intent_router import IntentRouter


def test_balance_query_intent():
    router = IntentRouter()
    plan = router.parse_query("What is the outstanding balance for Sharma Enterprises?")

    assert plan.doctype == "Customer"
    assert plan.action == "sum"
    assert "Sharma Enterprises" in plan.filters.get("customer_name", "")


def test_invoice_query_intent():
    router = IntentRouter()
    plan = router.parse_query("Show me recent sales invoices")

    assert plan.doctype == "Sales Invoice"
    assert plan.action == "list"
