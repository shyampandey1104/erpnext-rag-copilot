"""Intent parser and semantic query router for ERPNext Copilot."""

import re
from typing import Dict, Any, Optional
from pydantic import BaseModel


class QueryPlan(BaseModel):
    intent: str
    doctype: str
    action: str  # list, count, sum
    filters: Dict[str, Any] = {}
    field_to_aggregate: Optional[str] = None


class IntentRouter:
    """Translates natural language questions into structured Frappe Query Plans."""

    INTENT_RULES = [
        {
            "pattern": r"(?:balance|outstanding|due|owe)",
            "doctype": "Customer",
            "action": "sum",
            "field": "outstanding_amount",
        },
        {
            "pattern": r"(?:invoice|bill|sales)",
            "doctype": "Sales Invoice",
            "action": "list",
            "field": "grand_total",
        },
        {
            "pattern": r"(?:stock|inventory|qty|quantity)",
            "doctype": "Bin",
            "action": "list",
            "field": "actual_qty",
        },
        {
            "pattern": r"(?:lead|prospect|inquiry)",
            "doctype": "Lead",
            "action": "list",
            "field": "lead_name",
        },
    ]

    def parse_query(self, query: str) -> QueryPlan:
        q_lower = query.lower()

        # Extract party name if mentioned
        party_match = re.search(r"(?:for|of|customer)\s+([A-Za-z0-9\s]+?)(?:\?|$|\s+in)", query, re.IGNORECASE)
        party = party_match.group(1).strip() if party_match else None

        for rule in self.INTENT_RULES:
            if re.search(rule["pattern"], q_lower):
                filters = {}
                if party and rule["doctype"] in ("Customer", "Sales Invoice"):
                    filters["customer_name"] = party

                return QueryPlan(
                    intent="analytics_query",
                    doctype=rule["doctype"],
                    action=rule["action"],
                    filters=filters,
                    field_to_aggregate=rule.get("field"),
                )

        return QueryPlan(
            intent="general_search",
            doctype="Sales Invoice",
            action="list",
            filters={},
        )
