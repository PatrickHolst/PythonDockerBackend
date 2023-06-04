import json
from databaseHandler import DBHandler
from models.parent import Parent


def lambda_handler(event, context):
    try:
        id = event['pathParameters']['id']
        parent_data = json.loads(event['body'])
        parent = Parent(
            id=id,
            name=parent_data['name'],
            salary=parent_data['salary'],
            days=parent_data['days']
        )

        existing_parent = DBHandler.get_parent(id)
        if existing_parent is None:
            return {
                'statusCode': 404,
                'body': 'Parent not found'
            }

        DBHandler.update_parent(parent)

        response = {
            'statusCode': 200,
            'body': {
                'message': 'Parent ' + parent.name + ' updated successfully'
            }
        }
        response['headers'] = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type, X-Auth-Token, Origin, Authorization",
            "Access-Control-Allow-Methods": "PUT, GET, OPTIONS"
        }

        return response

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }
