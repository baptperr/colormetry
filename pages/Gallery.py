from acrylic import Color
import streamlit as st
import uuid
from backend.params import *
from backend.utils import *
from streamlit_gsheets import GSheetsConnection
import pandas as pd


conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=st.secrets.connections.gsheets.spreadsheet,
               worksheet="Sheet1", ttl=0)

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

# initiate CSS class "color-card"
st.markdown("""
<style>
    .color-card {
        padding: 6px;
        border-radius: 6px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        height: 100%; /* Ensure full height alignment */
        display: flex;
        align-items: center;
        justify_content: center;
    }
</style>
""", unsafe_allow_html=True)

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
if title_cols[0].button("Reload"):
    st.rerun()
title_cols[1].markdown(f'#### Gallery')
title_cols[2].markdown(color_text(m1,Color(ryb=[255,0,0])), unsafe_allow_html=True)
title_cols[3].markdown(color_text(m2,Color(ryb=[0,255,0])), unsafe_allow_html=True)
title_cols[4].markdown(color_text(m3,Color(ryb=[0,35,220])), unsafe_allow_html=True)

row_container = st.container()
with row_container:
    for i, row in enumerate(st.session_state.rows):

        R, Y, B = row['R'], row['Y'], row['B']
        text_content = row['text']
        id = row['id']
        cols = st.columns([8.5,1,1,1])

        main_ryb = Color(ryb=[R*25.5, Y*25.5, B*25.5])
        r_ryb = Color(ryb=[R*25.5, 0, 0])
        y_ryb = Color(ryb=[0, Y*25.5, 0])
        b_ryb = Color(ryb=[0, 0, B*25.5])
        text_color = '#ffffff' if sum([R, Y, B])/3 > 6 else '#000000'
        R_text_color = '#ffffff' if R > 10 else '#000000'
        Y_text_color = '#ffffff' if Y > 10 else '#000000'
        B_text_color = '#ffffff' if B > 6 else '#000000'

        with cols[0]:
            st.markdown(f"""
                <div class="color-card" style="background-color: {main_ryb.hex}; color: {text_color}; justify-content: start; padding-left: 20px;">
                    {text_content}
                </div>
            """, unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f"""
                <div class="color-card" style="background-color: {r_ryb.hex}; color: {R_text_color}; justify-content: center; padding-left: 7px;">
                    {R}
                </div>
            """, unsafe_allow_html=True)
        with cols[2]:
            st.markdown(f"""
                <div class="color-card" style="background-color: {y_ryb.hex}; color: {Y_text_color}; justify-content: center; padding-left: 7px;">
                    {Y}
                </div>
            """, unsafe_allow_html=True)
        with cols[3]:
            st.markdown(f"""
                <div class="color-card" style="background-color: {b_ryb.hex}; color: {B_text_color}; justify-content: center; padding-left: 7px;">
                    {B}
                </div>
            """, unsafe_allow_html=True)
        st.markdown('')
