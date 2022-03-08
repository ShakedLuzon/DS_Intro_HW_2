def reverse(sentence, reverse_word):
    word = ''
    if type(sentence) == str:
        sen = sentence.split()
        for i in sen:
            if i == reverse_word:
                word = i[::-1]
                return sentence.replace(i,word,1)      
        return 'The word was not found'
    else:
        return "invalid input"
    
print(reverse("i like them like", "like"))
        
            

