#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
	#start writing your code here
    return [z+' '+y+' '+x for z in subjects for y in verbs for x in objects]


subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))