import os
import re

pattern = ".*XmlUtil.*|.*NrdInboxProcessingServiceImpl.*"


def read_large_file(file_handler):
    for line in file_handler:
        yield line


with os.scandir('.') as entries:
    for entry in entries:
        if entry.is_file():
            if '.log' not in entry.name:
                continue
            print('Start refinement on ' + entry.name)
            with open(entry, 'r') as r:
                filtered = []
                regexp = re.compile(pattern)
                for line in read_large_file(r):
                    if regexp.match(line):
                        continue
                    filtered.append(line)
                data = ''.join(filtered)
                with open(entry, 'w') as w:
                    w.write(data)
                    print('Finish refinement on ' + entry.name)
