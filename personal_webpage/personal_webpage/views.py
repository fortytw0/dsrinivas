from django.shortcuts import render

import json
import markdown

def front_page(request) : 
    
    # loading updates
    updates = json.load(open('content/home/updates.json'))
    updates = [{'date' : update['date'] , 'text' : markdown.markdown(update['text']) } for update in updates] 

    print(updates)

    # loading notice board
    notice_board_md = open('content/home/notice_board.md').read().strip()
    notice_board = markdown.markdown(notice_board_md) if notice_board_md else False

    # loading introduction
    introduction = markdown.markdown(open('content/home/introduction.md').read())

    # loading publications
    publications = json.load(open('content/home/publications.json'))
    for year in publications : 
        for pub in year["papers"] : 
            pub["title"] = markdown.markdown(pub["title"])
            pub["authors"] = markdown.markdown(pub["authors"])
            pub["venue"] = markdown.markdown(pub["venue"])


    return render(request, 
                  "base.html", 
                  {"updates" : updates, "notice_board" : notice_board, "introduction":introduction, "publications":publications})
