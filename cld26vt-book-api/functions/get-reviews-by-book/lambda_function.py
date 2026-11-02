import json
import boto3

from utils.responses import sendResponse

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cloud-vt26-book-reviews")

def lambda_handler(event, context):
    # isbn som queryparamter
    isbn = event["queryStringParameters"]["isbn"]

    print(json.dumps(event))

    response = table.query(
        KeyConditionExpression="pk = :pk AND begins_with(sk, :sk)",
        ExpressionAttributeValues={
            ":pk": f"BOOK#{isbn}",
            ":sk": "REVIEW#"
        }
    )

    print(json.dumps(response))

    data = { "success": True, "reviews": response["Items"] }
    
    return sendResponse(200, data)