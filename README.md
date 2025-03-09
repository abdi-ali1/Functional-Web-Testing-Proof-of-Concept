## README - Functional Web Testing with Selenium

### 📌 Overview
This project performs functional web testing using Selenium WebDriver and Python. It tests a search functionality by opening a browser, performing a search query, and verifying if results appear.

### 🚀 Features
- Automatically launches a browser (Chrome) with Selenium
- Automatically accepts cookies on Google
- Searches a given website (default: Google, but configurable)
- Checks if search results are displayed
- Uses `webdriver-manager` to automatically manage ChromeDriver
- Robust error handling and explicit waits

### 🛠 Installation

#### Clone the repository
```bash
git clone https://github.com/abdi-ali1/Functional-Web-Testing-Proof-of-Concept.git
cd functional-web-testing
```

#### Create a virtual environment (optional but recommended)
```bash
python -m venv venv
```

#### Activate the virtual environment
**For macOS/Linux:**
```bash
source venv/bin/activate
```
**For Windows:**
```bash
venv\Scripts\activate
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

### 📄 Configuration
The test uses a configuration file (`config.yaml`).

#### 🔹 Default structure of `config.yaml`:
```yaml
url: "https://www.google.com"
query: "OpenAI"
```

### ▶️ Usage
Run the test with:
```bash
python src/main.py
```

### 🛠 Code Structure
#### Main Files
```
📂 src/
 ├── main.py               # Application entry point, reads configuration, and executes the test
 ├── functional_tester.py   # Contains the test logic and Selenium interaction
```

### 🖥 Logs & Debugging
- If you encounter errors, check the console output for error messages.
- You can add `print()` statements in `functional_tester.py` for extra debugging.

### ✅ Future Enhancements
- Support for multiple browsers (Firefox, Edge)
- Parallel tests with multiple search queries
- UI reporting with Allure or Robot Framework
