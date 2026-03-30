Scenario: Automated Log Monitoring & Alert System

Problem Statement

Production servers generate huge logs. Critical errors may go unnoticed, causing downtime.

🌍 Real-world Use Case

In companies, logs are monitored automatically. If keywords like ERROR, CRITICAL, FAILED appear → alert DevOps team.

🧠 Approach / Solution Strategy
Read log file continuously
Search for error patterns
Trigger alert (console/email)
Maintain state (avoid duplicate alerts)
⚙️ Method / Steps
Open and read log file
Scan for keywords
Store already processed lines
Alert on new errors
💻 Python Script


import time

LOG_FILE = "app.log"
KEYWORDS = ["ERROR", "CRITICAL", "FAILED"]

def monitor_logs():
    print("🚀 Monitoring started...")

    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)  # Move to end of file

        while True:
            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            for keyword in KEYWORDS:
                if keyword in line:
                    print(f"⚠️ ALERT: {line.strip()}")

if __name__ == "__main__":
    monitor_logs()





Explanation
file.seek(0,2) → starts reading new logs only
readline() → reads live updates
KEYWORDS → defines failure patterns
Loop runs continuously → real-time monitoring
🧪 Sample Output
🚀 Monitoring started...
⚠️ ALERT: ERROR Database connection failed
⚠️ ALERT: CRITICAL Service down
