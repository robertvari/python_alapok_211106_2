def call_myself(n):
    if n >= 10:
        print("n == 10. exit")
    else:
        print(f"I called myself {n} times")
        call_myself(n+1)


call_myself(0)