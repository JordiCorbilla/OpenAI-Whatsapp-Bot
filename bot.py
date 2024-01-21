# Copyright 2024 Jordi Corbilla. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import openai
import pyodbc
from fastapi import FastAPI, Form
import logging
import time
from twilio.rest import Client
from decouple import config

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")
twilio_number = config('TWILIO_NUMBER')
server = config('DB_SERVER')
database = config('DB_NAME')
client = Client(account_sid, auth_token)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
# Set up the OpenAI API client
openai.api_key = config("OPENAI_API_KEY")
whatsapp_number = config("TO_NUMBER")


def send_message(to_number, body_text):
    try:
        max_length = 1600
        # Calculate the number of messages
        num_messages = len(body_text) // max_length + (1 if len(body_text) % max_length > 0 else 0)

        for i in range(num_messages):
            # Calculate start and end indices for the substring
            start_index = i * max_length
            end_index = start_index + max_length

            # Get the substring for the current chunk
            message_chunk = body_text[start_index:end_index]

            # Send the chunk as a message
            message = client.messages.create(
                from_=f"whatsapp:{twilio_number}",
                body=message_chunk,
                to=f"whatsapp:{to_number}"
            )
            logger.info(f"Message {i + 1}/{num_messages} sent from {twilio_number} to {to_number}: {message.sid}")
            time.sleep(5)

    except Exception as e:
        logger.error(f"Error sending message to {to_number}: {e}")


@app.post("/message")
async def reply(Body: str = Form()):
    # Call the OpenAI API to generate text with GPT-3.5

    chat_response = "no data"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Your system message here, if any"},
                  {"role": "user", "content": Body}],
    )

    print(response)
    # Extracting and saving the response
    # The last message, if it's from the assistant, is the response
    if response['choices'] and response['choices'][0]['message']['role'] == 'assistant':
        chat_response = response['choices'][0]['message']['content'].strip()
    print(chat_response)

    send_message(whatsapp_number, chat_response)
    insert_text_into_db(whatsapp_number, Body, chat_response)
    return ""


def insert_text_into_db(sender, message, response):
    try:
        # Define the connection string for Windows Authentication
        conn_str = (
            f'DRIVER={{SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection=yes;'
        )

        # Establish a connection
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Define the insert query
        query = "INSERT INTO Conversations (sender, message, response) VALUES (?, ?, ?)"

        # Execute the query
        cursor.execute(query, sender, message, response)

        # Commit the transaction
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        print("Text inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
