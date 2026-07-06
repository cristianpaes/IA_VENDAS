from ai.schema import SchemaSelector

selector = SchemaSelector()

schema = selector.select(
    "Qual vendedor vendeu mais em janeiro?"
)

print(schema)