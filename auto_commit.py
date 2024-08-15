import os
import subprocess
from datetime import datetime

def find_git_root(start_path="."):
    cur_path = os.path.abspath(start_path)
    while cur_path != os.path.sep:
        if os.path.isdir(os.path.join(cur_path, ".git")):
            return cur_path
        cur_path = os.path.abspath(os.path.join(cur_path, os.pardir))
    raise FileNotFoundError(".git directory not found")

# 1. Git 리포지토리 루트로 이동
repo_dir = find_git_root()
os.chdir(repo_dir)

# 2. 파일 생성하기
date_str = datetime.now().strftime('%Y-%m-%d')
filename = f"develop_diary_{date_str}.txt"
with open(filename, 'w') as file:
    file.write(f"Develop diary entry for {date_str}.")

# 3. Git add, commit, push
subprocess.run(["git", "add", "."])
commit_message = f"Auto-commit: Develop diary entry for {date_str}"
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push"])
