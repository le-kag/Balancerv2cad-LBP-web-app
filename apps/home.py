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

    st.write("For further information on our research, read our HackMD available here: [link](https://hackmd.io/00CXctAPTZmHWSjBmbXtgw?view)")

    col1, col2 = st.beta_columns(2)

    with col1:
        st.write("""

        """)
        st.image(
                'https://i.imgur.com/rkF7Vm9.png'
            )

    with col2:
        st.write("""

         """)
        st.image(
            'https://i.imgur.com/XbafiLj.png'
            )
