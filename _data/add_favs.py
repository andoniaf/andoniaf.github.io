import yaml

favsFile = "linklog.yml"

with open(favsFile,'r') as readFile:
  data = yaml.safe_load(readFile)


  


with open(favsFile, 'w') as writeFile:
  orderedData = dict(sorted(data.items(), reverse=True))
  yaml.safe_dump(data, writeFile)
