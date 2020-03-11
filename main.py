from genericDataProcessor import readText,loadData, pickleData
import numpy as np
import quantities as pq
from quantities.units.electromagnetism import volt,milliamp, uF,ohm
from quantities.units.temperature import degC
from quantities import Quantity as q
from quantities import UncertainQuantity as uq
import pickle
import pylatex as tex
from pylatex import TikZ,Axis,Plot,Figure,Command
from pylatex.utils import NoEscape
from pylatex.math import Math
from pylatex.table import Tabular
import matplotlib
from pylatex.position import Center
import matplotlib.pyplot as plt

authors=["Nicholas Gower","Caleb Puls","Gauthan Anant","Ethan Radford"]
sections=['Title', 'Personnel', 'Executive Summary', 'Introduction', 'Equipment',"Data and analysis","Discussion and conclusion"]
for name in sections:
    open(name+".txt",'w').close()
def addSection(document,title,fileName):
  with doc.create(tex.Section(title):
    doc.append(readText(fileName))
def main():
	pickleData("data.xlsx","data.labdata")
	pickleData("equipment.xlsx","equipment.labdata")
	data=loadData("data.labData")
	equipmentList=loadData("equipment.labdata")
				  
				  
	doc=tex.Document("book",geometry_options={"margin":"1in")
  doc.preamble.append(Command('author', ",".join(authors))
  doc.preamble.append(Command('title',"Constructing a Tesla Coil")
  doc.append(Command("maketitle"))
  addSection(doc,'Introduction','Introduction.txt')
  with doc.create(tex.Section("Equipment"):
    with doc.create(Tabular("| l | l | l | l | l |")) as table:
      table.add_hline()
      table.add_row(["Name","SKU","Vendor","Price","Shipping Time"])
      table.add_hline()    
      for row in sheet:
      	table.add_row([row['Name'],row["SKU"],row["Vendor"],row["Price"],row["Shipping Time"])
      	table.add_hline()
  addSection(doc,'Data','dataAnalysis.txt')
