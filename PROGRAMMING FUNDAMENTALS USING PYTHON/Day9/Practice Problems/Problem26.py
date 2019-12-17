#PF-Prac-26
def check_occurence(string):
    return string.lower().count('jet') == string.lower().count('mat')
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))