from Bio.PDB import *
import os

pdbl = PDBList() 
new1=input("Enter PDB id: ")
file=pdbl.retrieve_pdb_file(new1, pdir = '.', file_format = 'pdb')

records = []
with open(file, "r") as f:
    for line in f: 
        if "HETATM" not in line and "CONECT" not in line or "ATP" in line: 
            records.append(line)

with open("new.pdb", "w") as f: 
    for line in records: 
        f.write(line)

with open("new.pdb", "r") as f:
    data=f.read()
    data=data.replace('ATP','LIG')
with open("new.pdb", "w") as f:
    for line in data:
        f.write(line)

os.startfile('new.pdb')