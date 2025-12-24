import streamlit as st
from google.oauth2 import service_account
from google.auth.transport.requests import Request # <--- Added this specific import
import googleapiclient.discovery

st.title("🔑 Key Validator")

try:
    # 1. Load the raw secrets dictionary
    if "connections" in st.secrets and "gsheets" in st.secrets["connections"]:
        info = dict(st.secrets["connections"]["gsheets"])
    else:
        st.error("Could not find [connections.gsheets] in secrets.toml")
        st.stop()

    # 2. Attempt the manual newline fix again
    if "\\n" in info["private_key"]:
        info["private_key"] = info["private_key"].replace("\\n", "\n")

    st.write("Checking credentials format...")

    # 3. Create Credentials Object directly
    creds = service_account.Credentials.from_service_account_info(
        info,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    st.success("✅ Credentials object created successfully (Format looks okay).")

    # 4. TEST: Try to "Refresh" the token (This contacts Google)
    st.write("Contacting Google to verify key signature...")

    # This was the line that failed before
    request = Request()
    creds.refresh(request)

    st.success("✅ Authentication Successful! Google accepted the Key.")

    # 5. Test Access to Sheet
    st.write(f"Attempting to access sheet...")
    service = googleapiclient.discovery.build('sheets', 'v4', credentials=creds)

    # Extract ID from URL
    # Supports both long URLs and raw IDs
    if "/d/" in info['spreadsheet']:
        sheet_id = info['spreadsheet'].split("/d/")[1].split("/")[0]
    else:
        sheet_id = info['spreadsheet']

    # Call the API
    sheet_metadata = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
    st.success(f"✅ Connection Established! Sheet Title: **{sheet_metadata.get('properties', {}).get('title')}**")

except ValueError as e:
    st.error(f"❌ Format Error: {e}")
    st.info("This usually means the Private Key string is malformed (missing headers or bad newlines).")

except Exception as e:
    # Check if it's a specific 401/Refresh error
    if "Unauthorized" in str(e) or "invalid_grant" in str(e):
         st.error(f"❌ Authentication Rejected (401): {e}")
         st.warning("Google says this key is invalid. The key string might be truncated, or the Service Account was deleted.")
    else:
        st.error(f"❌ Error: {e}")
