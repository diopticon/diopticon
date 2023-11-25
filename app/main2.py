# app/main.py

import streamlit as st
import os
from langchain.llms import OpenAI
from langchain.chains import Chain
from langchain.retrieval import Retrieval

# in local context, load environment variables from .env file
# this is already done through CI/CD pipeline
if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

DB_DIOPTICON_S = os.getenv("DB_DIOPTICON_S")
DB_DIOPTICON_D = os.getenv("DB_DIOPTICON_D")
DB_DIOPTICON_U = os.getenv("DB_DIOPTICON_U")
DB_DIOPTICON_P = os.getenv("DB_DIOPTICON_P")
DB_DIS_S = os.getenv("DB_DIS_S")
DB_DIS_D = os.getenv("DB_DIS_D")
DB_DIS_U = os.getenv("DB_DIS_U")
DB_DIS_P = os.getenv("DB_DIS_P")
OPENAI_API = os.getenv("OPENAI_API")

# Initialize LLMS
llm = OpenAI()

# Initialize the dinner parties database. This will be in the DB_DIS database.
# The data is available, but has not yet been integrated into the database.
# Some 20 'Dis op Dinsdag' evenings have been organized in the last five years.
database = {
    "parties": [
        {
            "date": "2022-01-01",
            "attendees": ["John", "Alice", "Bob"],
            "keynote": "Speaker A",
            "topic": "Topic 1"
        },
        {
            "date": "2022-02-01",
            "attendees": ["Alice", "Charlie", "David"],
            "keynote": "Speaker B",
            "topic": "Topic 2"
        },
        # ... add more parties
    ]
}

# Initialize the larger dataset
larger_dataset = {
    "network": {
        "members": ["John", "Alice", "Bob", "Charlie", "David", ...],  # 50 members
        "parties": database["parties"]
    }
}

# Initialize the retrieval module
retrieval = Retrieval(data=[database, larger_dataset])

# Define the chatbot's conversation chain
chatbot_chain = Chain()

# Add a step to retrieve information from the dinner parties database
chatbot_chain.add_step(
    "RetrievePartyInfo",
    inputs={
        "database": database,
        "retrieval": retrieval
    },
    outputs=["party_info"]
)

# Add a step to ask pertinent questions to a specific member of the network
chatbot_chain.add_step(
    "AskPertinentQuestions",
    inputs={
        "member": "Alice",
        "party_info": chatbot_chain.get_output("party_info")
    },
    outputs=["questions"]
)

# Run the chatbot chain
chatbot_chain.run()

# Streamlit app
st.title("Dis op Dinsdag")

# Chatbot functionality
user_input = st.text_input("User Input")
if user_input:
    # Add user input to the chatbot chain
    chatbot_chain.add_step("UserInput", inputs={"user_input": user_input})

    # Run the chatbot chain
    chatbot_chain.run()

    # Get the chatbot's response
    response = chatbot_chain.get_output("response")

    # Display the chatbot's response
    st.text_area("Chatbot Response", response)