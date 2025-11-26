import streamlit as st
import requests
import time
import plotly.graph_objects as go

# --- AFFILIATE CONFIGURATION ---
# 1. WP ENGINE (High Ticket - $200 Min)
LINK_WPENGINE = "https://www.shareasale.com/r.cfm?b=394686&u=YOUR_ID&m=41388"

# 2. CLOUDWAYS (Recurring Income)
LINK_CLOUDWAYS = "https://www.cloudways.com/en/?id=YOUR_ID"

# 3. WEBHOSTING UK (Your New Awin Link)
LINK_WHUK = "https://www.awin1.com/cread.php?awinmid=27692&awinaffid=2667810&ued=https%3A%2F%2Fwww.webhosting.uk.com%2Fwordpress-hosting"

st.set_page_config(page_title="Site Speed Doctor", page_icon="⚡", layout="centered")

# --- CUSTOM CSS (FIXED FOR DARK MODE) ---
st.markdown("""
<style>
    .main-header { font-size: 3rem; text-align: center; font-weight: 800; color: #333; margin-bottom: 10px; }
    .sub-header { font-size: 1.2rem; text-align: center; color: #666; margin-bottom: 30px; }
    .metric-box { text-align: center; padding: 20px; background: #f0f2f6; border-radius: 10px; margin: 10px 0; }
    
    /* FIXED: Force Text Black for Recommendation Box */
    .recommendation-box { 
        border-left: 5px solid #ff4b4b; 
        padding: 20px; 
        background-color: #fff5f5; 
        border-radius: 5px; 
        margin-top: 20px;
        color: #000000 !important;
    }
    .recommendation-box h3, .recommendation-box p, .recommendation-box strong {
        color: #000000 !important;
    }

    /* Buttons */
    .cta-button { 
        display: block; width: 100%; padding: 12px; margin: 5px 0;
        text-align: center; color: white !important; text-decoration: none; 
        font-weight: bold; border-radius: 8px; font-size: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.1s;
    }
    .cta-button:hover { transform: scale(1.02); }
    
    .btn-wpengine { background-color: #0ecad4; color: #000 !important; }
    .btn-cloudways { background-color: #2c3e50; }
    .btn-whuk { background-color: #0056b3; } /* WebHosting UK Blue */
    
    /* FIXED: Force Text Black for Info Cards */
    .info-card { 
        background-color: #e8f4f8; 
        padding: 15px; 
        border-radius: 8px; 
        border: 1px solid #d1e7dd; 
        text-align: center; 
        height: 100%; 
        color: #000000 !important;
    }
    .info-card b, .info-card h3, .info-card p {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIC ---
def check_ttfb(url):
    try:
        if not url.startswith(('http://', 'https://')): url = 'https://' + url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        start = time.time()
        response = requests.get(url, headers=headers, timeout=10)
        ttfb = (time.time() - start) * 1000
        return {"success": True, "ttfb": round(ttfb, 2), "url": url}
    except Exception as e:
        return {"success": False, "error": str(e)}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966486.png", width=80)
    st.markdown("### ⚡ Speed Benchmarks")
    st.info("""
    **Time To First Byte (TTFB)**
    
    🟢 **< 200ms:** Excellent
    
    🟡 **200-600ms:** Average
    
    🔴 **> 600ms:** Critical
    """)
    st.markdown("---")
    st.caption("Tool by [Your Name]")

# --- MAIN UI ---
st.markdown('<div class="main-header">⚡ Site Speed Doctor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Check your server response time (TTFB) instantly.</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col1:
    target_url = st.text_input("Website URL", placeholder="example.com", label_visibility="collapsed")
with col2:
    scan_btn = st.button("🚀 Test Speed", type="primary", use_container_width=True)

if not scan_btn:
    st.markdown("### Why Server Speed Matters")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="info-card">📈 <b>SEO Ranking</b><br><br>Google penalizes slow servers.</div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="info-card">💰 <b>Conversion</b><br><br>1s delay = 7% drop in sales.</div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="info-card">📱 <b>Mobile Users</b><br><br>Slow sites fail on 4G/5G.</div>', unsafe_allow_html=True)

if scan_btn and target_url:
    with st.spinner("Pinging server..."):
        result = check_ttfb(target_url)
        
    if result["success"]:
        ttfb = result["ttfb"]
        
        if ttfb < 200: color, msg, status = "green", "Excellent! Your server is fast.", "PASS"
        elif ttfb < 600: color, msg, status = "orange", "Acceptable, but could be faster.", "WARN"
        else: color, msg, status = "red", "CRITICAL: Your hosting is too slow.", "FAIL"

        fig = go.Figure(go.Indicator(
            mode = "gauge+number", value = ttfb, title = {'text': "Response Time (ms)"},
            gauge = {'axis': {'range': [0, 1500]}, 'bar': {'color': color},
                     'steps': [{'range': [0, 200], 'color': "#d4edda"}, {'range': [200, 600], 'color': "#fff3cd"}, {'range': [600, 1500], 'color': "#f8d7da"}],
                     'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 600}}
        ))
        st.plotly_chart(fig, use_container_width=True)

        if status == "FAIL" or status == "WARN":
            st.markdown(f"""
            <div class="recommendation-box">
                <h3 style="margin-top:0">⚠️ Diagnosis: {msg}</h3>
                <p>Your server took <strong>{ttfb}ms</strong> just to wake up.</p>
                <p><strong>Solution:</strong> Move to a high-performance host.</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🚀 Recommended Fixes:")
            
            # --- UPDATED TRIFECTA WITH WEBHOSTING UK ---
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f"""<a href="{LINK_WPENGINE}" target="_blank" class="cta-button btn-wpengine">💎 WP Engine<br><span style='font-size:0.8em'>Best Managed</span></a>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""<a href="{LINK_CLOUDWAYS}" target="_blank" class="cta-button btn-cloudways">☁️ Cloudways<br><span style='font-size:0.8em'>Best Speed</span></a>""", unsafe_allow_html=True)
            with c3:
                # UPDATED BUTTON FOR WHUK
                st.markdown(f"""<a href="{LINK_WHUK}" target="_blank" class="cta-button btn-whuk">🇬🇧 WebHosting UK<br><span style='font-size:0.8em'>Best Value</span></a>""", unsafe_allow_html=True)
        else:
            st.success(f"✅ {msg}")
            st.balloons()
    else:
        st.error(f"Error: {result.get('error')}")