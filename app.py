import streamlit as st
from PIL import Image
from api_calling import issue_generator               

st.title("Code Debugger")
st.write("Upload the screenshot of your code to get hints or corrected code")
st.divider()

# sidebar
with st.sidebar:
    uploaded_image= st.file_uploader("Choose screenshot of your code",type=["jpg","jpeg","png"],accept_multiple_files=True)
    if uploaded_image:
        if len(uploaded_image)>3:
            st.error("You can upload at max 3 images")
        else :
            st.subheader("your uploaded images")
            col = st.columns(len(uploaded_image))
            for i,img in enumerate(uploaded_image):
                with col[i]:
                    st.image(img)
            images_list = []
            for img in uploaded_image:
                image = Image.open(img)
                images_list.append(image)
            
        
    soln = st.selectbox("Select solution type",
                        ("Hints","Solution with code"),
                        index=None)
    clicked = st.button("Debug Code",type="primary")

if clicked:
    if len(uploaded_image)==0 :
        st.error("You must upload screenshot of your code")
    elif soln is None:
        st.error("You must select a solution option")
    else:
        with st.container(border=True):
            st.header(f"Your {soln}")
            with st.spinner("Your code is debugging"):
                txt = issue_generator(images_list,soln)
                st.markdown(txt)
            