#!/usr/bin/env pyton
import os
import random
import player
import dungeon

#Program begin


def menu():
  
  varm=0
  while 1==1:

    os.system('clear')
    
    print "1.- Crear jugador";
    print "2.- Mostrar atributos de jugador"
    print "3.- Herir";
    print "0.- salir";
    
    if varm=="1":
      newplayer=player.player();
  
    elif varm=="2":
      newplayer.getatr();

    elif varm=="3":
      hitdmg=01;
      hitdmg=int(raw_input("input damage"));
      newplayer.hit(hitdmg)

    elif varm=="9":
      pass
    elif varm=="0":
      exit()
    elif not varm:
      print "Not a valid answer"
    else:
      print "Not a valid option"
    varm=raw_input("")

      
#Main loop
os.system('clear')
menu()