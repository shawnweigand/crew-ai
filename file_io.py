from datetime import datetime

def save_markdown(task_output):
    # Get today's date
    today_date = datetime.now().strftime("%Y-%m-%d")
    # Set the file name
    filename = f"{today_date}.md"
    # Write the task output to txt
    with open(filename, "w") as file:
        file.write(task_output.result)
    print(f"Travel plan saved as {filename}")