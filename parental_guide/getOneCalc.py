from databaseHandler import DBHandler
import json


def lambda_handler(event, context):
    try:

        calcId = event['pathParameters']['id']
        calculation = DBHandler.get_calculation(calcId)

        if calculation is None:
            return {
                'statusCode': 404,
                'body': 'Calculation not found'
            }

        return {
            'statusCode': 200,
            'body': json.dumps(calculation, default=str)
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }
