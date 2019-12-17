#PF-Prac-5
def count_digits_letters(sentence):
    return [sum(c.isalpha() for c in sentence),sum(c.isdigit() for c in sentence)]

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))