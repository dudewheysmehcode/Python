#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def edit_distance(s,t):
    print "----------"
    distance = 0
    similars,offset,s_len,t_len= count_similars(s,t)
    print "---"
    best_action(s,t,similars,offset,s_len,t_len)
    
    if s_len == t_len:
        distance += s_len - similars
    
    if s_len < t_len:
        distance += t_len - s_len
        
    if s_len > t_len:
        distance += s_len - t_len
        
    return distance

def best_action(s,t,similars,offset,s_len,t_len):
    if s == t:
        return 0
    
    removeCount = replaceCount = insertCount = 0
    cs,ct = s,t
    
    if similars == len(offset):
        if s_len > t_len:
            for group in offset:
                if group[3] != 1:
                    cs = cs[0:group[1]] + cs[group[1]:]
                    removeCount += 1
            if cs == t:
                print cs
        
        
        
    if s_len == t_len:
        replaceAll = s_len
        for group in offset:
            print group[3]
        replaceUseSimilar = 0
        insert = 0
    
    if s_len > t_len:
        replace = s_len
        remove = 0
        insert = 0
    
    
    if s_len < t_len:
        replace = s_len
        remove = 0
        insert = 0
    return

def count_similars(s,t):
    similars = []
    s_seen = []
    t_seen = []
    offset = []
    s_len = len(s)
    t_len = len(t)
    
    sIndex=tIndex= 0
    
    for letter in s:
        sIndex = s.find(letter,sIndex)
        tIndex = t.find(letter)
        
        while t_used(t_seen, tIndex):
            tIndex = t.find(letter,tIndex+1)
        
        if tIndex != -1 and tIndex not in t_seen:
            s_seen.append(sIndex)
            t_seen.append(tIndex)
            similars.append(letter)
            if sIndex != tIndex:
                offset.append([letter,sIndex,tIndex,sIndex-tIndex])
    print offset
    print "Out of " + str(s_len) + " letters in s and " + str(t_len) + " letters in t,"
    print "there are " + str(len(similars)) + " similar letters, and"
    print "there are " + str(len(offset)) + " offset letters."
    return len(similars), offset, s_len, t_len

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def t_used(t,i):
    if i in t:
        return True
    return False

#For example:

# Delete the 'a'
print edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
print edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
print edit_distance('peter', 'sarah')
#>>> 5

# One deletion
print edit_distance('pete', 'peter')
#>>> 1
