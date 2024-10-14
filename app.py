import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/download.jfif")
img_lottie_animation = Image.open("images/download2.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Gomathy :wave:")
    st.title("A Nutritionist  From India")
    st.write(
        "I specialize in promoting health and wellness through personalized dietary planning and education. With a strong background in food science and human nutrition, I work closely with clients to assess their nutritional needs and develop tailored meal plans that align with their health goals, whether it’s weight management, improving energy levels, or managing chronic conditions."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - Assess - Evaluating dietary habits and nutritional needs.
            - Counsel - Providing guidance and support for dietary changes.
            - Plan - Developing personalized meal plans.
            - Educate - Teaching clients about nutrition and healthy eating."
            - Support - Offering ongoing motivation and encouragement.
            - Analyze - Reviewing food intake and nutrient levels.
            - Advocate - Promoting healthy lifestyle choices.
            - Collaborate - Working with other healthcare professionals.
            - Inspire - Encouraging clients to adopt healthier habits.

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("What is nutrition")
        st.write(
            """
                Nutrition is the science that studies how food affects the body and influences health. It involves the intake of essential nutrients, such as vitamins, minerals, carbohydrates, proteins, and fats, necessary for growth, energy, and overall well-being. Proper nutrition supports bodily functions, prevents diseases, and promotes a healthy lifestyle
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("World Nutrition Week")
        st.write(
            """
                World Nutrition Week is an annual observance dedicated to raising awareness about the importance of nutrition for overall health and well-being. It highlights the role of proper dietary practices in preventing malnutrition and promoting healthy lifestyles. Events and campaigns during this week aim to educate the public and encourage positive changes in eating habits worldwide.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/grinstagram123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
