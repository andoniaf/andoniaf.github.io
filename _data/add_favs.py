import sys
import yaml
from datetime import datetime

favsFile = "linklog.yml"

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

  # favTime = int(datetime.now().strftime("%Y-%m-%d-%H%M%S"))
  favTime = datetime.now().strftime("%Y-%m-%d-%H%M%S")

  data[favTime] = favEntry

  try:
    # print(data)
    orderedData = dict(sorted(data.items(), reverse=True))
    print(orderedData)
  except Exception as e:
    print(f'Sorting error: {e}')
    sys.exit()

  with open(favsFile, 'w') as writeFile:
    print("Save")
    yaml.safe_dump(orderedData, writeFile, sort_keys=False)


print(sys.argv)

if (len(sys.argv) >= 4):
  main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
else:
  print('Usage: add_favs.py <type> <title> <link> [<tags>]')
