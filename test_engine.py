from ai.engine import AIEngine


def main():

    engine = AIEngine()

    print("=" * 60)
    print("DataMind AI")
    print("=" * 60)

    while True:

        question = input("\nPergunta (ou 'sair'): ")

        if question.lower() in ["sair", "exit", "quit"]:
            break

        try:

            result = engine.ask(question)

            if not result["success"]:
                print("\n❌ Erro:")
                print(result["error"])
                continue

            print("\n" + "=" * 60)
            print("SQL GERADO")
            print("=" * 60)
            print(result["sql"])

            print("\n" + "=" * 60)
            print("RESULTADO")
            print("=" * 60)
            print(result["data"])

            print("\n" + "=" * 60)
            print("ANÁLISE")
            print("=" * 60)
            print(result["analysis"])

            print("\n" + "=" * 60)
            print("TEMPO")
            print("=" * 60)

            timing = result["timing"]

            print(f"Geração SQL : {timing['sql_generation']} s")
            print(f"Banco        : {timing['database']} s")
            print(f"Análise      : {timing['analysis']} s")
            print(f"Total        : {timing['total']} s")

        except Exception as e:
            print(f"\nErro: {e}")


if __name__ == "__main__":
    main()