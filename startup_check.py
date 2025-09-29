import os

def scan_startup():
    suspicious_keywords = ["keylogger", "logger", "stealth", "capture"]
    flagged = []

    log_path = "logs/startup.log"
    output_path = "logs/startup_output.log"

    if not os.path.exists(log_path):
        print(f"[!] Startup log not found: {log_path}")
        return

    with open(log_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            for keyword in suspicious_keywords:
                if keyword in line.lower():
                    flagged.append(line.strip())

    with open(output_path, "w") as out:
        if flagged:
            out.write("[!] Suspicious startup entries detected:\n")
            for entry in flagged:
                out.write(f"    {entry}\n")
            print(f"[✓] {len(flagged)} suspicious startup entries saved to {output_path}")
        else:
            out.write("[✓] No suspicious startup entries found\n")
            print(f"[✓] No suspicious startup entries found. Logged to {output_path}")

if __name__ == "__main__":
    scan_startup()
