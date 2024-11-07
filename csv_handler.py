import csv
from pathlib import Path
from datetime import datetime


class CSVLogger:
    def __init__(self, filename="user_log.csv", headers=None):
        """Initialize the CSVLogger with a specified filename and optional headers."""
        self.filepath = Path(filename)  # Use Path object for the file path
        self.headers = headers or ["date", "user", "time", "report"]
        self.cached_data = []  # Cache to hold the latest data

        # Ensure the directory exists
        if not self.filepath.parent.exists():
            self.filepath.parent.mkdir(parents=True, exist_ok=True)

        # Check if file exists and write headers if it doesn't
        if not self.filepath.exists():
            self._write_headers()

        # Initialize cache by reading the file initially
        self.refresh()

    def _write_headers(self):
        """Write headers to the CSV file if it doesn't already exist."""
        try:
            with self.filepath.open(mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
        except IOError as e:
            print(f"Error initializing CSV file: {e}")

    def write_data(self, user, time, report):
        """Write a single row of data to the CSV file and update cache."""
        data = {
            "date": datetime.now().date(),
            "user": user,
            "time": time,
            "report": report
        }

        try:
            with self.filepath.open(mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writerow(data)
            # Update the cache after writing new data
            self.cached_data.append(data)
        except IOError as e:
            print(f"Error writing to CSV file: {e}")

    def write_batch(self, data_rows):
        """Write a batch of rows to the CSV file and update cache."""
        try:
            with self.filepath.open(mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writerows(data_rows)
            # Update the cache after writing batch data
            self.cached_data.extend(data_rows)
        except IOError as e:
            print(f"Error writing batch to CSV file: {e}")

    def get_user_data(self, user_email):
        """Return a list of dictionaries for a specific user from the cached data."""
        return [row for row in self.cached_data if row["user"] == user_email]

    def refresh(self):
        """Refresh the cached data by reading the file."""
        try:
            with self.filepath.open(mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.cached_data = [row for row in reader]  # Refresh the cache
        except IOError as e:
            print(f"Error reading from CSV file: {e}")

    def get_all_data(self):
        """Return all data from the CSV."""
        return self.cached_data

logger = CSVLogger('data/time_and_reports.csv')

# Usage example
if __name__ == '__main__':
    logger = CSVLogger('data/time_and_reports.csv')

    # Writing some data
    logger.write_data(user="user@example.com", time="01:23:45", report="Completed tasks for the day.")
    logger.write_data(user="user2@example.com", time="01:43:45", report="Completed tasks for the day.")

    # Getting data for a specific user before refresh
    user_data = logger.get_user_data("user@example.com")
    print("User data for user@example.com before refresh:", user_data)

    # Simulate adding new data
    logger.write_data(user="user@example.com", time="02:10:00", report="Follow-up tasks completed.")

    # Refresh and get updated data for the user
    logger.refresh()
    refreshed_user_data = logger.get_user_data("user@example.com")
    print("User data for user@example.com after refresh:", refreshed_user_data)

    # For batch writing:
    # data_batch = [
    #     {"user": "user1@example.com", "time": "00:12:30", "report": "Initial report"},
    #     {"user": "user2@example.com", "time": "00:42:10", "report": "Additional report"}
    # ]
    # logger.write_batch(data_batch)
