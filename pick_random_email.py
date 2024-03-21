import csv
import sys
import random

def main(csv_file_path):
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header row
            emails = [row[0] for row in reader]
        
        if emails:
            random_email = random.choice(emails)
            print(random_email)
        else:
            print("The CSV file is empty or does not contain emails after the header.")
    except FileNotFoundError:
        print(f"The file {csv_file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pick_random_email.py <path_to_csv_file>")
    else:
        csv_file_path = sys.argv[1]
        main(csv_file_path)
