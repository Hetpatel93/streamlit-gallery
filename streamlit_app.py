import streamlit as st
import math
from PIL import Image

# Set up the page configuration
st.set_page_config(page_title="Discharge Rate Calculation", page_icon=":bar_chart:", layout="wide")

# Apply custom styles
st.markdown("""
    <style>
    body {
        background-image: url('background.jpg');  /* Use a relative path */
        background-size: cover;
        background-attachment: fixed; 
        background-position: center;
        margin: 0;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.8);
        color: #333;
    }
    .header {
        background-color: rgba(240, 237, 229, 0.9); 
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        color: #3C3C3C;
    }
    .footer {
        background-color: rgba(240, 237, 229, 0.9);
        color: #333;
        padding: 10px;
        text-align: center;
        position: fixed;
        bottom: 0;
        width: 100%;
        border-top: 1px solid #DDD;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='header'>Discharge Rate Calculation</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    d1 = st.number_input("Diameter 1 (mm):", value=1.0, format="%.2f") / 1000

with col2:
    d2 = st.number_input("Diameter 2 (mm):", value=1.0, format="%.2f") / 1000

h = st.slider("Head (m):", min_value=0.1, max_value=50.0, value=0.1, format="%.2f")

pi = math.pi
pi2 = pi / 4
A1 = (d1 ** 2)
a1 = pi2 * A1
A2 = (d2 ** 2)
a2 = pi2 * A2
cd = 0.66
g = 9.81
v = (2 * g * h)
V = v ** (1 / 2)
q1 = cd * A1 * A2 * V
p1 = (A1 ** 2)
p2 = (A2 ** 2)
d = (p1 - p2)
q2 = d ** (1 / 2)
flag = False

if d1 == d2:
    st.error("Diameter of both sections can never be the same!")
elif d1 < d2:
    st.error("Diameter-1 cannot be smaller than Diameter-2!")
elif q2 == 0 or q1 == 0 or h == 0:
    st.error("Diameter 2 cannot be zero")
else:
    Q = q1 / q2
    flag = True

def format_value(value):
    if value < 0.01:
        exponent = int(math.floor(math.log10(abs(value))))
        mantissa = value / (10 ** exponent)
        return f"{mantissa:.2f} X 10^{{{exponent}}}" 
    else:
        return f"{value:.2f}"

if flag:
    st.write(f"Discharge Rate (Q): {format_value(Q)}", " m^3/s")

st.header('Discharge Rate Formula')
st.latex(r'''
     Q_{th} = C_d \cdot a_1 \cdot a_2 \cdot \left\{\frac{\sqrt{2gh}}{\sqrt{a_1^2 - a_2^2}}\right\}
     ''')

# Add more latex explanations
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

# Ensure images are in the same directory as your script
images = [
    ("Venturi meter.png", "Venturi meter"),
    ("D2.png", "Diameter 1"),
    ("D1.png", "Diameter 2 (throat)"),
    ("H.png", "U-tube manometer"),
]

cols = st.columns(2)  

for i, (img_path, title) in enumerate(images):
    with cols[i % 2]:
        st.write(f"### {title}")
        st.image(img_path)

st.markdown("<h1 style='text-align: center;'>THANK YOU</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap'); 
    .footer {
        background: linear-gradient(to right, #ffffff, #e3e3e3, #ffffff);
        color: #333;
        padding: 15px;
        text-align: center;
        border-top: 1px solid #DDD;
        margin-top: 20px; 
        width: 100%; 
        box-sizing: border-box; 
        position: relative;
        font-family: 'Roboto', sans-serif; 
        font-weight: bold; 
        letter-spacing: 1px;
        text-transform: uppercase; 
    }
    </style>
    <div class='footer'>
        <p>By,</p><p> Het Patel, Mayank Patil, Umang Sanghavi, Jeet Panchal, Daksh Patel</p>
    </div>
    """, unsafe_allow_html=True)
