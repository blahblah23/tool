

from pprint import pprint



class Champion:

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
           return "I feel miserable!"
        elif s <= 0:
           return "I feel bad!"
        elif s <= 0.5:
           return "Could be worse!"
        elif s <= 1:
           return "Seems to be okay!"
        else:
           return "Great!" 
  
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)




#     class P:
#         def __init__(self,x):
#             self.x = x
#         @property
#         def x(self):
#             return self._x
#         @x.setter
#         def x(self, x):
#             if x < 0:
#                 self._x = 0
#             elif x > 1000:
#                 self._x = 1000
#             else:
#                 self._x = x
#         pprint(dir(x))
    
#     p = P(1001)

# pprint(dir(p))
# print(type(p.x))
# print(getattr(p, 'x'))


# import shit
# from pprint import pprint


# class feline:
#     def __init__(self):
#         print(self)

# class Cat(feline):
    # pass

# cat = Cat()

# print(cat.__class__.__name__)
# pprint(globals())



# Running a module populates its contents. 
# i.e this module: 




# #meat:
# import lettuce
# def chicken():
#     pass


# #start module is empty, then:
# import lettuce
# #now module only contains lettuce, then:
# def chicken():
#     pass
# #now module contains lettuce, chicken.




# #lettuce:
# from meat import chicken
# def salad():
#     pass



# # say lettuce is ran first. then:
# from meat import chicken
#     import lettuce
# # lettuce has not yet been imported, so Python executes the contents of lettuce:
#         from meat import chicken

# meat has been imported, but not yet fully executed. Python doesnt care. Python pulls the module out of sys.modules. At this point, meat is still empty. It hasnt defined chicken yet, nor even completed importing lettuce. Python cant find chicken in meat, so it fails.

# What if we imported chicken from the end of lettuce and lettuce from the end of meat? Python would start by executing this code:

# def chicken():
#     pass
# # lettuce doesnt exist yet, but it doesnt matter until chicken is called. 
# # now meat contains chicken. then:
# import lettuce
# #It has not been imported yet, so Python executes lettuce. It starts:
#     def salad():
#       pass
# #It defines salad. Then it executes:
#     from meat import chicken

# meat is in sys.modules, so it uses that. meat contains chicken, so it succeeds. Python finishes importing lettuce. That concludes importing lettuce from meat. Thats the last thing in meat, so the import of meat finishes, successful, as well.



