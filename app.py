import streamlit as st

# some FAQs
faqs = {
    "what are your business hours": "Our business hours are Monday to Friday, 9 AM to 6 PM.",
    "how do i reset my password": "You can reset your password by clicking 'Forgot Password' on the login page.",
    "where are you located": "We are located at 123 Main Street, Thrissur.",
    "what is your return policy": "You can return products within 30 days of purchase.",
    "how can i contact support": "You can contact us at support@1122.com."
}

# Mock order data
orders = {
    "12345": "Shipped and will arrive tomorrow.",
    "67890": "Processing. Expected to ship in 2 days.",
    "1122": "Delivered yesterday.",
    "2211": "Delivering Today"
}

# Greetings and goodbyes
casual_talks = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! How can I help you?",
    "thank you": "You're welcome! Is there anything else I can help with?",
    "bye": "Goodbye! Have a great day!"
}

# Streamlit app
st.title("Customer Service Bot")

st.write("Welcome! How can I help you today?")

# Enter the user query
user_input = st.text_input("You : ")

if user_input: 

    # transform the query into lowercase
    user_input = user_input.lower()

    # case 1 : to check the query will be casual 
    if user_input in casual_talks:
        st.write(f"Bot : {casual_talks[user_input]}")

    # case 2 : to check the query contains the word "order"
    elif "order" in user_input :
        order_id = ''.join(filter(str.isdigit, user_input)) # fetch the order id

        if order_id:
            if order_id in orders:
                st.write(f"Bot : {orders[order_id]}")
            else:
                st.write(f"Bot : {order_id} Sorry, I couldn't find that order. Please check the ID.")
        else:
            st.write("Bot : please add your order ID")

    else:
        st.write("Bot : I'm not sure how to answer that. Let me escalate this to a human agent.")
        name = st.text_input("May I have your Name? ")
        email = st.text_input("May I have your Email? ")
        if name and email:
            st.write(f"Bot : Thank you {name}! Our human agent will reach out to you at {email}.") 
                
    st.write("---")
    feedback = st.text_area("Would you like to leave feedback?")
    if feedback:
        st.write("Thank you for your feedback!")

if "faq_displayed" not in st.session_state:
    st.session_state["faq_displayed"] = False
if "selected_question" not in st.session_state:
    st.session_state["selected_question"] = list(faqs.keys())[0]

if st.button("FAQs"):
    st.session_state["faq_displayed"] = True

if st.session_state["faq_displayed"]:
    questions = list(faqs.keys())
    selected_question = st.selectbox("Select a question:", options=questions, key="faq_selectbox", index=0)
    st.session_state["selected_question"] = selected_question
    if st.button("Submit"):
        st.write(f"{faqs[st.session_state['selected_question']]}")
