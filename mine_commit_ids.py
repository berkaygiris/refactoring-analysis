from pydriller import *
import sys
DATA_DIR = "data/"
help_cmds = {"-h", "--h", "-help", "--help"}

if len(sys.argv) < 2 or sys.argv[1] in help_cmds or len(sys.argv) < 3:
    sys.exit("Use as \"mine_commit_ids.py <url> <filename>")

url = str(sys.argv[1])
file_name = str(sys.argv[2])

print("url: " + url)
print("filename: " + file_name)

f = open(DATA_DIR + file_name, "w")

repo = RepositoryMining(url)

for commit in repo.traverse_commits():
    print('{} {}'.format(commit.hash, commit.author_date))
    f.write('{} {}\n'.format(commit.hash, commit.author_date))

f.close()

