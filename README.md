# get-that-acm-paper
This is a very short script to download an acm dl paper AND change the pdf file name based on url, pdfurl or the doi of that paper. This script not intended for scraping and must be executed in a VPN-enabled environment. Please use at care.


# Usage
### Requirements
You must install the required packages to run the script
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Usage example
All three would work with the script
```
python run.py https://dl.acm.org/doi/pdf/10.1145/3449281
python run.py https://dl.acm.org/doi/10.1145/3449281
python run.py 10.1145/3449281
```

