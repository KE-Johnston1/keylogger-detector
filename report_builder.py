import os

def build_report():
    output_files = [
        "logs/output.log",
        "logs/startup_output.log",
        "logs/network_output.log",
        "logs/keystroke_output.log"
    ]

    report_path = "logs/final_report.log"

    with open(report_path, "w") as report:
        report.write("=== Keylogger Detection Toolkit Summary ===\n\n")
        for file in output_files:
            if os.path.exists(file):
                report.write(f"--- Results from {os.path.basename(file)} ---\n")
                with open(file, "r") as f:
                    report.write(f.read())
                report.write("\n")
            else:
                report.write(f"[!] Missing output file: {file}\n\n")

    print(f"[✓] Final report saved to {report_path}")

if __name__ == "__main__":
    build_report()
