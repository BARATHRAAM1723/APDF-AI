"""
SmartPDF: AI-Powered Research Paper Analyzer & Intelligent Assistant
Final-Year Computer Science Capstone Project
Modernized Streamlit Application Entrypoint
"""

import sys
from pathlib import Path

# Ensure root SmartPDF folder is on sys.path
APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

import streamlit as st

# Configure page metadata
st.set_page_config(
    page_title="SmartPDF – Academic Research Intelligence",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Advanced Modern UI Stylesheet
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Container constraints & padding */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3.5rem;
        max-width: 1320px;
    }

    /* Top Brand Navigation Card */
    .brand-container {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 0 18px 0;
        border-bottom: 1px solid rgba(226, 232, 240, 0.8);
        margin-bottom: 20px;
    }
    .brand-icon {
        width: 42px;
        height: 42px;
        background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 22px;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
    }
    .brand-title {
        font-size: 1.35rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: #0f172a;
        margin: 0;
        line-height: 1.1;
    }
    .brand-subtitle {
        font-size: 0.75rem;
        font-weight: 500;
        color: #64748b;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Navigation Radio Items Restyled as Menu Pills */
    div[data-testid="stSidebar"] div[role="radiogroup"] > label {
        background-color: transparent;
        padding: 9px 14px;
        border-radius: 8px;
        margin-bottom: 3px;
        transition: all 0.15s ease-in-out;
        font-weight: 500;
        font-size: 0.92rem;
        color: #334155;
        border: 1px solid transparent;
        cursor: pointer;
    }
    div[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
        background-color: #f1f5f9;
        color: #1e293b;
    }
    div[data-testid="stSidebar"] div[role="radiogroup"] > label[data-checked="true"] {
        background: #eef2ff !important;
        color: #4338ca !important;
        font-weight: 600;
        border-color: #c7d2fe !important;
    }

    /* Metric Cards Modern Styling */
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 16px 20px;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03), 0 4px 12px rgba(0,0,0,0.02);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        border-color: #cbd5e1;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.82rem !important;
        font-weight: 600 !important;
        color: #64748b !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.85rem !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        letter-spacing: -0.03em;
    }

    /* Primary and Secondary Buttons */
    button[kind="primary"] {
        background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 8px 20px !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        box-shadow: 0 2px 8px rgba(79, 70, 229, 0.28) !important;
        transition: all 0.2s ease !important;
    }
    button[kind="primary"]:hover {
        opacity: 0.94 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 14px rgba(79, 70, 229, 0.38) !important;
    }
    button[kind="secondary"] {
        border-radius: 8px !important;
        font-weight: 500 !important;
        border: 1px solid #cbd5e1 !important;
    }

    /* Sidebar Telemetry Pill Card */
    .telemetry-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 12px 14px;
        margin-top: 15px;
    }
    .telemetry-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-size: 0.78rem;
        font-weight: 700;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }
    .telemetry-badge {
        font-size: 0.72rem;
        padding: 2px 7px;
        border-radius: 12px;
        font-weight: 600;
    }
    .badge-optimal { background: #dcfce7; color: #15803d; }
    .badge-warning { background: #fef3c7; color: #b45309; }
    .badge-critical { background: #fee2e2; color: #b91c1c; }

    /* Custom Citation Cards */
    .citation-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #4f46e5;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .citation-title {
        font-size: 0.88rem;
        font-weight: 700;
        color: #1e293b;
        display: flex;
        justify-content: space-between;
    }
    .citation-snippet {
        font-size: 0.82rem;
        color: #475569;
        font-style: italic;
        margin-top: 4px;
    }

    /* Section Header Decorator */
    .section-header {
        font-size: 1.7rem;
        font-weight: 800;
        color: #0f172a;
        letter-spacing: -0.025em;
        margin-bottom: 4px;
    }
    .section-sub {
        font-size: 0.92rem;
        color: #64748b;
        margin-bottom: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

from database.db_manager import DatabaseManager
from modules.semantic_search import SemanticSearch
from modules.memory_manager import MemoryManager

# Import UI views
from frontend.dashboard import render_dashboard
from frontend.documents import render_upload_section, render_my_documents
from frontend.chat import render_chat_section
from frontend.summarizer_ui import render_summarizer
from frontend.comparison_ui import render_comparison_section
from frontend.gap_finder_ui import render_gap_finder
from frontend.settings import render_settings


# Cache database and search engine singletons in Streamlit session
@st.cache_resource
def get_database_manager():
    return DatabaseManager()


@st.cache_resource
def get_semantic_search():
    db = get_database_manager()
    return SemanticSearch(db_manager=db)


def main():
    db = get_database_manager()
    search_engine = get_semantic_search()

    # Sidebar Navigation
    with st.sidebar:
        st.markdown(
            """
            <div class="brand-container">
                <div class="brand-icon">📑</div>
                <div>
                    <h1 class="brand-title">SmartPDF</h1>
                    <p class="brand-subtitle">Research Assistant</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        menu_choice = st.radio(
            "Main Navigation",
            options=[
                "📊 Overview Dashboard",
                "📤 Ingest Papers",
                "📚 Paper Library",
                "🤖 Ask AI (Grounded Q&A)",
                "📝 Multi-Mode Summarizer",
                "⚖️ Comparative Matrix",
                "🔬 Research Gap Finder",
                "💬 Chat History",
                "⚙️ Settings & Telemetry",
            ],
            index=0,
            label_visibility="collapsed",
        )

        st.markdown("---")

        # Live Hardware Telemetry Widget (8 GB RAM Constraint)
        mem = MemoryManager.get_memory_snapshot()
        status_class = (
            "badge-critical"
            if mem["status"] == "CRITICAL"
            else ("badge-warning" if mem["status"] == "WARNING" else "badge-optimal")
        )

        st.markdown(
            f"""
            <div class="telemetry-card">
                <div class="telemetry-header">
                    <span>Host Memory</span>
                    <span class="telemetry-badge {status_class}">{mem['badge']}</span>
                </div>
                <div style="font-size: 1.15rem; font-weight: 800; color: #0f172a; margin-bottom: 2px;">
                    {mem['used_percent']}% <span style="font-size: 0.8rem; font-weight: 500; color: #64748b;">RAM used</span>
                </div>
                <div style="font-size: 0.78rem; color: #64748b; margin-bottom: 8px;">
                    {mem['available_ram_gb']} GB Free &bull; {mem['process_rss_mb']} MB Process RSS
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.progress(min(1.0, max(0.0, mem["used_percent"] / 100.0)))
        st.caption("Engine: **Intel Core i5 (CPU-Only)**")

    # Routing
    if menu_choice == "📊 Overview Dashboard":
        render_dashboard(db)
    elif menu_choice == "📤 Ingest Papers":
        render_upload_section(db, search_engine)
    elif menu_choice == "📚 Paper Library":
        render_my_documents(db)
    elif menu_choice == "🤖 Ask AI (Grounded Q&A)":
        render_chat_section(db, search_engine)
    elif menu_choice == "📝 Multi-Mode Summarizer":
        render_summarizer(db)
    elif menu_choice == "⚖️ Comparative Matrix":
        render_comparison_section(db)
    elif menu_choice == "🔬 Research Gap Finder":
        render_gap_finder(db)
    elif menu_choice == "💬 Chat History":
        st.markdown('<div class="section-header">💬 Chat Sessions & History</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Review prior research discussions or manage conversational sessions.</div>', unsafe_allow_html=True)

        sessions = db.get_all_sessions()
        if not sessions:
            st.info("No prior chat sessions found. Start a conversation in 'Ask AI' to record discussions.")
        else:
            for s in sessions:
                with st.expander(f"🗨️ {s['title']} ({s['message_count']} messages) — {s['created_at'].split()[0]}"):
                    st.write(f"Session UUID: `{s['session_uuid']}`")
                    col_open, col_del = st.columns([1, 1])
                    with col_open:
                        if st.button("Open in Ask AI", key=f"open_{s['session_uuid']}"):
                            st.session_state.current_session_uuid = s["session_uuid"]
                            st.success("Session activated! Navigate to 'Ask AI' in sidebar to view.")
                    with col_del:
                        if st.button("Delete Session", key=f"del_sess_{s['session_uuid']}", type="secondary"):
                            db.delete_session(s["session_uuid"])
                            st.rerun()
    elif menu_choice == "⚙️ Settings & Telemetry":
        render_settings(db)


if __name__ == "__main__":
    main()
