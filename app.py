import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os
import json
import uuid
import time

# Set page config
st.set_page_config(
    page_title="VetNet API Explorer",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load environment variables
load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL", "https://vetnet-microservice-gc3gdbpyhq-uc.a.run.app")
STATIC_TOKEN = os.getenv("STATIC_TOKEN", "Z4hi2ybPfPBKoLpiD1oEarcA7r5Et09pr98mt5oGQhYmUdWUzGPGvwFmz4hGGkmd")

# Simple and attractive color palette
COLORS = {
    "primary": "#4F46E5",    # Indigo
    "secondary": "#10B981",  # Emerald
    "background": "#F3F4F6",  # Light gray
    "surface": "#FFFFFF",    # White
    "text": "#1F2937",       # Dark gray
    "text_muted": "#6B7280", # Muted gray
    "border": "#E5E7EB",     # Light border
}

# Clean and modern styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        .main {
            background-color: #F3F4F6;
            min-height: 100vh;
            padding: 1rem;
        }
        
        .card {
            background: #FFFFFF;
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease;
        }
        
        .card:hover {
            transform: translateY(-2px);
        }
        
        .header {
            text-align: center;
            padding: 2rem;
            margin-bottom: 1rem;
        }
        
        .header-title {
            font-size: 2.5rem;
            font-weight: 700;
            color: #1F2937;
            margin-bottom: 0.5rem;
        }
        
        .header-subtitle {
            font-size: 1rem;
            color: #6B7280;
        }
        
        .stButton > button {
            background-color: #4F46E5;
            color: white;
            border-radius: 8px;
            padding: 0.75rem 1.5rem;
            font-weight: 500;
            border: none;
            transition: background-color 0.2s ease;
        }
        
        .stButton > button:hover {
            background-color: #4338CA;
        }
        
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div,
        .stNumberInput > div > div > input {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
            padding: 0.75rem;
            color: #1F2937;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #4F46E5;
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
        }
        
        [data-testid="stSidebar"] {
            background-color: #FFFFFF;
            border-right: 1px solid #E5E7EB;
            padding: 1rem;
        }
        
        .status-success {
            background-color: #10B981;
            color: white;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        .status-error {
            background-color: #EF4444;
            color: white;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        
        .metric-card {
            background: #4F46E5;
            color: white;
            border-radius: 8px;
            padding: 1rem;
            text-align: center;
            margin: 1rem 0;
        }
        
        .stTabs [role="tablist"] {
            background: #FFFFFF;
            border-radius: 8px;
            padding: 0.5rem;
            margin-bottom: 1rem;
        }
        
        .stTabs [aria-selected="true"] {
            background: #4F46E5;
            color: white;
            border-radius: 8px;
        }
        
        .stDataFrame {
            border-radius: 8px;
            border: 1px solid #E5E7EB;
        }
        
        .footer {
            text-align: center;
            padding: 2rem;
            margin-top: 2rem;
            color: #6B7280;
        }
    </style>
""", unsafe_allow_html=True)

# Default values
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

# Function to make API requests
def make_request(method, url, data=None, params=None):
    try:
        with st.spinner("Processing request..."):
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
            
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "status_code": e.response.status_code if e.response else None, "text": e.response.text if e.response else ""}
    finally:
        time.sleep(0.5)

# Generate sample UUIDs
def generate_sample_ids(count=2):
    return [str(uuid.uuid4()) for _ in range(count)]

# Header
st.markdown("""
    <div class='header'>
        <h1 class='header-title'>VetNet API Explorer</h1>
        <p class='header-subtitle'>Simple & Powerful API Testing</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    api_category = st.selectbox("Select Category", list(ENDPOINTS.keys()))
    operation = st.selectbox("Select Operation", ["GET", "POST", "PUT", "DELETE", "GET_MANY", "DELETE_MANY"])
    
    st.markdown("<h3>Configuration</h3>", unsafe_allow_html=True)
    api_url_input = st.text_input("API Base URL", value=API_BASE_URL)
    token_input = st.text_input("Static Token", value=STATIC_TOKEN, type="password")
    
    if st.button("Update Config", key="config_update"):
        API_BASE_URL = api_url_input
        STATIC_TOKEN = token_input
        HEADERS["static-token"] = STATIC_TOKEN
        st.markdown("<div class='status-success'>Configuration updated!</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Main content
st.markdown(f"<div class='card'><h2>{ENDPOINTS[api_category]['icon']} {api_category} API - {operation}</h2></div>", unsafe_allow_html=True)

# Input fields
params = None
if operation in ["PUT", "DELETE"]:
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3>Item ID</h3>", unsafe_allow_html=True)
        sample_id = str(uuid.uuid4())
        item_id = st.text_input("Enter Item ID", value=sample_id, placeholder=f"e.g., {sample_id}")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    item_id = None

# Pagination for GET
if operation == "GET" and not item_id:
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3>Pagination</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            page = st.number_input("Page Number", min_value=1, value=1)
        with col2:
            limit = st.number_input("Items per Page", min_value=1, value=10)
        params = {"page": page, "limit": limit}
        st.markdown("</div>", unsafe_allow_html=True)

# POST/PUT inputs
if operation in ["POST", "PUT"]:
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3>Request Data</h3>", unsafe_allow_html=True)
        data = {}
        fields = ENDPOINTS[api_category]["fields"]
        defaults = DEFAULT_VALUES.get(api_category, {})
        
        for field_name, field_info in fields.items():
            default_value = defaults.get(field_name, "")
            value = st.text_input(
                field_name.replace('_', ' ').title(),
                value=default_value,
                placeholder=field_info["placeholder"]
            )
            if value or not field_info["required"]:
                data[field_name] = value
            elif field_info["required"] and not value:
                st.markdown(f"<div class='status-error'>{field_name.replace('_', ' ').title()} is required</div>", unsafe_allow_html=True)
        
        st.markdown("<h4>Payload Preview</h4>", unsafe_allow_html=True)
        st.json(data)
        st.markdown("</div>", unsafe_allow_html=True)

# GET_MANY/DELETE_MANY inputs
elif operation in ["GET_MANY", "DELETE_MANY"]:
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h3>Bulk Operation</h3>", unsafe_allow_html=True)
        sample_ids = generate_sample_ids()
        default_ids = ", ".join(sample_ids)
        ids_input = st.text_area("Enter comma-separated IDs", value=default_ids, placeholder="e.g., id1, id2, id3")
        
        if ids_input:
            data = {"ids": [id.strip() for id in ids_input.split(",") if id.strip()]}
        else:
            data = {"ids": []}
        
        st.markdown("<h4>Request Preview</h4>", unsafe_allow_html=True)
        st.json(data)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    data = None

# Execute button
if st.button("Execute API Call"):
    if operation in ["GET_MANY", "DELETE_MANY"]:
        endpoint = ENDPOINTS[api_category][operation]
        method = "POST"
    else:
        endpoint = ENDPOINTS[api_category][operation]
        method = operation
        if item_id and "{id}" in endpoint:
            endpoint = endpoint.replace("{id}", item_id)
    
    full_url = f"{API_BASE_URL}{endpoint}"
    
    with st.expander("Request Details", expanded=True):
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"<h4>Request: {method} {full_url}</h4>", unsafe_allow_html=True)
        if params:
            st.markdown("<h4>Query Parameters</h4>", unsafe_allow_html=True)
            st.json(params)
        if data:
            st.markdown("<h4>Request Payload</h4>", unsafe_allow_html=True)
            st.json(data)
        st.markdown("</div>", unsafe_allow_html=True)
    
    result = make_request(method, full_url, data, params)
    
    with st.expander("Response", expanded=True):
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if "error" in result:
            st.markdown(f"<div class='status-error'>Error: {result['error']}</div>", unsafe_allow_html=True)
            if "status_code" in result and result["status_code"]:
                st.markdown(f"<p>Status Code: {result['status_code']}</p>", unsafe_allow_html=True)
            if "text" in result and result["text"]:
                try:
                    error_json = json.loads(result['text'])
                    st.json(error_json)
                except json.JSONDecodeError:
                    st.code(result['text'], language="text")
        else:
            st.markdown("<div class='status-success'>Request Successful!</div>", unsafe_allow_html=True)
            if operation == "DELETE_MANY" and "data" in result and "count" in result["data"]:
                st.markdown(f"<div class='metric-card'>Deleted {result['data']['count']} items</div>", unsafe_allow_html=True)
            
            st.markdown("<h4>Response Data</h4>", unsafe_allow_html=True)
            st.json(result)
            
            if method == "GET" and isinstance(result, dict) and "data" in result and isinstance(result["data"], list) and result["data"]:
                df = pd.DataFrame(result["data"])
                st.markdown("<h4>Data Table</h4>", unsafe_allow_html=True)
                st.dataframe(df, use_container_width=True)
                
                total_pages = result.get('totalPages', 1)
                current_page = result.get('page', 1)
                total_count = result.get('totalCount', len(df))
                
                st.markdown(f"""
                    <div class='metric-card'>
                        Page: {current_page}/{total_pages} | Total Records: {total_count}
                    </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        VetNet API Explorer - Simple, Fast, Reliable
    </div>
""", unsafe_allow_html=True)