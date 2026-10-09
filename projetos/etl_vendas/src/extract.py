import pandas as pd


def extract(caminho_entrada, caminho_saida):

    print(f"Lendo arquivo: {caminho_entrada}")

    df = pd.read_csv(caminho_entrada)

    print(f"{len(df)} registros encontrados.")

    df.to_csv(caminho_saida, index=False)

    print(f"Arquivo extraído salvo em: {caminho_saida}")