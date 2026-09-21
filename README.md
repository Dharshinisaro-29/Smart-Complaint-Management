# Smart Complaint Management System

## Project Overview

The Smart Complaint Management System is a serverless web application developed using AWS services. It allows users to register complaints and track their complaint status using a unique complaint ID.

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Cloud Platform:** Amazon Web Services (AWS)
* **Website Hosting:** Amazon S3
* **Backend:** AWS Lambda (Python)
* **REST API:** Amazon API Gateway
* **Database:** Amazon DynamoDB

## System Architecture

User → S3-hosted Web Application → API Gateway → AWS Lambda → DynamoDB

The frontend sends requests to API Gateway. Lambda functions process the requests and store or retrieve complaint details from DynamoDB.

## Features

* Register a new complaint.
* Generate a unique complaint ID.
* Store complaint details in DynamoDB.
* Track complaints using their complaint ID.
* Display the complaint category and current status.
* Display an error message when a complaint ID is not found.

## Project Structure

```text
Smart-Complaint-Management/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── lambda/
│   ├── create_complaint.py
│   └── track_complaint.py
├── screenshots/
└── README.md
```

## AWS Services Configuration

**Amazon S3:** Hosts the static frontend website.

**Amazon API Gateway:** Provides REST API endpoints for complaint registration and tracking.

**AWS Lambda:** Executes the Python backend code for creating and retrieving complaints.

**Amazon DynamoDB:** Stores complaint information using `complaintId` as the primary key.

## API Endpoints

| Method | Endpoint                    | Description                 |
| ------ | --------------------------- | --------------------------- |
| POST   | `/complaints`               | Register a new complaint    |
| GET    | `/complaints/{complaintId}` | Track an existing complaint |

## Testing

The application was tested by registering a new complaint and tracking it using the generated complaint ID. The complaint details were successfully retrieved from DynamoDB and displayed on the website.

## Screenshots
### Complaint registration page
<img width="1917" height="976" alt="frontend page" src="https://github.com/user-attachments/assets/3ce7b547-a29f-46cd-8ec7-b7db30a17b26" />

## Successful registration

<img width="1912" height="907" alt="result_user" src="https://github.com/user-attachments/assets/6e5d0451-7404-45a9-bc5a-eca47e9a3178" />

## Complaint tracking result

<img width="1916" height="892" alt="track complaint screenshot" src="https://github.com/user-attachments/assets/eeb486fa-ba47-4f9e-9447-b773c6e40060" />

## DynamoDB table

<img width="1917" height="842" alt="dynamoDB resut" src="https://github.com/user-attachments/assets/7f3c65c5-abb4-4f62-b7a7-14c7f00d409e" />

## API Gateway

<img width="1917" height="762" alt="image" src="https://github.com/user-attachments/assets/1d6e09e4-10db-421b-9bfc-bed190037a53" />

## Lambda functions

<img width="1911" height="871" alt="image" src="https://github.com/user-attachments/assets/e1ff4ed7-0f07-493f-8fe3-f062356daf98" />

<img width="1917" height="857" alt="image" src="https://github.com/user-attachments/assets/195d0319-dbc3-4cdd-bc8a-181d4f0b4026" />
<img width="1911" height="855" alt="image" src="https://github.com/user-attachments/assets/0df8aec5-49fa-4f0c-98de-856ca14bb2e8" />





## Conclusion

This project demonstrates how AWS serverless services can be integrated to develop and host a complaint management web application without managing traditional backend servers.

