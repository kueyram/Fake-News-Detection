# Streamlit interface
st.title("Fake News Detection App")
st.write("Enter the news article text below to determine if it is real or fake.")

# Input field
news_input = st.text_area("Enter News Text", placeholder="Type the news text here...")

if st.button("Analyze"):
    if news_input.strip():
        # Make prediction
        result = predict_fake_news(news_input)
        st.subheader(f"The news article is: **{result}**")
    else:
        st.error("Please enter a text to analyze.")

