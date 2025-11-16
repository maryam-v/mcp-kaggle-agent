# MCP Kaggle Agent

An intelligent agent for searching Kaggle datasets and competitions powered by [Model Context Protocol (MCP)](https://www.kaggle.com/mcp) and Gemini via Google ADK.

## 🚀 Overview

This project uses Google ADK to build a Gemini-powered agent that connects to Kaggle's MCP endpoint. The agent can search Kaggle datasets and competitions based on user queries and return structured results including:

- ✅ Dataset name  
- ✅ Full Kaggle URL  
- ✅ Short description  
- ✅ Community rating or votes

Example query:  
> "List 3 highly rated Kaggle datasets that contain OCR (Optical Character Recognition) data"

## 🧠 Technologies Used

- [Google ADK](https://github.com/google/adk)  
- [Gemini](https://deepmind.google/technologies/gemini/)  
- [Kaggle MCP](https://www.kaggle.com/mcp)  
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
   Use mcp_kaggle_competition.ipynb for interactive exploration
   Use mcp_kaggle_competition.py for script-based execution

## 📊 Example Output

[
  {
    "name": "Digit Recognizer (MNIST)",
    "url": "https://www.kaggle.com/c/digit-recognizer",
    "description": "Handwritten digit dataset widely used for OCR benchmarks.",
    "rating": "4.8/5"
  },
  {
    "name": "IAM Handwriting Dataset",
    "url": "https://www.kaggle.com/datasets/iam-handwriting",
    "description": "English handwritten text dataset for OCR beyond digits.",
    "rating": "4.7/5"
  },
  {
    "name": "CORD Document OCR",
    "url": "https://www.kaggle.com/datasets/cord-ocr",
    "description": "Receipt and document OCR dataset with annotations.",
    "rating": "4.6/5"
  }
]

## 📁 Project Structure

mcp-kaggle-agent/
├── mcp_kaggle_competition.ipynb   # Kaggle notebook version
├── mcp_kaggle_competition.py      # Script version
├── requirements.txt               # Dependencies
├── .gitignore                     # Clean repo setup
└── README.md                      # Project overview

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

Pull requests are welcome! If you'd like to contribute, please open an issue first to discuss your ideas.
