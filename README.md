# Financial Document Analyzer
# Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents. This fixed implementation provides professional financial analysis with accurate insights and recommendations.
# Setup Instructions
## Prerequisites
Python 3.8+

Groq API key (for Llama model)

## Installation
Clone the repository :

Install required packages:

 pip install -r requirements.txt

## Create a .env file with your API keys:

GROQ_API_KEY=your_groq_api_key_here

## Create the data directory:
mkdir data

# Adding Sample Documents
Download a financial document (e.g., Tesla's quarterly report)

Save it as data/TSLA-Q2-2025-Update.pdf or upload via the API

# API Documentation
## Base URL

http://localhost:8000

Endpoints

Health 

 URL: /
 
 Method: GET
 
 Response:

{
  "message": "Financial Document Analyzer API is running"
}

 Analyze Financial Document
 
 URL: /analyze
 
 Method: POST
 
Parameters:

file: PDF file (required)

query: Analysis query (optional, defaults to "Analyze this financial document for investment insights")

Request Format: multipart/form-data

Response:

{
  "status": "success",
  "query": "User query",
  "analysis": "Analysis results",
  "file_processed": "filename.pdf"
}

## Example Usage
### Using Python :

import requests

url = "http://localhost:8000/analyze"

files = {"file": open("financial_report.pdf", "rb")}

data = {"query": "Analyze this financial document for investment opportunities"}

response = requests.post(url, files=files, data=data)

print(response.json())

# Features
Document Processing: Upload and process PDF financial documents

Financial Analysis: AI-powered analysis of financial statements

Investment Recommendations: Data-driven investment suggestions

Risk Assessment: Evaluation of financial risks

Multi-Agent Architecture: Specialized agents for different analysis tasks

# Architecture
The system uses a multi-agent architecture with specialized roles:

Financial Analyst: Primary analysis of financial documents

Document Verifier: Validates document authenticity

Investment Advisor: Provides investment recommendations

Risk Assessor: Evaluates financial risks

# Important Notes
The current agent descriptions and task goals are intentionally humorous but should be updated for production use

The system uses Groq's Llama model for analysis, which requires a Groq API key

File uploads are temporarily stored and automatically cleaned up after processing

For production use, consider adding:

Authentication and authorization

Rate limiting

Proper error logging

Database storage for analysis results

More robust PDF parsing

# Limitations
Currently supports only PDF documents

Requires Groq API key for LLM functionality

Analysis quality depends on the clarity of the source document

The humorous agent descriptions need to be updated for professional use
