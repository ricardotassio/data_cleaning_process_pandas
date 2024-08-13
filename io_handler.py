from base_processor import BaseProcessor
import pandas as pd

class IOHandler(BaseProcessor):
    def read_csv(self, path: str) -> pd.DataFrame:
        try:
            print(f"FIRST STEP: Importing dataset!")
            self.dataset = pd.read_csv(path)
            print(f"Dataset imported!")
            return self.dataset
        except FileNotFoundError:
            print(f"Dataset not found!")
            return pd.DataFrame()

    def save_dataset(self, path: str) -> None:
        print(f"Saving cleaned dataset to {path}")
        self.dataset.to_csv(path, index=False)
        print("Dataset saved!")