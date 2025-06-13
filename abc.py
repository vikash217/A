import streamlit as st
import requests
import time
from datetime import datetime


# st.set_page_config(page_title="WooCommerce Uptime Monitor", layout="wide")
st.title("iCubes-Voye site uptime monitoring")
st.markdown("<meta http-equiv='refresh' content='30'>", unsafe_allow_html=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; UptimeMonitor/1.0; +https://voyeglobal.com)"
}

sites = {
    "Main Site": "https://voyeglobal.com",
    "Agoda": "https://agoda.voyeglobal.com",
}

def check_uptime(url):
    try:
        start = time.time()
        response = requests.get(f"{url}/wp-json", timeout=5, headers=HEADERS)
        latency = round(time.time() - start, 2)
        if response.status_code == 200:
            return "UP", latency
        else:
            return f"DOWN ({response.status_code})", None
    except Exception as e:
        return f"DOWN ({str(e)})", None



st.markdown(f"**Last checked:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

for name, url in sites.items():
    status, latency = check_uptime(url)
    
    col1, col2, col3 = st.columns([3,1,2])
    
    with col1:
        st.subheader(name)
        st.write(url)
    with col2:
        if status.startswith("UP"):
            st.markdown(f"<span style='color: green; font-weight:bold;'>{status}</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color: red; font-weight:bold;'>{status}</span>", unsafe_allow_html=True)
    with col3:
        st.write(f"Latency: `{latency if latency is not None else '-'} s`")
    
    st.markdown("---")
