import streamlit as st
import pandas as pd
import GPACop
import numpy as np
import calc
TotGPA = 0
cNAMES = []
cGPAS = []
try:
  if "page" not in st.session_state:
    st.session_state.page = ""
  def GPA_Calculator():
    st.session_state.page = calc.GPACalc()
    return st.session_state.page
  def page_2():
    st.title("In Progress")
  report_condition = False  
  table = ""
  st.sidebar.text("Menu")
  nv = st.navigation([GPA_Calculator,page_2])
  nv.run()
except:
  st.error("")
  
    
    
      
  
      
  
  



