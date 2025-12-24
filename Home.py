import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import uuid
from backend.quiz_contents import q_list
import random
from backend.utils import *

st.set_page_config(page_title="3 metrics", layout="centered")

st.title("Assess yourself on 3 interesting metrics")

# -----------------------------------------------------------------------------
#                                    TEST
#                          (not testing anything)
#                   (just a quiz but with a sexier name)
# -----------------------------------------------------------------------------

random.shuffle(q_list)

with st.form("test_form"):
    name = st.text_input("Enter your full name to be displayed on the leaderboard:", placeholder="John Smith")
    answers = []
    for q in range(12):
        st.write("---") # ---------------------------------------------------------
        answers.append(st.radio(
            q_list[q].text, [q_list[q].answers[j].text for j in range(4)]
        ))

    st.markdown("")
    st.markdown("")

    submitted = st.form_submit_button("Calculate Score")

# -----------------------------------------------------------------------------

if submitted:
    if not name:
        st.error("Please enter your name first!")
        st.stop()

    try:
        r_score, y_score, b_score = calculate_score(answers, q_list)

        conn = st.connection("gsheets", type=GSheetsConnection)

        df = conn.read(spreadsheet=st.secrets.connections.gsheets.spreadsheet,
                    worksheet="Sheet1", ttl=0)

        new_row = pd.DataFrame([{
            "id": str(uuid.uuid4()),
            "text": name,
            "R": r_score,
            "Y": y_score,
            "B": b_score
        }])

        updated_df = pd.concat([df, new_row], ignore_index=True)
        conn.update(worksheet="Sheet1", data=updated_df)

        st.success("Result calculated! Redirecting to the Gallery...")

        st.switch_page("pages/Gallery.py")

    except Exception as e:
        st.error(f"Could not save results: {e}")
