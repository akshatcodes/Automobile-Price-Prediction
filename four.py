import pickle
model = pickle.load(open('Four.pkl', 'rb'))
import streamlit as st

def development():
    string = "Price Predictor Application"
    st.set_page_config(page_title=string, page_icon="🚙")
    st.title("AUTOMOBILE PRICE PREDICTOR")
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaWwpwgPenA2c_wzM_dfZqVcwQ4PfcW5KNgQ&usqp=CAU",
         width=400,
    )
    st.markdown("#### Are You Planning to Sell Your Vehicle 🚗 ?")
    st.markdown("#### Come On !! Lets Evaluate The Price")
    st.write('')
    st.write('')

    Seller_Type_Individual = st.selectbox('Are you an individual or a vehicle dealer?', ('Individual','Car Dealer'), key='dealer')
    if (Seller_Type_Individual == 'Individual'):
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0

    years = st.number_input('In which year the vehicle was purchased ?', 1999, 2022, step=1, key='year')
    Years_old = 2022 - years
    Kms_Driven = st.number_input('What is distance completed by the vehicle ? (In Km) ', 0.00, 500000.00, step=500.00,
                                 key='drived')
    Present_Price = st.number_input('What is the current market price of the vehicle ?  (₹ Lakhs)', 0.00, 10000.00,
                                    step=0.5, key='present_price')
    Owner = st.radio("The number of owners the vehicle had previously ?", (0, 1, 2, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the vehicle ?', ('Petrol', 'Diesel', 'CNG'), key='fuel')
    if (Fuel_Type_Petrol == 'Petrol'):
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    elif (Fuel_Type_Petrol == 'Diesel'):
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    else:
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 0

    Transmission_Mannual = st.selectbox('What is the Transmission Type ?', ('Manual', 'Automatic'), key='manual')
    if (Transmission_Mannual == 'Mannual'):
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0

    if st.button("Estimate Price", key='predict'):
        try:
            Model = model
            prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel,
                                         Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0], 2)
            if output < 0:
                st.warning("SORRY !!! You will not be able to sell this vehicle !!")
            else:
                st.success("## CONGRATS !!!! 🥳🥳 \n## Now You Can Sell The Vehicle for {} Lakhs ".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")


if __name__ == '__main__':
    development()
