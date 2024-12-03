from openai import OpenAI
import json

#API key needed to access the api
client = OpenAI(api_key = "")

# Creates the response given to the AI, creates a JSON object form gpt-4o model
response = client.chat.completions.create(
    
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages= [{
        "role": "user",
        "content": '''
            Generate data about a restaurant in the form of the json object below.
            Place the restaurant in any american city.
            Here is the JSON object template you will populate:
            {
                "name": "<string>",
                "address": "<string>",
                "cuisine": "<string>",
                "openingHours": "<string>",
                "delivery": "<boolean>",
                "onlineOrdering": "<boolean>"
            }
        '''
    }]
    
)

# Create json object
json_object = json.loads(response.choices[0].message.content)

# create a file that contains json
file = open("data.json", "w")

# dump json created in the file
json.dump(json_object, file)

# close the file
file.close()
