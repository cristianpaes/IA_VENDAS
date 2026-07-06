class ResultAnalyzer:

    def analyze(self, df, question: str):

        if df is None or df.empty:
            return "Sem dados retornados."

        return {
            "linhas": len(df),
            "colunas": list(df.columns),
            "resumo": df.head(5).to_dict()
        }