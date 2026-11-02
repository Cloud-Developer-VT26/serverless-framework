import json
import boto3

from utils.responses import sendResponse

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cloud-vt26-book-reviews")

def lambda_handler(event, context):
    # isbn, memberId, rating, text
    review = json.loads(event["body"])

    table.put_item( 
        Item={
            "pk": f"BOOK#{review["isbn"]}",
            "sk": f"REVIEW#MEMBER#{review["memberId"]}",
            "rating": review["rating"],
            "text": review["text"]
        })

    table.put_item( 
        Item={
            "pk": f"MEMBER#{review["memberId"]}",
            "sk": f"REVIEW#BOOK#{review["isbn"]}",
            "rating": review["rating"],
            "text": review["text"]
        })

    data = { "success": True, "message": "Review added" }
    
    return sendResponse(200, data)