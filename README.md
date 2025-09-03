# Unstop Linkenite Email Challenge

This project processes customer email data to:
- Identify **issue types** such as Login Issues, Billing Errors, Downtime, and Integration Queries.
- Assign **priority levels**: High, Medium, or Low.

## Project Structure
unstop-Linkenite-email-challenge/
├── emails.csv # Input file provided in the challenge
├── solution.py # Python script for processing
├── processed_emails.csv # Output file with classified issues and priorities
├── README.md # Documentation
└── requirements.txt # Dependencies (pandas)
## How to Run

1. Clone the repository
git clone https://github.com/Venkatasaikishor/unstop-Linkenite-email-challenge.git
cd unstop-Linkenite-email-challenge
   
2.Install dependencies
pip install -r requirements.txt

3.Place the input file
Put your emails.csv file in this folder.

4.Run the script
python solution.py

5.Check the output
Open processed_emails.csv to see classified tickets with priority and issue type.

Example Output
sender	subject	body	Issue_Type	Priority
alice@example.com	Urgent request: system access	Unable to log in since yesterday	Login Issue	High
diana@client.co	Help required with account	Verification email never arrived	Integration Query	Medium

Requirements
Python 3.8+

pandas

Author
Pilli Venkata Sai Kishor

### `requirements.txt`
pandas

### `emails.csv`
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
