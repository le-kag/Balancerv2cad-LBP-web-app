import streamlit as st

def app():
    st.title('Home')

    st.write("""
    # Balancer Research Group - Initial Parameters of LBPs - Sensitivity Analysis
    By Chris Kagabe & Vasileios Panagiotidis
    """
    )

    st.write("""
    ### Using the balancerV2cad model we run a sensitivity analysis with cadCAD. Moreover we created a streamlit application that displays the results. With this tool we would like to help newcomers to easily get started with balancer and LBPs.
    """)

    st.image(
            'https://i.imgur.com/rkF7Vm9.png'
        )
    st.image(
            'https://i.imgur.com/XbafiLj.png',
        )
