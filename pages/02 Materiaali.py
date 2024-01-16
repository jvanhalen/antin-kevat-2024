from st_pages import Page, show_pages, add_page_title
import streamlit as st
import glob
from pathlib import Path

st.set_page_config(
    page_title="Materiaali",
    page_icon="👋",
    layout="wide"
)

st.markdown("""
# Materiaali

Tämän sivuston verkkomateriaali riittää kurssin suorittamiseen. Materiaalin tekijä on Antti Laaksonen ja löydät materiaalin lähdekoodin [GitHubista](https://github.com/hy-tikape/kevat-2024).

Tietokannan käyttäjälle tärkeä lähde ovat tietokantojen dokumentaatiot, joissa kerrotaan tarkasti niiden ominaisuuksista:

* [SQLite-dokumentaatio](https://www.sqlite.org/docs.html)
* [PostgreSQL-dokumentaatio](https://www.postgresql.org/docs/)

Jos haluat oppia myöhemmin lisää tietokantoja käyttävien järjestelmien suunnittelusta, yksi hyvä kirja on seuraava:

* Martin Kleppmann:
_Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems_
""")

st.sidebar.header("Navigointi")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
course_dir = current_dir / "_material" / "**"  # "**" stands for all the subdirectories (also hidden)

file_pattern = '*.md'  # Change the pattern based on your requirements

# Use glob.glob() to get a list of files matching the pattern
files = glob.glob(f"{course_dir}/{file_pattern}", recursive=True)


### PARSERI

def extract_anchor_links(markdown_text: str) -> str:
    """Extract anchors from Markdown text
    Args:
        markdown_text (str): Markdown text to be extracted
    Returns:
        str: A list of anchors in Markdown format
    """
    import re
    target_levels = ['#', '##']  # Voit määrittää halutut tasot tähän
    pattern = re.compile(r'^(#+)\s+(.+)', flags=re.MULTILINE)
    matches = pattern.findall(markdown_text)
    # Generate anchor and remove/change illegal characters
    # This doesn't work as Streamlit generates "random anchors" where umlauts exists.
    markdown_anchors = [f"[{heading}](#{heading.lower().replace(' ', '-').replace('.', '').replace('ä', '').replace('ö', '').replace('å', '')})" for level, heading in matches if level in target_levels]
    return markdown_anchors


def add_anchors_to_sidebar(markdown_anchors: str) -> None:
    """Add anchors to Streamlit sidebar

    Args:
        markdown_anchors (str): List of anchors in Markdown format
    """
    for anchor in markdown_anchors:
        st.sidebar.markdown(anchor, unsafe_allow_html=True)

# Print the list of matching files
files.sort()

for file_path in files:
    print(file_path)
    with open(file_path, 'r') as file:
        content = file.read()
        add_anchors_to_sidebar(extract_anchor_links(content))
        st.markdown(content, unsafe_allow_html=True)
