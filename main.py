import argparse

import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bi Sentence to Vector')
    parser.add_argument('module', type=str)
    parser.add_argument('params', type=str, nargs='+')

    args = parser.parse_args()

    if args.module == 'download':
        import setup

        # Download all requirements
        setup.download(args.params[0])

    elif args.module == 'parse':
        from data_process import process_data_file

        # Make train text file with input files which the user enters.
        #   params : input file names
        #   input file contents format : [Korean Sentence] \t [English Sentence]
        #   Two sentences in different languages must be split by '\t'
        open('ko-en.txt', 'w').close()
        for file_name in args.params:
            process_data_file(file_name, 'ko', 'en')

#     # elif args.module == 'fasttext':
#     #     fasttext('ko', 'en')
