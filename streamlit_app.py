import streamlit as st
import math
from PIL import Image

# Set up the page configuration
st.set_page_config(page_title="Flow Rate Calculation", page_icon=":bar_chart:", layout="wide")

# Apply custom styles
st.markdown("""
    <style>
    body {
        background-image: url('C:/Users/Het/Desktop/background.jpg'); /* Use correct file path */
        background-size: cover; /* Cover the entire background */
        background-attachment: fixed; /* Fix the background */
        background-position: center; /* Center the background image */
        margin: 0; /* Remove default margins */
    }
    .main {
        background-color: rgba(255, 255, 255, 0.8); /* Adjust transparency of main content */
        color: #333;
    }
    .header {
        background-color: rgba(240, 237, 229, 0.9); /* Slightly transparent header */
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        color: #3C3C3C;
    }
    .footer {
        background-color: rgba(240, 237, 229, 0.9); /* Slightly transparent footer */
        color: #333;
        padding: 10px;
        text-align: center;
        position: fixed;
        bottom: 0;
        width: 100%;
        border-top: 1px solid #DDD;
    }
    .content {
        padding: 20px;
    }
    .image-container {
        margin-bottom: 20px;
    }
    .image-container img {
        width: 100%;
        max-width: 600px;
        border-radius: 8px;
    }
    .footer p {
        margin: 5px;
    }
    /* Custom style for input boxes */
    .css-1y4p8pa input {
        background-color: #CACACA; /* Input box color */
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>Flow Rate Calculation</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    d1 = st.number_input("Diameter 1 (m):", value=1.0, format="%.5f")

with col2:
    d2 = st.number_input("Diameter 2 (m):", value=1.0, format="%.5f")

# Slider for Head (m)
h = st.slider("Head (m):", min_value=0.0, max_value=50.0, value=0.1, format="%.2f")

pi=math.pi
pi2=pi/4
A1=(d1**2)
a1=pi2*A1
A2=(d2**2)
a2=pi2*A2
cd=0.66
g=9.81
v=(2*g*h)
V=v**(1/2)
q1=cd*A1*A2*V
p1=(A1**2)
p2=(A2**2)
d=(p1-p2)
q2=d**(1/2)


if q2 == 0 or q1==0 or h==0 :
    Q = "0"
else:
    Q = q1 / q2
st.write(f"Flow Rate Ratio (Q): {Q}", format="%.5f")

st.header('Flow Rate Formula')
st.latex(r'''
     Q_{th} = C_d \cdot a_1 \cdot a_2 \cdot \left\{\frac{\sqrt{2gh}}{\sqrt{a_1^2 - a_2^2}}\right\}
     ''')

st.write("### Where,")
st.latex(r'''
Q_{th} = \text{Discharge measurement}
''')

st.latex(r'''
a_1 = \text{Area of pipe}
''')

st.latex(r'''
a_2 = \text{Area of throat}
''')

st.latex(r'''
h = \text{Pressure head}
''')

st.latex(r'''
C_d = 0.66 \, \text{(Discharge coefficient)}
''')

st.latex(r'''
g = 9.81 \, \text{m/s}^2 \, \text{(Acceleration due to gravity)}
''')

st.header('Venturimeter Used to Measure Flow Rate')

# Image section
images = [
    ("Venturi meter.png", "Venturi meter"),
    ("D2.png", "Diameter 1"),
    ("D1.png", "Diameter 2 (throat)"),
    ("H.png", "U-tube manometer"),
]

# Create columns based on the number of images
cols = st.columns(2)  # Adjust the number of columns as needed

for i, (img_path, title) in enumerate(images):
    with cols[i % 2]:  # Alternate between columns
        st.write(f"### {title}")
        st.image(img_path)

# Thank you section
st.markdown("<h1 style='text-align: center;'>THANK YOU</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap'); /* Import Roboto font */
    
    .footer {
        background: linear-gradient(to right, #ffffff, #e3e3e3, #ffffff); /* Gradient from white to gray to white */
        color: #333; /* Dark gray text */
        padding: 15px;
        text-align: center;
        border-top: 1px solid #DDD;
        margin-top: 20px; /* Margin to create space above the footer */
        width: 100%; /* Ensure footer spans full width */
        box-sizing: border-box; /* Include padding in width calculation */
        position: relative; /* Ensure the footer behaves as part of the normal document flow */
        font-family: 'Roboto', sans-serif; /* Change font to Roboto */
        font-weight: bold; /* Make text bold */
        letter-spacing: 1px; /* Adjust letter spacing for a distinctive look */
        text-transform: uppercase; /* Transform text to uppercase */
    }
    </style>
    <div class='footer'>
        <p>By,</p><p> Het Patel, Mayank Patil, Umang Sanghvi, Jeet Panchal, Daksh Patel</p>
    </div>
    """, unsafe_allow_html=True)
