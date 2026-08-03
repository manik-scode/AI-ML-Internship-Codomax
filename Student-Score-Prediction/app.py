import streamlit as st
import pandas as pd
from utils.preprocess import encode_features
import joblib
# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Student Score Prediction",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>

.stApp{
    background-color:#0B0F19;
    color:white;
}

.main-title{
    font-size:42px;
    font-weight:bold;
    color:#ffffff;
}

.sub-title{
    color:#9CA3AF;
    font-size:18px;
}

.card{
    background:#111827;
    padding:20px;
    border-radius:15px;
    border:1px solid #1F2937;
}

.metric{
    background:#111827;
    padding:18px;
    border-radius:12px;
    text-align:center;
    border:1px solid #1F2937;
}

.prediction{
    background:#1E293B;
    padding:30px;
    border-radius:15px;
    text-align:center;
    border:2px solid #3B82F6;
}

hr{
    border:1px solid #1F2937;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Load Model
# ---------------------------

model = joblib.load("models/ridge_model.joblib")

# ---------------------------
# Header
# ---------------------------

st.markdown(
    "<div class='main-title'>🎓 Student Score Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Predict student exam performance using Machine Learning (Ridge Regression)</div>",
    unsafe_allow_html=True
)

st.write("")

# ---------------------------
# Input Section
# ---------------------------

left,right = st.columns(2)

with left:

    st.markdown("## 📚 Academic Information")

    hours = st.slider(
        "Hours Studied",
        0,
        12,
        5
    )

    attendance = st.slider(
        "Attendance (%)",
        0,
        100,
        80
    )

    previous = st.slider(
        "Previous Scores",
        0,
        100,
        70
    )

    sleep = st.slider(
        "Sleep Hours",
        0,
        12,
        7
    )

    tutoring = st.slider(
        "Tutoring Sessions",
        0,
        10,
        2
    )

    physical = st.slider(
        "Physical Activity",
        0,
        10,
        2
    )

with right:

    st.markdown("## 👨‍🎓 Student Details")

    parental = st.selectbox(
        "Parental Involvement",
        ["Low","Medium","High"]
    )

    resources = st.selectbox(
        "Access to Resources",
        ["Low","Medium","High"]
    )

    activities = st.selectbox(
        "Extracurricular Activities",
        ["Yes","No"]
    )

    motivation = st.selectbox(
        "Motivation Level",
        ["Low","Medium","High"]
    )

    internet = st.selectbox(
        "Internet Access",
        ["Yes","No"]
    )

    income = st.selectbox(
        "Family Income",
        ["Low","Medium","High"]
    )

    teacher = st.selectbox(
        "Teacher Quality",
        ["Low","Medium","High"]
    )

    peer = st.selectbox(
        "Peer Influence",
        ["Negative","Neutral","Positive"]
    )

    disability = st.selectbox(
        "Learning Disabilities",
        ["Yes","No"]
    )

    education = st.selectbox(
        "Parental Education",
        ["High School","College","Postgraduate"]
    )

    distance = st.selectbox(
        "Distance From Home",
        ["Near","Moderate","Far"]
    )

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    school = st.selectbox(
        "School Type",
        ["Public","Private"]
    )

st.write("")

# ---------------------------
# Predict Button
# ---------------------------

if st.button("🚀 Predict Score", use_container_width=True):

    # ------------------------------------
    # Replace this with preprocessing later
    # ------------------------------------

    input_df = pd.DataFrame({
        "Hours_Studied":[hours],
        "Attendance":[attendance],
        "Parental_Involvement":[parental],
        "Access_to_Resources":[resources],
        "Extracurricular_Activities":[activities],
        "Sleep_Hours":[sleep],
        "Previous_Scores":[previous],
        "Motivation_Level":[motivation],
        "Internet_Access":[internet],
        "Tutoring_Sessions":[tutoring],
        "Family_Income":[income],
        "Teacher_Quality":[teacher],
        "Peer_Influence":[peer],
        "Physical_Activity":[physical],
        "Learning_Disabilities":[disability],
        "Parental_Education_Level":[education],
        "Distance_from_Home":[distance],
        "Gender":[gender],
        "School_Type":[school]
    })

    input_df = encode_features(input_df)

    prediction = model.predict(input_df)[0]



    st.write("")

    st.markdown(
        f"""
        <div class="prediction">
            <h2>📊 Predicted Exam Score</h2>
            <h1>{prediction:.2f} / 100</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if prediction>=90:
        st.success("⭐ Outstanding Performance")

    elif prediction>=75:
        st.success("🟢 Excellent Performance")

    elif prediction>=60:
        st.warning("🟡 Good Performance")

    elif prediction>=40:
        st.warning("🟠 Average Performance")

    else:
        st.error("🔴 Needs Improvement")

# ---------------------------
# Footer
# ---------------------------

st.write("")
st.write("---")

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Model","Ridge")

with c2:
    st.metric("R² Score","0.7709")

with c3:
    st.metric("Status","Ready")

st.caption("Developed by Manish Saini | AI & ML Internship | Codomax Digital Solutions")