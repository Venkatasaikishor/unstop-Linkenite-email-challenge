import pandas as pd

# === Step 1: Load the dataset ===
input_file = "emails.csv"  # Replace with actual file name if different
df = pd.read_csv(input_file)

# === Step 2: Mark ticket priority ===
priority_keywords = ["urgent", "critical", "immediate"]

def detect_priority(subject):
    subject_lower = subject.lower()
    if any(word in subject_lower for word in priority_keywords):
        return "High"
    return "Normal"

df['priority'] = df['subject'].apply(detect_priority)

# === Step 3: Categorize tickets ===
def categorize_ticket(body):
    text = str(body).lower()
    if "login" in text or "password" in text:
        return "Login Issue"
    elif "billing" in text or "charged" in text:
        return "Billing Issue"
    elif "server" in text or "downtime" in text:
        return "Server Downtime"
    elif "integration" in text or "api" in text:
        return "Integration Query"
    else:
        return "General"

df['category'] = df['body'].apply(categorize_ticket)

# === Step 4: Sort by priority and sent_date ===
df['sent_date'] = pd.to_datetime(df['sent_date'], format="%d-%m-%Y %H:%M")
df = df.sort_values(by=['priority', 'sent_date'], ascending=[False, True])

# === Step 5: Save processed output ===
output_file = "processed_emails.csv"
df.to_csv(output_file, index=False)

# === Step 6: Summary (optional console output) ===
summary = df.groupby('category').size().reset_index(name='ticket_count')
print("\n=== Ticket Summary by Category ===")
print(summary)
print(f"\nProcessed file saved as: {output_file}")
