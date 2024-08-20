from flask import Flask, render_template, request, jsonify
import os
import openai
import ast  # Importing ast for safe evaluation
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    # Define the prompt for the model with an example
    prompt = f"""
    You are an advanced travel recommendation assistant. The user provides their preferences, and your job is to recommend the top three travel destinations that match their criteria.
    Additionally, categorize the user's preferences into one of the following categories: 
    Beach, Mountain, Desert, Neon City, Rivers, Rainforest, Countryside, Island, Snowy Landscape, Savanna, Forest, Lakes, Urban, Historic City, Coastal Town, Cultural Hub, Volcanic Landscape, Caves, Waterfalls, Hot Springs.
    For each category, they have their respective jpeg filename: beach.jpg, cave.jpg, coastal-town.jpg, countryside.jpg, cultural-hub.jpg, desert.jpg, forest.jpg, historic-city.jpg, hot-spring.jpg, island.jpg, lake.jpg, mountain.jpg, neon-city.jpg, rainforest.jpg, river.jpg, savannah.jpg, snowy_landscape.jpg, urban.jpg, volcanic-landscape.jpg, waterfall.jpg.

    Return both the recommended destinations and the most relevant category as its respective filename. 
    For each destination, include a brief description with the destination name as a title followed by a brief paragraph.

    Example response:
    [
        "1. Gold Coast, Australia - A paradise for surfers and beach lovers, the Gold Coast offers stunning beaches and a vibrant city life. From surfing the waves at Surfers Paradise to exploring the lush hinterlands, there's something for everyone.",
        "2. Bali, Indonesia - Bali is famous for its beautiful beaches, vibrant nightlife, and rich culture. It offers something for every traveler, from surfing at Kuta Beach to visiting the ancient temples and enjoying the local cuisine.",
        "3. Waikiki, Hawaii - Waikiki is a world-famous destination known for its stunning beach, excellent surfing, and luxury resorts. The area also offers plenty of shopping, dining, and entertainment options.",
        "beach.jpg"
    ]

    User's preferences:
    {user_input}
    """

    # Use the OpenAI API to generate travel recommendations and determine the category
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )

    # Log the specific message content
    raw_response = completion.choices[0].message.content
    print("Raw API Response:", raw_response)

    # Safely evaluate the response to convert it from a string to a list
    try:
        # Replace escaped characters and evaluate the response safely
        cleaned_response = raw_response.replace('\\"', '"').replace('\\n', '')
        response_list = ast.literal_eval(cleaned_response)
        recommendations = response_list[0:3]  # Taking the first three elements as recommendations
        category = response_list[-1]  # Assuming the last element is the category
    except Exception as e:
        print("Error parsing the response:", e)
        return jsonify({'response': 'Error parsing the response', 'category': 'undefined'}), 500

    # Return the response and category as JSON
    return jsonify({'response': recommendations, 'category': category})

if __name__ == '__main__':
    app.run(debug=True)
