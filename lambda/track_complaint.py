import json
import boto3

table = boto3.resource("dynamodb").Table("Complaints")

def lambda_handler(event, context):
    print("RECEIVED EVENT:", json.dumps(event))
    complaint_id = event["pathParameters"]["complaintId"]

    result = table.get_item(
        Key={"complaintId": complaint_id}
    )

    item = result.get("Item")

        
    if not item:
        return {
            "statusCode": 404,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET,OPTIONS"
            },
            "body": json.dumps({
                "message": "Complaint not found"
            })
        }

        
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET,OPTIONS"
        },
        "body": json.dumps({
            "complaintId": item["complaintId"],
            "category": item["category"],
            "status": item["status"]
        })
    }
