import streamlit as st

st.set_page_config(page_title='BMI Calculation', page_icon='👨🏼‍⚕️', layout='centered')
st.title('💪🏻 BMI Calculator')
st.write("Let's Calculate Your **BODY MASS INDEX [BMI] And Understand What It Means")

st.header('ℹ️ Enter Your Details')

height = st.number_input('Enter Your Height (in cm) ', min_value=90,max_value=200,value=170)
weight = st.number_input('Enter Your Weight (in kg) ', min_value=10,max_value=200,value=65)

st.write(f"🎢 Your Height : {height} in cm")
st.write(f"🗿 Your Weight : {weight} in cm")

if st.button('Calculate BMI'):
    h_m = height / 100 # converting cm to m
    bmi = weight/ (h_m**2) # calculate the BMI 
    st.success(f"Your BMI Is **{bmi :.2f}**")

    #print BMI Category
    if bmi < 18.5:
        category = 'Underweight🥲'
        color = '#efee02'
    elif 18.5 <=  bmi < 25:
        category = 'Normal 😄'
        color = '#1db410'
    elif 25 <= bmi < 30:
        category = 'Overweight 🫣'
        color = '#d45363'
    else:
        category = 'Obese 😰'
        color = '#d70c25'

    st.write(category)

    st.markdown(
        f"""
        <div style='background-color:{color};padding:15px;border-radius:10px;text-align:center'>
        <h3>Your BMI Category : {category}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )