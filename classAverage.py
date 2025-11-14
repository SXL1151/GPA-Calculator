import streamlit as st
class AvgInp:
  def classAverageInpOL(j):
    classAVG = 0
    for i in range(1):
    
      classAVG = st.number_input("What is your average(%) in the class?",
           placeholder="Must be a number",min_value=0.10, max_value=100.00,
           key=f"cavgOL_{j}")
    return classAVG
  def classAverageInpHonors(j):
    classAVG = 0
    for i in range(1):
      
      classAVG = st.number_input("What is your average(%) in the class?",
           placeholder="Must be a number",min_value=0.10, max_value=100.00,
           key=f"cavgHon_{j}")
    return classAVG
  def classAverageInpAPIB(j):
    classAVG = 0
    for i in range(1):
    
      classAVG = st.number_input("What is your average(%) in the class?",
         placeholder="Must be a number",min_value=0.10, max_value=100.00,
         key=f"cavgAP_{j}")
    return classAVG
  
