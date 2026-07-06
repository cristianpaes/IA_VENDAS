import plotly.express as px


class ChartGenerator:

    def generate(self, df, config):

        chart_type = config.get("chart", "table")

        if df is None or df.empty:
            return None

        if chart_type == "bar":
            return px.bar(df, x=df.columns[0], y=df.columns[1])

        if chart_type == "line":
            return px.line(df, x=df.columns[0], y=df.columns[1])

        return None