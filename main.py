from io_handler import IOHandler
from data_cleaning import DataCleaning
from generate_report import GenerateReport

def main():
    file_path = 'sample_dataset.csv'
    output_path = 'cleaned_dataset.csv'

    io_handler = IOHandler()
    dataset = io_handler.read_csv(file_path)
    
    data_cleaning = DataCleaning()
    data_cleaning.dataset = dataset
    cleaned_dataset = data_cleaning.clean_dataset()

    io_handler.dataset = cleaned_dataset
    io_handler.convert_data_type('Age', 'int')

    io_handler.save_dataset(output_path)
    
    generate_report = GenerateReport()
    generate_report.dataset = cleaned_dataset
    generate_report.generate_report()

if __name__ == "__main__":
    main()

