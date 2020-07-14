import os
import json
import glob

PATH_TO_DATA = "_data"

papers = glob.glob(f"papers/*.json")

papers_json = {}

for paper in papers:
    with open(paper,'r') as p:
        paper = json.loads(p.read())
        papers_json[paper['title']]  = paper

with open(f"{PATH_TO_DATA}/papers.json","w")as f:
    f.write(json.dumps(paper))

