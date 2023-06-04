import json
from databaseHandler import DBHandler


def lambda_handler(event, context):
    try:
        id = event['pathParameters']['id']
        parent = DBHandler.get_parent(id)

        if parent is None:
            return {
                "statusCode": 404,
                "body": "Parent not found"
            }

        DBHandler.delete_parent(id)

        response = {
            "statusCode": 200,
            "body": json.dumps({
                'message': 'Parent deleted successfully'
            })
        }

        # Add CORS headers
        response['headers'] = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type, X-Auth-Token, Origin, Authorization",
            "Access-Control-Allow-Methods": "DELETE, OPTIONS"
        }

        return response

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Internal Server Error: {str(e)}"
        }
