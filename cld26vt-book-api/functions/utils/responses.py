import json

def sendResponse(statusCode, body):
    return {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(body)
    }