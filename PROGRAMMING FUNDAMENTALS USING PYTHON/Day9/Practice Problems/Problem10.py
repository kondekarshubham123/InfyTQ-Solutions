#PF-Prac-10
def string_both_ends(input_string):
	#start writing your code here
    if len(input_string)>1:
        return input_string[0:2]+input_string[(len(input_string)-2)::]
    else:return -1

input_string="se"
print(string_both_ends(input_string))