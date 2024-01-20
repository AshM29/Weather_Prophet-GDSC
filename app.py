import streamlit as st
st.title('Weather Forecast')
st.write('This is a demo app')
with st.sidebar:
  st.write('This is a sidebar')
col1,col2=st.columns(2)
with col1:
   a=st.number_input('Enter a value',value=10)
with col2:
   b=st.text_input('Enter text')
   c=st.selectbox(label='Choose',options=[1,2,3])
sub=st.button(label='Submit')
if sub:
  st.write(a)
  st.write(b)
print(a)

  
