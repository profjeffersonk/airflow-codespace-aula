from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
from pathlib import Path
import sys


# ============================================================
# CAMINHOS DO PROJETO
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

SRC_PATH = (
    PROJECT_ROOT
    / "projetos"
    / "etl_vendas"
    / "src"
)

sys.path.append(str(SRC_PATH))


# ============================================================
# IMPORTAÇÃO DAS FUNÇÕES
# ============================================================

from extract import extract
from transform import transform
from load import load


# ============================================================
# ARQUIVOS
# ============================================================

RAW = (
    PROJECT_ROOT
    / "projetos"
    / "etl_vendas"
    / "data"
    / "raw"
    / "vendas.csv"
)

STAGING = (
    PROJECT_ROOT
    / "projetos"
    / "etl_vendas"
    / "data"
    / "staging"
    / "vendas_extraidas.csv"
)

PROCESSED = (
    PROJECT_ROOT
    / "projetos"
    / "etl_vendas"
    / "data"
    / "processed"
    / "vendas_agrupadas.csv"
)


# ============================================================
# TASKS
# ============================================================

def executar_extract():

    extract(
        caminho_entrada=RAW,
        caminho_saida=STAGING
    )


def executar_transform():

    transform(
        caminho_entrada=STAGING,
        caminho_saida=PROCESSED
    )


def executar_load():

    load(
        caminho=PROCESSED
    )


# ============================================================
# DAG
# ============================================================

with DAG(
    dag_id="etl_vendas",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=executar_extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=executar_transform,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=executar_load,
    )


    extract_task >> transform_task >> load_task