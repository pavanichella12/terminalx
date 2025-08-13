# 🚀 Terminal X AI - Financial Research Assistant

**Advanced AI-powered financial document analysis using Google Gemini**

## 🌟 Live Demo
**[Deploy to Streamlit Cloud](https://share.streamlit.io/)**

## 📋 Quick Start

### Local Development
```bash
# Clone and setup
git clone <your-repo>
cd finance
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set up API key
# Add your Gemini API key to .streamlit/secrets.toml
GEMINI_API_KEY = "your-api-key-here"

# Run locally
streamlit run terminal_x_gemini.py
```

### Deploy to Streamlit Cloud
1. **Push to GitHub**: Upload your code to a GitHub repository
2. **Connect to Streamlit Cloud**: 
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and main file: `terminal_x_gemini.py`
3. **Add Secrets**: In Streamlit Cloud dashboard, add your Gemini API key
4. **Deploy**: Click "Deploy" - your app will be live in minutes!

## 🎯 Features

### **Multi-Prompt AI Pipeline**
- 📊 **Document Classification** - Identifies document types
- 💰 **Financial Metrics Extraction** - Extracts key financial data
- ⚠️ **Risk Analysis** - Identifies and categorizes risks
- 🎯 **Investment Thesis Generation** - Creates investment recommendations
- ✅ **Quality Check** - Validates analysis accuracy
- 📋 **Executive Summary** - Generates professional summaries

### **Production-Ready Features**
- ✅ **Real AI Integration** - Live Gemini 2.5 Pro API calls
- ✅ **Robust Error Handling** - Multiple parsing strategies
- ✅ **Format Flexibility** - Handles any input/output format
- ✅ **Professional UI** - Clean, enterprise-ready interface
- ✅ **Download Results** - Export analysis as JSON

## 🏗️ Architecture

### **7-Prompt System**
```
Document Input → Classifier → Metrics → Risks → Thesis → Quality → Summary
```

### **Technology Stack**
- **AI/LLM**: Google Gemini 2.5 Pro
- **Framework**: Streamlit
- **Language**: Python 3.9+
- **Deployment**: Streamlit Cloud

## 📊 Sample Data

The app includes sample financial documents:
- 📄 **Investment Memo** - Apple Inc. analysis
- 📈 **Quarterly Report** - Earnings analysis
- 💰 **Financial Model** - Valuation projections

## 🔧 Configuration

### **API Setup**
1. Get Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add to `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-api-key-here"
```

### **Environment Variables**
- `GEMINI_API_KEY`: Your Google Gemini API key

## 🚀 Deployment Options

### **Streamlit Cloud (Recommended)**
- ✅ **Free hosting**
- ✅ **Easy deployment**
- ✅ **Automatic scaling**
- ✅ **Perfect for demos**

### **Heroku**
- ✅ **Professional hosting**
- ✅ **Custom domain support**
- ✅ **Advanced features**

### **AWS/GCP**
- ✅ **Enterprise deployment**
- ✅ **Full control**
- ✅ **High performance**

## 📈 Performance

### **Analysis Pipeline**
- **Processing Time**: ~10-30 seconds per document
- **AI Model**: Gemini 2.5 Pro (latest)
- **Accuracy**: High confidence with multiple validation steps
- **Reliability**: Robust error handling and fallbacks

### **Cost Analysis**
- **Free Tier**: $50/month Google AI credits
- **Per Analysis**: ~$0.02-0.05
- **Demo Cost**: ~$0.10-0.25 total

## 🎯 Use Cases

### **Investment Analysis**
- Analyze investment memos
- Extract financial metrics
- Generate investment theses
- Risk assessment

### **Financial Research**
- Document classification
- Data extraction
- Comparative analysis
- Executive summaries

### **Due Diligence**
- Comprehensive analysis
- Risk identification
- Valuation assessment
- Recommendation generation

## 🔒 Security

### **API Key Management**
- Secure storage in Streamlit secrets
- Environment variable protection
- No hardcoded credentials

### **Data Privacy**
- No data storage
- Real-time processing only
- Secure API communication

## 🛠️ Development

### **Project Structure**
```
finance/
├── terminal_x_gemini.py      # Main application
├── data_collector.py         # Data collection utilities
├── requirements.txt          # Dependencies
├── README.md                # Documentation
├── .streamlit/
│   ├── config.toml          # Streamlit configuration
│   └── secrets.toml         # API keys (local only)
└── data/
    ├── raw/                 # Sample documents
    └── processed/           # Processed data
```

### **Adding New Features**
1. **New Analysis Type**: Add new prompt to `_initialize_prompts()`
2. **New Model**: Update model selection in `__init__()`
3. **New UI**: Add components to `main()` function

## 📞 Support

### **Troubleshooting**
- **API Errors**: Check API key and billing setup
- **Deployment Issues**: Verify requirements.txt and dependencies
- **Performance**: Monitor API rate limits

### **Contact**
For questions or issues, please refer to the deployment platform documentation.

## 🎉 Success Stories

This Terminal X AI system demonstrates:
- ✅ **Real AI Integration** - Live API calls
- ✅ **Production Readiness** - Error handling and robustness
- ✅ **Domain Expertise** - Financial analysis workflows
- ✅ **Professional Quality** - Enterprise-ready interface

**Perfect for AI Prompt Engineer interviews and demonstrations!** 🚀 