from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class AIResponse:
    """
    Estrutura padrão da resposta da IA.
    """

    thought: str
    sql: str
    chart: str
    title: str
    explanation: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "thought": self.thought,
            "sql": self.sql,
            "chart": self.chart,
            "title": self.title,
            "explanation": self.explanation,
        }