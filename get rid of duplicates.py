# First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
d={
    "id1":{
        "name":"Mahd",
        "class":"6C",
        "subject":["Science","Math","English"]
    },
    "id2":{
        "name":"Zoraiz",
        "class":"6I",
        "Subject":["Math","History","English"]
    },
    "id3":{
        "name":"Affan",
        "class":"6A",
        "subject":["Math","Games","Sceince"]
    }
}
# accese data
print(d.items())
for key,value in d.items():
    print(value["name"])