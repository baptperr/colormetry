import streamlit as st
import uuid

def color_text(text, color_ryb, font_size=12, bold=True, text_color=False):
    if not text_color:
        text_color = '#ffffff' if sum(color_ryb._ryb)/3 > 180 else '#000000'
    else:
        text_color = text_color.hex
    hex_color = color_ryb.hex
    return f"""
        <span style="
            font-size: {font_size}px;
            background-color: {hex_color};
            color: {text_color};
            padding: 0.1em 0.1em;
            border-radius: 0.3em;
            {'font-weight: bold;' if bold else ''}">
            {text}
        </span>
        """

def color_title(text, color_ryb, font_size=32, bold=True, text_color=False):
    if not text_color:
        text_color = '#ffffff' if sum(color_ryb._ryb)/3 > 180 else '#000000'
    else:
        text_color = text_color.hex
    hex_color = color_ryb.hex
    return f"""
        <span style="
            font-size: {font_size}px;
            background-color: {hex_color};
            color: {text_color};
            padding: 0.2em 0.5em;
            border-radius: 0.3em;
            {'font-weight: bold;' if bold else ''}">
            {text}
        </span>
        """

def add_row():
    st.session_state.rows.append({"id": str(uuid.uuid4()),
                              "text": "",
                              "R": 3,
                              "Y": 3,
                              "B": 3})

def delete_row(row_id):
    st.session_state.rows = [row for row in st.session_state.rows if row['id'] != row_id]
