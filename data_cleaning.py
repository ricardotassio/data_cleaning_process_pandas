from base_processor import BaseProcessor
import pandas as pd

class DataCleaning(BaseProcessor):
    def clean_dataset(self) -> pd.DataFrame:
        print(f"REPLACING UNDERAGE ENTRIES WITH THE MEDIAN AGE")
        median_age = self.dataset['Age'].median()
        self.dataset.loc[self.dataset['Age'] < 18, 'Age'] = median_age
        print(f"Standardizing Gender Values...")
        self.dataset['Gender'] = self.dataset['Gender'].replace({
            'F': 'Female', 'f': 'Female',
            'M': 'Male', 'm': 'Male'
        })

        print(f"Handling missing age values...")
        male_avg_age = self.dataset[self.dataset['Gender'] == 'Male']['Age'].mean()
        female_avg_age = self.dataset[self.dataset['Gender'] == 'Female']['Age'].mean()

        self.dataset.loc[(self.dataset['Age'].isnull()) & (self.dataset['Gender'] == 'Male'), 'Age'] = male_avg_age
        self.dataset.loc[(self.dataset['Age'].isnull()) & (self.dataset['Gender'] == 'Female'), 'Age'] = female_avg_age

        overall_avg_age = self.dataset['Age'].mean()
        self.dataset['Age'].fillna(overall_avg_age, inplace=True)
        print(f"Replacing remaining missing values with 'N/A'")
        self.dataset.fillna({'Gender': 'N/A', 'Occupation': 'N/A'}, inplace=True)

        print(f"REMOVING ALL THE MISSING COLUMNS ")
        self._remove_missing_in_columns(['Gender', 'Occupation'])

        return self.dataset

    def _remove_missing_in_columns(self, columns: list) -> None:
        print(f"Removing rows with missing values in columns: {columns}")
        initial_shape = self.dataset.shape
        self.dataset = self.dataset.dropna(subset=columns)
        final_shape = self.dataset.shape
        print(f"Rows before removal: {initial_shape[0]}, Rows after removal: {final_shape[0]}")