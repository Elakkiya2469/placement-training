def merge_the_tools(string, k):
    for i in range (0,len(string),k):
        un=""
        for c in string[i:i+k]:
            if c not in un:
                un+=c
        print(un)
