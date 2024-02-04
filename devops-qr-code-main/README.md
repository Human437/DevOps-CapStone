# devops-qr-code

This is the sample application for the DevOps Capstone Project.
It generates QR Codes for the provided URL, the front-end is in NextJS and the API is written in Python using FastAPI.

## Application

**Front-End**: A web application where users can submit URLs.

**API**: API that receives URLs and generates QR codes. The API stores the QR codes in cloud storage (Azure Blob Storage)

## Running locally

### API

The API code exists in the `api` directory. You can run the API server locally:

- Clone this repo
- Make sure you are in the `api` directory
- Create a virtualenv by typing in the following command: `python -m venv .venv`
- Install the required packages: `pip install -r requirements.txt`
- Create a `.env` file, and add you Azure Storage Connection String
- Also, change the storage account and container name in `main.py`
- *Optional*: Uncomment lines 62,63, and 66 to enable local storage of generated QR codes. This may be helpful for local testing
- Run the API server: `uvicorn main:app --reload`
- Your API Server should be running on port `http://localhost:8000`

### Front-end

The front-end code exits in the `front-end-nextjs` directory. You can run the front-end server locally:

- Clone this repo
- Make sure you are in the `front-end-nextjs` directory
- Install the dependencies: `npm install`
- Run the NextJS Server: `npm run dev`
- Your Front-end Server should be running on `http://localhost:3000`


## Goal

The goal is to get hands-on with DevOps practices like Containerization, CICD and monitoring.

## Original Author

[Rishab Kumar](https://github.com/rishabkumar7)

## Changes Made

Rewrote API to include the option to store generated QR codes locally for testing and to store generated QR codes in Azure Blob Storage instead of AWS

## License

[MIT](./LICENSE)
