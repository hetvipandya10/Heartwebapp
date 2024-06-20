import streamlit as st

st.title("Welcome to Heart App")

Age=st.slider("Select Age=",29,77)
sex=st.slider("Select sex=",0,1)
ChestPainType=st.slider("select ChestPainType=",1,4)
BP=st.slider("Select BP=",94,200)
Cholesterol=st.slider("Select Cholesterol=",126,564)
FBSover120=st.slider("Select FBSover120=",0,1)
EKGresults=st.slider("Select EKGresults=",0,2)
MaxHR=st.slider("Select MaxHR=",71,202)
ExerciseAngina=st.slider("Select ExerciseAngina=",0,1)
STdepression=st.slider("select STdepression=",0.0,6.2)
SlopeOfSt=st.slider("select SlopeOfSt=",1,3)
NumberOfVesselsfluro=st.slider("select NumberOfVesselsfluro=",0,3)
Thallium=st.slider("select Thallium=",3,7)

import pickle
model=pickle.load(open("Heart.pkl","rb"))
if st.button("Predict"):
    prd=model.predict([[Age,sex,ChestPainType,BP,Cholesterol,FBSover120,EKGresults,MaxHR,ExerciseAngina,STdepression,SlopeOfSt,NumberOfVesselsfluro,Thallium]])
    st.success("The heart is "+ prd[0])

