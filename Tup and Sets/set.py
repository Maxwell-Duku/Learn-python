num = {1, 2, 3}
for nums in num:
    print(num)
    
    
    
    
Regions = ["Western", "Northern", "Central", "Savanna", "Western", "Tamale", "Central"]
print(len(set(Regions)))
#print(set(Regions))
print(list(set(Regions)))




#################################SET METHODS################################


#####ADD METHOD######
s = set([1, 2, 3, 4])
s.add(5)
print(s)


##########REMOVE METHOD########
set1 = {1,2,3,4,5}
set1.remove(3)
print(set1)

##########COPY METHOD##########
cop = set([1,2,3,4])
another_cop = cop.copy()
print(cop)



###########CLEAR METHOD##########
days = ("monday", "tuesday",)
days.clear()


##########SET MATH METHOD############
math_students = {"Max", "Elvis", "Michael", "Edward"}
science_students = {"Max", "Alex", "Elvis"}
math_students & science_students
