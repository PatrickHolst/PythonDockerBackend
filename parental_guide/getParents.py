import json
from databaseHandler import DBHandler


def lambda_handler(event, context):
    try:
        parents = DBHandler.get_parents()
        items = parents['Items']

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS, GET"
            },
            "body": json.dumps(items, default=str)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Internal Server Error: {str(e)}"
        }
