import os
import sys

EXCLUDE_DIRS = {'node_modules', '__pycache__', '.git', 'dist', 'build', '.venv', 'venv'}
TARGET_EXTENSIONS = {'.py', '.ts', '.tsx', '.json', '.js', '.css', '.html', '.md', '.ini', '.yaml', '.yml', '.sql'}

def count_lines_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            return len(lines)
    except Exception as e:
        return 0

def calculate_loc(root_dir):
    total_loc = 0
    file_count = 0
    extension_counts = {}

    print(f"Scanning directory: {root_dir}")
    print("=" * 60)

    for root, dirs, files in os.walk(root_dir):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in TARGET_EXTENSIONS:
                full_path = os.path.join(root, file)
                loc = count_lines_in_file(full_path)
                total_loc += loc
                file_count += 1
                extension_counts[ext] = extension_counts.get(ext, 0) + loc

    print("\n--- LOC Breakdown by Extension ---")
    for ext, loc in sorted(extension_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {ext:<10}: {loc:,} lines")

    print("=" * 60)
    print(f"Total Files Processed : {file_count}")
    print(f"Total Lines of Code   : {total_loc:,} LOC")
    print("=" * 60)
    return total_loc

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    calculate_loc(target)
