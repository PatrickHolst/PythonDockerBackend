import json
import uuid
from databaseHandler import DBHandler
from models.parent import Parent


def lambda_handler(event, context):
    try:
        request_body = json.loads(event['body'])
        parent_data = Parent(id=str(uuid.uuid4()),
                             name=request_body['name'],
                             salary=request_body['salary'],
                             days=request_body['days'])

        DBHandler.add_parent(parent_data)

        return {
            'statusCode': 201,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type, X-Auth-Token, Origin, Authorization",
                "Access-Control-Allow-Methods": "OPTIONS, POST"
            },
            'body': {
                'message': 'Parent ' + parent_data.name + ' created successfully',
                'id': parent_data.id
            }
        }
    except RuntimeError as e:
        if str(e) == 'Parent already exists':
            return {
                'statusCode': 409,
                'body': 'Parent already exists'
            }
        else:
            return {
                "statusCode": 500,
                "body": f"Internal Server Error: {str(e)}"
            }
