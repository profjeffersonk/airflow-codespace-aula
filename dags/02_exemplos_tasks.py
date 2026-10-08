from airflow import DAG
from airflow.operators.python import PythonOperator, ShortCircuitOperator
from datetime import datetime


def iniciar():
    print("Pipeline iniciado!")


def processar():
    print("Processando dados...")


def erro():
    print("Executando tarefa com erro!")
    raise Exception("Erro proposital!")


def decidir():
    print("Decidindo se executa...")
    return False


def tarefa_pulada():
    print("Essa mensagem nunca será exibida!")


with DAG(
    dag_id="exemplo_multiplas_tasks",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    inicio = PythonOperator(
        task_id="inicio",
        python_callable=iniciar,
    )

    processamento = PythonOperator(
        task_id="processamento",
        python_callable=processar,
    )

    tarefa_erro = PythonOperator(
        task_id="tarefa_com_erro",
        python_callable=erro,
    )

    decidir_execucao = ShortCircuitOperator(
        task_id="decidir_execucao",
        python_callable=decidir,
    )

    tarefa_pulada = PythonOperator(
        task_id="tarefa_pulada",
        python_callable=tarefa_pulada,
    )

    inicio >> processamento

    processamento >> tarefa_erro

    processamento >> decidir_execucao >> tarefa_pulada
	