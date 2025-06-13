import streamlit as st
import requests
import time
from streamlit_autorefresh import st_autorefresh


# st.set_page_config(page_title="Uptime Monitor", layout="wide")
st.title("iCubes-Voye Site uptime monitoring")

st_autorefresh(interval=30 * 1000, key="uptime-refresh")

sites = {
    "Main Site": "https://voyeglobal.com",
   
}

def check_uptime(url):
    try:
        start = time.time()
        response = requests.get(f"{url}/wp-json", timeout=5)
        latency = round(time.time() - start, 2)
        if response.status_code == 200:
            return "UP - Site is working fine.", latency
        else:
            return f"DOWN ({response.status_code})", None
    except Exception as e:
        return f"DOWN ({str(e)})", None

for name, url in sites.items():
    status, latency = check_uptime(url)
    st.subheader(f"{name} ({url})")
    st.markdown(f"**Status:** {status}")
    if latency is not None:
        st.markdown(f"**Latency:** `{latency}` seconds")
    st.markdown("---")
