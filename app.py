import streamlit as st
from multiapp import MultiApp
from apps import home, model_1, model_2, model_3, model_4, model_5, model_6 # import your app modules here

app = MultiApp()

st.markdown("""
# Balancerv2cad Web App


""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Simulation 1", model_1.app)
app.add_app("Simulation 2", model_2.app)
app.add_app("Simulation 3", model_3.app)
app.add_app("Simulation 4", model_4.app)
app.add_app("Simulation 5", model_5.app)
app.add_app("Simulation 6", model_6.app)
# The main app
app.run()
