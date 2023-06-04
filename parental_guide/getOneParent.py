from databaseHandler import DBHandler
import json


def lambda_handler(event, context):
    try:
        id = event['pathParameters']['id']
        parent = DBHandler.get_parent(id)

        if parent is None:
            return {
                'statusCode': 404,
                'body': 'Parent not found'
            }

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS, GET"
            },
            "body": json.dumps(parent, default=str)
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }
