import streamlit as st
import uuid
import pandas as pd
from acrylic import Color

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

def sync_widgets_to_rows():
    """
    Loops through the rows in memory and updates them with
    whatever is currently typed in the widgets.
    """
    for i, row in enumerate(st.session_state.rows):
        unique_id = row['id']

        # We reconstruct the keys we used in the layout
        k_txt = f"k_txt_{unique_id}"
        k_R = f"k_R_{unique_id}"
        k_Y = f"k_Y_{unique_id}"
        k_B = f"k_B_{unique_id}"

        # If the widget exists in session_state, grab its value
        if k_txt in st.session_state:
            st.session_state.rows[i]['text'] = st.session_state[k_txt]
        if k_R in st.session_state:
            st.session_state.rows[i]['R'] = st.session_state[k_R]
        if k_Y in st.session_state:
            st.session_state.rows[i]['Y'] = st.session_state[k_Y]
        if k_B in st.session_state:
            st.session_state.rows[i]['B'] = st.session_state[k_B]

def save_all_to_db(conn):
    """Syncs data and overwrites the Google Sheet"""
    sync_widgets_to_rows()

    # Convert list of dicts back to DataFrame
    updated_df = pd.DataFrame(st.session_state.rows)

    # Write to Google Sheets
    conn.update(worksheet="Sheet1", data=updated_df)
    st.cache_data.clear() # Force reload on next run

def add_row(conn):
    # 1. Harvest current data first! (So we don't lose edits)
    sync_widgets_to_rows()

    # 2. Add the new empty row
    st.session_state.rows.append({
        "id": str(uuid.uuid4()),
        "text": "",
        "R": 3, "Y": 3, "B": 3
    })

    # 3. Save everything
    save_all_to_db(conn)

def delete_row(row_id, conn):
    # 1. Harvest current data (so we save edits to OTHER rows)
    sync_widgets_to_rows()

    # 2. Filter out the deleted row
    st.session_state.rows = [r for r in st.session_state.rows if r['id'] != row_id]

    # 3. Save
    save_all_to_db(conn)
