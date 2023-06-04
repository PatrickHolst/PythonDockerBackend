import boto3
import botocore

dynamodb = boto3.resource(
    'dynamodb', endpoint_url='http://host.docker.internal:8000')


class DBHandler:
    @staticmethod
    def get_table(table_name):
        table = dynamodb.Table(table_name)
        return table
##################################################################################

    @staticmethod
    def update_parent(parent):
        try:
            DBHandler.get_table('parents').update_item(
                Key={'ParentId': parent.id},
                UpdateExpression='SET #nameAttr = :nameVal, salary = :salaryVal, days = :daysVal',
                ExpressionAttributeNames={'#nameAttr': 'name'},
                ExpressionAttributeValues={
                    ':nameVal': parent.name,
                    ':salaryVal': parent.salary,
                    ':daysVal': parent.days
                }
            )
        except Exception as error:
            raise RuntimeError(
                'Error when updating parent:\nStacktrace: ' + str(error))

    @staticmethod
    def get_parent(id):
        try:
            response = DBHandler.get_table('parents').get_item(
                Key={'ParentId': str(id)}
            )

            parent = response.get('Item')

            return parent

        except Exception as error:
            raise RuntimeError(
                'Error when getting parent:\nStacktrace: ' + str(error))

    @staticmethod
    def get_parents():
        try:
            parents_table = DBHandler.get_table('parents')
            response = parents_table.scan()
            return response
        except Exception as error:
            raise RuntimeError(
                'Error when getting parent:\nStacktrace: ' + str(error))

    @staticmethod
    def delete_parent(id):
        try:
            DBHandler.get_table('parents').delete_item(
                Key={'ParentId': str(id)})
        except Exception as error:
            raise RuntimeError(
                'Error when deleting parent:\nStacktrace: ' + str(error))

    @staticmethod
    def add_parent(parent):
        DBHandler.get_table('parents').put_item(
            Item={
                'ParentId': parent.id,
                'name': parent.name,
                'salary': parent.salary,
                'days': parent.days,
            },
            ConditionExpression='attribute_not_exists(ParentId)'
        )
##################################################################################

    @staticmethod
    def add_calc(calculation):
        DBHandler.get_table('calculations').put_item(
            Item={
                'calcId': calculation.calcId,
                'startDate': calculation.startDate,
                'endDate': calculation.endDate,
                'numberOfDaysToSave': calculation.numberOfDaysToSave,
                'leastAmountEachMonth': calculation.leastAmountEachMonth,
                'parentToStayAtHomeFirst': calculation.parentToStayAtHomeFirst,
            },
            ConditionExpression='attribute_not_exists(calcId)'
        )

    @staticmethod
    def get_calculations():
        try:
            calcTable = DBHandler.get_table('calculations')
            response = calcTable.scan()
            return response
        except Exception as error:
            raise RuntimeError(
                'Error when getting parent:\nStacktrace: ' + str(error))

    @staticmethod
    def get_calculation(calcId):
        try:
            response = DBHandler.get_table('calculations').get_item(
                Key={'calcId': str(calcId)}
            )

            calculation = response.get('Item')

            return calculation

        except Exception as error:
            raise RuntimeError(
                'Error when getting calculation:\nStacktrace: ' + str(error))

    @staticmethod
    def delete_calculation(calcId):
        try:
            DBHandler.get_table('calculations').delete_item(
                Key={'calcId': str(calcId)})
        except Exception as error:
            raise RuntimeError(
                'Error when deleting parent:\nStacktrace: ' + str(error))

    @staticmethod
    def update_calculation(calculation):
        try:
            DBHandler.get_table('calculations').update_item(
                Key={'calcId': calculation.calcId},
                UpdateExpression='SET startDate = :startDateVal, endDate = :endDateVal, numberOfDaysToSave = :daysToSaveVal, leastAmountEachMonth = :amountVal, parentToStayAtHomeFirst = :parentVal',
                ExpressionAttributeValues={
                    ':startDateVal': calculation.startDate,
                    ':endDateVal': calculation.endDate,
                    ':daysToSaveVal': calculation.numberOfDaysToSave,
                    ':amountVal': calculation.leastAmountEachMonth,
                    ':parentVal': calculation.parentToStayAtHomeFirst
                }
            )
        except Exception as error:
            raise RuntimeError(
                'Error when updating calculation:\nStacktrace: ' + str(error))
