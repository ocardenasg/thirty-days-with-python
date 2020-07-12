import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(BASE_DIR, 'files')
os.makedirs(files_dir, exist_ok=True)

for i in range(0, 10):
    fname = f"file_{i}.txt"
    file_path = os.path.join(files_dir, fname)
    if os.path.exists(file_path):
        print(f"Skipped {fname}")
        continue
    with open(file_path, 'w') as f:
        f.write(f"Hello world {i}")
