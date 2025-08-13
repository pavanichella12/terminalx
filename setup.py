#!/usr/bin/env python3
"""
Terminal X AI - Financial Research Assistant
Setup script for easy deployment
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

def create_secrets_file():
    """Create secrets file template"""
    secrets_dir = ".streamlit"
    secrets_file = os.path.join(secrets_dir, "secrets.toml")
    
    if not os.path.exists(secrets_dir):
        os.makedirs(secrets_dir)
    
    if not os.path.exists(secrets_file):
        with open(secrets_file, "w") as f:
            f.write("# Add your Gemini API key here\n")
            f.write("GEMINI_API_KEY = \"your-api-key-here\"\n")
        print("✅ Created .streamlit/secrets.toml template")
        print("📝 Please add your Gemini API key to .streamlit/secrets.toml")
    else:
        print("✅ .streamlit/secrets.toml already exists")

def main():
    """Main setup function"""
    print("🚀 Terminal X AI - Setup")
    print("=" * 40)
    
    check_python_version()
    install_requirements()
    create_secrets_file()
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Add your Gemini API key to .streamlit/secrets.toml")
    print("2. Run: streamlit run terminal_x_gemini.py")
    print("3. Open: http://localhost:8501")

if __name__ == "__main__":
    main() 