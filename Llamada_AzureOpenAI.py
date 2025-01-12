"""
This script interacts with the Azure OpenAI service to generate chat completions using the GPT-4 model.
Modules:
    os: Provides a way of using operating system dependent functionality.
    base64: Provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data.
    openai: Provides the AzureOpenAI class for interacting with the Azure OpenAI service.
Environment Variables:
    ENDPOINT_URL: The URL endpoint for the Azure OpenAI service.
    DEPLOYMENT_NAME: The name of the deployment for the Azure OpenAI model.
    AZURE_OPENAI_API_KEY: The API key for authenticating with the Azure OpenAI service.
Constants:
    endpoint (str): The URL endpoint for the Azure OpenAI service.
    deployment (str): The name of the deployment for the Azure OpenAI model.
    subscription_key (str): The API key for authenticating with the Azure OpenAI service.
Functions:
    None
Usage:
    The script initializes the Azure OpenAI client with the provided endpoint and API key.
    It prepares a chat prompt and sends it to the Azure OpenAI service to generate a completion.
    The user can interact with the bot by providing input, and the bot will respond with a generated completion.
    The interaction continues until the user types "exit".
Example:
    Run the script and interact with the bot by typing messages. Type "exit" to quit the interaction.
"""
import os  
import base64
from openai import AzureOpenAI  

endpoint = os.getenv("ENDPOINT_URL", "Endpoint de conexión")  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "Key de conexión con Azure OpenAI")  

# Inicializar el cliente de Azure OpenAI con autenticación basada en claves    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-05-01-preview",  
)


#IMAGE_PATH = "YOUR_IMAGE_PATH"
#encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

#Prepare la indicación de chat 
chat_prompt = [
{
    "role": "system",
    "content": [
        {
            "type": "text",
            "text": "Es un asistente de inteligencia artificial que ayuda a los usuarios a encontrar información."
        }
    ]
}
] 

# Incluir el resultado de voz si la voz está habilitada  
messages = chat_prompt  

# Generar finalización  
completion = client.chat.completions.create(  
    model=deployment,  
    messages=messages #,  
    #max_tokens=800,  
    #temperature=0.7,  
    #top_p=0.95,  
    #frequency_penalty=0,  
    #presence_penalty=0,  
    #stop=None,  
    #stream=False
)
while True:
    user_input = input("User (Exit to quit): ")
    user_input_lower = user_input.lower()
    if user_input_lower == "exit":
        break
    chat_prompt = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_input
                }
            ]
        }
    ] 
    messages = chat_prompt
    completion = client.chat.completions.create(
        model=deployment,
        messages=messages
    )
    print("Bot:", completion.to_dict()['choices'][0]['message']['content'])
