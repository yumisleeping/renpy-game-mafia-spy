# Define characters here
define luca =   Character("     Luca Kaneshiro", color="#ffffff")
define ett =    Character("     Ettore", color="#ffffff")
define yn =     Character("[ynbox]", color="#ffffff")
define stranger = Character("       ???", color="#ffffff")

define blink = Fade(0.5, 0.5, 0.5)
define blinklonger = Fade(3, 3.5, 3.5)

#------------------------------------------------------------------

# Define character positions here

transform half_left:
    xalign 0.33 yalign 1.5

transform half_left_closer:
    xalign 0.33 yalign -3

#------------------------------------------------------------------

# Define soundtrack here
define playlista = "audio/soundtrack.mp3"

# SFX
define surprise = "audio/sfx/surprise.mp3"
define fire = "audio/sfx/fire-crackling.mp3"
define ettchuckle = "audio/sfx/ett-chuckle.mp3"
define pog = "audio/sfx/pog.mp3"
define doorcreak = "audio/sfx/door-creak.mp3"
define woodcreak = "audio/sfx/wood-creak.wav"
define nightambience = "audio/sfx/night-ambience.wav"
define knifestab = "audio/sfx/knife-stab.mp3"
define peoplewalking = "audio/sfx/people-walking.mp3"
define spooky = "audio/sfx/spooky.mp3"

#------------------------------------------------------------------

# Define char images here

#Luca
image luca neutral = "images/Kaneshiro/neutral.png"
image luca neutral2 = "images/Kaneshiro/neutral-look-away.png"
image luca happy = "images/Kaneshiro/happy.png"
image luca surprised = "images/Kaneshiro/surprised.png"
image luca angry = "images/Kaneshiro/angry.png"
image luca shock = "images/Kaneshiro/shock.png"

#Ettore
image ett smirk = "images/Ettore/smirk.png"
image ett  indifferent = "images/Ettore/indifferent.png"

#S/N
image yn normal = "images/YN/yn-silhouette.png"

# NPC
image stranger man = "images/npc/man-pointing.png"
image stranger strangeman = "images/npc/strange-man.png"


# Define scenery images here
image namescreen = "images/scenery/rename-screen.png"
image bar = "images/scenery/bar.jpg"
image fireplace = "images/scenery/fireplace.png"
image italianstreet = "images/scenery/italian-street.png"
image blackoverlay = "images/scenery/black-overlay.png"
image littlegirlsroom = "images/scenery/littlegirlsroom.png"
image doorpeek = "images/scenery/door-peek.png"
image bloody = "images/scenery/bloody.png"
image blackscreen = "images/scenery/blackscreen.png"

#------------------------------------------------------------------

label start:

    # Luca e Ettore zom: 1.3 truecenter
    # yn zoom: 1.2

    stop music

    # call screen ayo

    play sound pog volume 0.5
    call askname from _call_askname

    # play music playlista volume 0.3
    

    call act1 from _call_act1
    call past from _call_past

    return

#------------------------------------------------------------------

label askname:
    scene namescreen at truecenter:
        zoom 0.7

    $ ynbox = "       " + renpy.input("What's your name?", length=32)
    $ yname = ynbox.strip()

    if yname == "":
        $ ynbox = "       " + "Y/N"
        $ yname = "Y/N"

    menu:
        "Are you sure your name is [yname]?"

        "Yes.":
            pass
        "No, rename.":
            call askname from _call_askname_1

    return

#------------------------------------------------------------------

label act1:
    play sound fire volume 0.15 loop

    scene fireplace at truecenter:
        zoom 0.45
    with fade

    show yn normal at right:
        zoom 1.2
    with dissolve    
    yn "\"I CHANGED MY MIND, I DON'T WANT TO DO THIS ANYMORE!\""
    
    "I screamed at the top of my lungs, trying to free myself from the leather bindings that bound my arms and legs to the metal chair."

    hide yn
    show ett indifferent at truecenter:
        zoom 1.3
    with dissolve    
    ett "\"But you were so solicitous when you offered to undertake this task.\""
    
    "The burly white-haired man spoke softly as he poked the fire with the tip of his knife."
    "The flames further hardening the already etched contours of his features, which had aged with uncommon grace."

    ett "\"What's making you hesitate?\""


    "He lazily backed away from the fireplace, and although his massive figure disappeared into the shadows of the dimly lit room,"

    hide ett
    with moveoutright

    "the reddish glow that came from the object in his hand terrified me."
    "The tip of the knife shouldn't have that color, let alone glow in the dark."

    play audio ettchuckle
    "My silence and staring at the object in his hand must have been answer enough, as his chuckle sent a shiver down my spine."


    show ett smirk at truecenter:
        zoom 1.3
    with dissolve    
    ett "\"This?\""

    "he announced good-naturedly, his agile hand movements drawing fiery arcs in the air."

    ett "\"Our little [yname] should be used to feeling pain by now.\""

    "I made the terrible mistake of blinking."
    hide ett
    with blink

    "And when I opened my eyes again, his ocher breath, a mix of whiskey and tobacco, ruffled the few hairs on the back of my neck that weren't drenched in sweat."
    "His hand stroked my hair before I felt his short nails scrape my scalp, and with clenched teeth, I waited for his tug."
    "And he came, relentless, making my neck beg to let go of my shoulders and roll around freely."
    "He kept the pressure on, looking forward to the scream that would escape my throat and the heartbreaking tears"
    "that would leave crystalline paths on my soot-smeared face, but when several minutes had passed,"
    "with no rousing reaction, he just snorted, throwing my head forward with force and snapping the tongue."

    show ett indifferent at truecenter:
        zoom 1.3
    with dissolve    
    ett "\"My, my...\""

    "He muttered, opening an intricately carved wooden box of blue jewels that sat on the mantelpiece,"
    "and once more, he leaned into the flames with his knife in hand."

    ett "\"It's not fun to play with you.\""

    hide ett
    show yn normal at right:
        zoom 1.2
    with dissolve
    yn "\"You should have known by now.\""
    
    hide yn
    with dissolve

    "I commented, recovering from the brief bout of dread."
    "His predictable behavior brought me back to reality, away from my fears and nightmares"
    "that came with the anticipation the unknown brought."
    "His violent attitude was familiar to me. After all, Master had entrusted him with my education within the corporation."
    "And he hated me every second of every day for it. Partly because I got in the way of his \"{i}harmless hobby{/i}\", as he liked to point out."
    "Causing pain was his favorite pastime, and the closer people were to him, the more satisfied he became with hurting them."
    "Lovers of his, for example, didn't last long in his raw, bloody hands. Meg had a busy schedule,"
    "shouldering endless hospital bills, for injuries she couldn't explain beyond the terse \"{i}I found they like this.{/i}\""
    "But then came the hardest part, which was convincing the victims not to report him."
    "Which was easily resolved when she sighed and pointed to the door, in silent order for him to clean up his own mess."
    "And it was when he paid a last visit that his presence was enough to silence them for eternity."
    "But, for some twisted reason, I never reacted to his torture."
    "Not that he'd taken me as his lover. Nor would he be so low as to lay his hands on the child he helped raise."
    "He just disliked people in general."
    "Especially me, for being \"{i}boring as fuck{/i}\". And I find it is better to be a living bore than a buried or crippled bore."

    hide ett
    show yn normal at right:
        zoom 1.2
    with dissolve    
    yn "\"I'm telling you I don't want to go on.\""

    "The words came out in my nonchalant tone I used with gang members."

    yn "\"No one mentioned that I would need to pass a physical exam before joining {i}his{/i} organization.\""

    hide yn
    show ett smirk at truecenter:
        zoom 1.3
    with dissolve    
    ett "\"I wonder what you were thinking would happen.\""

    "He turned his face briefly to me, his smile playing at the corner of his lips."

    ett "\"That dear [yname] would pop up at his door and slip in without drawing attention?\""

    hide ett
    with dissolve

    "I rolled my eyes. That's exactly what I was thinking when I volunteered to infiltrate the infamous Luca Kaneshiro's gang."
    "Followers of him received the title of Lucubs, when they became useful to the mafia. And yet,"
    "as a way of recognizing his most faithful men and women, Kaneshiro tattooed black flames on his body to represent them."
    "Rumors had it that the Kaneshiro organization had gone several years without its leader,"
    "but that he appeared out of nowhere, looking the same, not having aged a year since he disappeared."
    "And if they were already dangerous in their leader's absence, now that he had returned,"
    "the situation on our side went from bad to worse."

    show ett indifferent at truecenter:
        zoom 1.3
    with dissolve    
    ett "\"He wouldn't accept you.\""

    "Ettore commented."

    ett "\"You're not his style.\""

    "{i}Thanks God!{/i} I thought bitterly."

    "The last thing I wanted was to get the attention of another mobster. I was already curled up to my neck in my current position."

    ett "\"And the scar that will remain on your body won't help at all.\""

    "He walked over and sat on my lap as he trailed his finger along my chin and down to my neck."

    ett "\"Yeah. It won't work one bit.\""

    "And without warning he ripped open my blouse and pressed the smoking knife to the side of my hip,"
    "where the insignia of the Italian gang, to which we belonged, was tattooed."
    "I wheezed in pain, unable to contain the screaming and crying."

    show ett smirk at truecenter:
        zoom 1.3
    with dissolve

    "I saw him lick his lips before my consciousness slipped away and I passed out."    

    return

#------------------------------------------------------------------

label past:

    stop sound
    hide ett
    
    scene italianstreet at truecenter:
        zoom 1.25
    with blinklonger
    play music peoplewalking volume 0.08

    show stranger man at left:
        zoom 0.4
    stranger "\"Search every inch of this place, leave nothing behind!\""

    "a squeaky voice commanded, laughing and pointing to the cafeteria, which only a few hours ago belonged to my mothers."

    hide stranger
    show blackoverlay at truecenter:
        zoom 2
    with dissolve

    "My mother Belamina was really beautiful. And she told me that was her curse. She was born into the mafia."
    "And her father, permanently dissatisfied with his wife being unable"
    "to bear a male heir to run the \"family business\" in the future, despised her immensely."
    "And, exhausted from putting up with my grandfather's immaturity, grandma left,"
    "leaving him with only the clothes on his back, and countless collectors on his tail"
    "His financial management was as ridiculous as he was, and my grandmother was smarter than he ever gave her credit for."
    "She'd embezzled money from the organization from the moment they were married,"
    "already knowing what kind of man he was, and refusing to go down with him."
    "And when my grandfather's life was cut short in some dank alleyway reeking of urine and vomit,"
    "my grandmother came out of hiding and moved to Japan with my mother."

    hide blackoverlay
    with dissolve

    "And there she opened a coffee shop, which unsurprisingly became a success."
    "Gaining branches in several different neighborhoods, and pleasing both locals and foreigners."
    "And it was there that my mother Mina, as she liked to be called, met my mother Sawako."
    "Sawako was a flower girl, who despite her name meaning \"refreshing child\","
    "looked more like something out of a horror movie, with her long black hair, tattoo on her neck and narrow eyes."
    "While the true mafia heiress, Mina, had the appearance of a princess,"
    "who with her enchanting voice would be able to subdue the most ferocious of creatures."
    "I'd like to think the two of them were happy. But as the years passed,"
    "their laughter and faces faded, lost in the swirl of memories."
    "And I could no longer identify the particular features of her. Which of the two did I look more like?"
    "Or did I have a little bit of both in me, if not in appearance then in personality?"
    "But it would be impossible to know. Everyone who knew them, with the exception of me, was dead."
    "The past was persistent and traveled until it found us on the other side of the world, in our little corner of fairy tales,"
    "where life was colorful and full of smiles and affectionate hugs, which only my mothers and grandmother knew how to offer."
    "Mina was very clear during my upbringing, her rules should never be disobeyed:"

    "\"{i}Never talk to strangers.{/i}\""
    "\"{i}Never follow anyone.{/i}\""
    "\"{i}We will never send another person to pick you up from school.{/i}\""
    "\"{i}If you notice that you are being followed, enter the first trade you see and call us.{/i}\""
    "It was simple rules, but I didn't realize it…"

    show stranger strangeman at right:
        zoom 0.27
    with moveinright

    "I didn't pay enough attention to the man who stood out from the crowd with his dizzying height and who left as soon as I"

    hide stranger
    with moveoutright

    "wrapped my little arms around my mother's blond hair and walked back to the house, while told all the news of the little school."

    stop music

    show littlegirlsroom at truecenter:
        zoom 1.25
    show doorpeek at truecenter:
        zoom 1.25
    with blink

    play music nightambience volume 0.08
    with dissolve
    play sound doorcreak volume 0.25
    "I hadn't found his presence so strange, until I saw him enter the room by the crevice in the wardrobe door,"
    "through which I was spying."
    
    play sound woodcreak volume 0.25
    "The silence underscored his heavy tread on the woods, which creaked under his weight."

    show stranger strangeman at half_left:
        zoom 0.27
    with dissolve

    "He stopped in front of the dressing table, touching the portrait of the wedding ceremony."
    "This was the only personal object they displayed with pride. But my existence was not to be revealed."
    "My room was simple, without any decorations, and I didn't have many toys like the other children, besides the small black dragon"
    "with green eyes, which I strangled in my arms. Now I clearly remembered him. And he knew about me."
    "\"{i}Pay attention, use this if you are in danger. Do you know how to identify when you are in danger?{/i}\""
    "\"{i}Excellent. Now show me.{/i}\""
    "My mother's words echoed in my mind."
    "I'd been trained daily, ever since I'd demonstrated enough hand-eye coordination to hold a knife and cut through the old attic pillows."

    show stranger strangeman at half_left_closer:
        zoom 0.42
    with dissolve

    "His hand gripped the doorknob, unhurriedly turning. As soon as he opened the door,"

    hide doorpeek
    with dissolve

    "I withdrew the butterfly knife from its hiding place under the dragon's wings and pressed it deep between his ribs."

    play audio knifestab volume 0.8
    with dissolve

    "Maybe my war cry had alerted him, maybe I was just weak, but he wasn't hurt."
    "Instead, the man snatched the object from my trembling hands, slapped me that sent me rolling across the floor,"
    "and, after a punch to the stomach, lifted me onto his shoulders."

    hide stranger
    show blackoverlay at truecenter:
        zoom 2
    with dissolve

    "It was in the jolt of his walk that I glimpsed..."

    stop music
    
    hide blackoverlay
    play sound spooky volume 0.75
    show bloody at truecenter:
        zoom 2
    with vpunch

    "{sc=2.5}{color=#832510}{b}...all the blood and the inert bodies of my family{/b}{/color}{/sc}"
    "{sc=3}{color=#832510}{b}being left stretched out on the floor.{/b}{/color}{/sc}"

    show blackoverlay at truecenter:
        zoom 2
    show blackscreen at truecenter:
        zoom 2
    with blinklonger    

    "And that's how I joined, at the age of nine, the gang that destroyed my life."

    menu:
        "..."

        "[[END CHAPTER.]":
            pass

    return

#------------------------------------------------------------------