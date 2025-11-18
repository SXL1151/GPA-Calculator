import streamlit as st
import pandas as pd
import GPACop
import numpy as np
import calc
TotGPA = 0
cNAMES = []
cGPAS = []
def GPA_Calculator():
  st.Page(calc.GPACalc())
def page_2():
  st.title("In Progress")
report_condition = False  
table = ""
st.sidebar.text("Menu")
nv = st.navigation([GPA_Calculator,page_2])
nv.run()
  
    
    
      
  
      
  
  



