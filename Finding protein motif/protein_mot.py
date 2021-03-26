import re
import requests

url="http://www.uniprot.org/uniprot/chosen_id.fasta"

dataset = "A2Z669 B5ZC00 P07204_TRBM_HUMAN P20840_SAG1_YEAST"
split_data = dataset.split()
specific_url = ""
for ids in split_data:
    specific_url = url.replace("chosen_id", ids)
    req = requests.get(specific_url)
    
    print(req.text)
