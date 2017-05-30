import sys,time,random
import turtle
import pyglet
try:
    from phue import Bridge
except:
    pass
#Port: Marianas Trench

prompt = '> '
typing_speed = 90 #wpm
Character_Attributes = []

try:
    b = Bridge('192.168.0.9') # 192.168.0.9
    b.get_api()
    b.set_light([1,2,3], 'on', True)
    b.get_light(1, 'on')
    b.get_light(2, 'on')
    b.get_light(3, 'on')
except:
    pass

def lights(color,brightness):
    """lights('color',brightness)
    Colors must be defined inside Rainbow. Brightness goes from 1-254"""
    Rainbow = {'red': [.765,.223], 'green': [.214,.709], 'blue': [0.168,0.041], 'gold': [0.4859,0.4599], 'grey': [0.3227,0.329]}    
    try:
        lights = b.get_light_objects()
        for light in lights:
            light.brightness = brightness
            light.xy = Rainbow[color]
    except:
        pass
    
def typewriter():
        tw = pyglet.media.load('sounds/typewriter.wav') 
        tw.play()
                
def zombiebrain():
    zb = pyglet.media.load('sounds/zombiebrain.wav') 
    zb.play()
    return
        
def manscream():
    ms = pyglet.media.load('sounds/manscream.wav') 
    ms.play()
    return
        
def flip():
    flip = pyglet.media.load('sounds/flip.wav') 
    flip.play()
    return
        
def music():
    try:
        snd = pyglet.media.load('sounds/Sunless.wav')
        looper = pyglet.media.SourceGroup(snd.audio_format, None)
        looper.loop = True
        looper.queue(snd)
        p = pyglet.media.Player()
        p.queue(looper)
        p.play()
        return
    except:
        pass
		
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ('')

def yesno(answer):
    """yesno(input)
        returns yes or no depending on input"""
    yes = ["yes",'y','YES','ye','y','Y','yess']
    no = ["NO",'no','n','N','nO','No']
    if  answer in yes:
        answer = 'yes'
        return answer
    elif answer in no:
        answer = 'no'
        return answer
    else:
        return answer
        
def Map():
    if 'Report Filled' in Character_Attributes:
        print ("""                 \t5. View Secret Map""")

def secretmap():
    try:
        screen = turtle.Screen()
  # this assures that the size of the screen will always be 400x400 ...
    except:
            pass
            
def goback():
        while True:
                print ("\nWould you like to go back to port?")        
                go_back = yesno(input(prompt))    
                if go_back == 'yes':
                        flip()
                        start()
                if go_back == 'no':
                        break
                else:
                        print("Invalid command, Please enter yes or no.\n")

def leaveport():
    typewriter()
    manscream()
    lights("grey", 120)
    slow_type ("""\n\tYou leave the dusty shadow of a port, and explore\n\tthe blinded underwater trench. You are quickly eaten alive\n\tby a gigantic Goblin Shark never to be heard from again""")
    sys.exit("\nYou are dead\n")

def start():
    while True:
        print ("""
                You explore Marianas Trench(Pick 1-4):                                     
                \t1. Fill port report
                \t2. Interact with humanoid inhabitants of port
                \t3. Explore town
                \t4. Leave Port""")
        Map()
        lights('red',120)
        explore = input(prompt)
        
        if explore == "1" :
                flip()
                Fill_port_report()
                break
        elif explore == "2":
                flip()
                interact()
                break
        elif explore == "3":
                flip()
                explore_town()
                break
        elif explore == "4":
                flip()
                leaveport()
        elif explore == "5"  and 'Report Filled' in Character_Attributes:
                flip()
                secretmap()
        else:
                print("Invalid command")        
        
def Fill_port_report():
    while True:    
        lights('blue',120)
        if 'Report Filled' in Character_Attributes:
                print ("\nYou have already filed a port reported.")
                goback()
        else:
                print ("\nYou file a port report of Mariana's trench.")
                typewriter()
                slow_type ("\n\tIt takes many hours as the fog is thick and visibility poor.")
                slow_type ("""\tThe Docks are deserted and it doesnt't look like anyone \n\thas been around for a long time. Your crew finds a map hidden inside \n\ta small empty cabin. It's tattered and old but it could be useful.""")
                Character_Attributes.append('Report Filled') 
                slow_type ("\nPort Report Complete.\n")
                goback()

def marianas_port():
    lights('red',120)
    music()
    while True:
        slow_type ("\n\tWould you like to dock at Mariana's Trench (Port)? yes/no")
        Dock_Port = yesno(input(prompt))
               
        if  Dock_Port == 'no':
            leaveport()            
        elif Dock_Port == 'yes':
            flip()
            start()             
        else:
            print ("Invalid Command")                            
                    
def interact():
    while True:
        lights('green',120)
        print ("\nYou interact with some of the locals\n")
        typewriter()
        slow_type ("""\tYou find a small village deep inside a valley within the island.\n\tThe inhabitents seem friendly. You notice most of the villagers are\n\tolder, many with worms crawling through their skulls. They offer \n\tyou and your crew some home cooking. Your crew looks rejoiced\n\tand a tear comes to your eyes as its been weeks since you've had\n\ta hot home cooked meal.""")
        print ("\nDo you accept their offer? yes/no")
        village = yesno(input(prompt))
        if village == 'yes':
            filled_up()
        if village == 'no':
            goback()
        else:
            print ("Invalid command")
                     
def filled_up():        
    while True:
        typewriter()
        slow_type ("""\tYou graciouslly accept their offer. However after you take a few bites\n\tyou realize that the food is horendous, its some kind of slimy green soup\n\tthat jumps as it sneaks down your throat. You hesistate but want \n\tsay something about the food.""")
        print ("""
        What do you do?(Pick 1 or 2):                                     
        \t1. Be polite and swallow your food with a smile
        \t2. Tell the nice zombies their food taste like garbage.""")
        food = input(prompt)
        if food == "1":
                Character_Attributes.append('filled up')
                typewriter()
                slow_type ("\n\tThe villagers applaud you for your cunning white lie. They")
                slow_type ("\thaven't seen anyone with such manners in a long time. We know")
                slow_type ("\tour food is awful that is the way we like it. We insist you")
                slow_type ("\tmeet with our king he is looking for someone as cunning as you.")
                print ("\n You and your crew are now filled up")
                goback()
        elif food == "2":
                zombiebrain()
                manscream()
                typewriter()
                slow_type ("""\n\tThe Zombie villagers get upset and rip you and your crew to\n\tshreads. Your last thoughts as your head is knawed off is\n\t"Maybe that wasn't the brightest of ideas" """)
                time.sleep(4)
                sys.exit("\nYou are dead.\n")
        else:
                print ("Invalid command")

def explore_town():
    while True:
        print ("You find a small village deep inside a valley within the island.")
        print ("More descriptions will go here")
        print ("""
                What do you do?(Pick 1 or 2):                                     
                \t1. Go to the Village King's hut
                \t2. Visit place of interest
                \t3. Go back to port.""")
        town_explore = input(prompt)
        if town_explore == "1" :
                interact_king()
                break
        elif town_explore == "2":
                place_of_interest()
        elif town_explore == "3":
                goback()
                break
        else:
            print("Invalid command")

def interact_king():
    while True:
        lights('gold', 160)
        slow_type ("\nGreetings I am King Kram.")
        if 'filled up' in Character_Attributes:
            slow_type ("\n\tAh I see my people have deemed you worthy, not many meet them")
            slow_type ("\tand live to tell the tale of another day. I then have a request for you.")
            slow_type ("\tA member of my tribe has gone missing inside caverns deep within the island")
            slow_type ("\tCould you venture in and fetch him for me. He went in without a map and")
            slow_type ("\thas been missing for weeks.")
            
            print ("""
                    What do you do?(Pick 1 or 2):                                     
                    \t1. I generously Accept your quest. 
                    \t2. Decline and leave this foolish island. 
                    \t3. Go back""")
            Speaktoking = input(prompt)
            
            if Speaktoking == "1" :
                explore_dungeon()
                
            elif Speaktoking == "2":
                leaveport()
                
            elif Speaktoking == "3":
                goback()
            
            else:
                print("Invalid command")               
        else:
            slow_type ("\n\tYou don't look very Important, Be gone with yourself.")
            slow_type ("\tGuards show him the door!")
            goback()
   
def place_of_interest():
    while True:    
        print ("\nPlace of interest dialogue")
        typewriter()
        slow_type ("\n\tDialogue")
        goback()
   
def explore_dungeon():
    while True:    
        print ("\nYou will explore dungeon here. Map found when doing port report will help here")
        print ("You will go through the dungeon to find the tools the king needs\n")
        print ("The dungeon is not yet implemented")
        print ("""
                    What do you do?(Pick 1 or 2):                                     
                    \t1. Navigate through dungeon command 1
                    \t2. Navigate through dungeon command 1
                    \t3. Go back to town""")
                                    
        dungeon_explore = input(prompt)
            
        if dungeon_explore == "1" :
            explore_dungeon()            
        elif dungeon_explore == "2":
            explore_dungeon()            
        elif dungeon_explore == "3":
            goback()        
        else:
            print("Invalid command")
       
        
marianas_port()

