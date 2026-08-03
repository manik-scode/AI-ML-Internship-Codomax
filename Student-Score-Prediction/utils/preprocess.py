import pandas as pd

def encode_features(df: pd.DataFrame) -> pd.DataFrame:

    mappings = {

        "Parental_Involvement":{
            "Low":0,
            "Medium":1,
            "High":2
        },

        "Access_to_Resources":{
            "Low":0,
            "Medium":1,
            "High":2
        },

        "Motivation_Level":{
            "Low":0,
            "Medium":1,
            "High":2
        },

        "Family_Income":{
            "Low":0,
            "Medium":1,
            "High":2
        },

        "Teacher_Quality":{
            "Low":0,
            "Medium":1,
            "High":2
        },

        "Peer_Influence":{
            "Negative":0,
            "Neutral":1,
            "Positive":2
        },

        "Parental_Education_Level":{
            "High School":0,
            "College":1,
            "Postgraduate":2
        },

        "Distance_from_Home":{
            "Near":0,
            "Moderate":1,
            "Far":2
        },

        "Extracurricular_Activities":{
            "No":0,
            "Yes":1
        },

        "Internet_Access":{
            "No":0,
            "Yes":1
        },

        "Learning_Disabilities":{
            "No":0,
            "Yes":1
        },

        "Gender":{
            "Female":0,
            "Male":1
        }

    }

    for column,mapping in mappings.items():
        df[column]=df[column].map(mapping)

    df = pd.get_dummies(
        df,
        columns=["School_Type"],
        drop_first=True,
        dtype=int
    )

    if "School_Type_Public" not in df.columns:
        df["School_Type_Public"] = 0

    return df