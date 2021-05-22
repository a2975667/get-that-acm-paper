import wget
import sys
import pikepdf
import requests
from os import rename

input = sys.argv[1]

if input[0:4] == "http":
    if input.split('/')[-3] == 'doi':
        url = "https://dl.acm.org/doi/pdf/" + '/'.join(input.split('/')[-2:])
    else:
        url = input
else:
    url = "https://dl.acm.org/doi/pdf/" + str(input)

filename = url.split('/')[-1]

file = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
open(filename, 'wb').write(file.content)
pdf = pikepdf.open(filename)
paper_title = pdf.open_metadata()['dc:title'] + '.pdf'

rename(filename, paper_title)

print("Downloaded: ", paper_title)