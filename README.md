
# Insurance Policy Analysis System

A modern, AI-powered web application designed for processing and analyzing insurance policy documents. This system uses advanced LLM technology and structured extraction to provide intelligent query responses with zero-token processing for common questions.

## 🚀 Features

### Core Capabilities

- **Insurance Policy Processing**: Specialized for insurance documents with automatic section identification
- **Zero-Token Query Processing**: Answer common questions instantly without using API tokens
- **Multi-Format Document Support**: Process PDF, DOCX, and TXT files
- **Intelligent Query Processing**: Ask natural language questions about your policies
- **Vector Database Search**: FAISS-powered semantic search for relevant content
- **Structured Data Extraction**: Automatically extract key policy information
- **Query History**: Track and review previous questions and answers
- **Specialized Query Types**: Get targeted responses based on policy aspects

### Document Types Supported

- **Insurance Policies**: Coverage analysis, exclusions, claims processes, premium information, policy duration, terms & conditions, and definitions

### Query Types

- **General Query**: For general questions about the policy
- **Coverage Details**: Focuses on what is covered under the insurance policy
- **Exclusions**: Identifies what is not covered
- **Claims Process**: Provides step-by-step guidance on filing claims
- **Premium Information**: Details about premium payments and fees
- **Policy Duration**: Explains policy terms and renewal conditions
- **Terms & Conditions**: Clarifies contractual obligations
- **Policy Definitions**: Provides definitions for insurance-specific terms

## ⚡ Zero-Token Query Processing

Structured extraction answers many queries instantly, including:

- Policy duration (e.g., "What is the policy duration?")
- Coverage details (e.g., "What is covered?")
- Exclusions (e.g., "What are the exclusions?")
- Claims process (e.g., "How do I file a claim?")
- Premium info (e.g., "How much is the premium?")
- Terms & conditions (e.g., "What are the terms?")
- Definitions (e.g., "What does 'deductible' mean?")

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI/ML**: Groq API (LLaMA 3 70B), Sentence Transformers
- **Vector Database**: FAISS
- **Document Processing**: PyMuPDF, python-docx
- **Deployment**: Gunicorn, Heroku/Railway ready

## 📋 Prerequisites

- Python 3.8+
- pip
- Groq API Key
- Team Bearer Token

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/insurance-policy-analysis.git
cd insurance-policy-analysis
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
FLASK_SECRET_KEY=your_secret_key_here
TEAM_BEARER_TOKEN=your_team_bearer_token_here
```

Run the app:

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

## 📖 Usage Guide

1. **Upload Insurance Policy**:
   - Upload or drag PDF, DOCX, TXT (≤16MB)
2. **View Analysis**:
   - See extracted info: coverage, exclusions, etc.
3. **Ask Questions**:
   - Type in natural language
   - Choose query type
   - Click "Get Answer"
4. **Review Results**:
   - Zero-token or AI-generated answer
   - Token usage info shown
   - Query history available

## 🔧 Configuration

- Update `app.py`, `document_analyzer.py`, and `groq_api.py` as needed
- Customize UI in `templates/index.html`

## 🚀 Deployment

### Heroku

Create `Procfile`:

```bash
web: gunicorn app:app
```

Deploy:

```bash
heroku create your-app-name
git push heroku main
heroku config:set GROQ_API_KEY=your_groq_api_key
heroku config:set FLASK_SECRET_KEY=your_secret_key
heroku config:set TEAM_BEARER_TOKEN=your_team_bearer_token
```

### Railway

- Connect GitHub repo
- Set ENV variables:
  - `GROQ_API_KEY`
  - `FLASK_SECRET_KEY`
  - `TEAM_BEARER_TOKEN`

### Docker (Optional)

## 📁 Project Structure

```
insurance-policy-analysis/
├── app.py
├── document_analyzer.py
├── groq_api.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── uploads/
│   └── vector_db/
└── .env
```

## 🔍 API Endpoints

- `POST /upload`: Upload document
- `GET /download/<filename>`: Download document
- `POST /query`: Process query
- `POST /analyze`: Analyze content
- `GET /`: Main UI
- `GET /health`: Health check
- `POST /hackrx/run`: Hackathon special endpoint

## 🧪 Testing

Upload sample documents and test queries like:

- "What is the policy duration?"
- "What is covered under this policy?"
- "What are the exclusions?"
- "How do I file a claim?"
- "How much is the premium?"

## 🤝 Contributing

```bash
git checkout -b feature/amazing-feature
git commit -m 'Add amazing feature'
git push origin feature/amazing-feature
```

## 📝 License

MIT License – see `LICENSE` file

## 🙏 Acknowledgments

- Groq
- Flask
- FAISS
- Sentence Transformers
- PyMuPDF

## 📞 Support

- GitHub Issues
- Email: kuppamajith@gmail.com, mohammedsameer2818@gmail.com
- Docs: [GitHub Repo]https://github.com/MagicalCoder-12/Hackaton,(https://github.com/mohammedsameer12345/hackathan)
