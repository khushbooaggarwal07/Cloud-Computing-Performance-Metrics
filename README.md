# Cloud-Computing-Performance-Metrics
Dashboard for analyzing cloud computing performance metrics such as CPU usage, memory utilization, power consumption, and virtual machine behavior using real-world data.

The dataset used in this project is too large to be hosted on GitHub. You can download it from the link below.

**Step-by-Step Setup Instructions (for Cloud Computing Performance Metrics Dashboard)-**

**1\. Install Python**

*   Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)
*   Important: During installation, check the box that says "Add Python to PATH".
*   To verify installation, open Command Prompt and run: python --version

**2\. Install VS Code**

*   Download from: [https://code.visualstudio.com/](https://code.visualstudio.com/)

**3\. Create a Project Folder**

*   Make a new folder anywhere, e.g., C:\\Users\\YourName\\cloud\_dashboard\_project
*   Save your code file (e.g., [dashboard.py](http://dashboard.py)) and dataset (vmCloud\_data.csv) inside this folder.

**4\. Open Terminal / Command Prompt in the Project Folder**

*   Open Command Prompt and navigate using cd
*   cd C:\\Users\\YourName\\cloud\_dashboard\_project
*   Or open folder in VS Code and go to Terminal → New Terminal

**5\. Create a Virtual Environment**

python -m venv venv

**6\. Activate the Virtual Environment**

On Windows:

venv\\Scripts\\activate

You’ll see (venv) appear in the terminal prompt if it's activated.

**7\. Install Required Packages**

In the same terminal (with virtual environment activated), run:

pip install streamlit pandas openpyxl

**8\. Download the Dataset**

*   Go to: [https://www.kaggle.com/datasets/abdurraziq01/cloud-computing-performance-metrics](https://www.kaggle.com/datasets/abdurraziq01/cloud-computing-performance-metrics)
*   Download the CSV file.
*   Rename it to vmCloud\_data.csv (if needed) and place it inside your project folder.

**9\. Save the Python Code**

*   Create a new Python file (e.g., [dashboard.py](http://dashboard.py)) and copy-paste your Cloud Dashboard code into it.
*   Make sure this line in your code matches the actual file path:

df = pd.read\_csv(r"vmCloud\_data.csv")

**10\. Run the Dashboard**

*   Use this command in the terminal:

streamlit run [dashboard.py](http://dashboard.py)

Your browser will open with the dashboard.

