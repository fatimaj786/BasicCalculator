# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to a Basic Calculator')

# TAKE WEIGHT INPUT in kgs
getFNumber = st.number_input("Enter your first number", format='%f')
getSNumber = st.number_input("Enter your second number", format='%f')
getOperator = st.selectbox('Select an operation', ('Addition', 'Subtraction', 'Multiplication', 'Division'))

result = None
# calculation
if getOperator == 'Addition':
    result = getFNumber + getSNumber
elif getOperator == 'Subtraction':
    result = getFNumber - getSNumber
elif getOperator == 'Multiplication':
    result = getFNumber * getSNumber
elif getOperator == 'Division':
    if number2 != 0:
        result = getFNumber / getSNumber
    else:
        result = 'Error! Division by zero.'

# check if the button is pressed or not
if st.button('Calculate'):
    # print the BMI INDEX
    st.text("Your ans is {}.".format(result))

# Display result
st.write('The result is:', result)
