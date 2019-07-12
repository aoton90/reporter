from reporter import header
import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
import json

class generator:
    
    def __init__ (self, json_path, xls_path, md_path,png_path):
        self.json_path = json_path
        self.xls_path = xls_path
        self.md_path = md_path
        self.png_path = png_path
    
    def create_graph(self):
        series = pd.read_excel(self.xls_path).set_index("année").transpose().dropna(how="all",axis=1)
        series.index = series.index.astype(int)
        series.plot(y=['dette_immo_menages','prix_logement_Fr'])
        plt.savefig(self.png_path)

        
    def create_markdown(self):
        with open(self.json_path, 'r') as in_file:
            reloaded = json.load(in_file)
            
        sortie = header.create_header(reloaded) + f"\n![alt text]({self.png_path})"

        with open(self.md_path, "w", encoding='utf-8') as out_file:
            out_file.write(sortie)
       
    