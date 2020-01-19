def repeat_stuff(stuff, num_repeats=10):
  return stuff*num_repeats
  
stuff = repeat_stuff("Row ", 3)

lyrics = (repeat_stuff("Row ", 3) + "Your Boat. ")

song = repeat_stuff(lyrics)

print(song)
