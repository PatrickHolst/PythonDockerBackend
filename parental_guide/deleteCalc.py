from databaseHandler import DBHandler


def lambda_handler(event, context):
    try:
        calcId = event['pathParameters']['id']
        calculation = DBHandler.get_calculation(calcId)

        if calculation is None:
            return {
                'statusCode': 404,
                'body': 'Calculation not found'
            }
        DBHandler.delete_calculation(calcId)

        return {
            'statusCode': 200,
            'body': {
                'message': 'Calculation deleted successfully'
            }
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Internal Server Error: {str(e)}"
        }
