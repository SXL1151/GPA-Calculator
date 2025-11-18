import streamlit as st
import pandas as pd
import GPACop
import numpy as np
TotGPA = 0
cNAMES = []
cGPAS = []
class GPACalc:
  st.title("GPA CALCULATOR")
  stuVerify = st.checkbox("I am a Coppell ISD student")
  if not stuVerify:
    st.warning(
        "WARNING: THIS GPA CALCULATOR MAY NOT BE ACCURATE FOR YOUR SCHOOL DISTRICT"
    )
  #pdb.set_trace()
  ChoGPA = st.selectbox("What type of GPA would you like to calculate?", ("Weighted GPA", "Unweighted GPA"))
  if ChoGPA == "Weighted GPA":
    
    while True:
      num_classes = st.number_input("How many classes do you have?",
                                    min_value=0, key = f"cnum_{1}")
    
      if num_classes == 0:
        st.badge("You have no classes, therefore, your GPA cannot be calculated",
                 color="blue")
        break
      try:
        num_classes = int(num_classes)
        st.text(f"You have {num_classes} classes")
        break
      except ValueError:
        st.badge("Please enter an integer", color="red")
    st.divider()
    st.file_uploader("Upload an image of your transcript", type="JPG")
    for i in range(num_classes):
      cName = st.text_input("Class #" + str(i + 1) + ": What is the class name?)",
                            placeholder="optional", key=f"cname_{i}"
                            )
      if cName == "":
  
        cName = "Class #" + str(i+1)
      else:
        pass
      
      cLevel = st.selectbox("What is your class level?",("On-Level", "Honors", "AP/IB"), key = f"clevel_{i}")
      
      
      if cLevel == "On-Level":
        #cAverage = classAverage.classAverageInp
        cGPA = GPACop.CoppellGPAScale.OLGPA(num_classes-(num_classes-i))
        TotGPA = TotGPA + cGPA
        cNAMES.append(cName)
        cGPAS.append(str(cGPA))
        st.text("________________________________________________________________________________________________________________________________________________________________________________")
      elif cLevel == "Honors":
        cGPA = GPACop.CoppellGPAScale.HonorGPA(num_classes-(num_classes-i))
        TotGPA = TotGPA + cGPA
        cNAMES.append(cName)
        cGPAS.append(str(cGPA))
        st.text("________________________________________________________________________________________________________________________________________________________________________________")
      elif cLevel == "AP/IB":
        cGPA = GPACop.CoppellGPAScale.APIBGPA(num_classes-(num_classes-i))
        TotGPA = TotGPA + cGPA
        cNAMES.append(cName)
        cGPAS.append(str(cGPA))
        st.text("________________________________________________________________________________________________________________________________________________________________________________")
  elif ChoGPA == "Unweighted GPA":
    while True:
      num_classes = st.number_input("How many classes do you have?",
                                    min_value=0, key = f"cnum_{1}")
  
      if num_classes == 0:
        pass
        break
      try:
        num_classes = int(num_classes)
        st.text(f"You have {num_classes} classes")
        break
      except ValueError:
        st.badge("Please enter an integer", color="yellow")
    for i in range(num_classes):
      
      cName = st.text_input("Class #" + str(i + 1) + ": What is the class name?)",
                            placeholder="optional", key=f"cname_{i}"
                            )
      if cName == "":
        
        cName = "Class #" + str(i+1)
      else:
        pass
      
      cGPA = GPACop.CoppellGPAScale.UnweighedGPA(num_classes-(num_classes-i))
      TotGPA = TotGPA + cGPA
      cNAMES.append(cName)
      cGPAS.append(str(cGPA))
      #pdb.set_trace()
      
      
      st.text("________________________________________________________________________________________________________________________________________________________________________________")
        
  try:
    st.warning(f"Your total GPA is {TotGPA/num_classes}")
  except:
    pass
  report_condition = True
  finTable = {"Class Name": cNAMES, "Class GPA": cGPAS}
  cNAMES.append("TOTAL GPA")
  try:
    cGPAS.append(str(TotGPA/num_classes))
    booGo = True
  except ZeroDivisionError:
    pass
    booGo = False
  if booGo == False:
    pass
  elif booGo == True:
    st.table(finTable)
    report_condition = True
  #pdb.set_trace()
  try:
    finTable2 = pd.DataFrame(finTable)
    csv = finTable2.to_csv(index=False).encode('utf-8')
  except:
    pass
  #buttonDown = st.button()
  if (report_condition == True):
    if st.button("Prepare Download", type="primary"):
    
      if (report_condition == True):
        st.download_button(
            label="Download GPA Report",
            data = csv,
            file_name="GPA_Report.csv",
            mime="Report/csv",
            icon=":material/download:",
            type="primary",
            on_click="ignore"
        )
