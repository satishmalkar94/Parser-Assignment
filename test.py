
f = open("test.txt", "r")
fileData = f.read().replace('\n','')

cLangFlag = None
javaFlag = None

cLang = ["extern","register","signed"," main() ",
"typedef","volatile","printf(","scanf(","#include<","%d","%s","%c","malloc(","calloc(","stdio.h","conio.h"]

javaLang = ["System.out.println(","println","final","abstract","implements","interface","extends","package","native","strictfp","super","synchronized","volatile","transient","throws","Integer.parseInt()"]

if any(element in fileData for element in cLang):
    cLangFlag = True

if any(element in fileData for element in javaLang):
    javaFlag = True


if (cLangFlag and javaFlag):
    print("file is ambiguous")

if(not(cLangFlag and javaFlag) and cLangFlag):
    print("program is written in c")

if (not(cLangFlag and javaFlag) and javaFlag):
    print("program is written in Java")



