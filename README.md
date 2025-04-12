# 🌟 QuoteHub

QuoteHub is a **serverless quote-sharing web app** powered by AWS Cloud Services. It allows users to submit and view motivational quotes using a dynamic frontend connected to a cloud-native backend.

This project demonstrates the integration of **AWS Lambda**, **API Gateway**, **Amazon DynamoDB**, and **Amazon S3** to build a lightweight and scalable serverless application.


## 🚀 Features

- 🎲 Fetch random motivational quotes
- ➕ Add your own quotes to the database
- ☁️ Serverless architecture for scalability
- 🧩 Clean and simple frontend hosted on S3

---

## 🛠️ Tech Stack

| Layer       | Technology        |
|------------|-------------------|
| Frontend    | HTML, CSS (Static Site) |
| Hosting     | Amazon S3 (Static Website Hosting) |
| Backend     | AWS Lambda (Python) |
| API Routing | Amazon API Gateway |
| Database    | Amazon DynamoDB |

---

## 🧱 Architecture

```plaintext
[HTML/CSS (S3)]
     ↓
[API Gateway]
     ↓
[AWS Lambda]
     ↓
[DynamoDB]
```

> 📍 The frontend (hosted on S3) communicates with backend APIs via API Gateway, which triggers Lambda functions that read/write to DynamoDB.

---

## 📁 Project Structure

```
QuoteHub/
│
├── index.html                  # Frontend UI
├── lambda/
│   ├── get-quote.py           # Fetch quote Lambda function
│   └── add-quote.py           # Add quote Lambda function
├── architecture-diagram.png   # System architecture diagram
└── README.md
```

---

## 🔧 Setup & Deployment

### 1. Frontend (Amazon S3)
- Create an S3 bucket
- Enable **Static Website Hosting**
- Upload `index.html`
- Make the bucket **public** or use a CloudFront distribution

### 2. Backend (Lambda & API Gateway)
- Create two Lambda functions:
  - `add-quote`: accepts JSON with `quote` and `author`, and stores it in DynamoDB
  - `get-quote`: retrieves a random quote from DynamoDB
- Connect both to **API Gateway** (HTTP API or REST API)

### 3. Database (DynamoDB)
- Create a table named `quotes`
- Partition Key: `id` (string)
- Add attributes: `quote`, `author`

---

## ✅ Example Payloads

**POST /add-quote**

```json
{
  "quote": "The best way to get started is to quit talking and begin doing.",
  "author": "Walt Disney"
}
```

**GET /get-quote**

```json
{
  "quote": "The harder you work for something, the greater you'll feel when you achieve it.",
  "author": "Anonymous"
}
```

---

## 🎯 Learning Outcomes

- Hands-on with AWS Lambda & API Gateway
- Real-time integration of frontend and backend
- Using DynamoDB as a NoSQL backend for quotes
- Hosting a static site on S3

---

## 📌 Future Improvements

- Add user authentication (Cognito)
- Support categories/tags for quotes
- Track number of likes/shares per quote
- Mobile-friendly responsive design

---

## 🧑‍💻 Author

**QuoteHub** was developed as a cloud computing mini-project to explore AWS services and serverless application architecture.

> 🌈 “A quote a day keeps the burnout away.” – QuoteHub
