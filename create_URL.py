def space2plus(word) :
    word = word.replace(" ", "+")
    return word
def createYoutubeURL(word) :
    word =space2plus(word)
    return f'https://www.youtube.com/results?search_query={word}'
def createDaumURL(word) :
    word =space2plus(word)
    return f'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={word}'
def createNaverURL(word) :
    word =space2plus(word)
    return f'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query={word}'
def createGoogleURL(word) :
    word =space2plus(word)
    return f'https://www.google.com/search?q={word}&sca_esv=a19c4e940f5aec6f&rlz=1C1IBEF_koKR958KR958&ei=UjTbZePvLeGP2roPzY2qiAo&udm=&ved=0ahUKEwjj4I7ZwMaEAxXhh1YBHc2GCqEQ4dUDCBA&uact=5&oq={word}&gs_lp=Egxnd3Mtd2l6LXNlcnAiD-yKpO2LsOu4jOyeoeyKpDIFEC4YgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAuGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEC4YgAQyFBAuGIAEGJcFGNwEGN4EGN8E2AEBSLoOUIQFWNQLcAN4ApABA5gBjAGgAdkLqgEEMC4xMrgBA8gBAPgBAZgCCKACvgTCAgQQABhHwgIEEAAYA8ICCxAAGIAEGLEDGIMBwgIEEC4YA8ICERAuGIAEGLEDGIMBGMcBGNEDwgIOEC4YgAQYsQMYxwEY0QPCAgoQLhiABBiKBRhDwgIKEAAYgAQYigUYQ8ICGRAuGIAEGIoFGEMYlwUY3AQY3gQY3wTYAQHCAgsQLhiABBixAxiDAcICChAuGEMYgAQYigXCAhkQLhhDGIAEGIoFGJcFGNwEGN4EGN8E2AEBmAMAiAYBkAYKugYGCAEQARgUkgcDNC40&sclient=gws-wiz-serp'
