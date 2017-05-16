import boto3
from botocore.exceptions import ClientError

def handler(event, context):
  try:
    table = boto3.resource('dynamodb', region_name='us-west-2').Table('pizzashop')
    table.update_item(
      Key={'pizzamenuid': event['menu_id']},
      UpdateExpression="SET selection = :a",
      ExpressionAttributeValues={':a': event['selection']})
	  return "200 OK"
  except Exception as e:
    return e.message