import pandas as pd
from preprocessing import Preprocess

dataset = pd.read_table('SMSSpamCollection', header=None, encoding="utf-8")
# take text column
text_column = dataset[1]

sentences = text_column.tolist()
# below technique list 
"""
lcc = Lower case convertion
rurls = Revoing URLs
ntw = convert numbers to words
res = Removing Extra Spaces
"""
techniques = ["lcc", "rht", "rurls","rn", "sc", "ntw","ata","sto","ec","ps","l","re","ret","ew","etw","rp","rs","rfw","rrw","rsc", "res"]

# test_techniques = ["lcc", "rht", "rurls", "rn", "ntw", "sc", "ata", "sto", "ec", "ps", "l", "re", "ret", "ew", "etw", "rp", "rs", "rfw", "rrw", "rsc", "res"]
# temp_sent = ['one of the other reviewers has mentioned that after watching just oz episode you all be hooked . they are right , as this is exactly what happened with me . the first thing that struck me about oz was its brutality and unflinching scenes of violence , which set in right from the word go . trust me , this is not a show for the faint hearted or timid . this show pulls no punches with regards to drugs , sex or violence . its is hardcore , in the classic use of the word . it is called oz as that is the nickname given to the oswald maximum security state penitentiary . it focuses mainly on emerald city , an experimental section of the prison where all the cells have glass fronts and face inwards , so privacy is not high on the agenda . em city is home to many..aryans , muslims , gangstas , latinos , christians , italians , irish and more ... so scuffles , death stares , dodgy dealings and shady agreements are never far away . i would say the main appeal of the show is due to the fact that it goes where other shows would not dare . forget pretty pictures painted for mainstream audiences , forget charm , forget romance ... oz does not mess around . the first episode i ever saw struck me as so nasty it was surreal , i could not say i was ready for it , but as i watched more , i developed a taste for oz , and got accustomed to the high levels of graphic violence . not just violence , but injustice ( crooked guards who all be sold out for a nickel , inmates who all kill on order and get away with it , well mannered , middle class inmates being turned into prison bitches due to their lack of street skills or prison experience ) watching oz , you may become comfortable with what is uncomfortable viewing ... thats if you can get in touch with your darker side .',
#  "a wonderful little production . the filming technique is very unassuming very old-time-bbc fashion and gives a comforting , and sometimes discomforting , sense of realism to the entire piece . the actors are extremely well chosen michael sheen not only i has got all the polar i but he has all the voices down pat too ! you can truly see the seamless editing guided by the references to williams ' diary entries , not only is it well worth the watching but it is a terrific written and performed piece . a masterful production about one of the great master is of comedy and his life . the realism really comes home with the little things : the fantasy of the guard which , rather than use the traditional dream ' techniques remains solid then disappears . it plays on our knowledge and our senses , particularly with the scenes concerning orion and halliwell and the sets ( particularly of their flat with halliwell is murals decorating every surface ) are terribly well done .",
#  "i thought this was a wonderful way to spend time on a too hot summer weekend , sitting in the air conditioned theater and watching a lighthearted comedy . the plot is simplistic , but the dialogue is witty and the characters are likable ( even the well bread suspected serial killer ) . while some may be disappointed when they realize this is not match point : risk addiction , i thought it was proof that woody allen is still fully in control of the style many of us have grown to love . this was the most i i'd laughed at one of woody is comedies in years ( dare i say a decade ? ) . while i i've never been impressed with scarlet johnson , in this she managed to tone down her i sexy i image and jumped right into a average , but spirited young woman . this may not be the crown jewel of his career , but it was wittier than i devil wears prada i and more interesting than i superman i a great comedy to go see with friends .",
#  'basically there is a family where a little boy ( jake ) thinks there is a zombie in his closet & his parents are fighting all the time . this movie is slower than a soap opera ... and suddenly , jake decides to become rambo and kill the zombie . ok , first of all when you are going to make a film you must decide if its a thriller or a drama ! as a drama the movie is watchable . parents are divorcing & arguing like in real life . and then we have jake with his closet which totally ruins all the film ! i expected to see a boogeyman similar movie , and instead i watched a drama with some meaningless thriller spots . out of just for the well playing parents & descent dialogs . as for the shots with jake : just ignore them .',
#  'petter matter is i love in the time of money i is a visually stunning film to watch . mri matter offers us a vivid portrait about human relations . this is a movie that seems to be telling us what money , power and success do to people in the different situations we encounter . this being a variation on the arthur schnitzel is play about the same theme , the director transfers the action to the present time new york where all these different characters meet and connect . each one is connected in one way , or another to the next person , but no one seems to know the previous point of contact . stylishly , the film has a sophisticated luxurious look . we are taken to see how these people live and the world they live in their own habitat . the only thing one gets out of all these souls in the picture is the different stages of loneliness each one inhabits . a big city is not exactly the best place in which human relations find sincere fulfillment , as one discerns is the case with most of the people we encounter . the acting is good under mri matter is direction . steve buscemi , rosario dawson , carol kane , michael imperial , adrian greater , and the rest of the talented cast , make these characters come alive . we wish mri matter good luck and await anxiously for his next work .']

# remaining techniques 
"""
	lcc = lower case convertion
	rht = Removing HTML tags
	rurls = Revoing Urls 
	rn = Removing Numbers
	ntw = convert numbers to words
	sc = Spelling Correction
	ata = convert accented to ASCII code
	sto = short_to_original
	ec = Expanding Contractions
	ps = Stemming (Porter Stemming)
	l = Lemmatization
	re = Removing Emojis
	ret = Removing Emoticons
	ew = Convert Emojis to words
	etw = Convert Emoticons to words
	rp = Removing Punctuations
	rs = Removing Stopwords
	rfw = Removing Frequent Words
	rrw = Removing Rare Words
	rsc = Removing Single characters
	res = Removing Extra Spaces
"""
print(f"******** Before preprocessing technique ******* ")
for sent in temp_sent[:1]:
	print(sent)
preprocessing = Preprocess()

preprocessed_text = preprocessing.preprocessing(sentences, techniques)
print(f"******** After preprocessing ****************")
for sent in temp_sent[:1]:
	print(sent)
