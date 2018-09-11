allscores=[{'school_class': '4a', 'scores': [3,4,4,5,4]},{'school_class': '5a', 'scores': [3,5,5,3,2,3]},{'school_class': '6a', 'scores': [2,5,4,2,3,4,4]} ]

sumScore=[]
countScore=[]
for i in allscores:
	s=sum(i.get('scores'))
	k=len(i.get('scores'))
	sr=round(s/k,2)
	schoolclass=i.get('school_class')
	sumScore.append(s)
	countScore.append(k)
	print()	
	print('Average Score for {} is:{}'.format(schoolclass,sr))
	print('Number of students:{}, Scores summ: {}'.format(k,s))
print()	
print('Average score for school is {}'.format(sum(sumScore)/sum(countScore)))
print('Number of students:{}, Scores summ: {}'.format(sum(countScore),sum(sumScore)))