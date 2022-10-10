import re

with open("assets/dark_and_stormy_night_template.txt" , "r") as file:
    print(file.read())


def read_template(x):
    try:
      with open(x) as file:
          return file.read()
    except:
        raise FileNotFoundError
    
    

def loop_inputs(label):
    list1 = []
    with open(label) as label2:
        label3=parse_template(label2.read())
    for i in range(len(label3[1])):
        l = input(f"{label3[1][i]} ==>")
        list1.append(l)
    tuples = tuple(list1)
    new_phrase=merge(label3[0],tuples)
    with open("assets/response.txt","w+") as story:
        story.write(new_phrase)
    with open("assets/response.txt") as story:
        print(story.read())

    
    

        

def parse_template(s):
    x = re.findall("{(.*?)}",s)
    q = re.sub('{.+?}','{}',s)
    return q,(tuple)(x)
    
        
    

def merge(m , y):
    return m.format(*y)


if __name__ == "__main__" :
    print("**Welcome to madlibs game**")
    print("**Mad Libs ara a word replacement game **")
    print("** So you will enter same words and then **")
    print("** it will replaced in a paragraph it**")
    print("** may be funny and you will lough ... **")
    print("** just answer the questions and press enter ..**")
    parse_template("It was a {Adjective} and {Adjective} {Noun}.")
    #loop_inputs("assets/dark_and_stormy_night_template.txt")
    loop_inputs("assets/story.txt")
