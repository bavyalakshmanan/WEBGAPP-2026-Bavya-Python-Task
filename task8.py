class students:
     def __init__ (self,name,project,depart):
          self.name = name
          self._project = project
          self.__depart = depart

     def depart(self):
      return self.__depart    
     
     def details(self):
         return f"{self.name} from the department of {self.__depart} has done the project {self._project}"
         
s1 = students("RAJ","HABBIT TRACKING","VLSI")
print(s1.details())
#when calling the method "()" important