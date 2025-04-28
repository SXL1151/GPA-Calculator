import classAverage
import pdb
import streamlit as st
class CoppellGPAScale:
    def OLGPA(i):
        while True:
            #pdb.set_trace()
            classAvg = classAverage.AvgInp.classAverageInpOL(i)
            #pdb.set_trace()
            test1 = "test1"
            #pdb.set_trace()
            try:
               classAvg = float(classAvg)
            except:
                st.badge("Incorrect Input!", color = "red")
                st.badge("Try again", color = "red")
                #classAvg = classAverage.classAverageInp()
            if float(classAvg) > 100 or float(classAvg) < 0:
                st.text("Wrong input")
                st.text("Try again")
                

            classAvg = float(classAvg)
            classAvg = round(classAvg)
            classGPA = 0
            if (classAvg >= 97) and (classAvg <= 100):
                
                classGPA = 5.0
            elif (classAvg >= 94) and (classAvg <= 96):
                
                classGPA = 4.8
            elif (classAvg >= 90) and (classAvg <= 93):
                
                classGPA = 4.6
            elif (classAvg >= 87) and (classAvg <= 89):
                
                classGPA = 4.4
            elif (classAvg >= 84) and (classAvg <= 86):
                
                classGPA = 4.2
            elif (classAvg >= 80) and (classAvg <= 83):
                
                classGPA = 4.0
            elif (classAvg >= 77) and (classAvg <= 79):
                
                classGPA = 3.8
            elif (classAvg >= 74) and (classAvg <= 76):
                
                classGPA = 3.6
            elif (classAvg >= 71) and (classAvg <= 73):
                
                classGPA = 3.4
            elif (classAvg == 70):
                
                classGPA = 3.2
            elif (classAvg < 70) or (classAvg == 69):
                #pdb.set_trace()
                
                classGPA = 0.0
            else:
                st.text("Re-input average")
                return
            st.badge(f"Your GPA for this class is {classGPA}")    
            return classGPA
    def HonorGPA(i):
        while True:

            classAvg = classAverage.AvgInp.classAverageInpHonors(i)
            #pdb.set_trace()
            test1 = "test1"
            #pdb.set_trace()
            try:
               classAvg = float(classAvg)
            except:
                st.badge("Incorrect Input!", color = "red")
                st.badge("Try again", color = "red")
                #classAvg = classAverage.classAverageInp()
            if float(classAvg) > 100 or float(classAvg) < 0:
                st.text("Wrong input")
                st.text("Try again")

            #pdb.set_trace()
            classAvg = float(classAvg)
            classAvg = round(classAvg)
            classGPA = 0
            #pdb.set_trace()
            if (classAvg >= 97) and (classAvg <= 100):
                
                classGPA = 5.5
            elif (classAvg >= 94) and (classAvg <= 96):
                
                classGPA = 5.3
            elif (classAvg >= 90) and (classAvg <= 93):
                
                classGPA = 5.1
            elif (classAvg >= 87) and (classAvg <= 89):
                
                classGPA = 4.9
            elif (classAvg >= 84) and (classAvg <= 86):
                
                classGPA = 4.7
            elif (classAvg >= 80) and (classAvg <= 83):
                
                classGPA = 4.5
            elif (classAvg >= 77) and (classAvg <= 79):
                
                classGPA = 4.3
            elif (classAvg >= 74) and (classAvg <= 76):
                
                classGPA = 4.2
            elif (classAvg >= 71) and (classAvg <= 73):
                
                classGPA = 3.9
            elif (classAvg == 70):
                
                classGPA = 3.7
            elif (classAvg < 70):
                
                classGPA = 0.0
            else:
                st.text("Re-input average")
                return
            st.badge(f"Your GPA for this class is {classGPA}")
            return classGPA
    def APIBGPA(i):
        while True:
            classAvg = classAverage.AvgInp.classAverageInpAPIB(i)
            #pdb.set_trace()
            test1 = "test1"
            #pdb.set_trace()
            try:
               classAvg = float(classAvg)
            except:
                st.badge("Incorrect Input!", color = "red")
                st.badge("Try again", color = "red")
                #classAvg = classAverage.classAverageInp()
            if float(classAvg) > 100 or float(classAvg) < 0:
                st.text("Wrong input")
                st.text("Try again")
            classAvg = float(classAvg)
            classAvg = round(classAvg + 0.5)
            classGPA = 0
            if (classAvg >= 97) and (classAvg <= 100):
                
                classGPA = 6.0
            elif (classAvg >= 94) and (classAvg <= 96):
                
                classGPA = 5.8
            elif (classAvg >= 90) and (classAvg <= 93):
                
                classGPA = 5.6
            elif (classAvg >= 87) and (classAvg <= 89):
                
                classGPA = 5.4
            elif (classAvg >= 84) and (classAvg <= 86):
                
                classGPA = 5.2
            elif (classAvg >= 80) and (classAvg <= 83):
                
                classGPA = 5.0
            elif (classAvg >= 77) and (classAvg <= 79):
                
                classGPA = 4.8
            elif (classAvg >= 74) and (classAvg <= 76):
                
                classGPA = 4.6
            elif (classAvg >= 71) and (classAvg <= 73):
                
                classGPA = 4.4
            elif (classAvg == 70):
                
                classGPA = 4.2
            elif (classAvg < 70):
                
                classGPA = 0.0
            else:
                st.text("Re-input average")
                return
            st.badge(f"Your GPA for this class is {classGPA}")
            return classGPA
    def UnweighedGPA(i):
        while True:
            classAvg = classAverage.AvgInp.classAverageInpOL(i)#fix this
            #pdb.set_trace()
            test1 = "test1"
            #pdb.set_trace()
            try:
               classAvg = float(classAvg)
            except:
                st.badge("Incorrect Input!", color = "red")
                st.badge("Try again", color = "red")
                #classAvg = classAverage.classAverageInp()
            if float(classAvg) > 100 or float(classAvg) < 0:
                st.text("Wrong input")
                st.text("Try again")
            classAvg = float(classAvg)
            classAvg = round(classAvg + 0.5)
            classGPA = 0
            if (classAvg >= 97) and (classAvg <= 100):
                
                classGPA = 4.0
            elif (classAvg >= 94) and (classAvg <= 96):
                
                classGPA = 3.8
            elif (classAvg >= 90) and (classAvg <= 93):
                
                classGPA = 3.6
            elif (classAvg >= 87) and (classAvg <= 89):
                
                classGPA = 3.4
            elif (classAvg >= 84) and (classAvg <= 86):
                
                classGPA = 3.2
            elif (classAvg >= 80) and (classAvg <= 83):
                
                classGPA = 3.0
            elif (classAvg >= 77) and (classAvg <= 79):
                
                classGPA = 2.8
            elif (classAvg >= 74) and (classAvg <= 76):
                
                classGPA = 2.6
            elif (classAvg >= 71) and (classAvg <= 73):
                
                classGPA = 2.4
            elif (classAvg == 70):
                
                classGPA = 2.2
            elif (classAvg < 70):
                
                classGPA = 0.0
            else:
                st.text("Re-input average")
                return
            st.badge(f"Your GPA for this class is {classGPA}")    
            return classGPA
