import pandas as pd


def load(caminho):

    print(f"Carregando arquivo: {caminho}")

    df = pd.read_csv(caminho)

    print("Dados carregados com sucesso!")

    print(df)