def httpsError(status):
    match status:
        case 400:
            return "bad request"
        case 404:
            return "not found"
        case 418:
            return "i am taipbot"
        case _:
            return "something's wrong the internet"
        
hE=httpsError(800)  
print(hE)      
        