import sys
import json

help_cmds = {"-h", "--h", "-help", "--help"}
if len(sys.argv) < 2 or sys.argv[1] in help_cmds:
    sys.exit("Use as \"refactor_counter.py <projectname>")
    
projectname = str(sys.argv[1])

with open(projectname + "-rminer.json", "r") as f:
    dict = json.load(f, strict=False)

outfile = open(projectname + "-refactoring.commits", "w")

count_commits = 0
count_refactorings = 0
for commit in dict["commits"]:
    if len(commit["refactorings"]) > 0:
        outfile.write("{} {}\n".format(commit["sha1"], len(commit["refactorings"])))
        count_commits += 1
        count_refactorings += len(commit["refactorings"])

outfile.write("Total commits: {}\n".format(len(dict["commits"])))
outfile.write("Total refactoring commits: {}\n".format(count_commits))
outfile.write("Total refactorings: {}\n".format(count_refactorings))

