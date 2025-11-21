# ⚡ Site Speed Doctor

**Is your hosting killing your SEO?**

Site Speed Doctor is a Python-based utility tool that audits website server performance by measuring **Time To First Byte (TTFB)**. It identifies slow server response times—a critical SEO ranking factor—and recommends high-performance cloud hosting upgrades to fix the bottleneck.

🔗 **Live Demo:** [https://site-speed-doctor.streamlit.app](https://site-speed-doctor.streamlit.app)

---

## 🚀 Features

* **Precision Auditing:** Uses Python's `requests` library to ping servers and measure TTFB in milliseconds (ms).
* **Visual Diagnostics:** Features an interactive "Speedometer" Gauge (built with Plotly) to visualize server health.
* **Traffic Light Logic:**
    * 🟢 **Excellent (<200ms):** Google Core Web Vitals compliant.
    * 🟡 **Acceptable (200-600ms):** Needs improvement.
    * 🔴 **Critical (>600ms):** Severe ranking penalty risk.
* **Smart Recommendations:** Automatically suggests specific infrastructure upgrades (Cloudways, Kinsta) based on the severity of the lag.

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** (Frontend UI)
* **Requests** (Network Analysis)
* **Plotly** (Data Visualization)

---

## 💻 Installation (Run Locally)

To run this tool on your own machine or VPS:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mampadif/site-speed-doctor.git](https://github.com/mampadif/site-speed-doctor.git)
    cd site-speed-doctor
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

---

## 💰 Monetization Strategy

This tool generates **high-intent leads** for web hosting companies.

1.  **The Problem:** Users come to test their site because they suspect it is slow.
2.  **The Proof:** The tool scientifically proves their current host is underperforming (e.g., "Your TTFB is 1.2s").
3.  **The Solution:** The tool provides deep-links to high-performance alternatives (Cloudways, Kinsta) to solve the specific technical issue identified.

**Affiliate Partners:**
* Cloudways
* Kinsta
* Bluehost

---

*Built by [Fred Mampadi]*
