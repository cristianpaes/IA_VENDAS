from database.executor import SQLExecutor

executor = SQLExecutor()

df = executor.execute("""
SELECT *
FROM fato_vendas
LIMIT 10;
""")

print(df)