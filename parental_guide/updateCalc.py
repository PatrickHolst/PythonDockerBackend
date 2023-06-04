import json
from databaseHandler import DBHandler
from models.calculation import Calculation


def lambda_handler(event, context):
    try:
        calcId = event['pathParameters']['id']
        calculation_data = json.loads(event['body'])
        calculation = Calculation(
            calcId=calcId,
            startDate=calculation_data['startDate'],
            endDate=calculation_data['endDate'],
            numberOfDaysToSave=calculation_data['numberOfDaysToSave'],
            leastAmountEachMonth=calculation_data['leastAmountEachMonth'],
            parentToStayAtHomeFirst=calculation_data['parentToStayAtHomeFirst'],
        )

        existing_calculation = DBHandler.get_calculation(calcId)
        if existing_calculation is None:
            return {
                'statusCode':  404,
                'body': 'Calculation not found'
            }

        DBHandler.update_calculation(calculation)
        return {
            'statusCode': 200,
            'body': {
                'message': 'Calculation updated successfully'
            }
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': {
                'message': 'Internal Server Error'
            }
        }
