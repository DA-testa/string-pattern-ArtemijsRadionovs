# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    check_for_I = input().replace('\r','')
    if check_for_I == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif check_for_I == "F":
        file_name = input().replace('\r','')
        try:
            with open('./tests/' + file_name, 'r') as f:
                pattern = input().rstrip()
                text = input().rstrip()
        except FileNotFoundError:
                print("File not found!")
                return
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p_len = len(pattern)
    t_len = len(text)
    pat_hash = sum(ord(pattern[i])*pow(101, i) for i in range(p_len))
    
    substr_hash = [sum(ord(text[i+j])*pow(101, j) for j in range(p_len)) for i in range(t_len - p_len+1)]
    
    occurr = [i for i in range(t_len-p_len+1) if substr_hash[i] == pat_hash]
    # and return an iterable variable
    return occurr


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

