from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from geopy.geocoders import Nominatim
import folium

lm = LoginManager()
db = SQLAlchemy()

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Rio Grande do Norte, Natal, R. Jaguarari")
onco_e_vida = locator.geocode("R. Cônego Luiz Wanderley, 1317 - Lagoa Nova, Natal - RN")
acalanto_natal = locator.geocode("Natal - RN, , R. dr.Luís Coelho, 410")
aldeias_infantis = locator.geocode("Avenida do sol, 3258 Candelária, Natal - RN")
inst_bem_estar = locator.geocode("Av. Prudente de Morais, 507, Rio Grande do Norte, Natal")
ceap_rn = locator.geocode("Av.Duque de Caxias 191 Ribeira,Natal - RN")
gp_reviver = locator.geocode("Av. Miguel Castro - 612, Natal - RN")
inst_bem_viver = locator.geocode("Rua Sete de Setembro, nº 52, Kobrasol, São José, SC")
onco_e_vida_ext = locator.geocode("R. Barão de Melgaço, 3963 - Centro Norte, Cuiabá - MT")

mapc = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)

location_list = [
  {'link': 'https://oncoevida.org.br/','name' : 'Onco e Vida', 'data': onco_e_vida}, 
  {'link': 'https://projetoacalantonatal.com.br','name': 'Projeto Acalanto Natal', 'data': acalanto_natal}, 
  {'link': 'https://www.aldeiasinfantis.org.br/conheca/onde-estamos/no-brasil/natal','name': 'Aldeias Infantis','data': aldeias_infantis}, 
  {'link': 'http://www.institutodobem.org.br','name': 'Instituto do Bem Estar','data': inst_bem_estar}, 
  {'link': 'https://voluntarios.com.br/entidade/1952','name': 'Ceap-RN','data': ceap_rn}, 
  {'link': 'https://www.gruporeviver.com','name': 'Grupo Reviver','data': gp_reviver}, 
  {'link': 'https://pt-br.facebook.com/institutobemviver/','name': 'Instituto bem viver','data': inst_bem_viver},
  {'link': 'https://institutociranda.org.br','name': 'Onco e Vida','data': onco_e_vida_ext}
]

for loc in location_list:
  folium.Marker(
    location=[loc['data'].latitude, loc['data'].longitude],
    popup=f"""
      <i>{loc['name']}</i><br>
      <a href='{loc['link']}' target='_blank'>Acesse aqui</a>
    """,
    tooltip="Click here!",
    icon=folium.Icon(color="purple")
  ).add_to(mapc)

map_html = mapc._repr_html_()