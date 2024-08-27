
### README.md

# Travel Recommendation Chatbot

This project is a Flask-based web application that recommends travel destinations based on user preferences. It leverages the OpenAI API to process user input and generate personalized travel suggestions. The application is deployed on AWS Elastic Beanstalk.

## Features

- **Travel Recommendations:** Provides the top three travel destinations based on user preferences.
- **Category-Based Backgrounds:** Changes the background image based on the type of destination recommended (e.g., beach, mountains, city).
- **Interactive User Interface:** Users can input their travel preferences, and the app responds with personalized suggestions and dynamic visual changes.

## Getting Started

### Prerequisites

To run this project locally, you will need:

- **Python 3.8+**
- **pip**
- **Flask**
- **Gunicorn**
- **OpenAI API Key**

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/amajety1/VacationChatbot.git
   cd chatbot
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the Application:**

   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000`.

### Deployment

The application is deployed on AWS Elastic Beanstalk. To deploy it yourself:

1. **Initialize Elastic Beanstalk:**

   ```bash
   eb init
   ```

2. **Create an Environment and Deploy:**

   ```bash
   eb create your-env-name
   eb deploy
   ```

3. **Open the Application:**

   ```bash
   eb open
   ```

### Usage

1. **Enter your travel preferences** in the input box (e.g., "I want to go surfing and enjoy seafood").
2. **Receive recommendations**: The chatbot will suggest three destinations that match your criteria.
3. **View dynamic changes**: The background image will change based on the type of destination (e.g., beach, mountains).

### Project Structure

```
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── Procfile             # For Gunicorn in Elastic Beanstalk
├── .gitignore           # Git ignore file
├── templates/
│   └── index.html       # HTML template
└── static/
    └── images/          # Background images based on destination type
```

### Contributing

Contributions are welcome! Please fork this repository and submit a pull request for review.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments

- **OpenAI API**: For providing the AI-powered recommendations.
- **AWS Elastic Beanstalk**: For hosting the application.
- **Flask**: For the web framework.


```
