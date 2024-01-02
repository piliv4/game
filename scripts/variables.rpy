label defineCharacters:
  
  #DEFINE CHARACTERS

  $ mc = PersonMC( Character(""),"", "", "", 0 , "" )

  $ incognito = Person( Character ("???"), "", "", "",20)

  $ bazooka =  PersonPL( Character("Bazooka"),"bazookalias", "Bazooka", "Bazkoare", 22, 50)

  $ panero =  PersonPL( Character("Pan"),"Panalias", "Melnik", "Panero", 21, 50)  

  $ joseluis = PersonPL( Character("Lolero"),"loleralias", "Jose Luis", "García", 19, 50)

  return

# · DEFINE IMAGES ·

image negro = "negro.png"
#DEFINE BACKGROUNDS(BG)

image bg_fuego = "bg_clase_con_fuego.png" 

image bg_patio = "bg_exterior.png"

image bg_patio_medicos = "bg_medicos_en_upv.png"

#DEFINE CHARACTERS/PERSONAJES (CH/PJ)

image ch_bazooka = "bazooka_idle.png"

image ch_jl_happy = "sprite_jl_contento.png"

image ch_jl_blush = "sprite_jl_sonrojado.png"

image ch_jl_surprised = "sprite_jl_sorprendido.png"

image ch_jl_think = "sprite_jl_pensando"

#DEFINE SCENES (SC)

image sc_tetaspan ="sc_tetaspan.png"

image sc_tetaspanborrosas = "sc_tetaspanborrosas.png"

#DEFINE OPTIONS

#chapter 0


label option_1:
  #añadir sprite Jose Luis avergonzadao
  joseluis.character "Ay madre, qué vergüenza"
  
  joseluis.character "Te debo estar dando una primera impresión terrible."
  return


label option_2:
  show ch_jl_surprised

  joseluis.character "¿No sabes qué es el LoL?"

  hide ch_jl_surprised

  #añadir sprite Jose Luis mansplaining

  joseluis.character "League of Legends, también conocido por sus siglas LoL, es un videojuego multijugador de arena de batalla en línea desarrollado y publicado por Riot Games que se caracteriza por…"

  #añadir sprite Jose Luis avergonzado

  joseluis.character "Estoy hablando demasiado..."
  return

label option_3:
  show ch_jl_happy

  joseluis.character "¡Me alegro!"
  
  hide ch_jl_happy
  return
  
label option_4:
  show ch_jl_think

  joseluis.character "Qué mal"

  hide ch_jl_think
  return

label option_5:
  bazooka.character "Te odio"
  return
  
label option_6:
  bazooka.character "ZAAAAAMNNNN"
  return
