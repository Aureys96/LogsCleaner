import os
import re
from itertools import filterfalse

pattern = ".*XmlUtil.*|.*NrdInboxProcessingServiceImpl.*"


with os.scandir('.') as entries:
    for entry in entries:
        if entry.is_file():
            if '.log' not in entry.name:
                break
            print('Start refinement on ' + entry.name)
            with open(entry, 'r') as r:
                data = r.read()
                splitlines = data.splitlines()
                regexp = re.compile(pattern)
                filtered = list(filterfalse(lambda line: regexp.search(line), splitlines))
                data = '\n'.join(filtered)
                with open(entry, 'w') as w:
                    w.write(data)
                    print('Finish refinement on ' + entry.name)
