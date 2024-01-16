import streamlit as st
from openai import OpenAI
import json
import re

# Initialize the OpenAI API key
client = OpenAI( api_key='', organization='' )

# Initialize variables
highlighted_text = ""
sentiment = ""
modified_text = ""

# Initialize session state variables
if 'sentiment' not in st.session_state:
    st.session_state['sentiment'] = ""
if 'highlighted_text' not in st.session_state:
    st.session_state['highlighted_text'] = ""

# Function to analyze sentiment
def analyze_sentiment(text):
    model = "gpt-4-1106-preview"
    response_format = {"type": "json_object"}
    messages = [
        {"role": "system", "content": "You need to analyze the sentiment of a text the user inputs about the climate. Return the analysis as a json object. The sentiment can be admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, or neutral."},
        {"role": "system", "content": "Directly modify the text by highlighting words with significant sentiment using HTML styling, by using a background-color with a corner radius of 5px. Apply colors as follows: Red for 'anger', Blue for 'sadness', Yellow for 'joy', Green for 'disgust', Gold for 'admiration', Orange for 'amusement', DarkRed for 'annoyance', LightGreen for 'approval', Pink for 'caring', Gray for 'confusion', Violet for 'curiosity', Crimson for 'desire', LightSlateGray for 'disappointment', DarkSlateGray for 'disapproval', RosyBrown for 'embarrassment', YellowGreen for 'excitement', Indigo for 'fear', Lavender for 'gratitude', SlateBlue for 'grief', DeepPink for 'love', DarkOrange for 'nervousness', LightCoral for 'optimism', SkyBlue for 'pride', Khaki for 'realization', PaleGreen for 'relief', Olive for 'remorse', Orchid for 'surprise', and White for 'neutral'. For darker colors, use white font color. Leave the rest of the text unstyled. Return the result as an HTML-formatted string within a json object. Example: {\"sentiment\": <sentiment>,\"text\":<html>}}"},
        {"role": "user", "content": text}
    ]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format=response_format,
            temperature=0.3,
        )

        print(response.choices[0].message.content)

        if response.choices:
            response_json = json.loads(response.choices[0].message.content)
            modified_html_text = response_json.get("text", "")
            average_sentiment = response_json.get("sentiment", "") 
            return infer_sentiments_from_highlighted_text(modified_html_text), modified_html_text, average_sentiment
        else:
            return "Error", "No choices available in the response"

    except Exception as e:
        print(e)
        return "Error", str(e)

# Function to infer sentiment from highlighted text
def infer_sentiments_from_highlighted_text(html_text):
    sentiments_detected = []
    sentiment_colors = {
        "Blue": "sadness", "Red": "anger", "Yellow": "joy", "Green": "disgust", "Gold": "admiration",
        "Orange": "amusement", "DarkRed": "annoyance", "LightGreen": "approval", "Pink": "caring",
        "Gray": "confusion", "Violet": "curiosity", "Crimson": "desire", "LightSlateGray": "disappointment",
        "DarkSlateGray": "disapproval", "RosyBrown": "embarrassment", "YellowGreen": "excitement",
        "Indigo": "fear", "Lavender": "gratitude", "SlateBlue": "grief", "DeepPink": "love",
        "DarkOrange": "nervousness", "LightCoral": "optimism", "SkyBlue": "pride", "Khaki": "realization",
        "PaleGreen": "relief", "Olive": "remorse", "Orchid": "surprise", "White": "neutral"
    }

    for color, sentiment in sentiment_colors.items():
        if f"<span style='background-color: {color};" in html_text:
            sentiments_detected.append(sentiment)

    return ', '.join(sentiments_detected) if sentiments_detected else "Unknown"


# Function to modify text
def modify_text(original_text, new_sentiment, highlighted_text):
    model = "gpt-4-1106-preview"
    response_format = {"type": "json_object"}
    messages = [
        {"role": "system", "content": "You need to modify the text the user inputs about the climate. The sentiment of the text needs to be changed to the following:"},
        {"role": "system", "content": new_sentiment},
        {"role": "system", "content": "Avoid the use of the word 'sustainable' by replacing it with a synonym without impacting the meaning. Make sure the original meaning of the text is not lost upon modifying the sentiment."},
        {"role": "system", "content": "Modify the text as follows without losing the original facts. Stay as close as possible to the original text. You are not allowed to go against the facts and meaning in the sentence, but you are allowed to use words with different sentiment with the same meaning to change the overall sentiment of the text: Apply HTML styling to highlight words, by using a background-color with a corner radius of 5px, with sentiment using specific colors. Use Red for 'anger', Blue for 'sadness', Yellow for 'joy', Green for 'disgust', Gold for 'admiration', Orange for 'amusement', DarkRed for 'annoyance', LightGreen for 'approval', Pink for 'caring', Gray for 'confusion', Violet for 'curiosity', Crimson for 'desire', LightSlateGray for 'disappointment', DarkSlateGray for 'disapproval', RosyBrown for 'embarrassment', YellowGreen for 'excitement', Indigo for 'fear', Lavender for 'gratitude', SlateBlue for 'grief', DeepPink for 'love', DarkOrange for 'nervousness', LightCoral for 'optimism', SkyBlue for 'pride', Khaki for 'realization', PaleGreen for 'relief', Olive for 'remorse', Orchid for 'surprise', and White for 'neutral'. For the darker colors, the font color of the sentiment needs to be white. Return the result as an HTML-formatted string within a JSON object.  Example: {\"modified_text\": <html>}}"},
        {"role": "user", "content": original_text}
    ]

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            response_format=response_format,
            temperature=0.5,
        )
        print(response.choices[0].message.content)
        response_json = json.loads(response.choices[0].message.content)
        modified_html_text = response_json.get("modified_text", "")

        return modified_html_text
    
    except Exception as e:
        print(e)
        return "Error" 

# Streamlit app layout
st.title("Sentiment Analysis and Modification App")

# sentiment colors with their corresponding sentiments
sentiment_colors = {
    "Gold": "Admiration", "Orange": "Amusement", "Red": "Anger", "DarkRed": "Annoyance", "LightGreen": "Approval", "Pink": "Caring", "Gray": "Confusion", "Violet": "Curiosity", "Crimson": "Desire", "LightSlateGray": "Disappointment", "DarkSlateGray": "Disapproval", "Green": "Disgust",  "RosyBrown": "Embarrassment", "YellowGreen": "Excitement", "Indigo": "Fear", "Lavender": "Gratitude", "SlateBlue": " Grief", "Yellow": "Joy", "DeepPink": "Love", "DarkOrange": "Nervousness", "LightCoral": "Optimism", "SkyBlue": "Pride", "Khaki": "Realization", "PaleGreen": "Relief", "Olive": "Remorse", "Blue": "Sadness","Orchid": "Surprise", "White": "Neutral"
}

# dark colors for which the font color needs to be white
dark_colors = ["DarkRed", "Blue", "Green", "DarkSlateGray", "Indigo", "SlateBlue", "Olive"]

# join the sentiment colors into an HTML string
sentiment_color_html = "".join(
    [f"<div style='background-color: {color}; color: {'white' if color in dark_colors else 'black'};margin-bottom: 5px;display: flex; justify-content: center; border-radius: 5px; width: 150px;'>{sentiment}</div>"
     for color, sentiment in sentiment_colors.items()]
)

# sidebar with the sentiment colors
st.sidebar.markdown("<h1 style='display: flex; align-items: center; margin-top: -40px; margin-bottom: 25px;'>" + "Sentiment Colors" + "</h1>", unsafe_allow_html=True)
# st.sidebar.markdown(sentiment_color_html, unsafe_allow_html=True)
st.sidebar.markdown("<div style='display: flex; flex-direction: column; align-items: center;'>" + sentiment_color_html + "</div>", unsafe_allow_html=True)

user_input = st.text_area("Enter your text:", height=150)

sentiment_labels = {
    0: 'admiration', 1: 'amusement', 2: 'anger', 3: 'annoyance', 4: 'approval', 5: 'caring',
    6: 'confusion', 7: 'curiosity', 8: 'desire', 9: 'disappointment', 10: 'disapproval',
    11: 'disgust', 12: 'embarrassment', 13: 'excitement', 14: 'fear', 15: 'gratitude',
    16: 'grief', 17: 'joy', 18: 'love', 19: 'nervousness', 20: 'optimism', 21: 'pride',
    22: 'realization', 23: 'relief', 24: 'remorse', 25: 'sadness', 26: 'surprise', 27: 'neutral'
}

# display the sentiment and highlighted text after clicking the button
if st.button("Analyze Sentiment"):
    sentiment, highlighted_text, average_sentiment = analyze_sentiment(user_input)
    st.session_state['sentiment'] = average_sentiment
    st.session_state['highlighted_text'] = highlighted_text
    st.markdown("**Sentiment:** " + sentiment, unsafe_allow_html=True)
    st.markdown("**Highlighted Text:**", unsafe_allow_html=True)
    st.markdown(highlighted_text, unsafe_allow_html=True)

new_sentiment = st.selectbox("Choose a new sentiment:", list(sentiment_labels.values()))

# display the modified text after clicking the button
if st.button("Modify Text"):
    modified_text = modify_text(user_input, new_sentiment, st.session_state['highlighted_text'])
    st.markdown("**Original Text:**", unsafe_allow_html=True)
    st.markdown(st.session_state['highlighted_text'], unsafe_allow_html=True)
    st.markdown("**Original Sentiment:** " + st.session_state['sentiment'], unsafe_allow_html=True)
    st.markdown("**Modified Text:**", unsafe_allow_html=True)
    st.markdown(modified_text, unsafe_allow_html=True)