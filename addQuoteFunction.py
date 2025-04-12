import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Quotes')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        quote = body.get('quote')
        author = body.get('author')

        if not quote or not author:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Quote and author are required.'})
            }

        # Generate a unique ID
        quote_id = str(uuid.uuid4())

        table.put_item(
            Item={
                'id': quote_id,
                'quote': quote,
                'author': author
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Quote added successfully!'})
        }

    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to add quote.'})
        }
