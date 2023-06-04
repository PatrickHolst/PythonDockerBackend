import json
from databaseHandler import DBHandler


def lambda_handler(event, context):
    try:
        calculations = DBHandler.get_calculations()
        items = calculations['Items']

        return {
            'statusCode': 200,
            'body': json.dumps(items, default=str)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Internal Server Error: {str(e)}"
        }
