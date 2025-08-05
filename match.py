#match statement takes an expression and compares it to a series of patterns, similar to switch statement in C,C++,or Java
def http_error(status):
     match status:
          case 404:
               print("Bad request")
          case 400:
               print("Page not found")
          case 500:
               print("Internal server error")
          case _:
               return "Something is wrong with the server"
#function call
http_error(404)               
http_error(500)