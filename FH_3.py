# Open a file for writing
fo = open("foo.txt", "w")
string = "Python is a great language.\nYeah its great!!\n"
fo.write( string )
# Close opend file
fo.close()
        
#open file for reading
fo = open("foo.txt", "r")

string = ""
#read from file
string = fo.read();
print(f"file content is :\n\t{string}")

#close file
fo.close()


fo = open("foo.txt", "w")
string = "I love Python!"
fo.write( string )
# Close opend file
fo.close()
fo = open('foo.txt')
ans = fo.read();
print(ans)
fo.close()
