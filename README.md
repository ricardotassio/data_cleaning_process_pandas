# Data Processing and Reporting System

## Project Structure

The project is divided into several modular classes, each with its own responsibility:

- **`BaseProcessor`**: The base class that provides shared functionalities such as data type conversion.
- **`IOHandler`**: Handles reading and writing CSV files.
- **`DataCleaning`**: Cleans the dataset, handling missing values and standardizing entries.
- **`GenerateReport`**: Generates various reports, including age averages, gender distribution, and more.

## Files

- **`base_processor.py`**: Contains the `BaseProcessor` class.
- **`io_handler.py`**: Contains the `IOHandler` class.
- **`data_cleaning.py`**: Contains the `DataCleaning` class.
- **`generate_report.py`**: Contains the `GenerateReport` class.
- **`main.py`**: The entry point of the application, coordinating the entire process.

## Setup

### Prerequisites

- Python 3.x
- Pandas (`pip install pandas`)
- Numpy (`pip install numpy`)

### Installation

1. Clone the repository or download the project files.
2. Ensure all required Python packages are installed:
   ```sh
   pip install pandas numpy
   ```

## Usage

### Running the Program

1. Place your dataset in the root directory and name it `sample_dataset.csv` (or update the `file_path` in `main.py`).
2. Run the `main.py` script:
   ```sh
   python main.py
   ```
3. The program will:
   - Import the dataset.
   - Clean the dataset by replacing missing values and standardizing entries.
   - Convert the `Age` column to integers.
   - Save the cleaned dataset to `cleaned_dataset.csv`.
   - Generate and print various reports to the console.

### Example Output

When you run the program, you should see output in the console that includes:

- The average age of all individuals, males, and females.
- The distribution of genders in the dataset.
- The age range by gender.
- The top N oldest and youngest individuals.

## Customization

- **Input File**: Modify the `file_path` variable in `main.py` to use a different dataset.
- **Output File**: Modify the `output_path` variable in `main.py` to change where the cleaned dataset is saved.
