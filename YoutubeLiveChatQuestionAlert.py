import pytchat
chat = pytchat.create(video_id="11 character live video ID")
wordlist = ("?", "what", "when", "where", "which", "who", "why", "how")
while chat.is_alive():
    for c in chat.get().sync_items():
        for i in wordlist:
            if i in c.message:
                print(f"QUESTION ASKED FROM  -  [{c.author.name}]")
                print(f"{c.datetime} :   {c.message}")