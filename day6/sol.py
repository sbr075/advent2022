
with open("day6/input.txt", "r") as file:
    inp = file.read()
    msg_len = 4
    
    for i in range(msg_len, len(inp)):
        marker = inp[i-msg_len:i]
        if len(set(marker)) == msg_len: break
    
    print(i)