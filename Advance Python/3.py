class MyContextManager:
     def _enter_(self):
          print("Entering MyContextManager")
          return self
     
     def _exit_ (self, exc_type, exc_value, traceback):
          print("Exiting Context")
          
with MyContextManager() as manager:
          print("Inside the context")
          raise ValueError("Something has gone wrong")