#Write a program that asks a user for their favouritenumber between 1 and 100 and then tells them a joke based on the number. You should use a minimum of 3 jokes
#Creat dictionart with jokes
jokes = [
"I can't hear what they're saying cuz I'm talking",
"Telling my daughter garlic is good for you. Good immune system and keeps pests away.Ticks, mosquitos, vampires... men.",
"I've been going through a really rough period at work this week It's my own fault for swapping my tampax for sand paper.",
"If I could have dinner with anyone, dead or alive... ...I would choose alive.",
"Two guys walk into a bar. The third guy ducks.",
"Why can't Barbie get pregnant? Because Ken comes in a different box. Heyooooooo",
"Why was the musician arrested? He got in treble.",
"Did you hear about the guy who blew his entire lottery winnings on a limousine? He had nothing left to chauffeur it.",
"What do you do if a bird shits on your car? Don't ask her out again.",
"He was a real gentlemen and always opened the fridge door for me",
"Telling my daugthers date that 'she has lice and its very contagious the closer you get to her.' *Correct way to parent.",
"What should you do before criticizing Pac-Man? WAKA WAKA WAKA mile in his shoes",
"What's the difference between an illegal Mexican and an autonomous robot...? Nothing... they were both made to steal American jobs.",
"What do you call a barbarian you can't see? an Invisigoth.",
"How do you spell Canda? C,eh,N,eh,D,eh",
"You ever notice that the most dangerous thing about marijuana is getting caught with it?",
"What did Arnold Schwarzenegger say at the abortion clinic? Hasta last vista, baby.",
"My wife is in a bad mood. I think her boyfriend forgot their anniversary. Way to go, dude. Now we all suffer...",
"My speech today will be like a mini-skirt. Long enough to cover the essentials but short enough to hold your attention!",
"Thanksgiving joke What does Miley Cyrus eat for Thanksgiving? Twerky! Just kidding... Drugs. She eats drugs.",
"Why do you never see elephants hiding in trees? 'Cause they are freaking good at it",
"How did the blonde die raking leaves? She fell out of the tree.",
"'That guy is such a douche-bag! Is he single? Maybe I can fix him!'  women.",
"My son just got a tattoo of a heart, a spade, a club, and a diamond, all without my permission. I guess I'll deal with him later.",
"What do you call a potato in space? Spudnik",
"How to get a cop's attention",
"What happens to a necrophiliac after death? Reserection",
"Why did the chicken hold a seance? To get to the other side.",
"Where do baby cows go to eat lunch? At the calf-eteria.",
"What's the difference between a painting and Jesus. You only require one nail to put up the painting.",
"Mom: 'Do you want this?' Me: 'No.' Mom: 'Ok I'll give it to your brother.' Me: 'No I want it.'",
"How do you fit 4 gays on one barstool? Flip it over!",
"I am looking forward to 6pm Thanksgiving Day when Walmart opens its doors for its annual sale of trampled human corpses.",
"ttrium-barium-copper oxide walks into a bar The bartender tells him, 'We don't serve superconductors here.' He leaves without resistance.",
"A guy pick up a woman Then he puts her down",
"Every night, I take all of the singles out of my wallet, spread them on the bed, and pretend I was pretty that day.",
"Which gospel contains Jesus' parable about the shades of numbers? Math hue.",
"Ibuprofen is my favorite headache medicine that also sounds like a reggae professor.",
"Ted Cruz getting elected.",
"Before I destroy a wasp's nest I like to capture a single wasp and tell it my entire diabolical plan.",
"What's Al-Qaeda's favorite American football team? The New York jets.",
"INTERVIEWER: Why do you want to work here? ME: *crumbs tumbling from my mouth* Oh, I don't. I was just walking by and saw you had donuts.",
"Coming on valentines day. Fifty shades of grey. There won't be a dry seat in the cinema.",
"Did you hear about the midget psychic who escaped from prison? He's a small medium at large.",
"Someone didnt click the button in /r/thebutton Yeah... Thats a good joke , he impossible!",
"What's the difference between a car tyre, and 365 condoms? One's a Goodyear, an the other's a great year.",
"Roses are red, Violets are blue. I have a gun. Get in the van.",
"I've struggled for years to be above the influence... But I've never been able to get that high",
"With Facebook, you can stay in touch with people you would otherwise never talk to, but that's only one of the many awful things about it",
"What's the difference between a blonde and a washer? When you dump your load in a washer, it doesn't follow you around for a week.",
"Have you ever heard of the movie 'Constipation'? No? Most likely because it never came out.",
"What's black, blue and doesn't look too well? Stevie Wonder",
"I saw a French rifle on eBay today It's never been fired but I heard it was dropped once.",
"What did the car said to the valet? I've been through a lot.",
"Bill Clinton must be the luckiest man in the world. All of the sex he has, with Hillary, you know it's hate sex.",
"yeah girl.. shake that thing where poop comes out of. it really turns me on when your poop factory shakes faster than usual",
"I can't stand when people say they hate both of the presidential candidates.",
"A Mexican fireman had twin boys He named them Jose and Hose B",
"I was drinking at the bar, so I took a bus home. That may not be a big deal to you, but I've never driven a bus before!",
"Donald Trump will ban the sale of shredded cheese He wants to make America grate again",
"Things have really turned around for me since I re-named my penis and testicles 'JD Power and Associates'",
"My sex face is the same as my first pee in three hours face.",
"My cat just walked by me carrying a toy mouse I don't remember buying her. Women be shoppin!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
"Why did the Xbox owner cross the road? To fuck your mom.",
"Sometimes you check the amount of subscribed people. When you do this, there are 4,111,093,0003.666 'humorists'. 2/3rds of a person? Really?",
"I don't believe in Bigfoot; because he never believed in me. I'd scan the crowd at my ballet recitals, and always see that one empty seat.",
"What did the porn actress say when she opened the door? Make sure to come upstairs.",
"I don't judge people based on color, race, religion, sexuality, or gender...I base it on whether or not they're an asshole.",
"Why were the baker's hands brown? Because he kneaded a poo.",
"Not to get too technical, but chemistry says alcohol IS a solution. So I win.",
"I often think if I'd taken a different path in life, I could be lying on a slightly more comfortable sofa right now.",
"I'm terrible at telling jokes... I always punch up the fuck lines",
"What did the hillbilly say to his sister after she asked him to have sex with her? If you incest.",
"You know what, we need a huge spoon to take care of this -Guy who invented shovels",
"How to keep the flies off the bride at an Italian wedding Keep a bucket of shit next to her",
"What do grandparents smell like? 'Depends'.",
"7% of all hearing loss is a result of sitting in a restaurant next to a table full of women who just received dessert.",
"What do people from the 1930's and /r/news jokes have in common? They're both old.",
"I like my slaves like I like my coffee Fair Trade.",
"ME: I fell off a 50 ft tall ladder once GIRL: holy cow how did you survive ME: I fell off the bottom rung",
"What do you call a blind dinosaur? A do-think-he-saurus :) !! Lol What do you call a blind dinosaurs dog? A do-you-think-he-saurus-rex",
"I just bought a very tiny amphibian for a pet. It's my-newt!",
"This may be not be a mainstream opinion, but I don't believe you should cut down a Christmas tree unless you intend on eating it.",
"Jenna Jameson to Oprah, 'There's a little bit of Jenna Jameson in everyone.' I'm pretty sure she got that backwards.",
"Even after 20 years, Jared Fogle is still getting into smaller and smaller jeans.",
"I have a degree in men's studies. It's called 'world history'.",
"Why don't most fans like the first 39 episodes of DBZ? Its pretty gay, just Saiyan.",
"My ex-wife still misses me... But her aim is gettin better.",
"This doctor once told me eating a bagel was like eating 5 slices of bread and I was like ok, cool, I like bread",
"What do you call a three-humped camel? Pregnant",
"What did the two tampons say to each other? Nothing, they're both stuck-up cunts.",
"What do you call Jay-Z having a leg transplant? A hip-hop hip op.",
"What defies the law of gravity? Women. They heavier they are, the easier they are to pick up.",
"Everything has to be related in a woman: if the mouth shuts, the legs open.",
"Wanna hear a pun about long hair? Rapunzel.",
"'I'm so pissed I could punch a ba-' 'A what?'' Big Baby from Toy Story 3 hovers over me, sawed-off shotgun in hand. 'A bagel. I HATE carbs.'",
"What's the difference Donald Trump and my Vagina? One's a Cunt and the other has nice hair.",
"My doctor had to put me on a new medication that's supposed to help lower the amount of karate in my blood",
"Wife: make sure to put the toilet seat down Me: okay Me: [to toilet seat] you're worthless and nobody likes you",
"What's the difference between a blonde and a supermarket trolley? A: The supermarket trolley has a mind of its own.",

]

import random

#randomly select a joke from the list
joke = random.choice(jokes)
while True:
    print("hello, and welcome to jokebot. I have a joke for you:")
    print("press 1 to read a joke")
    print("press 2 to exit")
    choice = int(input())
    if choice == 1:
        joke = random.choice(jokes)
        print("-----------------------------------------------------")
        print(joke)
        print("-----------------------------------------------------")
    elif choice == 2:
        print("bye")
        break
    else:
        print("invalid input")
