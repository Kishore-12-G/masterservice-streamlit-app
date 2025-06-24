import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os
import json
import uuid
import time

# Set page config FIRST
st.set_page_config(
    page_title="VetNet API Explorer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL", "https://vetnet-microservice-gc3gdbpyhq-uc.a.run.app")
STATIC_TOKEN = os.getenv("STATIC_TOKEN", "Z4hi2ybPfPBKoLpiD1oEarcA7r5Et09pr98mt5oGQhYmUdWUzGPGvwFmz4hGGkmd")

# Modern color palette
COLORS = {
    "primary": "#6366F1",          # Indigo
    "secondary": "#8B5CF6",        # Violet
    "accent": "#06B6D4",           # Cyan
    "success": "#10B981",          # Emerald
    "warning": "#F59E0B",          # Amber
    "error": "#EF4444",            # Red
    "background": "#0F0F23",       # Deep dark blue
    "surface": "#1A1A2E",          # Dark surface
    "glass": "rgba(255, 255, 255, 0.1)",  # Glass effect
    "text": "#E2E8F0",             # Light text
    "text_muted": "#94A3B8",       # Muted text
    "border": "rgba(255, 255, 255, 0.2)",  # Subtle borders
}

# Apply revolutionary styling
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        /* Reset and base styles */
        * {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        
        .main {{
            background: linear-gradient(135deg, {COLORS["background"]} 0%, #0D1117 50%, {COLORS["surface"]} 100%);
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }}
        
        /* Animated background particles */
        .main::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.1) 0%, transparent 50%);
            pointer-events: none;
            z-index: -1;
            animation: float 20s ease-in-out infinite;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            33% {{ transform: translateY(-20px) rotate(1deg); }}
            66% {{ transform: translateY(-10px) rotate(-1deg); }}
        }}
        
        /* Glassmorphism cards */
        .glass-card {{
            background: {COLORS["glass"]};
            backdrop-filter: blur(20px);
            border: 1px solid {COLORS["border"]};
            border-radius: 20px;
            padding: 2rem;
            margin: 1.5rem 0;
            box-shadow: 
                0 8px 32px rgba(0, 0, 0, 0.3),
                0 4px 16px rgba(0, 0, 0, 0.2),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}
        
        .glass-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .glass-card:hover {{
            transform: translateY(-5px);
            box-shadow: 
                0 20px 40px rgba(0, 0, 0, 0.4),
                0 8px 20px rgba(0, 0, 0, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
        }}
        
        .glass-card:hover::before {{
            left: 100%;
        }}
        
        /* Premium header */
        .premium-header {{
            background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]}, {COLORS["accent"]});
            background-size: 300% 300%;
            animation: gradientShift 8s ease infinite;
            border-radius: 24px;
            padding: 3rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
            margin-bottom: 2rem;
        }}
        
        @keyframes gradientShift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        
        .premium-header::after {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url("data:image/svg+xml,%3Csvg viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cdefs%3E%3Cpattern id='grid' width='10' height='10' patternUnits='userSpaceOnUse'%3E%3Cpath d='M 10 0 L 0 0 0 10' fill='none' stroke='rgba(255,255,255,0.1)' stroke-width='0.5'/%3E%3C/pattern%3E%3C/defs%3E%3Crect width='100' height='100' fill='url(%23grid)'/%3E%3C/svg%3E");
            opacity: 0.3;
            pointer-events: none;
        }}
        
        .header-title {{
            font-size: 3.5rem;
            font-weight: 800;
            color: white;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            margin: 0;
            position: relative;
            z-index: 1;
        }}
        
        .header-subtitle {{
            font-size: 1.2rem;
            color: rgba(255, 255, 255, 0.9);
            margin: 0.5rem 0 0 0;
            font-weight: 400;
            position: relative;
            z-index: 1;
        }}
        
        /* Modern buttons */
        .stButton > button {{
            background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]}) !important;
            color: white !important;
            border: none !important;
            border-radius: 16px !important;
            padding: 16px 32px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            box-shadow: 
                0 8px 25px rgba(99, 102, 241, 0.4),
                0 4px 12px rgba(0, 0, 0, 0.2) !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            position: relative !important;
            overflow: hidden !important;
        }}
        
        .stButton > button::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.6s;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-3px) !important;
            box-shadow: 
                0 15px 35px rgba(99, 102, 241, 0.5),
                0 8px 20px rgba(0, 0, 0, 0.3) !important;
        }}
        
        .stButton > button:hover::before {{
            left: 100%;
        }}
        
        .stButton > button:active {{
            transform: translateY(-1px) !important;
        }}
        
        /* Elegant input fields */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div,
        .stNumberInput > div > div > input {{
            background: {COLORS["glass"]} !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid {COLORS["border"]} !important;
            border-radius: 12px !important;
            color: {COLORS["text"]} !important;
            padding: 16px !important;
            font-size: 16px !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
        }}
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stNumberInput > div > div > input:focus {{
            border-color: {COLORS["primary"]} !important;
            box-shadow: 
                0 0 0 3px rgba(99, 102, 241, 0.1),
                0 8px 25px rgba(0, 0, 0, 0.15) !important;
            transform: translateY(-2px) !important;
        }}
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {COLORS["surface"]} 0%, {COLORS["background"]} 100%) !important;
            border-right: 1px solid {COLORS["border"]} !important;
        }}
        
        [data-testid="stSidebar"] > div {{
            padding-top: 2rem !important;
        }}
        
        /* Status indicators */
        .status-success {{
            background: linear-gradient(135deg, {COLORS["success"]}, #059669);
            color: white;
            padding: 20px;
            border-radius: 16px;
            margin: 20px 0;
            box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
            border: 1px solid rgba(16, 185, 129, 0.3);
        }}
        
        .status-error {{
            background: linear-gradient(135deg, {COLORS["error"]}, #DC2626);
            color: white;
            padding: 20px;
            border-radius: 16px;
            margin: 20px 0;
            box-shadow: 0 8px 25px rgba(239, 68, 68, 0.3);
            border: 1px solid rgba(239, 68, 68, 0.3);
        }}
        
        .status-warning {{
            background: linear-gradient(135deg, {COLORS["warning"]}, #D97706);
            color: white;
            padding: 20px;
            border-radius: 16px;
            margin: 20px 0;
            box-shadow: 0 8px 25px rgba(245, 158, 11, 0.3);
            border: 1px solid rgba(245, 158, 11, 0.3);
        }}
        
        /* Metric cards */
        .metric-card {{
            background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]});
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            color: white;
            margin: 1rem 0;
            box-shadow: 0 12px 30px rgba(99, 102, 241, 0.3);
            position: relative;
            overflow: hidden;
        }}
        
        .metric-card::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
            animation: rotate 20s linear infinite;
        }}
        
        @keyframes rotate {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        
        /* Enhanced tabs */
        .stTabs [role="tablist"] {{
            background: {COLORS["glass"]} !important;
            backdrop-filter: blur(10px) !important;
            border: 1px solid {COLORS["border"]} !important;
            border-radius: 16px !important;
            padding: 8px !important;
            margin-bottom: 24px !important;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]}) !important;
            color: white !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4) !important;
        }}
        
        /* Progress bar */
        .stProgress > div > div > div {{
            background: linear-gradient(90deg, {COLORS["primary"]}, {COLORS["accent"]}) !important;
            border-radius: 10px !important;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4) !important;
        }}
        
        /* Expander styling */
        .stExpander {{
            background: {COLORS["glass"]} !important;
            backdrop-filter: blur(15px) !important;
            border: 1px solid {COLORS["border"]} !important;
            border-radius: 16px !important;
            margin: 1rem 0 !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1) !important;
        }}
        
        /* Headers */
        h1, h2, h3, h4, h5, h6 {{
            color: {COLORS["text"]} !important;
            font-weight: 700 !important;
        }}
        
        /* Icon styling */
        .icon-container {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]});
            border-radius: 20px;
            font-size: 24px;
            margin-right: 20px;
            box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
            position: relative;
            overflow: hidden;
        }}
        
        .icon-container::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.2) 0%, transparent 70%);
            animation: rotate 15s linear infinite;
        }}
        
        .section-header {{
            display: flex;
            align-items: center;
            margin-bottom: 2rem;
        }}
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: {COLORS["surface"]};
            border-radius: 10px;
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]});
            border-radius: 10px;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background: linear-gradient(135deg, {COLORS["secondary"]}, {COLORS["accent"]});
        }}
        
        /* Dataframe styling */
        .stDataFrame {{
            background: {COLORS["glass"]} !important;
            backdrop-filter: blur(10px) !important;
            border-radius: 16px !important;
            border: 1px solid {COLORS["border"]} !important;
            overflow: hidden !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1) !important;
        }}
        
        /* Footer */
        .premium-footer {{
            background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]});
            color: white;
            text-align: center;
            padding: 3rem 2rem;
            border-radius: 24px;
            margin: 3rem 0 2rem 0;
            position: relative;
            overflow: hidden;
        }}
        
        .premium-footer::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
            animation: rotate 30s linear infinite;
        }}
        
        /* Pulse animation for active elements */
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.8; }}
        }}
        
        .pulse {{
            animation: pulse 2s ease-in-out infinite;
        }}
        
        /* Floating labels */
        .floating-label {{
            position: relative;
            margin-bottom: 1.5rem;
        }}
        
        .floating-label input:focus + label,
        .floating-label input:not(:placeholder-shown) + label {{
            transform: translateY(-25px) scale(0.8);
            color: {COLORS["primary"]};
        }}
        
        .floating-label label {{
            position: absolute;
            top: 16px;
            left: 16px;
            color: {COLORS["text_muted"]};
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            pointer-events: none;
            z-index: 1;
        }}
    </style>
""", unsafe_allow_html=True)

# Default values for all fields
DEFAULT_VALUES = {
    "Companies": {
        "name": "Quantum Innovations",
        "logo": "https://example.com/logo.png",
        "industry": "Quantum Computing",
        "website": "https://quantum-innovations.com",
        "location": "San Jose, CA"
    },
    "Degrees": {
        "name": "Masters in Artificial Intelligence"
    },
    "Universities": {
        "name": "MIT",
        "location": "Cambridge, Massachusetts",
        "country": "United States",
        "website": "https://www.mit.edu"
    },
    "Job Titles": {
        "name": "Chief Technology Officer"
    },
    "Skills": {
        "name": "Quantum Algorithm Design"
    },
    "Field of Studies": {
        "name": "Quantum Physics"
    }
}

# API Endpoints configuration
ENDPOINTS = {
    "Companies": {
        "GET": "/companies",
        "POST": "/companies",
        "PUT": "/companies/{id}",
        "DELETE": "/companies/{id}",
        "GET_MANY": "/companies/getMany",
        "DELETE_MANY": "/companies/deleteMany",
        "icon": "🏢",
        "fields": {
            "name": {"type": "text", "required": True, "placeholder": "e.g., Acme Corporation"},
            "logo": {"type": "text", "required": False, "placeholder": "e.g., https://example.com/logo.png"},
            "industry": {"type": "text", "required": False, "placeholder": "e.g., Technology"},
            "website": {"type": "text", "required": False, "placeholder": "e.g., https://acme.com"},
            "location": {"type": "text", "required": False, "placeholder": "e.g., San Francisco, CA"}
        }
    },
    "Degrees": {
        "GET": "/degrees",
        "POST": "/degrees",
        "PUT": "/degrees/{id}",
        "DELETE": "/degrees/{id}",
        "GET_MANY": "/degrees/getMany",
        "DELETE_MANY": "/degrees/deleteMany",
        "icon": "🎓",
        "fields": {
            "name": {"type": "text", "required": True, "placeholder": "e.g., Bachelor of Science in Computer Science"}
        }
    },
    "Universities": {
        "GET": "/universities",
        "POST": "/universities",
        "PUT": "/universities/{id}",
        "DELETE": "/universities/{id}",
        "GET_MANY": "/universities/getMany",
        "DELETE_MANY": "/universities/deleteMany",
        "icon": "🏛️",
        "fields": {
            "name": {"type": "text", "required": True, "placeholder": "e.g., Harvard University"},
            "location": {"type": "text", "required": False, "placeholder": "e.g., Cambridge, Massachusetts"},
            "country": {"type": "text", "required": False, "placeholder": "e.g., United States"},
            "website": {"type": "text", "required": False, "placeholder": "e.g., https://www.harvard.edu"}
        }
    },
    "Job Titles": {
        "GET": "/jobtitles",
        "POST": "/jobtitles",
        "PUT": "/jobtitles/{id}",
        "DELETE": "/jobtitles/{id}",
        "GET_MANY": "/jobtitles/getMany",
        "DELETE_MANY": "/jobtitles/deleteMany",
        "icon": "👔",
        "fields": {
            "name": {"type": "text", "required": True, "placeholder": "e.g., Software Engineer"}
        }
    },
    "Skills": {
        "GET": "/skills",
        "POST": "/skills",
        "PUT": "/skills/{id}",
        "DELETE": "/skills/{id}",
        "GET_MANY": "/skills/getMany",
        "DELETE_MANY": "/skills/deleteMany",
        "icon": "🛠️",
        "fields": {
            "name": {"type": "text", "required": True, "placeholder": "e.g., Python Programming"}
        }
    },
    "Field of Studies": {
        "GET": "/fieldofstudies",
        "POST": "/fieldofstudies",
        "PUT": "/fieldofstudies/{id}",
        "DELETE": "/fieldofstudies/{id}",
        "GET_MANY": "/fieldofstudies/getMany",
        "DELETE_MANY": "/fieldofstudies/deleteMany",
        "icon": "📚",
        "fields": {
            "name": {"type": "text", "required": True, "placeholder": "e.g., Computer Science"}
        }
    }
}

# Headers for API requests
HEADERS = {
    "static-token": STATIC_TOKEN,
    "Content-Type": "application/json"
}

# Function to make API requests with visual progress
def make_request(method, url, data=None, params=None):
    try:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Enhanced progress animation
        for percent in range(0, 101, 10):
            progress_bar.progress(percent)
            if percent < 30:
                status_text.markdown(f"<div style='text-align: center; color: {COLORS['accent']};'>🚀 Initializing connection... {percent}%</div>", unsafe_allow_html=True)
            elif percent < 70:
                status_text.markdown(f"<div style='text-align: center; color: {COLORS['primary']};'>⚡ Processing request... {percent}%</div>", unsafe_allow_html=True)
            else:
                status_text.markdown(f"<div style='text-align: center; color: {COLORS['success']};'>✨ Finalizing... {percent}%</div>", unsafe_allow_html=True)
            time.sleep(0.05)
        
        if method == "GET":
            response = requests.get(url, headers=HEADERS, params=params)
        elif method == "POST":
            response = requests.post(url, headers=HEADERS, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=HEADERS, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=HEADERS)
        else:
            return {"error": "Unsupported method"}
        
        progress_bar.progress(100)
        status_text.markdown(f"<div style='text-align: center; color: {COLORS['success']};'>✅ Response received!</div>", unsafe_allow_html=True)
        time.sleep(0.3)
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None, "text": e.response.text if e.response else ""}
    finally:
        time.sleep(0.5)
        progress_bar.empty()
        status_text.empty()

# Generate sample UUIDs for bulk operations
def generate_sample_ids(count=2):
    return [str(uuid.uuid4()) for _ in range(count)]

# Premium header
st.markdown(f"""
    <div class='premium-header'>
        <h1 class='header-title'>⚡ VetNet API Explorer</h1>
        <p class='header-subtitle'>Next-Generation API Testing Platform</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar with premium design
with st.sidebar:
    st.markdown(f"""
        <div class='glass-card' style='text-align: center;'>
            <div class='icon-container' style='margin: 0 auto 1rem auto;'>
                🎯
            </div>
            <h2 style='margin: 0; font-size: 1.5rem;'>Control Center</h2>
            <p style='margin: 0.5rem 0 0 0; color: {COLORS["text_muted"]};'>Configure your API operations</p>
        </div>
    """, unsafe_allow_html=True)
    
    api_category = st.selectbox("🔍 Select API Category", list(ENDPOINTS.keys()))
    operation = st.selectbox("⚙️ Select Operation", ["GET", "POST", "PUT", "DELETE", "GET_MANY", "DELETE_MANY"])
    
    st.markdown(f"""
        <div class='glass-card'>
            <div class='section-header'>
                <div class='icon-container'>🔧</div>
                <div>
                    <h3 style='margin: 0;'>Configuration</h3>
                    <p style='margin: 0; color: {COLORS["text_muted"]}; font-size: 0.9rem;'>API Settings</p>
                </div>
            </div>
    """, unsafe_allow_html=True)
    
    api_url_input = st.text_input("🌐 API Base URL", value=API_BASE_URL, placeholder="https://your-api-url.com")
    token_input = st.text_input("🔐 Static Token", value=STATIC_TOKEN, type="password")
    
    if st.button("🔄 Update Configuration", key="config_update", use_container_width=True):
        API_BASE_URL = api_url_input
        STATIC_TOKEN = token_input
        HEADERS["static-token"] = STATIC_TOKEN
        st.markdown(f"<div class='status-success'>✅ Configuration updated successfully!</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='glass-card'>
            <div class='section-header'>
                <div class='icon-container'>📚</div>
                <div>
                    <h3 style='margin: 0;'>Quick Guide</h3>
                    <p style='margin: 0; color: {COLORS["text_muted"]}; font-size: 0.9rem;'>How to use</p>
                </div>
            </div>
            <div style='color: {COLORS["text"]}; line-height: 1.8;'>
                <div style='margin-bottom: 1rem;'>
                    <span style='color: {COLORS["primary"]}; font-weight: 600;'>1.</span> Select category & operation
                </div>
                <div style='margin-bottom: 1rem;'>
                    <span style='color: {COLORS["primary"]}; font-weight: 600;'>2.</span> Review pre-filled sample data
                </div>
                <div style='margin-bottom: 1rem;'>
                    <span style='color: {COLORS["primary"]}; font-weight: 600;'>3.</span> Execute API call
                </div>
                <div style='margin-bottom: 1rem;'>
                    <span style='color: {COLORS["primary"]}; font-weight: 600;'>4.</span> Analyze response data
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='glass-card' style='text-align: center; background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]});'>
            <div style='color: white; font-weight: 600; font-size: 1.1rem;'>
                VetNet API Explorer
            </div>
            <div style='color: rgba(255, 255, 255, 0.8); font-size: 0.9rem; margin-top: 0.5rem;'>
                Version 2.0 Premium
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main content area
st.markdown(f"""
    <div class='glass-card'>
        <div class='section-header'>
            <div class='icon-container'>{ENDPOINTS[api_category].get('icon', '📊')}</div>
            <div>
                <h2 style='margin: 0; font-size: 2rem;'>{api_category} API</h2>
                <p style='margin: 0; color: {COLORS["text_muted"]}; font-size: 1.1rem;'>{operation} Operation</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Input fields based on operation
params = None
if operation in ["PUT", "DELETE"]:
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='section-header'>
                <div class='icon-container'>🆔</div>
                <div>
                    <h3 style='margin: 0;'>Item Identifier</h3>
                    <p style='margin: 0; color: {COLORS["text_muted"]}; font-size: 0.9rem;'>Specify the item ID for the operation</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Generate sample ID with enhanced explanation
        sample_id = str(uuid.uuid4())
        st.markdown(f"""
            <div style='background: {COLORS["glass"]}; 
                        backdrop-filter: blur(10px); 
                        border: 1px solid {COLORS["border"]}; 
                        border-radius: 12px; 
                        padding: 1rem; 
                        margin: 1rem 0;
                        color: {COLORS["text"]};'>
                <div style='display: flex; align-items: center; margin-bottom: 0.5rem;'>
                    <span style='font-size: 1.2rem; margin-right: 0.5rem;'>💡</span>
                    <span style='font-weight: 600;'>Sample UUID Format</span>
                </div>
                <code style='background: rgba(99, 102, 241, 0.1); 
                           color: {COLORS["primary"]}; 
                           padding: 0.5rem; 
                           border-radius: 6px; 
                           font-family: monospace;'>{sample_id}</code>
            </div>
        """, unsafe_allow_html=True)
        
        item_id = st.text_input("🔑 Enter Item ID", value=sample_id, placeholder=f"e.g., {sample_id}")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    item_id = None

# Pagination parameters for GET requests
if operation == "GET" and not item_id:
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='section-header'>
                <div class='icon-container'>📊</div>
                <div>
                    <h3 style='margin: 0;'>Pagination Settings</h3>
                    <p style='margin: 0; color: {COLORS["text_muted"]}; font-size: 0.9rem;'>Control data retrieval parameters</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            page = st.number_input("📄 Page Number", min_value=1, value=1, help="Page number (defaults to 1)")
        with col2:
            limit = st.number_input("📝 Items per Page", min_value=1, value=10, help="Number of items per page (defaults to 10)")
        
        params = {"page": page, "limit": limit}
        
        # Display pagination info
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, {COLORS["accent"]}, {COLORS["primary"]}); 
                        color: white; 
                        padding: 1rem; 
                        border-radius: 12px; 
                        margin: 1rem 0;
                        text-align: center;'>
                <span style='font-weight: 600;'>📊 Retrieving page {page} with {limit} items per page</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# Handle different request types
if operation in ["POST", "PUT"]:
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='section-header'>
                <div class='icon-container'>📝</div>
                <div>
                    <h3 style='margin: 0;'>Request Payload</h3>
                    <p style='margin: 0; color: {COLORS["text_muted"]}; font-size: 0.9rem;'>Configure the data to be sent</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        data = {}
        fields = ENDPOINTS[api_category]["fields"]
        defaults = DEFAULT_VALUES.get(api_category, {})
        
        for field_name, field_info in fields.items():
            default_value = defaults.get(field_name, "")
            
            if field_info["type"] == "text":
                value = st.text_input(
                    f"✨ {field_name.replace('_', ' ').title()}", 
                    value=default_value,
                    placeholder=field_info["placeholder"],
                    key=f"{operation}_{api_category}_{field_name}"
                )
                if value or not field_info["required"]:
                    data[field_name] = value
                elif field_info["required"] and not value:
                    st.markdown(f"""
                        <div class='status-warning'>
                            ⚠️ {field_name.replace('_', ' ').title()} is required for {operation} operation
                        </div>
                    """, unsafe_allow_html=True)
        
        # Enhanced JSON display
        st.markdown(f"""
            <div style='margin: 1.5rem 0;'>
                <h4 style='color: {COLORS["text"]}; margin-bottom: 1rem;'>📋 Payload Preview</h4>
            </div>
        """, unsafe_allow_html=True)
        st.json(data)
        st.markdown("</div>", unsafe_allow_html=True)

elif operation in ["GET_MANY", "DELETE_MANY"]:
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"""
            <div class='section-header'>
                <div class='icon-container'>🔢</div>
                <div>
                    <h3 style='margin: 0;'>Bulk Operation</h3>
                    <p style='margin: 0; color: {COLORS["text_muted"]}; font-size: 0.9rem;'>Specify multiple IDs for batch processing</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        sample_ids = generate_sample_ids()
        default_ids = ", ".join(sample_ids)
        
        # Enhanced bulk operation UI
        st.markdown(f"""
            <div style='background: {COLORS["glass"]}; 
                        backdrop-filter: blur(10px); 
                        border: 1px solid {COLORS["border"]}; 
                        border-radius: 12px; 
                        padding: 1rem; 
                        margin: 1rem 0;
                        color: {COLORS["text"]};'>
                <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                    <span style='font-size: 1.2rem; margin-right: 0.5rem;'>💡</span>
                    <span style='font-weight: 600;'>Sample IDs Generated</span>
                </div>
                <div style='font-family: monospace; 
                           background: rgba(99, 102, 241, 0.1); 
                           padding: 0.8rem; 
                           border-radius: 8px; 
                           font-size: 0.9rem;
                           color: {COLORS["primary"]};'>
                    {sample_ids[0]}<br>
                    {sample_ids[1]}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        ids_input = st.text_area(
            "📋 Enter comma-separated IDs", 
            value=default_ids,
            placeholder="e.g., id1, id2, id3",
            key=f"{operation}_ids",
            height=120
        )
        
        if ids_input:
            data = {"ids": [id.strip() for id in ids_input.split(",") if id.strip()]}
        else:
            data = {"ids": []}
        
        # Display processed IDs count
        st.markdown(f"""
            <div style='background: linear-gradient(135deg, {COLORS["success"]}, #059669); 
                        color: white; 
                        padding: 1rem; 
                        border-radius: 12px; 
                        margin: 1rem 0;
                        text-align: center;'>
                <span style='font-weight: 600;'>🎯 Processing {len(data["ids"])} items</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style='margin: 1.5rem 0;'>
                <h4 style='color: {COLORS["text"]}; margin-bottom: 1rem;'>📋 Request Preview</h4>
            </div>
        """, unsafe_allow_html=True)
        st.json(data)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    data = None

# Enhanced execution button
st.markdown("<br>", unsafe_allow_html=True)
execute_col, spacer_col = st.columns([1, 2])
with execute_col:
    if st.button("🚀 Execute API Call", use_container_width=True, help="Launch your API request with style"):
        # Enhanced request processing
        if operation in ["GET_MANY", "DELETE_MANY"]:
            endpoint = ENDPOINTS[api_category][operation]
            method = "POST"
        else:
            endpoint = ENDPOINTS[api_category][operation]
            method = operation
            if item_id and "{id}" in endpoint:
                endpoint = endpoint.replace("{id}", item_id)
        
        full_url = f"{API_BASE_URL}{endpoint}"
        
        # Display request details with premium styling
        with st.expander("📤 Request Details", expanded=True):
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style='background: linear-gradient(135deg, {COLORS["primary"]}, {COLORS["secondary"]}); 
                           color: white; 
                           padding: 1.5rem; 
                           border-radius: 12px; 
                           margin-bottom: 1rem;'>
                    <h4 style='margin: 0 0 1rem 0;'>🎯 Request Configuration</h4>
                    <div style='display: grid; gap: 0.8rem;'>
                        <div><strong>URL:</strong> <code style='background: rgba(255,255,255,0.2); padding: 0.2rem 0.5rem; border-radius: 4px;'>{full_url}</code></div>
                        <div><strong>Method:</strong> <span style='background: rgba(255,255,255,0.2); padding: 0.2rem 0.8rem; border-radius: 4px; font-weight: 600;'>{method}</span></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if params:
                st.markdown(f"""
                    <div style='margin-bottom: 1rem;'>
                        <h4 style='color: {COLORS["text"]}; margin-bottom: 0.5rem;'>🔍 Query Parameters</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.json(params)
                
            if data:
                st.markdown(f"""
                    <div style='margin-bottom: 1rem;'>
                        <h4 style='color: {COLORS["text"]}; margin-bottom: 0.5rem;'>📦 Request Payload</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.json(data)
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Make the API request
        result = make_request(method, full_url, data, params)
        
        # Display response with premium styling
        with st.expander("📥 Response Analysis", expanded=True):
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            
            if "error" in result:
                st.markdown(f"""
                    <div class='status-error'>
                        <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                            <span style='font-size: 2rem; margin-right: 1rem;'>❌</span>
                            <div>
                                <h3 style='margin: 0;'>Request Failed</h3>
                                <p style='margin: 0; opacity: 0.9;'>{result['error']}</p>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                if "status_code" in result and result["status_code"]:
                    st.markdown(f"""
                        <div style='background: rgba(239, 68, 68, 0.1); 
                                   border: 1px solid rgba(239, 68, 68, 0.3); 
                                   border-radius: 12px; 
                                   padding: 1rem; 
                                   margin: 1rem 0;'>
                            <strong>Status Code:</strong> {result['status_code']}
                        </div>
                    """, unsafe_allow_html=True)
                
                if "text" in result and result["text"]:
                    st.markdown(f"""
                        <div style='margin: 1rem 0;'>
                            <h4 style='color: {COLORS["text"]};'>Response Details:</h4>
                        </div>
                    """, unsafe_allow_html=True)
                    try:
                        error_json = json.loads(result['text'])
                        st.json(error_json)
                    except json.JSONDecodeError:
                        st.code(result['text'], language="text")
            else:
                st.markdown(f"""
                    <div class='status-success'>
                        <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                            <span style='font-size: 2rem; margin-right: 1rem;'>✅</span>
                            <div>
                                <h3 style='margin: 0;'>Request Successful!</h3>
                                <p style='margin: 0; opacity: 0.9;'>Your API call completed successfully</p>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Special handling for deleteMany responses
                if operation == "DELETE_MANY":
                    if "data" in result and "count" in result["data"]:
                        st.markdown(f"""
                            <div class='metric-card'>
                                <div style='position: relative; z-index: 2;'>
                                    <div style='font-size: 2rem; margin-bottom: 0.5rem;'>🗑️</div>
                                    <div style='font-size: 2rem; font-weight: 700;'>{result['data']['count']}</div>
                                    <div style='opacity: 0.9;'>Items Deleted</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                
                # Display the response
                st.markdown(f"""
                    <div style='margin: 1.5rem 0;'>
                        <h4 style='color: {COLORS["text"]}; margin-bottom: 1rem;'>📄 Response Body</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.json(result)
                
                # Display data in enhanced table format
                if method == "GET":
                    if isinstance(result, dict) and "data" in result:
                        if isinstance(result["data"], list) and result["data"]:
                            df = pd.DataFrame(result["data"])
                            st.markdown(f"""
                                <div style='margin: 2rem 0 1rem 0;'>
                                    <h4 style='color: {COLORS["text"]}; margin-bottom: 1rem;'>📊 Data Visualization</h4>
                                </div>
                            """, unsafe_allow_html=True)
                            st.dataframe(df, use_container_width=True)
                            
                            # Enhanced pagination info
                            total_pages = result.get('totalPages', 1)
                            current_page = result.get('page', 1)
                            total_count = result.get('totalCount', len(df))
                            
                            st.markdown(f"""
                                <div style='background: linear-gradient(135deg, {COLORS["accent"]}, {COLORS["primary"]}); 
                                           color: white; 
                                           padding: 1rem; 
                                           border-radius: 12px; 
                                           margin: 1rem 0;
                                           text-align: center;'>
                                    <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;'>
                                        <div>
                                            <div style='font-size: 1.5rem; font-weight: 700;'>{current_page}</div>
                                            <div style='opacity: 0.9; font-size: 0.9rem;'>Current Page</div>
                                        </div>
                                        <div>
                                            <div style='font-size: 1.5rem; font-weight: 700;'>{total_pages}</div>
                                            <div style='opacity: 0.9; font-size: 0.9rem;'>Total Pages</div>
                                        </div>
                                        <div>
                                            <div style='font-size: 1.5rem; font-weight: 700;'>{total_count}</div>
                                            <div style='opacity: 0.9; font-size: 0.9rem;'>Total Records</div>
                                        </div>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.json(result["data"])
                    elif isinstance(result, list) and result:
                        df = pd.DataFrame(result)
                        st.markdown(f"""
                            <div style='margin: 2rem 0 1rem 0;'>
                                <h4 style='color: {COLORS["text"]}; margin-bottom: 1rem;'>📊 Data Visualization</h4>
                            </div>
                        """, unsafe_allow_html=True)
                        st.dataframe(df, use_container_width=True)
                        
                        st.markdown(f"""
                            <div style='background: linear-gradient(135deg, {COLORS["success"]}, #059669); 
                                       color: white; 
                                       padding: 1rem; 
                                       border-radius: 12px; 
                                       margin: 1rem 0;
                                       text-align: center;'>
                                <div style='font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;'>{len(df)}</div>
                                <div style='opacity: 0.9;'>Total Records Retrieved</div>
                            </div>
                        """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

# Premium footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='premium-footer'>
        <div style='position: relative; z-index: 2;'>
            <div style='font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;'>
                ⚡ VetNet API Explorer
            </div>
            <div style='opacity: 0.9; font-size: 1rem;'>
                Premium Enterprise API Testing Solution
            </div>
            <div style='margin-top: 1rem; opacity: 0.8; font-size: 0.9rem;'>
                Powered by Advanced Technology Stack
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)