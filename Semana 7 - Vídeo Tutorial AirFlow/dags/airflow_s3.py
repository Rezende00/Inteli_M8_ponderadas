from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
import boto3
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

aws_region_name = os.getenv('AWS_REGION_NAME')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_session_token = os.getenv('AWS_SESSION_TOKEN')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'conexao_com_aws',
    default_args=default_args,
    description='Essa dag será utilizada para conectar com o amazon S3',
    schedule_interval=timedelta(days=1),
)

def connect_to_s3():
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region_name,
            aws_session_token=aws_session_token
        )
        response = s3_client.list_buckets()
        print("Buckets S3:")
        for bucket in response['Buckets']:
            print(f' - {bucket["Name"]}')
    except Exception as e:
        print(f"Erro ao conectar ao S3: {e}")

s3_connection_task = PythonOperator(
    task_id='s3_connection_task',
    python_callable=connect_to_s3,
    dag=dag,
)


def list_buckets():
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region_name,
            aws_session_token=aws_session_token
        )
        response = s3_client.list_buckets()
        print("Buckets S3:")
        for bucket in response['Buckets']:
            print(f' - {bucket["Name"]}')
    except Exception as e:
        print(f"Erro ao listar buckets: {e}")

list_buckets_task = PythonOperator(
    task_id='list_buckets',
    python_callable=list_buckets,
    dag=dag,
)

def choose_bucket():
    chosen_bucket = 'atividade-ponderada-airflow'
    print("Bucket Escolhido:", chosen_bucket)
    return chosen_bucket

choose_bucket_task = PythonOperator(
    task_id='choose_bucket',
    python_callable=choose_bucket,
    dag=dag,
)


def list_files_in_bucket(**kwargs):
    chosen_bucket = kwargs['ti'].xcom_pull(task_ids='choose_bucket')
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region_name,
        aws_session_token=aws_session_token
    )
    response = s3_client.list_objects(Bucket=chosen_bucket)
    print(f"Arquivos no Bucket {chosen_bucket}:")
    for file in response.get('Contents', []):
        print(f' - {file["Key"]}')

list_files_task = PythonOperator(
    task_id='list_files_in_bucket',
    python_callable=list_files_in_bucket,
    provide_context=True,
    dag=dag,
)

def preprocess_file(**kwargs):
    ti = kwargs['ti']
    chosen_bucket = ti.xcom_pull(task_ids='choose_bucket')
    chosen_file = 'Listagem_dos_Filmes_Brasileiros_e_Estrangeiros_Exibidos_2009_a_2019.csv'  

    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region_name,
        aws_session_token=aws_session_token
    )

    with open(chosen_file, 'wb') as f:
        s3_client.download_fileobj(Bucket=chosen_bucket, Key=chosen_file, Fileobj=f)

    df = pd.read_csv(chosen_file, encoding='latin1')

    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    if df.isnull().values.any():
        print("Dados nulos encontrados. Preenchendo com 'N/A'...")
        df.fillna('N/A', inplace=True)

        df.to_csv(chosen_file, index=False)
        with open(chosen_file, 'rb') as f:
            s3_client.upload_fileobj(f, Bucket=chosen_bucket, Key=chosen_file)
        print("Arquivo pré-processado salvo no S3.")
        return 'branch_has_nulls'
    else:
        print("Não foram encontrados dados nulos. Arquivo válido.")
        return 'branch_no_nulls'

preprocess_file_task = PythonOperator(
    task_id='preprocess_file',
    python_callable=preprocess_file,
    provide_context=True,
    dag=dag,
)

s3_connection_task >> list_buckets_task >> choose_bucket_task >> list_files_task >> preprocess_file_task 

if __name__ == "__main__":
    dag.cli()