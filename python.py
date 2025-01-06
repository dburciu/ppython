import re
import os
import argparse

def search_in_file(pattern, file_path, case_insensitive=False, exclude=False, only_count=False):
    matches = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if case_insensitive:
                    found = re.search(pattern, line, re.IGNORECASE)
                else:
                    found = re.search(pattern, line)

                if (found and not exclude) or (not found and exclude):
                    matches += 1
                    if not only_count:
                        print(f"{file_path}:{line_number}:{line.strip()}")
    except Exception as e:
        print(f"Could not read file {file_path}: {e}")
    
    return matches

def search_in_directory(pattern, folder_path, case_insensitive=False, exclude=False, only_count=False):
    total_matches = 0
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_matches = search_in_file(pattern, file_path, case_insensitive, exclude, only_count)
            total_matches += file_matches
            if only_count and file_matches > 0:
                print(f"{file_path}: {file_matches}")

    if only_count:
        print(f"Total matches across all files: {total_matches}")

def main():
    parser = argparse.ArgumentParser(description="A simple grep-like tool in Python.")
    parser.add_argument("pattern", help="The text or regex pattern to search for.")
    parser.add_argument("path", help="The file or folder to search in.")
    parser.add_argument("-ignoreCase", action="store_true", help="Make the search case insensitive.")
    parser.add_argument("-exclude", action="store_true", help="Find lines that do not match the pattern.")
    parser.add_argument("-count", action="store_true", help="Count matches instead of showing them.")

    args = parser.parse_args()

    if os.path.isfile(args.path):
        matches = search_in_file(args.pattern, args.path, args.ignoreCase, args.exclude, args.count)
        if args.count:
            print(f"{args.path}: {matches}")
    elif os.path.isdir(args.path):
        search_in_directory(args.pattern, args.path, args.ignoreCase, args.exclude, args.count)
    else:
        print("Invalid path. Please provide a valid file or folder.")

if __name__ == "__main__":
    main()
