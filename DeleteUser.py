# This script will be used to delete IAM User

import boto3 


def delete_user(username):
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName=username
    )

    print(response)


delete_user('demo-user')  # you can change out the name of the user here