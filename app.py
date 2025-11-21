import streamlit as st
import requests
import time
import pandas as pd
from streamlit_javascript import st_javascript

# --- CONFIGURATION ---
# Replace this with your actual NordVPN affiliate link once approved
LINK_VPN = "https://nordvpn.com/affiliate/link"

st.set_page_config(page_title="IP Leak Detector", page_icon="🛡️", layout="centered")

# --- CUSTOM CSS (The "Alarm" Style) ---
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; text-align: center; margin-bottom: 1rem; font-weight: 800; color: #333; }
    .alert-box { 
        background-color: #FFEBEE; 
        border: 2px solid #FF5252; 
        padding: 30px; 
        border-radius: 15px; 
        text-align: center; 
        margin-bottom: 25px; 
        box-shadow: 0 4px 15px rgba(255, 82, 82, 0.2);
    }
    .ip-text { font-family: 'Courier New', monospace; font-size: 3.5rem; font-weight: bold; color: #D32F2F; margin: 10px 0; }
    .label-text { font-size: 1.1rem; color: #555; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
    .cta-button { 
        display: block; width: 100%; padding: 18px; 
        background-color: #2962FF; color: white !important; 
        text-align: center; text-decoration: none; font-weight: bold; 
        border-radius: 10px; font-size: 1.3rem; 
        transition: transform 0.1s;
        box-shadow: 0 6px 12px rgba(41, 98, 255, 0.2);
    }
    .cta-button:hover { transform: scale(1.02); background-color: #0039CB; }
</style>
""", unsafe_allow_html=True)

# --- LOGIC: CLIENT-SIDE FETCH ---
def get_client_ip():
    """Uses JavaScript to fetch the user's real IP address from the browser."""
    js_code = """await fetch('https://api.ipify.org').then(function(response) { return response.text() })"""
    return st_javascript(js_code)

def get_location_data(ip_address):
    """Queries the Geolocation API using the specific IP found."""
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        return response.json()
    except Exception:
        return None

# --- UI LAYOUT ---
st.markdown('<div class="main-header">🛡️ IP Leak Detector</div>', unsafe_allow_html=True)
st.write("Hackers, advertisers, and your ISP can see your location. Click below to see exactly what they see.")

# 1. Run JS immediately to be ready (Invisible)
client_ip = get_client_ip()

# The Trigger
if st.button("🔍 SCAN MY CONNECTION", type="primary", use_container_width=True):
    
    if client_ip:
        with st.spinner("Triangulating your location..."):
            time.sleep(1.0) # Dramatic delay
            data = get_location_data(client_ip)

        if data and data.get('status') == 'success':
            
            # 1. THE ALARM (The "Pain")
            st.markdown(f"""
            <div class="alert-box">
                <div class="label-text">YOUR PUBLIC IP ADDRESS IS:</div>
                <div class="ip-text">{data.get('query')}</div>
                <div style="color: #D32F2F; font-weight: bold;">⚠️ YOU ARE CURRENTLY EXPOSED</div>
            </div>
            """, unsafe_allow_html=True)

            # 2. THE DETAILS (The Proof)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**📍 Location Detected:**")
                st.info(f"{data.get('city')}, {data.get('country')}")
            with c2:
                st.markdown("**🏢 ISP Detected:**")
                st.warning(f"{data.get('isp')}")

            # 3. THE MAP (The Visual Impact)
            st.markdown("### 🗺️ Your Physical Location")
            if 'lat' in data and 'lon' in data:
                map_data = pd.DataFrame({'lat': [data['lat']], 'lon': [data['lon']]})
                st.map(map_data, zoom=11)

            # 4. THE SOLUTION (The Affiliate Pitch)
            st.markdown("---")
            st.markdown("""
            ### 🛑 Stop broadcasting your life.
            Your ISP sells this data. Hackers use it to find you.
            
            **The only way to hide this is a VPN.**
            """)
            
            st.markdown(f"""
            <a href="{LINK_VPN}" target="_blank" class="cta-button">
                🔒 Secure My Connection Now with NordVPN
            </a>
            <p style="text-align: center; margin-top: 12px; font-size: 0.8rem; color: #666;">
                30-Day Money-Back Guarantee • Instant Privacy
            </p>
            """, unsafe_allow_html=True)

        else:
            st.error("Could not locate IP details. Please try again.")
    else:
        st.info("Initializing scanner... please click again.")

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=100)
    st.markdown("### Digital Forensics")
    st.write("""
    This tool queries the global DNS network to see how your connection appears to the outside world.
    
    **Status:** 🔴 Unprotected
    """)