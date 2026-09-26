import numpy as np
from tkinter import Tk , filedialog

from docx import Document


def upload():
    root = Tk()
    root.withdraw()
    file = filedialog.askopenfilename()
    
    return file

file = upload()

print(file)



def read_file(file):
    
    document = Document(file)
    
    production = []
    defects = []
    workers = []
    
    tables = document.tables[0]
    
    for row in tables.rows[1:]:
        
        production.append(int(row.cells[1].text))
        defects.append(int(row.cells[2].text))
        workers.append(int(row.cells[3].text))
        
        
    return production , defects , workers


production , defects , workers = read_file(file)











class Analysis:
    
    def __init__(self , production , defects , workers):
        self.production = np.array(production)
        self.defects = np.array(defects)
        self.workers = np.array(workers)
        
        
        
    def high_prod(self):
        return np.max(self.production)
    
    def low_prod(self):
        return np.min(self.production)
    def avg_prod(self):
        return np.mean(self.production)
            
        
    def defect(self):
         return np.sum(self.defects)
     
    def avg_defect(self):
              return np.mean(self.defects)
     
    def prod_per_worker(self):
         return np.mean(self.production/self.workers)
         
        
analyzer = Analysis(production , defects , workers)





print("\n================================")
print("       PRODUCTION ANALYSIS")
print("================================")

print(f"{'Analysis':<25} {'Result':>10}")
print("--------------------------------")

print(f"{'Highest Production':<25} {analyzer.high_prod():>10}")
print(f"{'Lowest Production':<25} {analyzer.low_prod():>10}")
print(f"{'Average Production':<25} {analyzer.avg_prod():>10.2f}")
print(f"{'Total Defects':<25} {analyzer.defect():>10}")
print(f"{'Average Defects':<25} {analyzer.avg_defect():>10.2f}")
print(f"{'Production / Worker':<25} {analyzer.prod_per_worker():>10.2f}")

print("================================")