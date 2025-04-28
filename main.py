import streamlit as st
import pdb
import GPACop
import classAverage
TotGPA = 0
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
      st.badge("Please enter an integer", color="yellow")
  for i in range(num_classes):
    cName = st.text_input("Class #" + str(i + 1) + ": What is the class name?)",
                          placeholder="optional", key=f"cname_{i}"
                          )
    cLevel = st.selectbox("What is your class level?",("On-Level", "Honors", "AP/IB"), key = f"clevel_{i}")
    
    
    if cLevel == "On-Level":
      #cAverage = classAverage.classAverageInp
      TotGPA = TotGPA + GPACop.CoppellGPAScale.OLGPA(num_classes-(num_classes-i))
      st.text("________________________________________________________________________________________________________________________________________________________________________________")
    elif cLevel == "Honors":
      TotGPA = TotGPA + GPACop.CoppellGPAScale.HonorGPA(num_classes-(num_classes-i))
      st.text("________________________________________________________________________________________________________________________________________________________________________________")
    elif cLevel == "AP/IB":
      TotGPA = TotGPA + GPACop.CoppellGPAScale.APIBGPA(num_classes-(num_classes-i))
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
    GPACop.CoppellGPAScale.UnweighedGPA(num_classes-(num_classes-i))
    st.text("________________________________________________________________________________________________________________________________________________________________________________")
      
try:
  st.warning(f"Your total GPA is {TotGPA/num_classes}")
except:
  st.badge("No classes to calculate GPA", color="red")
    

    


