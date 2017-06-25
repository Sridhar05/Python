

text_results = ['hello', 'foo' , 'hi' , 'good' , 'this' , 'hi' ]
scores = [4,2,4,5,1,4,6,7 ]

def combine_list(list1, list2):

	if len(list1) != len(list2):
		list1 = list1[0:len(list2)]
		#raise Exception("Array must be equal")
		
	return sorted([(list1[i], list2[i]) for i in xrange(len(list1))], reverse=True)



print combine_list(scores, text_results)
