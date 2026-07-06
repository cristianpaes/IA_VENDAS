from ai.client import AIClient

client = AIClient()

resposta = client.generate("""
Responda SOMENTE este JSON:

{
    "nome":"Cristian"
}
""")

print(resposta)