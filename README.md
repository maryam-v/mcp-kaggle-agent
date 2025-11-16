# MCP Kaggle Agent

An intelligent agent for searching Kaggle datasets and competitions powered by [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) and Gemini via [Google ADK](https://google.github.io/adk-docs/).

## 🚀 Overview

This project uses Google ADK to build a Gemini-powered agent that connects to Kaggle's MCP endpoint. The agent can search Kaggle datasets and competitions based on user queries and return structured results including:

- ✅ Dataset name  
- ✅ Full Kaggle URL  
- ✅ Short description  
- ✅ Community rating or votes

Example query:  
> "List 3 highly rated Kaggle datasets that contain OCR (Optical Character Recognition) data"

## 🧠 Technologies Used

- [Google ADK](https://google.github.io/adk-docs/)  
- [Gemini](https://deepmind.google/technologies/gemini/)  
- [Kaggle MCP](https://www.kaggle.com/docs/mcp)  
- Python 3.11  
- Kaggle Notebooks

## 📦 Setup Instructions

1. **Add your Google API key to Kaggle secrets**  
   - Go to **Kaggle → Account → Secrets**  
   - Add a new secret named `GOOGLE_API_KEY`

2. **Install dependencies**  
   If running locally:
   ```bash
   pip install google-adk

3. **Run the notebook or script**
   Use mcp-kaggle-agent.ipynb for interactive exploration.
   
   Use mcp-kaggle-agent.py for script-based execution.

## 📊 Example Output
```
[
  {
    "name": "standard OCR dataset ",
    "url": "https://www.kaggle.com/datasets/preatcher/standard-ocr-dataset",
    "description": "Optical Character Recognition Dataset containing Various Fonts and Style",
    "rating": 80
  },
  {
    "name": "Aida Calculus Math Handwriting Recognition Dataset",
    "url": "https://www.kaggle.com/datasets/aidapearson/ocr-data",
    "description": "Synthetic handwritten calculus math expressions for recognition and OCR tasks",
    "rating": 74
  },
  {
    "name": "OCR Receipts Text Detection - retail dataset",
    "url": "https://www.kaggle.com/datasets/trainingdatapro/ocr-receipts-text-detection",
    "description": "Photos of the receipts and text detection - ocr dataset",
    "rating": 70
  }
]
```
## 📁 Project Structure
```
mcp-kaggle-agent/
├── mcp-kaggle-agent.ipynb         # Kaggle notebook version
├── mcp-kaggle-agent.py            # Script version
├── requirements.txt               # Dependencies
├── .gitignore                     # Clean repo setup
└── README.md                      # Project overview
```

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

Pull requests are welcome! If you'd like to contribute, please open an issue first to discuss your ideas.
