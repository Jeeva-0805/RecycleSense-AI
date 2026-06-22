import streamlit as st
from waste_info import waste_data
from classifier import classify_waste

st.set_page_config(
    page_title="RecycleSense AI",
    page_icon="♻️"
)

st.title("♻️ RecycleSense AI")
st.markdown("""
### ♻️ Sustainable Waste Management

Upload an image of waste and receive recycling guidance,
disposal recommendations, and environmental impact information.
""")
st.subheader("Intelligent Recycling Assistant")

uploaded_file = st.file_uploader(
    "Upload a waste image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    category = classify_waste(uploaded_file.name)

    st.success(f"Predicted Category: {category}")

    st.write("### Disposal Method")
    st.write(waste_data[category]["disposal"])

    st.write("### Recycling Tip")
    st.write(waste_data[category]["tip"])

    st.write("### Environmental Impact")
    st.write(waste_data[category]["impact"])