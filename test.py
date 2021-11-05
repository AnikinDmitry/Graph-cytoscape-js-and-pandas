import pandas as pd
import json

file = pd.read_excel("./example.xlsx")

nodes_list = sorted(set(file["node1"].tolist() + file["node2"].tolist()))
links_list = list(file["node1"] + file["node2"])

nodes = [{'data': {'id': node}} for node in nodes_list]
links = [{'data': {'source': link[0], 'target': link[1]}} for link in links_list]

with open('data.json', 'w') as file: 
	json.dump(nodes + links, file, indent=4)