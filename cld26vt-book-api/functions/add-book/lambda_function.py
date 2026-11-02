import json
import boto3

from utils.responses import sendResponse 

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("cloud-vt26-book-reviews")

def lambda_handler(event, context):
    # isbn, title, author
    book = json.loads(event["body"])

    table.put_item( 
        Item={
            "pk": f"BOOK#{book["isbn"]}",
            "sk": "PROFILE",
            "title": book["title"],
            "author": book["author"]
        })

    data = { "success": True, "message": "Book added" }

    return sendResponse(200, data)