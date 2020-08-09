import sys
import yaml
from datetime import datetime

favsFile = "linklog_test.yml"

# Fav entry example
# {'type': 'read',
#  'title': 'Read Me',
#  'link': 'https://read.me',
#  'tags': ['sre', 'slo']
# }


def main(favType, favTitle, favLink, *args):
  with open(favsFile,'r') as readFile:
    data = yaml.safe_load(readFile)

  favEntry = {
    'type': favType,
    'title': favTitle,
    'link': favLink
  }

  if args[0]:
    favEntry.update({'tags': list(args)[0]})

  print(f'New entry: {favEntry}')

  favTime = int(datetime.now().strftime("%Y%m%d%H%M%S"))

  data[favTime] = favEntry

  with open(favsFile, 'w') as writeFile:
    orderedData = dict(sorted(data.items(), reverse=True))
    yaml.safe_dump(orderedData, writeFile)



print(f'Args: {sys.argv}')

if (len(sys.argv) > 1):
  main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])

