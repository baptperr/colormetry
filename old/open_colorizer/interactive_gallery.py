from acrylic import Color
import streamlit as st
import uuid
from backend.params import *
from backend.utils import *
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# ----------------------------------------------------------

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=st.secrets.connections.gsheets.spreadsheet,
               worksheet="Sheet1", ttl=5)

if df.empty:
    st.session_state.rows = []
else:
    df['R'] = df['R'].fillna(0).astype(int)
    df['Y'] = df['Y'].fillna(0).astype(int)
    df['B'] = df['B'].fillna(0).astype(int)
    df['text'] = df['text'].fillna("")
    st.session_state.rows = df.to_dict('records')


if "rows" not in st.session_state:
    st.session_state.rows = [{"id": str(uuid.uuid4()),
                              "text": "",
                              "R": 3,
                              "Y": 3,
                              "B": 3}]


css_rules = []

st.title(title)
# ---------------------
# ---------------------
st.markdown("""
<style>
    .color-card {
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        height: 100%; /* Ensure full height alignment */
        display: flex;
        align-items: center;
        justify_content: center;
    }
    .stButton button {
        margin-top: 8px; /* Align delete button visually */
    }
</style>
""", unsafe_allow_html=True)
# ---------------------
# ---------------------


st.markdown('')
if st.button("Take the test"):
    st.switch_page("Home.py")
st.markdown('')
st.error(f'### **{m1}**')
# st.markdown(color_title(m1, Color(ryb=[255,0,0])), unsafe_allow_html=True)
agency_expander = st.expander(f":red[_{m1_subtext}_]")
agency_expander.markdown(m1_spiel)

st.warning(f'### **{m2}**')
# st.markdown(color_title(m2, Color(ryb=[0,255,0])), unsafe_allow_html=True)
horizon_expander = st.expander(f":yellow[_{m2_subtext}_]")
horizon_expander.markdown(m2_spiel)

st.info(f'### **{m3}**')
# st.markdown(color_title(m3, Color(ryb=[0,0,255])), unsafe_allow_html=True)
vision_expander = st.expander(f":blue[_{m3_subtext}_]")
vision_expander.markdown(m3_spiel)

st.markdown('#### ')
title_cols = st.columns([1.6, 6.8,1,1,1])
title_cols[0].button("Reload", on_click=save_all_to_db, args=[conn])
title_cols[1].markdown(f'#### Gallery')
title_cols[2].markdown(color_text(m1,Color(ryb=[255,0,0])), unsafe_allow_html=True)
title_cols[3].markdown(color_text(m2,Color(ryb=[0,255,0])), unsafe_allow_html=True)
title_cols[4].markdown(color_text(m3,Color(ryb=[0,35,220])), unsafe_allow_html=True)

row_container = st.container()
with row_container:
    for i, row in enumerate(st.session_state.rows):
        # cols = st.columns([0.9,7.5,1,1,1]) # user interactive
        cols = st.columns([8.5,1,1,1])

        id = row['id']
        # with cols[0]:
        #     st.button('✕', key=f'del_{id}', on_click=delete_row, args=[id, conn])
        with cols[0]:
            st.session_state.rows[i]['text'] = st.text_input(
                f"txt_{id}", value=row["text"], key=f"k_txt_{id}", label_visibility="collapsed")
        with cols[1]:
            st.session_state.rows[i]['R'] = st.number_input(
                f"R_{id}", 0, 10, row["R"], key=f"k_R_{id}", label_visibility="collapsed")
        with cols[2]:
            st.session_state.rows[i]['Y'] = st.number_input(
                f"Y_{id}", 0, 10, row["Y"], key=f"k_Y_{id}", label_visibility="collapsed")
        with cols[3]:
            st.session_state.rows[i]['B'] = st.number_input(
                f"B_{id}", 0, 10, row["B"], key=f"k_B_{id}", label_visibility="collapsed")

        R, Y, B = st.session_state.rows[i]['R'], st.session_state.rows[i]['Y'], st.session_state.rows[i]['B']

        main_text_color = '#ffffff' if sum([R, Y, B])/3 > 6 else '#000000'
        R_text_color = '#ffffff' if R > 10 else '#000000'
        Y_text_color = '#ffffff' if Y > 10 else '#000000'
        B_text_color = '#ffffff' if B > 6 else '#000000'

        block_index = i+1

        css_rules.append(f"""input[aria-label="txt_{id}"] {{
                        background-color: {Color(ryb=[R*25.5, Y*25.5, B*25.5]).hex} !important;
                        color: {main_text_color} !important;
                        font-weight: bold;
                        font-size: 24px;
                        border-color: rgba(0,0,0,0.1) !important; }}
                        div[data-baseweb="input"]:has(input[aria-label="txt_{id}"]) {{
                        background-color: {Color(ryb=[R*25.5, Y*25.5, B*25.5]).hex} !important; }} """)

        css_rules.append(f"""input[aria-label="R_{id}"] {{
                        background-color: {Color(ryb=[R*25.5, 0, 0]).hex} !important;
                        font-size: 18px;
                        color: {R_text_color} !important; }}
                        div[data-baseweb="input"]:has(input[aria-label="R_{id}"]) {{ background-color: {Color(ryb=[R*25.5, 0, 0]).hex} !important; }} """)

        css_rules.append(f"""input[aria-label="Y_{id}"] {{
                        background-color: {Color(ryb=[0, Y*25.5, 0]).hex} !important;
                        font-size: 18px;
                        color: {Y_text_color} !important; }}
                        div[data-baseweb="input"]:has(input[aria-label="Y_{id}"]) {{ background-color: {Color(ryb=[0, Y*25.5, 0]).hex} !important; }} """)

        css_rules.append(f"""input[aria-label="B_{id}"] {{
                        background-color: {Color(ryb=[0, 0, B*25.5]).hex} !important;
                        font-size: 18px;
                        color: {B_text_color} !important; }}
                        div[data-baseweb="input"]:has(input[aria-label="B_{id}"]) {{ background-color: {Color(ryb=[0, 0, B*25.5]).hex} !important; }} """)

st.markdown(f"""
    <style>
    {''.join(css_rules)}
    input {{ font-weight: bold; }}</style>
    """, unsafe_allow_html=True)

# st.button("Add ＋", on_click=add_row, args=[conn], width='stretch')

# -----------------------------------------------------------------------------
#                                    TODO
# -----------------------------------------------------------------------------

# refine speil about the 3 metrics
# write a memory file
# fill out
