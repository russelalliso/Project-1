#Allison Russell & Emilyn Cawlfield
#B5
#Project 1

#Welcome- plan is to write a short choose-your-own-adventure story. User can choose which direction the story takes without all those annoying page turns.


def ShortStory(userName):

  print("Welcome to our short story adventure, %s. Would you like to play?"%(userName))
  play = input()
  play = play.lower()
  if play == "yes" or play == "y" or play == "sure":
    adventure = True
  else:
    print("Okay, goodbye.")
    return


  health = 0
  ending = 0

  while True:
    #Story beginning
    print("""
      You’ve been working for Rocky Research Lab for a while now and you’ve finally been assigned a project. It requires you to travel to a mysterious jungle for some field research on Endangered Bornean Flat-Headed Frogs. Though you are sad to leave your desk and shiny nametag that says "Dr Melvin Vizsla", you are excited for an adventure. The plane landed in Indonesia yesterday, and after a good night of sleep and some great food, you are ready to begin your adventure. You first gather all your gear and head out further into the jungle. Shifting your glasses, you prepare to take your first step into the dense wood. But then you realize you have no idea where you're going. You remember someone saying that the only way to find things is to get lost (though that might have been from a movie), so you go in anyways. You end up just walking around aimlessly and just like that movie said, you get lost. Though it seems okay at first, it gets super scary once the sun sets, and you come to your first big decision. 
      Choice 1:
      Do you set up camp, get some sleep, and wait the night out? (type 1)
      Or do you keep on walking? (type 2)
      """)
    
    
    
    choice1 = int(input(""))
    
    #Choice 1
    
    
    if choice1 == 1:
      print("""
      So you decided to set up camp, get some sleep, and wait out the night. So, you set up your camp and once your head hits the pillow you fall asleep instantly. Unfortunately, your sleep is rather rudely interrupted by a jaguar, and you wake up to claws slicing through the fabric of your tent. You quickly get up and run, leaving your tent behind but swinging your backpack on as you attempt to escape. You run as fast as you can but you come to a fork in the trail and reach your second big choice.
      Choice 2:
      Do you run left? (type 3)
      Or Do you run right? (type 4)
      """)
      choice2 = int(input(""))
    elif choice1 == 2:
      print("""
      So, you decided to keep on walking. It gets dark, really fast but you just keep walking. You don’t know exactly what you’re looking for but you think the farther into the forest you get the better chance of finding the frog you’re supposed to research. The sun starts to rise and your feet become numb so you wonder if you should stop and rest.
      """)
      choice2 = int(input("Choice 2: \nDo you stop and rest?(type 20)\nContinue walking?(type 2)\nOr get some food out to give you more energy?(type 1) \n"))
    else:
      print("That is not a valid choice. In choosing to do neither, you just stand there awkwardly. It is no surprise when a jaguar finds you, and you are eaten alive. \nTHE END")
      break
    
    
    #Choice 2 1+2
    while choice2 == 20:
      health += 1
      choice2 = int(input("You rest for a few minutes. Do you want to continue resting (type 20), eat something (type 1), or begin to walk again? (type 2) \n"))

    if choice2 == 1:
      #eat something
      print("You eat a granola bar that you kept with your camping supplies before continuing to walk. As you journey, you come to a fork in the road.")
      health += 2
      choice3 = int(input("Choice 3: \nDo you go left and continue to follow the widest and most travelled path so you don't get so lost that you can't find your way back out of the jungle? (type 4) \nDo you go straight towards the trees that look like just the right type of habitat for frogs? (type 5)\nOr do you go right, towards a downhill stretch of path that looks like an easy way to go given how tired you are? (type 6)\n"))
    elif choice2 == 2:
      #walk
      print("You decide to keep walking through the dense jungle though your feet ache. However, you are too tired to take your camping supplies with you, so you leave them all behind. You continue for about an hour, then stop again. Your stomach yearns for a bite of food. After sitting in misery for a couple minutes, wishing you had eaten earlier, your hunger motivates you to get back up and walk just a bit more to find something edible.")
      choice3 = 0
    elif choice2 == 3:
      #complete
      ending = 1
      break
    elif choice2 == 4:
      print("""
      You run right, and soon you are hacking your way through dense undergrowth. After running for awhile you think you have lost the jaguar. You hear twigs snap behind you, you turn around, and the jaguar is there, snarling. You stumble backwards but the ground underneath your feet gives way and you find yourself falling. You’re falling fast, you can feel your heart beating. All of a sudden, the ground curves, and you find yourself on a very intense slide. You are trying to find a way to stop yourself but you can’t. Unfortunately, the ground drops away and you find yourself free falling once again, but this time you hear water in the distance and soon plunge deep into an underground lake. Once you resurface you have a decision to make.
      """)
      choice3 = int(input("Choice 3: \nDo you climb back up the way you came? (type 1) \nDo you explore this strange underground world?  (type 2) \nOr do you stop and rest for a moment? (type 3)\n"))
    else:
      if choice1 == 1:
        print("That is not a valid choice. You hesitate, racked with terror. That is enough for the jaguar to catch up to you and eat you. \nTHE END")
      else:
        print("That is not a valid choice. In choosing to do nothing, you quickly expire. The jungle is not a place where indecisive people survive. \nTHE END")
      break

    #Choice 3 1,2,3,+4
    if choice3 == 1:
      print("""
      You choose to climb up the way you came. At first you try to climb up the dirt to get back up to the hole you fell out of but the dirt is wet so you just keep slipping. But then you see rocks that are dry and look easy to climb. So you walk over there and start climbing the rocks. You finally make it to the hole you fell out of. You start climbing up the hole, and at last, you made it to the top. The jaguar isn't anywhere to be seen so you sit down and come to your next decision.
      """)
      choice4 = int(input("Choice 4: \nDo you find somewhere to take a nap and sleep for a little bit? (type 1) \nOr do you continue to walk in hope of finding food?(type 2) \n"))
    elif choice3 == 2:
      print("""
      Choosing to explore right away, you look around and find yourself in a vast network of tunnels snaking around under the earth. You pick a tunnel at random and begin to walk. It gets very dark, all of your matches are wet, and your flashlight isn’t turning on. Your next choice is here.
      """)
      choice4 = int(input("Choice 4: \nDo you go back to the lake, set down your stuff, and wait for it to dry? (type 5) \nOr do you keep exploring without light? (type 6) \n"))
    elif choice3 == 3:
      print("You decide to catch your breath, and so you sit down beside the lake. Thinking about life back home, you soon find you are getting sleepy, and realize you have another choice before you.")
      choice4 = int(input("Choice 4: \nDo you let yourself fall asleep? (type 8) \nOr do you try to explore this underground tunnel network? (type 7) \n"))
    elif choice3 == 4:
      print("You decide to take the path to the left, a well-used path that you know will make it easy for you to go back the way you came. However, what you forget is that paths in this part of the jungle are not made by humans. A jaguar, awaiting the prey that so frequently uses this path, greets you with a snarl as you walk around a corner.")
      print("Choice 4: \nDo you play dead and hope that the jaguar leaves you alone? (type 10)")
      if health >= 6:
        print("Do you pick up a nearby rock and throw it towards the jaguar so that you can daze it and maybe escape? (type 11) \nDo you throw your phone (which doesn't have service since you are in the jungle, and so is basically useless, and quicker to grab than a rock but may be less effective) at the jaguar? (type 12)")
      elif health > 2:
        print("Do you throw your phone (which doesn't have service this deep in the jungle and so is basically useless) at the jaguar to daze it so you can escape? (type 12)")
      else:
        print("Do you stand very still and hope that the jaguar thinks that you are a tree? (type 13)")
      print("Or do you run as fast as possible away from the jaguar? (type 14)")
      choice4 = int(input(""))
    elif choice3 == 5:
      print("You decided to go straight, towards the trees that look like just the right habitat for frogs You start to look around in the tree, but you realize you can see anything so you start climbing up into the tree. You think you see a frog but its on a really skinny branch. So you come to a decision.")
      choice4 = int(input("Choice 4: \nDo you climb over on to the skinny branch?(type 4) \nDo you climb down and figure out a different way?(type 3) \nOr do you leave the frog alone and find a differnt one somehwhere else?(type 9)"))
    elif choice3 == 6:
      print("You decide to take the path on the right, and begin an easygoing descent.")
      ending = 2
      break
    elif choice3 == 0:
      choice4 = 0
    else:
      print("That is not a valid choice. In choosing to do nothing, you quickly expire. The jungle is not a place where indecisive people survive. \nTHE END")
      break

    #Choice 4 1,2,3,4,5,6,7,+8
    if choice4 == 1:
      print("You decide to sleep, so you lay down and enjoy several hours of sleep. However, this was a mistake. The sounds of the jungle around you infiltrate your dreams and you soon find yourself in a nightmare. You wake up in a panic and before you can think rationally you run.")
      ending = 7
      break
    elif choice4 == 2 or choice4 == 0:
      print()
      ending = 6
      break
    elif choice4 == 3:
      print("So you decided to climb down and figure out a different way. Once you are back on the ground you look around in hope of finding some other way to get to the frog, which isn't as easy as you thought it was going to be. You find some wood so you might be able to build a ladder or you can try to climb the tree next to the other tree with the frog, and hope you can reach it. So what do you do?")
      choice5 = int(input("Choice 5: \nDo you build a ladder out of the wood you found and the rope you have?(type 5) \nOr do you climb the other tree?(type 6)"))
    elif choice4 == 4:
      print("You decided to climb the skinny branch to get to the frog. You start to make your way very slowly, keeping in mind that this tree is very high up. You are almost to the frog when you hear a tiny crack. You turn your head to see the branch about to snap of the tree. You scamble and try to get back to the trunk of the tree. But, it was too late the branch snapped of and you fell with it.")
      ending = 5
      break
    elif choice4 == 5:
      print("You choose to return to the lake to let your supplies dry. As you lay everything out, you wonder where you are. Exhausted from everything that you have been through, it's no surprise when you fall asleep.")
      ending = 3
      break
    elif choice4 == 6:
      print("""
      You keep walking, feeling along the tunnel walls, hoping you don’t unwittingly walk into something dangerous. You continue on in silence, walking for what feels like hours but is probably only minutes, when suddenly your hand runs into something protruding from the tunnel wall. You feel it, curious, and learn that it is square shaped (strangely enough). Your back itches, so you decide to use it as a back scratcher and begin to do so when it falls back into the wall and you realize that the entire tunnel is rising, and fast.
      """)
      ending = 4
      break
    elif choice4 == 7:
      print("You decide to explore the underground tunnels. Searching in your bag, you find your matches. They were wet before, because of your unwilling plunge into the lake, but now they are mostly dry. You light a torch that you see on a nearby wall (though you wonder how it got there), and begin to explore. Soon you come across what looks very much like a puzzle. From what you’ve seen in movies, this is the type of puzzle where you can step on some floor tiles but others mean certain death. You reach your next big decision.")
      choice5 = int(input("Choice 5: \nDo you try to run through it as fast as possible? (type 1) \nOr do you try to work your way slowly through the puzzle? (type 2) \n"))
    elif choice4 == 8:
      print("You choose to let yourself succumb to your sleepiness.")
      ending = 3
      break
    elif choice4 == 9:
      print("You decided to let this frog go and try to find a different one. So you're walking around of somewhat of the same area and you spot a big spot with the trees that you were looking for. But you can either got left or right. Which way do you go?")
      choice5 = int(input("Choice 5:\nDo you go left?(tpye 3)\nOr do you go right?(type 4) \n"))
    elif choice4 == 10:
      print("You decide to play dead and hope that the jaguar will leave you alone. It walks over to you, and you hold your breath as it sniffs you and then loses interest. Thank goodness! However, it doesn't leave the area.")
      choice5 = int(input("Choice 5: \nDo you want to get up and run? (type 8) \nOr do you want to wait on the ground and hope that the jaguar goes away? (type 7)"))
    elif choice4 == 11:
      print("You pick up a rock and hurl it towards the jaguar with all your might. Because you rested so long earlier and ate that granola bar, you have enough strength to knock the jaguar out. You run, sprinting towards freedom.")
      ending = 8
      break
    elif choice4 == 12:
      print("You throw your phone at the jaguar, but you miss. Instead of hitting the jaguar, it sails past and hits a tree. You see it sail up into the air as rope wraps around it, and you realize that it just triggered a trap. An arrow flies from out of nowhere past your phone and buries itself in your neck.")
      ending = 9
      break
    elif choice4 == 13:
      print("You stand as still as possible, hoping that the jaguar leaves you be. It stares you down for about 5 minutes (although it feels longer) and then seems to lose interest. As soon as it looks away, you take off and don't look back.")
      ending = 7
      break
    elif choice4 == 14:
      print("You take off and run from the jaguar as fast as you can. Your feet pound against the ground until, suddenly, the ground beneath you gives way and you find that you are falling. You fall, slide, fall, slide, and then tumble to a stop deep inside what looks like a cave system. Exhausted, you lay there, and eventually fall asleep.")
      ending = 3
      break
    else:
      print("That is not a valid choice. In choosing to do nothing, you quickly expire. The jungle is not a place where indecisive people survive. \nTHE END")
      break

    #Choice 5
    if choice5 == 1:
      #do later
      print("You decide to run through the puzzle as fast as possible, narrowly dodging arrows that rain down around you. Somehow you make it through alive, and you follow the tunnel up a steep slope until you are out in the sunshine once more. Relieved, you decide you are done exploring the jungle and just want to go home.")
      ending = 10
      break
    elif choice5 == 2:
      print("You decide to slowly work your way through the puzzle, stepping carefully from tile to tile, listening and feeling to try to find the right tile without triggering any of the wrong ones. Unfortunately, you are not practied at the art of jungle puzzles, and you realize too late that you just stepped onto the wrong tile (only three rows in)! The walls shake, and suddenly you feel an arrow pierce through your neck.")
      ending = 9
      break
    elif choice5 == 3:
      print("You decided to go left and as you're walking you fall into the ground. You have no idea where you are, but you are really tired and you want to sleep, so you start walking (in hope of finding some way out).")
      ending = 4
      break
    elif choice5 == 4:
      print("You decide to go right. As it turns out, that was precisely the way to go. You find the perfect frog for your lab.")
      ending = 10
      break
    elif choice5 == 5:
      print("You decided to build a ladder out of the wood you find and the rope that you have in your backpack. You start by grabbing the wood and tie the wood pieces together. Once you're finished you prop it up against a branch. You are hoping that this is going to work. You climb up the ladder... And it worked! You got the frog.")
      ending = 11
      break
    elif choice5 == 6:
      print("You have decided to climb up the other tree, so you do just that. You're really close to the frog but you are also on anther skinny branch. You grab the frog as quick as you can but the branch snaps. You fall and land hard on the ground. Luckily, you didn't break anything. You will just have some bruises. The only bad part is, you let go of the frog, and it got away. However, after this adventure you just decide to go home and let someone else try to catch this frog.")
      ending = 12
      break
    elif choice5 == 7:
      print("You decide to remain still. The jaguar prowls nearby.")
      ending = 13
      break
    elif choice5 == 8:
      print("You glance at the jaguar, and when it seems distracted, you jump up and begin to run.")
      ending = 7
      break
    else:
      print("That is not a valid choice. In choosing to do nothing, you quickly expire. The jungle is not a place where indecisive people survive. \nTHE END")
      break
      
  #Endings
  if ending == 1:
    print("You run left, and after a tense 5 minutes, you find yourself at the edge of a deep ravine. The jaguar closes in behind you and leaps, pushing you off the cliff, and you both fall to your death. \nTHE END")
    return
  elif ending == 2:
    print("Unfortunately for you, what at first seemed like an easygoing descent soon turned into pure terror. The path got steeper and steeper, and soon you find yourself sliding down the path instead of walking. When the path ends at the edge of a cliff, you cannot stop yourself in time and you go hurtling to your death. \nTHE END")
    return
  elif ending == 3:
    print("You awake to the sound of people calling your name. It looks like someone sent out a rescue party for you! How long were you there in the cave? They are very relieved to see you, and so you have no choice but to go with them and return home. You tell them of all your adventures, and how you fell into the cave, and they are very impressed. Returning home to your wife and daughter, you decide that you are never going back into that rainforest without a guide. \nTHE END")
    return
  elif ending == 4:
    print("Soon you find yourself in what feels like another world. Everything is tinted yellow, and you wonder if exhaustion is making you insane. Then you realize that everything is yellow because everything is made of gold! Elated, you begin to stuff as much gold as possible into your backpack before exploring this new world. After walking around for a few minutes, you realize that you are underground. The golden room stretches on for what feels like miles, then unexpectedly ends. Frustrated at reaching a dead end, you pound on the wall, which suddenly springs to life and whirls around, leaving you out in the bright sunshine. Startled, you fall over, and suddenly hear people shouting your name. A rescue party! How long have you been gone? It only felt like a day or two, but somehow you know it has been much longer. Shrugging it off, you return home to your wife and daughter, now the richest man you know. For all your wealth, however, you refuse to speak of your adventures. No one else can ever learn of the golden room. \nTHE END")
    return
  elif ending == 5:
    print ("You're falling and falling fast. You start to wonder why you've been falling for so long. Soon you realize that it's because the ground is gone and now you are free falling. You don't know where you're going to end up. You hope you land on some nice grass or some water, but unfortunately, no. You fell on to concrete and snapped your neck and you dies.\nTHE END")
    return
  elif ending == 6:
    print ("You walk in hope of finding food. At first you find nothing but then a couple feet in front of you, you see a bush. It has berries on it. You walk over and start eating some berries and then soon become really tired out of nowhere so you lay down and fall asleep. But you never wake up. It turns out that you just ate poisonous berries and died in your sleep.\nTHE END")
    return
  elif ending == 7:
    print("You run and run and run, not stopping until you realize the trees are thinning. Using your phone (which finally has service since you are no longer in the jungle), you call someone to come get you. You return home, forever scarred by your adventures. \nTHE END")
    return
  elif ending == 8:
    print("""However, your victory is short-lived. As you run away, you trip on a rock and are knocked out yourself. You wake up in a hospital room, wondering how you got there. You ask the nurses, 'Where am I? Who am I? What's my name?'
    """)
    global loop
    loop = 5
    global userName
    userName = input("What's your name?")
    return loop
  elif ending == 9:
    print("Lying on the ground, blood pooling around you from the arrow, you wish you could have seen your wife and daughter one last time. That's the last thought you ever think. \nTHE END")
    return
  elif ending == 10:
    print("Returning home, you make sure to tell everyone about your amazing adventures through the jungle. Your wife and daughter are happy to have you home, and you are happy that you never have to wear such a heavy backpack ever again. \nTHE END")
    return
  elif ending == 11:
    print("After you get the frog you decide to take it home with you to the lab so you can do some research. You made it home and you showed the frog to your coworkers. You told them all about your journey and they were very impressed because those frogs are really hard to catch. After a while of researching your boss had you take the frog back to island you got it from.\nTHE END")
    return
  elif ending == 12:
    print("You catch a plane back to England. Back to your wife and daughter. Once you land you go straight home and give your family the biggest hug you've ever given. You're happy to be home even though that journery was a once in a lifetime experience.\nTHE END")
    return
  elif ending == 13:
    print("Unfortunately, that doesn't last long. You shift, trying to find a more comfortable position, and the jaguar hears your rustling. it pounces, and that's the last people ever hear of Dr. Melvin Vizsla. \nTHE END")
    return
  else:
    return


loop = 0

userName = input("What is your name? \n")
ShortStory(userName)

if loop == 5:
  ShortStory(userName)
else:
  print("Thank you for playing our story! Try again sometime and see if you can get a different ending!")
