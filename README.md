# Unstop Linkenite Email Challenge

This project is a solution for the **Unstop Linkenite Email Challenge**.  
It processes customer email data to:
- **Classify issue types** (e.g., Login Issue, Billing Issue, Downtime, Integration Query, General Query)
- **Assign priority levels** (High, Medium, Low) based on urgency keywords.


## 📂 Project Structure

unstop-Linkenite-email-challenge/
├── emails.csv # Input file provided in the challenge
├── solution.py # Python script for processing
├── processed_emails.csv # Output file with classified issues and priorities
├── README.md # Documentation
└── requirements.txt # Dependencies (pandas)

## 🚀 How to Run

### 1. Clone the repository

git clone https://github.com/Venkatasaikishor/unstop-Linkenite-email-challenge.git
cd unstop-Linkenite-email-challenge
   
2. Install dependencies
pip install -r requirements.txt

3. Place your input file

Put the provided emails.csv in the root folder of the repository.

4. Run the script
python solution.py

5. Check the output

The processed data with Issue_Type and Priority will be available in:
processed_emails.csv

📊 Example Output

| sender                                        | subject                       | body                             | Issue\_Type       | Priority |
| --------------------------------------------- | ----------------------------- | -------------------------------- | ----------------- | -------- |
| [alice@example.com](mailto:alice@example.com) | Urgent request: system access | Unable to log in since yesterday | Login Issue       | High     |
| [diana@client.co](mailto:diana@client.co)     | Help required with account    | Verification email never arrived | Integration Query | Medium   |


🛠 Requirements

Python 3.8+

pandas

👤 Author

Pilli Venkata Sai Kishor
`requirements.txt`

pandas :
`emails.csv`
- Use the dataset provided in the challenge.
- Ensure it’s placed in the same directory as `solution.py`.

### Steps to Push to GitHub
cd unstop-Linkenite-email-challenge
git init
git branch -M main
git remote add origin https://github.com/<your-username>/unstop-Linkenite-email-challenge.git
git add .
git commit -m "Initial commit for Unstop Linkenite Email Challenge"
git push -u origin main
