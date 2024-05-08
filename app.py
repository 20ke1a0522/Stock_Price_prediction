import streamlit as st 
import pickle
import hydralit_components as hc

# menu_data = [
#     {'label':"Left End"},
#     {'label':"Book"},
#     {'label':"Component"},
#     {'label':"Dashboard"},
#     {'label':"Right End"},
# ]
# over_theme = {'txc_inactive': 'purple','menu_background':'red','txc_active':'yellow','option_active':'blue'}

# menu_id = hc.nav_bar(
#     menu_definition=menu_data,
#     override_theme=over_theme,
# )
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Select a page", ["Home", "About", "Contact"])

custom_css = """
<style>
body {
    background-image: url('download.jpeg');
    background-size: cover;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
model=pickle.load(open('model.pkl','rb'))


#menu = ["Google Stock","Amazon Stock"]
#choice = st.sidebar.selectbox("Menu",menu)


st.title("Stock Price Prediction")

H=st.text_input('Enter the High value:')
L=st.text_input('Enter the Low value: ')
O=st.text_input('Enter the Open value:')
V=st.text_input('Enter the volume values:')


if st.button('Predict'):
    H=float(H)
    L=float(L)
    O=float(O)
    V=float(L)

    data=[[H,L,O,V]]
    result=model.predict(data)
    st.success(result)
    st.write('Closing of Stock Value')