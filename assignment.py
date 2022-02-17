##1,2,3,4

class MyUser():
    def __init__(self,id,name,username,email):
        self.id=id
        self.name=name
        self.username=username
        self.email=email

    def __str__(self):
        return f'MyUser {self.name}{self.username}{self.id}{self.email}'

class SpeedUser:
    def __init__(self,d):
        self.__dict__=d
       #obj.dic= obj(dic)

    def __str__(self):
        result=""
        for k,v in self.__dict__.items():
            result+=f'{k} ={(str)(v)} \n'
        return result


def getUser():
    response=requests.get('http://jsonplaceholder.typicode.com/users') # list of string ['{}''{}'{}'{}{}]
    if response.status_code//100 ==2:
        return  json.loads(response.content) # list of users  => list of dic

def findUser(nameToCheck,userList):
    for user in userList:
        temp=SpeedUser(user)
        if temp.name ==nameToCheck:
            return temp
    return 'this name was not found '


userJson=getUser()
rightuser=findUser('Ervin Howell', userJson)

print(rightuser)
print(rightuser.address)