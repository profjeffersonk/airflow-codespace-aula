import pandas as pd


def transform(caminho_entrada, caminho_saida):

    print(f"Lendo arquivo: {caminho_entrada}")

    df = pd.read_csv(caminho_entrada)

    print("Calculando faturamento...")

    df["faturamento"] = (
        df["quantidade"] * df["preco"]
    )

    print("Agrupando vendas por produto...")

    resultado = (
        df
        .groupby("produto")
        .agg(
            quantidade_total=("quantidade", "sum"),
            faturamento_total=("faturamento", "sum")
        )
        .reset_index()
    )

    resultado.to_csv(
        caminho_saida,
        index=False
    )

    print(f"Arquivo transformado salvo em: {caminho_saida}")