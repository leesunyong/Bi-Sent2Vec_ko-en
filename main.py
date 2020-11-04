import argparse
from data_process import process_data_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bi Sentence to Vector')
    parser.add_argument('module', type=str)
    parser.add_argument('input', type=str,
                        help='data file for embedding words')

    args = parser.parse_args()

    if args.module == 'process':
        process_data_file(args.input, 'ko', 'en')
