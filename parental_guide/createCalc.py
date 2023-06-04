import json
import uuid
from databaseHandler import DBHandler
from models.calculation import Calculation


def lambda_handler(event, context):
    try:
        request_body = json.loads(event['body'])
        calc_data = Calculation(calcId=str(uuid.uuid4()),
                                startDate=request_body['startDate'],
                                endDate=request_body['endDate'],
                                numberOfDaysToSave=request_body['numberOfDaysToSave'],
                                leastAmountEachMonth=request_body['leastAmountEachMonth'],
                                parentToStayAtHomeFirst=request_body['parentToStayAtHomeFirst'])
        DBHandler.add_calc(calc_data)

        return {
            'statusCode': 201,
            'body': {
                'message': 'Calculation created successfully',
                'id': calc_data.calcId
            }
        }
    except RuntimeError as e:
        if str(e) == 'Calculation already exists':
            return {
                'statusCode': 409,
                'body': 'Calculation already exists'
            }
        else:
            return {
                'statusCode': 500,
                "body": f"Internal Server Error: {str(e)}"

            }
