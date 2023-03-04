import base64
import os

import boto3
from botocore.exceptions import ClientError
import json


def load_secrets_manager_env():
    app_env = 'test'

    secret_name = f"myapp/{app_env}"
    region_name = "ap-northeast-2"

    session = boto3.session.Session(
        # aws_access_key_id='',
        # aws_secret_access_key='',
        profile_name='Fitpet-dev',
        region_name=region_name
    )
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    envs = json.loads(get_secret_value_response['SecretString'])

    # Set the secret values as environment variables
    for key, value in envs.items():
        os.environ[key] = value
