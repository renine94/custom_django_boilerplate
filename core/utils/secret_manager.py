from botocore.exceptions import ClientError

import os
import boto3
import json

from core.enums.const import AWSEnum


def load_secrets_manager_env():
    app_env = os.environ.get('APP_ENV') or 'test'

    secret_name = f"myapp/{app_env}"
    region_name = "ap-northeast-2"

    session = boto3.session.Session(
        aws_access_key_id=os.environ.get(AWSEnum.AWS_ACCESS_KEY_ID.value),
        aws_secret_access_key=os.environ.get(AWSEnum.AWS_SECRET_ACCESS_KEY.value),
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
        print('Secret Manager 에서 환경변수 값들을 가져오지 못하였습니다.')
        raise e

    envs = json.loads(get_secret_value_response['SecretString'])

    # Set the secret values as environment variables
    for key, value in envs.items():
        os.environ[key] = value
