#!/usr/bin/python3

convert = __import__('02-csv')

def main():
    """ main """
    csv_file = "data.csv"
    convert.convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")

if __name__ == "__main__":
    main()
