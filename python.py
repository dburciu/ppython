import re

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

