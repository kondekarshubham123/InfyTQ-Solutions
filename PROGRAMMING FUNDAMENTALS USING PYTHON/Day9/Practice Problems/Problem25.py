#PF-Prac-25
def list_of_count(word_list):
    #start writing your code here
    return [len(i) for i in word_list]

word_list=["COme","here"]
print(list_of_count(word_list))