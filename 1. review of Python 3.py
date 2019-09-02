'''
1. what is 7 to the power of for
2. split the string 'Hi there sam!'
3. waht  is the main difference between a tupple and a list?
4. create a function that grab the email website domain from a string in the form
   'user@domain.com' and return 'domain.com'
5. create a basc function that returns True if the word 'dog' is contained in the
   input string. Do not worry about edge cases like punctuation being attached to 
   the word dog, but do count for capitalization
6. create a function that counts the number of times the word 'dog' occurs in a 
   string. again ignore edge cases 'this dog runs faster than the other dog'
7. use lambda expression and the filter function to filter out words from a list
  that do not start with the letter 's', for example: ['soup','dog','salad','cat','great']
8. you are driving a little too fast, and a police officer stops you. write  function
   to return one of three possible results: "No ticket", "Small ticke", "Big ticket", if
   your speed is 60 or less the result is "No ticket". If speed is between 61 an 80 inclusive
   e result is "Small ticket". If speed is 81 or more, the result is "Big ticket". unless it 
   is your birthday, your speed can be 5 higher in all casses


'''

print("\nanswer 1:\n")
print(7**4)
print((pow(7,4)))
#---------------------------

print("\nanswer 2:\n")
s="hi there sam!"
print(s.split())
#---------------------------

print("\nanswer 3:\n")
print("te main difference is that a list is mutable and a tupple is immutable")
#---------------------------

print("\nanswer 4:\n")
name="user@hotmail.com"
def func(name):
	count=0
	if '@' in name:
		for letter in name:
			if letter=='@':
				count+=1
				break

			else:
				count+=1
		domain=name[count:]			
		return domain

	else:
		print("this is not an email")

# or
def func2(name):
	return name.split('@')[1]
print(func(name))
print(func2(name))
#---------------------------

print("\nanswer 5:\n")

def dog(sentence):
		return 'dog'in sentence.lower()

sentence='Is there a Dog here?'
print(dog(sentence))

#---------------------------
print("\nanswer 6:\n")

def dog2(sentence2):
	count=0
	for position in range(0,len(sentence2)-2,1):
		if 'dog'==sentence2[position]+sentence2[position+1]+sentence2[position+2]:
			count+=1
	return count

sentence2="this dog runs faster than the other dog"
print(dog2(sentence2))
#---------------------------
print("\nanswer 7:\n")
lista=['soup','dog','salad','cat','great']
print("using a function called 'func")
def func(lista):
	return	[word for word in lista if word[0]=='s']
print(func(lista))

print("using lambda expression and filter")

print(list(filter(lambda x:x[0]=='s', lista)))

#---------------------------
print("\nanswer 8:\n")

def ticket(speed,birthday):
	if birthday:
		limit=[speed<=60,61<speed and speed<=80,81<speed]
	else:
		limit=[speed<60,61<speed<=80,81<speed]

	if limit[0]:
		return 'No ticket'
	elif limit[1]:
		return 'Small ticket'
	else:
		return 'Big ticket'

print(ticket(81,True))
print(ticket(81,False))

