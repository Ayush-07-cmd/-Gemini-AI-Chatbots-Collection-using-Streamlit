import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key
genai.configure(api_key="AIzaSyD1XJtiSMuln2ZdcJtVakXJUZNw0y_fkC4")  # Replace with your Gemini API key

# Load the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state.messages = []

st.set_page_config(page_title="🎬 Gemini Movie & Web Series Chatbot", page_icon="🎥")
st.title("🎥 Gemini AI - Movie & Web Series Expert Chatbot")

# Add context: 100 Bollywood, 50 Hollywood, 50 Indian Web Series
bollywood_movies = """
Sholay, Dangal, Lagaan, 3 Idiots, Dilwale Dulhania Le Jayenge, Mughal-e-Azam, Mother India, Gully Boy,
Chak De India, Taare Zameen Par, PK, Queen, Kahaani, Andaz Apna Apna, Barfi, Swades, Bajrangi Bhaijaan,
Zindagi Na Milegi Dobara, Kal Ho Naa Ho, My Name is Khan, Rockstar, Kabir Singh, War, Raazi, Padmaavat,
Bhaag Milkha Bhaag, Uri, Yeh Jawaani Hai Deewani, Rang De Basanti, Tanu Weds Manu, Sanju, Airlift, Haider,
Kesari, Badhaai Ho, Article 15, Drishyam, Stree, Piku, Neerja, A Wednesday, Omkara, Black, Ta Ra Rum Pum,
Kabhi Khushi Kabhie Gham, Student of the Year, Don, Ra.One, KGF Chapter 1, KGF Chapter 2, RRR, Pushpa,
Singham, Dabangg, Housefull, Hera Pheri, Welcome, Bhool Bhulaiyaa, Phir Hera Pheri, Bheeshma, Badrinath Ki Dulhania,
Dil Chahta Hai, Hum Aapke Hain Koun, Jo Jeeta Wohi Sikandar, Deewaar, Amar Akbar Anthony, Anand, Aashiqui 2,
Baazigar, Devdas, Veer-Zaara, Mohabbatein, Hum Dil De Chuke Sanam, Kaho Naa... Pyaar Hai, Dhoom, Dhoom 2, Dhoom 3,
Race, Race 2, Singham Returns, Chennai Express, Happy New Year, Ek Tha Tiger, Tiger Zinda Hai, Sultan, Fan,
Tamasha, Rockstar, Jab We Met, Love Aaj Kal, Cocktail, Luka Chuppi, Dream Girl, Bala, Shubh Mangal Zyada Saavdhan,
Chhichhore, Dil Bechara, Malang, Batla House
"""

hollywood_movies = """
Titanic, Inception, The Dark Knight, Interstellar, Avatar, The Matrix, Gladiator, The Godfather,
Pulp Fiction, Fight Club, Shawshank Redemption, Forrest Gump, Saving Private Ryan, Avengers: Endgame,
Avengers: Infinity War, Iron Man, Captain America: Civil War, Black Panther, Doctor Strange, Thor: Ragnarok,
Guardians of the Galaxy, Joker, The Batman, Spider-Man: No Way Home, The Social Network, The Wolf of Wall Street,
The Revenant, The Irishman, Parasite, Everything Everywhere All At Once, Whiplash, La La Land, A Star Is Born,
The Grand Budapest Hotel, 1917, Dune, Oppenheimer, Barbie, John Wick, Mission: Impossible – Fallout,
Top Gun: Maverick, No Time To Die, Knives Out, Glass Onion, Get Out, Us, Her, Ex Machina, The Truman Show, The Prestige
"""

indian_web_series = """
Sacred Games, Mirzapur, Paatal Lok, The Family Man, Made in Heaven, Delhi Crime, Asur, Panchayat, Breathe, Special Ops,
Scam 1992, Aarya, Kota Factory, TVF Pitchers, Gullak, Criminal Justice, Bard of Blood, Inside Edge, Leila, Mumbai Diaries,
Ray, Betaal, JL50, Tandav, Hostages, Undekhi, Bhaukaal, The Forgotten Army, Bombay Begums, The Raikar Case,
The Final Call, The Great Indian Murder, Yeh Kaali Kaali Ankhein, Campus Diaries, Aspirants, Flames, Indori Ishq,
College Romance, ImMature, Cubicles, Engineering Girls, Apharan, The Night Manager, Rocket Boys, Rana Naidu, Dahaad,
Farzi, Trial by Fire, Scoop, The Railway Men, Sultan of Delhi
"""

# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Ask about any movie or web series...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Prompt with built-in movie/web series knowledge
    prompt = (
        "You are a helpful assistant who specializes in Bollywood and Hollywood movies, and Indian web series only.\n"
        "You must answer *only* questions related to:\n"
        "- Movie plots, actors, directors\n"
        "- Web series characters, seasons, reviews\n"
        "- Cinema history, trivia, or recommendations\n\n"
        "If the question is outside this domain, reply with:\n"
        "'Sorry, I can only answer questions related to movies and web series.'\n\n"
        f"Popular Bollywood Movies:\n{bollywood_movies}\n\n"
        f"Famous Hollywood Movies:\n{hollywood_movies}\n\n"
        f"Top Indian Web Series:\n{indian_web_series}\n\n"
        f"User query: {user_input}"
    )

    try:
        response = st.session_state.chat.send_message(prompt)
        answer = response.text
    except Exception as e:
        answer = "⚠️ Sorry, something went wrong. Please try again later."
        st.error(f"Technical details: {e}")

    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
