"""
SmartPDF Configuration Module
Centralized settings, path resolution, memory parameters, and hardware limits.
Optimized for: Intel Core i5 13th Gen, 8GB RAM, CPU-only inference, Windows 11.
"""

import os
from pathlib import Path

# Base Directory: root of the SmartPDF application
BASE_DIR = Path(__file__).resolve().parent

# Load environment variables from .env file if present
ENV_PATH = BASE_DIR / ".env"
try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=ENV_PATH)
except ImportError:
    # Graceful manual parsing if python-dotenv is not yet installed
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as _f:
            for _line in _f:
                _line = _line.strip()
                if _line and not _line.startswith("#") and "=" in _line:
                    _k, _v = _line.split("=", 1)
                    os.environ.setdefault(_k.strip(), _v.strip())

# ==============================================================================
# 1. DIRECTORY & STORAGE PATHS
# ==============================================================================
STORAGE_DIR = BASE_DIR / "storage"
UPLOAD_DIR = STORAGE_DIR / "uploads"
INDEX_DIR = STORAGE_DIR / "indexes"
CACHE_DIR = STORAGE_DIR / "cache"
DB_PATH = STORAGE_DIR / "smartpdf.db"

# Ensure runtime directories exist
for directory in [STORAGE_DIR, UPLOAD_DIR, INDEX_DIR, CACHE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# 2. DOCUMENT PROCESSING & CHUNKING DEFAULTS
# ==============================================================================
# Chunking constraints tailored for research papers
DEFAULT_CHUNK_SIZE = int(os.getenv("DEFAULT_CHUNK_SIZE", 500))  # in words/tokens
DEFAULT_CHUNK_OVERLAP = int(os.getenv("DEFAULT_CHUNK_OVERLAP", 75))  # in words/tokens
MIN_CHUNK_SIZE = 100
MAX_CHUNK_SIZE = 1500

# File upload constraints
MAX_UPLOAD_SIZE_MB = int(os.getenv("MAX_UPLOAD_SIZE_MB", 35))
ALLOWED_EXTENSIONS = {".pdf"}

# ==============================================================================
# 3. AI & EMBEDDING MODEL CONFIGURATION (CPU-ONLY)
# ==============================================================================
# 384-dimensional dense representations, fast CPU throughput, ~90MB memory footprint
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_DIM = 384
EMBEDDING_DEVICE = "cpu"
EMBEDDING_BATCH_SIZE = int(os.getenv("EMBEDDING_BATCH_SIZE", 16))
NORMALIZE_EMBEDDINGS = True

# ==============================================================================
# 4. VECTOR DATABASE CONFIGURATION (FAISS CPU)
# ==============================================================================
# FAISS CPU uses Flat Index with Inner Product on L2-normalized vectors (Cosine Similarity)
FAISS_INDEX_FILE = INDEX_DIR / "faiss_index.bin"
FAISS_METADATA_FILE = INDEX_DIR / "faiss_metadata.pkl"
DEFAULT_TOP_K = int(os.getenv("DEFAULT_TOP_K", 5))
SIMILARITY_THRESHOLD = float(os.getenv("SIMILARITY_THRESHOLD", 0.25))

# ==============================================================================
# 5. RETRIEVAL-AUGMENTED GENERATION (RAG) & LLM
# ==============================================================================
# Supported providers: "gemini", "groq", "openai", "local", "extractive_only"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini").lower()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

# Local quantized LLM parameters (default: disabled to conserve 8 GB RAM)
ENABLE_LOCAL_LLM = os.getenv("ENABLE_LOCAL_LLM", "false").lower() == "true"
LOCAL_LLM_MODEL_PATH = os.getenv("LOCAL_LLM_MODEL_PATH", "")

# LLM Generation constraints
MAX_GENERATION_TOKENS = 800
TEMPERATURE = 0.2  # Low temperature for factual, grounded academic responses
REQUEST_TIMEOUT_SECONDS = 30

# ==============================================================================
# 6. OCR CONFIGURATION
# ==============================================================================
TESSERACT_CMD = os.getenv("TESSERACT_CMD", r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# ==============================================================================
# 7. MEMORY & HARDWARE CONSTRAINTS (8 GB RAM / CPU-ONLY)
# ==============================================================================
MEMORY_WARNING_THRESHOLD_PERCENT = float(os.getenv("MEMORY_WARNING_THRESHOLD_PERCENT", 82.0))
MEMORY_CRITICAL_THRESHOLD_PERCENT = float(os.getenv("MEMORY_CRITICAL_THRESHOLD_PERCENT", 90.0))
PROCESS_MEMORY_LIMIT_MB = 1500  # Target process memory limit for SmartPDF
AUTO_GC_THRESHOLD_MB = 600       # Trigger Python gc.collect() when process delta exceeds this

# ==============================================================================
# 8. APPLICATION METADATA
# ==============================================================================
APP_NAME = "SmartPDF"
APP_SUBTITLE = "AI-Powered Research Paper Analyzer & Intelligent Assistant"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Computer Science Capstone Project"
