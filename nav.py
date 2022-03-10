import data_vis
import hipotesis
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Milestone 1 - Batch 009",
    page_icon=':scream_cat:',
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.github.com/fathiyahkhaq",
        'About': "**Milestone 1 - Phase 0**  \n Fathiyah kalamal Haq - Batch009"
    }
)

PAGES = {
    'Data Visualization': data_vis,
    'Hyphothesis Testing': hipotesis
}

selected = st.sidebar.selectbox('Select a Page', list(PAGES.keys()))
page = PAGES[selected]
page.app()