import numpy as np
import json
import pandas as pd
import requests as req
import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static1.moviewebimages.com/wordpress/wp-content/uploads/2022/04/star-wars-jedi-dont-use-force-enough-featured-image-Cropped.jpg?q=50&fit=contain&w=1140&h=&dpr=1.5");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()




######################################################

# names = ['Luke Skywalker', 'C-3PO', 'R2-D2', 'Darth Vader', 'Leia Organa', 'Owen Lars',
# 'Beru Whitesun lars', 'R5-D4', 'Biggs Darklighter', 'Obi-Wan Kenobi', 'Anakin Skywalker',
# 'Wilhuff Tarkin', 'Chewbacca', 'Han Solo', 'Greedo', 'Jabba Desilijic Tiure', 'Wedge Antilles',
# 'Jek Tono Porkins', 'Yoda', 'Palpatine', 'Boba Fett', 'IG-88', 'Bossk', 'Lando Calrissian',
# 'Lobot', 'Ackbar', 'Mon Mothma', 'Arvel Crynyd', 'Wicket Systri Warrick', 'Nien Nunb',
# 'Qui-Gon Jinn', 'Nute Gunray', 'Finis Valorum', 'Padmé Amidala', 'Jar Jar Binks', 'Roos Tarpals',
# 'Rugor Nass', 'Ric Olié', 'Watto', 'Sebulba', 'Quarsh Panaka', 'Shmi Skywalker', 'Darth Maul',
# 'Bib Fortuna', 'Ayla Secura', 'Ratts Tyerel', 'Dud Bolt', 'Gasgano', 'Ben Quadinaros',
# 'Mace Windu', 'Ki-Adi-Mundi', 'Kit Fisto', 'Eeth Koth', 'Adi Gallia', 'Saesee Tiin',
# 'Yarael Poof', 'Plo Koon', 'Mas Amedda', 'Gregar Typho', 'Cordé', 'Cliegg Lars',
# 'Poggle the Lesser', 'Luminara Unduli', 'Barriss Offee', 'Dormé', 'Dooku', 'Bail Prestor Organa',
# 'Jango Fett', 'Zam Wesell', 'Dexter Jettster', 'Lama Su', 'Taun We', 'Jocasta Nu', 'R4-P17',
# 'Wat Tambor', 'San Hill', 'Shaak Ti', 'Grievous', 'Tarfful', 'Raymus Antilles', 'Sly Moore',
# 'Tion Medon']

# planets = ['Tatooine','Alderaan','Yavin IV','Hoth','Dagobah','Bespin','Endor','Naboo','Coruscant','Kamino','Geonosis',
# 'Utapau','Mustafar','Kashyyyk','Polis Massa','Mygeeto','Felucia','Cato Neimoidia','Saleucami','Stewjon', 'Eriadu', 'Corellia',
# 'Rodia','Nal Hutta','Dantooine','Bestine IV', 'Ord Mantell', 'unknown', 'Trandosha','Socorro','Mon Cala',
# 'Chandrila','Sullust','Toydaria', 'Malastare','Dathomir', 'Ryloth', 'Aleen Minor', 'Vulpter', 'Troiken',
# 'Tund', 'Haruun Kal', 'Cerea', 'Glee Anselm', 'Iridonia', 'Tholoth', 'Iktotch', 'Quermia', 'Dorin', 'Champala',
# 'Mirial', 'Serenno', 'Concord Dawn', 'Zolan', 'Ojom', 'Skako', 'Muunilinst', 'Shili', 'Kalee','Umbara']

# species = ['Human', 'Droid', 'Wookie', 'Rodian', 'Hutt', "Yoda's species", 'Trandoshan', 'Mon Calamari',
# 'Ewok', 'Sullustan', 'Neimodian', 'Gungan', 'Toydarian', 'Dug', "Twi'lek", 'Aleena', 'Vulptereen', 'Xexto',
# 'Toong', 'Cerean', 'Nautolan', 'Zabrak', 'Tholothian', 'Iktotchi', 'Quermian', 'Kel Dor', 'Chagrian', 'Geonosian',
# 'Mirialan', 'Clawdite', 'Besalisk', 'Kaminoan', 'Skakoan', 'Muun', 'Togruta', 'Kaleesh', "Pau'an"]

# starships = ['CR90 corvette', 'Star Destroyer', 'Sentinel-class landing craft', 'Death Star', 'Millennium Falcon',
# 'Y-wing', 'X-wing', 'TIE Advanced x1', 'Executor', 'Rebel transport', 'Slave 1', 'Imperial shuttle', 'EF76 Nebulon-B escort frigate',
# 'Calamari Cruiser', 'A-wing', 'B-wing', 'Republic Cruiser', 'Droid control ship', 'Naboo fighter', 'Naboo Royal Starship', 'Scimitar',
# 'J-type diplomatic barge', 'AA-9 Coruscant freighter', 'Jedi starfighter', 'H-type Nubian yacht', 'Republic Assault ship', 'Solar Sailer',
# 'Trade Federation cruiser', 'Theta-class T-2c shuttle', 'Republic attack cruiser', 'Naboo star skiff', 'Jedi Interceptor',
# 'arc-170', 'Banking clan frigte', 'Belbullab-22 starfighter', 'V-wing']


# vehicles = ['Sand Crawler', 'T-16 skyhopper', 'X-34 landspeeder', 'TIE/LN starfighter', 'Snowspeeder',
# 'TIE bomber', 'AT-AT', 'AT-ST', 'Storm IV Twin-Pod cloud car', 'Sail barge', 'Bantha-II cargo skiff',
# 'TIE/IN interceptor', 'Imperial Speeder Bike', 'Vulture Droid', 'Multi-Troop Transport', 'Armored Assault Tank',
# 'Single Trooper Aerial Platform', 'C-9979 landing craft', 'Tribubble bongo', 'Sith speeder', 'Zephyr-G swoop bike',
# 'Koro-2 Exodrive airspeeder', 'XJ-6 airspeeder', 'LAAT/i', 'LAAT/c', 'AT-TE', 'SPHA', 'Flitknot speeder',
# 'Neimoidian shuttle', 'Geonosian starfighter','Tsmeu-6 personal wheel bike', 'Emergency Firespeeder', 'Droid tri-fighter',
# 'Oevvaor jet catamaran', 'Raddaugh Gnasp fluttercraft', 'Clone turbo tank', 'Corporate Alliance tank droid', 'Droid gunship', 'AT-RT']

# films = ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith']



st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

col1, mid, col2 = st.columns([80,40,80])
with col1:
    pick = st.selectbox('“Your path you must decide“ - Yoda', ['Make a choice', 'People', 'Planets', 'Species', 'Starships', 'Vehicles', 'Films'])
    if pick == "Make a choice":
        pick = ""



cat = pick
if cat == "films":
    cat = "title"
else:
    cat ="name"


######################################################

# CI DESSOUS LES FONCTIONS QUI M'ONT PERMIS DE RECUPERER LES LISTES

site = "https://swapi.dev/api/"

all_urls = []
names = []

def get_url(page, sel):
    right_url = page+sel.lower()
    url = req.get(right_url).json()
    if right_url not in all_urls:
        all_urls.append(right_url)
    return url


if "next" not in get_url(site, pick):
    next_ = None
    all_urls = "https://swapi.dev/api/"
else:
    next_ = True
    next_url = site + pick
    if next_url not in all_urls:
        all_urls.append(next_url)


while next_:
    urls = req.get(next_url).json()
    if urls["next"] != None:
        next_url = urls["next"]
        all_urls.append(next_url)
    else:
        next_ = False

def get_name(url_list):
    if url_list == "https://swapi.dev/api/":
        pass
    else:
        for page in url_list:
            url = req.get(page).json()["results"]
            for i in range(len(url)):
                names.append(url[i][cat])
        pass

get_name(all_urls)


with col2:
    inp = pick
    if inp == "People":
        inp = st.selectbox('“You will find only what you bring in.“ - Yoda', names)
    elif inp == "Planets":
        inp = st.selectbox('“You will find only what you bring in.“ - Yoda', names)
    elif inp == "Species":
        inp = st.selectbox('“You will find only what you bring in.“ - Yoda', names)
    elif inp == "Starships":
        inp = st.selectbox('“You will find only what you bring in.“ - Yoda', names)
    elif inp == "Vehicles":
        inp = st.selectbox('“You will find only what you bring in.“ - Yoda', names)
    elif inp == "Films":
        inp = st.selectbox('“You will find only what you bring in.“ - Yoda', names)

def category(pick, inp):
    if pick == "Make a choice":
        return None
    elif inp == "":
        return None
    choice = pick.lower()
    url = f"https://swapi.dev/api/{choice}/?search={inp}"
    response = req.get(url).json()
    infos = response["results"]
    result = []
    for info in infos:
        result.append(info)
    return st.write(result)

st.write(category(pick, inp))
