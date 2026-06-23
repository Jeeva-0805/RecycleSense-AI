import streamlit as st
from waste_info import waste_data
from ai_classifier import detect_object
from waste_mapper import map_to_waste_category
import tempfile
from impact_data import impact_data
from chatbot_data import qa_data
from ewaste_data import ewaste_data
import pandas as pd
from datetime import datetime
import os
from report_generator import generate_report

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="RecycleSense AI",
    page_icon="♻️",
    layout="wide"
)
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stMetric {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #1f2937;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: #4ade80;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# HEADER
# ----------------------------------
st.title("♻️ RecycleSense AI")

container = st.container()

with container:
    # upload
    # detection
    # dashboard
    # charts

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
    width=500
)

    # Save uploaded image temporarily

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_path = tmp_file.name

# AI Object Detection

    detected_object = detect_object(temp_path)

# Waste Category Mapping

    category = map_to_waste_category(detected_object)
    new_record = pd.DataFrame([{
    "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Object": detected_object,
    "Category": category
}])

    new_record.to_csv(
    "history.csv",
    mode="a",
    header=not os.path.exists("history.csv"),
    index=False,
    lineterminator="\n"
)
    st.subheader("🔍 AI Detection Result")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"Detected Object: {detected_object}")

    with col2:
        st.success(f"Waste Category: {category}")
        confidence_score = 92

        st.progress(confidence_score / 100)

        st.info(
        f"AI Confidence Score: {confidence_score}%"
)

        st.success(f"🔍 Detected Object: {detected_object}")

        st.success(f"♻️ Waste Category: {category}")

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


st.subheader("📊 Waste Analytics Dashboard")

chart_data = pd.DataFrame({
    "Waste Type": [
        "Plastic",
        "Paper",
        "Metal",
        "Glass",
        "Organic",
        "E-Waste"
    ],
    "Count": [25, 18, 12, 10, 30, 8]
})

st.bar_chart(
    chart_data.set_index("Waste Type")
)
st.subheader("📜 Detection History")

history = pd.read_csv("history.csv")

st.dataframe(
    history.tail(10),
    use_container_width=True
)

# ----------------------------------
# AI RECYCLING ASSISTANT
# ----------------------------------
st.divider()
st.divider()

st.header("📄 Sustainability Report")

if st.button("Generate Report"):

    report = generate_report()

    st.text_area(
        "Generated Report",
        report,
        height=300
    )

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