"""Natural Language RAG Response Engine for ERPNext."""

from typing import Dict, Any, List
from copilot.intent_router import IntentRouter, QueryPlan


class CopilotEngine:
    def __init__(self):
        self.router = IntentRouter()

    def generate_response(self, user_question: str, mock_erp_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        plan = self.router.parse_query(user_question)

        # Aggregate or format answer
        if plan.action == "sum" and plan.field_to_aggregate:
            total = sum(float(row.get(plan.field_to_aggregate, 0)) for row in mock_erp_data)
            answer = f"The total {plan.field_to_aggregate.replace('_', ' ')} across {len(mock_erp_data)} record(s) is ₹{total:,.2f}."
        else:
            answer = f"Found {len(mock_erp_data)} matching {plan.doctype} records in ERPNext."

        return {
            "question": user_question,
            "query_plan": plan.model_dump(),
            "answer": answer,
            "data": mock_erp_data[:5],
        }
