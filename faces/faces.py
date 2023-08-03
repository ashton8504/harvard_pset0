def faces():
    msg = input()

    if ":)" in msg:
        msg = msg.replace(":)", "🙂")
        print(msg)
    if ":(" in msg:
        msg = msg.replace(":(", "🙁")
        print(msg.title())
        
faces()

# 🙂🙁

#modified_msg = msg.replace(":)", "🙂").replace(":(", "🙁")
# msg_two = msg.replace(":(", "🙁")