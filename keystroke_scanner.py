import os

def scan_keystrokes():
    suspicious_patterns = ["backspace", "clipboard", "stealth", "capture"]
    flagged = []

    log_path = "logs/keystrokes.log"
    output_path = "logs/keystroke_output.log"

    if not os.path.exists(log_path):
        print(f"[!] Keystroke log not found: {log_path}")
        return

    with open(log_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            for pattern in suspicious_patterns:
                if pattern in line.lower():
                    flagged.append(line.strip())

    with open(output_path, "w") as out:
        if flagged:
            out.write("[!] Suspicious keystroke patterns detected:\n")
            for entry in flagged:
                out.write(f"    {entry}\n")
            print(f"[✓] {len(flagged)} suspicious keystroke entries saved to {output_path}")
        else:
            out.write("[✓] No suspicious keystroke patterns found\n")
            print(f"[✓] No suspicious keystroke patterns found. Logged to {output_path}")

if __name__ == "__main__":
    scan_keystrokes()
