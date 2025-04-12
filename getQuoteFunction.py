import json
import boto3
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Quotes')

def lambda_handler(event, context):
    try:
        # Scan the table to get all quotes
        response = table.scan()
        items = response.get('Items', [])

        if not items:
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'quote': 'No quotes available.',
                    'author': 'System'
                })
            }

        # Pick a random quote
        selected = random.choice(items)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'quote': selected['quote'],
                'author': selected['author']
            })
        }

    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to fetch quote'})
        }
