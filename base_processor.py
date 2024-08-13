import pandas as pd

class BaseProcessor:
    def __init__(self):
        self.dataset = None

    def convert_data_type(self, column_name: str, target_type: str) -> None:
        print(f"Converting {column_name} to {target_type}...")
        try:
            self.dataset[column_name] = self.dataset[column_name].astype(target_type)
            print(f"{column_name} is now {self.dataset[column_name].dtype}")
        except ValueError as e:
            print(f"Error converting {column_name} to {target_type}: {e}")