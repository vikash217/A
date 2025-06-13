import streamlit as st
import requests
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; UptimeMonitor/1.0; +https://voyeglobal.com)"
}

sites = {
    "Main Site": "https://voyeglobal.com",
}

def check_uptime(url):
    try:
        start = time.time()
        response = requests.get(f"{url}/wp-json", timeout=5, headers=HEADERS)
        latency = round(time.time() - start, 2)
        if response.status_code == 200:
            return "🟢 UP", latency
        else:
            return f"🔴 DOWN ({response.status_code})", None
    except Exception as e:
        return f"🔴 DOWN ({str(e)})", None

st.set_page_config(page_title="WooCommerce Uptime Monitor", layout="wide")
st.title("🌐 WooCommerce Multisite Uptime Monitor")

for name, url in sites.items():
    status, latency = check_uptime(url)
    st.subheader(f"{name} ({url})")
    st.markdown(f"**Status:** {status}")
    if latency is not None:
        st.markdown(f"**Latency:** `{latency}` seconds")
    st.markdown("---")
