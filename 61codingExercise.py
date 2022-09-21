# create the dictionary of marks of students and convert them into grade 
dictionary={
    "rohan":85,
    "jitendria":87,
    "rajesh":80,
    "raj":81,
    "naman":65
}
print(type(dictionary))
for i in dictionary.items():
    print(i)

#convert the marks into grading system
def grade(marks):
    match marks:
        case marks if 90<= marks<=100:
            return "A+" 
        case marks if 80<= marks <90:
            return "A"
        case marks if 60<= marks <70:
            return "C" 
        case marks if 50<= marks <60:
            return "D" 
        
# call the fucntion
for i,j in dictionary.items():
    g=grade(j)
    print(f"{i}:{g}") 

       
