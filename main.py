import streamlit as st
import pandas as pd
import GPACop

TotGPA = 0
cNAMES = []
cGPAS = []
report_condition = False  
table = ""

st.image(
    "https://media-hosting.imagekit.io/08168422c2f645f9/IMG_1657.png?Expires=1839961164&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=D51gbtOWwAKHNmzhT6r9HNI5K-VKbdti3-2kbUwdd2A649TiXaLzf6GmwO42h5L8ty1RMsmuEkfIxoADqIWfQVDg0XY0uICM~JgnPdXAA0gIqDZUuVYHXG2O3MWt9GoVGR58Sw71K7H3u3zZ5pEY7ezwOnoXcoLK4oSX1uS~EKvwALG-1K9VTUUBtdsmhFlp~TxkSIOh9TW6jC5FD6~XZodWv1uTvHU7OvVewGnrSrL56RlBtsa0CTaHjkq6tPcq-XYirpcVOUagFam2yWQy23IFAgSdH73tSvhrrkkv6v6qTkkVpt5ZK8qghM2hArQwqG8k~D6z-Kg95D0eIuUaaA__",
    width=20)
st.title("GPA CALCULATOR")
stuVerify = st.checkbox("I am a Coppell ISD student")
if stuVerify == True:
  st.badge("Coppell ISD Student Verified", color="green")
else:
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
      st.badge("You have no classes, therefore, your GPA cannot be calculated",
               color="blue")
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
  #report_condition = True
except:
  st.badge("No classes to calculate GPA", color="red")

finTable = {"Class Name": cNAMES, "Class GPA": cGPAS}
cNAMES.append("TOTAL GPA")
try:
  cGPAS.append(str(TotGPA/num_classes))
  booGo = True
except ZeroDivisionError:
  st.badge("No classes to build GPA Table", color="red")
  booGo = False
if booGo == False:
  pass
elif booGo == True:
  st.table(finTable)
  report_condition = True
#pdb.set_trace()
try:
  finTable = pd.DataFrame(finTable)
  csv = finTable.to_csv(index=False).encode('utf-8')
except:
  pass
#buttonDown = st.button()
if (report_condition == True):
  if st.button("Prepare Download"):
  
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

  
  
    

    





