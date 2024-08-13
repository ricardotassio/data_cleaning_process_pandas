from base_processor import BaseProcessor
import pandas as pd

class GenerateReport(BaseProcessor):
    def generate_report(self) -> None:
        self._calculate_age_average()
        self._calculate_gender_distribution()
        self._age_range_by_gender()
        self._top_n_oldest_youngest(5)

    def _calculate_age_average(self) -> None:
        print(f"Calculating the overall average age...")
        overall_avg_age = self.dataset['Age'].mean()
        print(f"Overall Average Age: {overall_avg_age}")

        print(f"Calculating the average age by gender...")
        male_avg_age = self.dataset[self.dataset['Gender'] == 'Male']['Age'].mean()
        female_avg_age = self.dataset[self.dataset['Gender'] == 'Female']['Age'].mean()
        print(f"Average Age - Males: {male_avg_age}, Females: {female_avg_age}")

    def _calculate_gender_distribution(self) -> None:
        print(f"Calculating gender distribution...")
        gender_distribution = self.dataset['Gender'].value_counts()
        print("Gender Distribution:")
        print(gender_distribution)

    def _age_range_by_gender(self) -> None:
        print(f"Calculating age range by gender...")
        male_age_range = self.dataset[self.dataset['Gender'] == 'Male']['Age'].agg(['min', 'max'])
        female_age_range = self.dataset[self.dataset['Gender'] == 'Female']['Age'].agg(['min', 'max'])
        print(f"Age Range - Males: {male_age_range}, Females: {female_age_range}")

    def _top_n_oldest_youngest(self, N: int) -> None:
        print(f"Identifying the top {N} oldest and youngest individuals...")
        oldest = self.dataset.nlargest(N, 'Age')
        youngest = self.dataset.nsmallest(N, 'Age')
        print(f"Top {N} Oldest Individuals:")
        print(oldest)
        print(f"Top {N} Youngest Individuals:")
        print(youngest)
