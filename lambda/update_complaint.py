
import json
import boto3

table = boto3.resource("dynamodb").Table("Complaints")

def lambda_handler(event, context):
    data = event.get("body", event)

    if isinstance(data, str):
        data = json.loads(data)

    complaint_id = data["complaintId"]
    status = data["status"]

    if status not in ["Pending", "In Progress", "Resolved"]:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Invalid status"})
        }

    table.update_item(
        Key={"complaintId": complaint_id},
        UpdateExpression="SET #s = :status",
        ConditionExpression="attribute_exists(complaintId)",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":status": status}
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Complaint status updated",
            "complaintId": complaint_id,
            "status": status
        })
    }
