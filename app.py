import streamlit as st
from waste_info import waste_data
from classifier import classify_waste
from impact_data import impact_data
from chatbot_data import qa_data
from ewaste_data import ewaste_data

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="RecycleSense AI",
    page_icon="♻️",
    layout="wide"
)

# ----------------------------------
# HEADER
# ----------------------------------
st.title("♻️ RecycleSense AI")

st.markdown("""
### 🌱 Intelligent Recycling Assistant

Upload an image of waste and receive recycling guidance,
environmental impact information, and sustainability insights.
""")

# ----------------------------------
# IMAGE UPLOAD
# ----------------------------------
uploaded_file = st.file_uploader(
    "Upload a waste image",
    type=["jpg", "jpeg", "png"]
)

# ----------------------------------
# WASTE ANALYSIS
# ----------------------------------
if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded Waste Image",
        use_container_width=True
    )

    category = classify_waste(uploaded_file.name)

    st.success(f"Predicted Category: {category}")

    # Dashboard
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="♻️ Waste Items Analyzed",
            value="1"
        )

    with col2:
        st.metric(
            label="🌱 Sustainability Score",
            value="85/100"
        )

    with col3:
        st.metric(
            label="🌍 CO₂ Saved",
            value=impact_data[category]["co2_saved"]
        )

    st.divider()

    # Disposal Information
    st.subheader("🗑️ Disposal Method")
    st.write(
        waste_data[category]["disposal"]
    )

    st.subheader("♻️ Recycling Tip")
    st.write(
        waste_data[category]["tip"]
    )

    # Environmental Impact
    st.subheader("🌍 Environmental Impact")

    st.info(
        f"""
CO₂ Saved: {impact_data[category]['co2_saved']}

Decomposition Time: {impact_data[category]['decomposition']}

Environmental Benefit:
{impact_data[category]['benefit']}
"""
    )

# ----------------------------------
# AI RECYCLING ASSISTANT
# ----------------------------------
st.divider()

st.header("🤖 AI Recycling Assistant")

question = st.selectbox(
    "Choose a sustainability question",
    list(qa_data.keys())
)

if question:
    st.success(
        qa_data[question]
    )

# ----------------------------------
# E-WASTE ADVISOR
# ----------------------------------
st.divider()

st.header("🔋 E-Waste Advisor")

device = st.selectbox(
    "Select an electronic item",
    list(ewaste_data.keys())
)

st.warning(
    f"Hazard: {ewaste_data[device]['hazard']}"
)

st.write(
    f"Disposal Method: {ewaste_data[device]['disposal']}"
)

st.success(
    f"Environmental Benefit: {ewaste_data[device]['benefit']}"
)

# ----------------------------------
# SIDEBAR
# ----------------------------------
st.sidebar.title("About RecycleSense AI")

st.sidebar.info(
    """
RecycleSense AI is an AI-powered sustainability platform
that helps users identify waste categories, understand
their environmental impact, and learn proper recycling
practices.

SDG Alignment:

• SDG 12 - Responsible Consumption and Production

• SDG 11 - Sustainable Cities and Communities

• SDG 13 - Climate Action
"""
)

# ----------------------------------
# RESPONSIBLE AI
# ----------------------------------
st.sidebar.subheader("Responsible AI")

st.sidebar.write("✅ Fairness")
st.sidebar.write("✅ Transparency")
st.sidebar.write("✅ Ethics")
st.sidebar.write("✅ Privacy")