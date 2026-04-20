def main():
    name="Desmond"
    text="Yeah"
    height: int = 10
    print(f"{name} is a good guy! {text}", end=' a ')
    print("Hi, ",name)
    print(name+text)#python doesn't know how to glue different types, like string and integers
    print(name+str(height))
    print("i am a year one student","i am 18", sep=' ')
    print("i have a dog.\
          i have too!")#\: is to distinguish two statements
if __name__=="__main__":
    main() 