from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract necessary information from the payload
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    # Handle different intents (customize based on your needs)
    response = handle_intent(intent, parameters)

    # Return a JSON response
    return JSONResponse(content={
        "fulfillmentText": response
    })

def handle_intent(intent: str, parameters: dict):
    # This function can handle different intents based on their names
    # Add more intents as needed and provide responses
    if intent == 'greeting':
        return "Hello! How can I assist you today?"
    elif intent == 'goodbye':
        return "Goodbye! Have a great day!"
    # Add more intents here as needed

    return "Sorry, I didn't understand your request."

