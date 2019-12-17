#PF-Prac-2

def bracket_pattern(input_str):
    return input_str.startswith('(') and (input_str.count('(')==input_str.count(')'))
input_str="(())("
print(bracket_pattern(input_str))