import sys

fp = open('/Usr/share/dict/words','r')
#read the file
file_contents = fp.readlines()

s=[]                                               #assign empty array and accumulate the results to it
def easy_word_search(word):
    for i in file_contents:
        if(i[0:len(word)] == word):
            s.append(i)
    print s


print "enter the prefix"
get_user_input = raw_input()
easy_word_search(get_user_input)
