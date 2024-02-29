def limitLength(words, limit, debug) :

    if (type(words)==list) :
        if len(words) > limit :
            if debug : print('걸렀습니다.')
            return words[:limit]
    else :
        if debug : print('안 걸렀습니다.')
        return words