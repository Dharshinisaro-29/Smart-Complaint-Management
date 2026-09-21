
import json
import uuid
import boto3

table = boto3.resource("dynamodb").Table("Complaints")

def lambda_handler(event, context):
    data = event.get("body", event)

    if isinstance(data, str):
        data = json.loads(data)

    complaint_id = "CMP-" + uuid.uuid4().hex[:8].upper()

    table.put_item(Item={
        "complaintId": complaint_id,
        "name": data["name"],
        "phone": data["phone"],
        "category": data["category"],
        "description": data["description"],
        "location": data["location"],
        "status": "Pending"
    })

        
    return {
        "statusCode": 201,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST,OPTIONS"
        },
        "body": json.dumps({
            "message": "Complaint registered successfully",
            "complaintId": complaint_id
        })
    }
       
