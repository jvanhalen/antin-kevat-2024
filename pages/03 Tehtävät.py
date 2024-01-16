import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Tehtävät",
    page_icon="👋",
    layout="wide"
)

st.markdown(
"""
# Tehtävät

Kurssi suoritetaan ratkomalla SQL-tehtäviä ja Tasks-tehtäviä. Molemmat osasuoritukset tehdään itsenäisesti kurssin materiaalin ja muiden lähteiden avulla. Kurssilla ei ole sallittua palauttaa toisen henkilön tai tekoälyn antamia vastauksia.

Kaikissa tehtävissä voit lähettää vastauksia uudestaan ilman rajoituksia eikä yritysten määrä vaikuta pisteisiin.

Kaikkien kurssin suoritusten deadline on su 10.3.2024 klo 23:59.

## SQL-tehtävät

Kurssin SQL-tehtävät suoritetaan [SQL Trainer](https://sqltrainer.withmooc.fi/) -järjestelmässä, jossa on 100 tehtävää SQL-kielen harjoitteluun. Saat yhden kurssipisteen jokaisesta tehtävästä.

Tehtävät 1–20 liittyvät materiaalin lukuun 2, tehtävät 21–40 liittyvät materiaalin lukuun 3 ja tehtävät 41–60 liittyvät materiaalin lukuun 4. Tehtävät 61–100 ovat vaikeampia tehtäviä, joissa yhdistellään kurssilla opittuja tekniikoita.

## Tasks-tehtävät

Tasks-tehtävät julkaistaan tammikuun loppuun mennessä.


""")


#Kurssin muut tehtävät palautetaan [Tasks](https://tasks.withmooc.fi/tikape-syksy-2023)-järjestelmään. Näet jokaisessa tehtävässä, montako pistettä saat tehtävästä.
#Kun lähetät vastauksen, saat automaattisesti pisteet tehtävästä. Kurssin henkilökunta käy läpi tehtävät kurssin jälkeen, mutta pisteesi eivät muutu, ellet ole tahallisesti kiertänyt automaattista tarkastusta.
#Viimeisessä tehtävässä on ohjeet kurssisuorituksen rekisteröintiin, ja voit tarkastaa kurssin pistetilanteen sekä antaa kurssipalautteen.
