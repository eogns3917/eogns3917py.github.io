mylist = "1 2 3 4 5 6 7" #문자담기
splist = mylist.split(' ')    #a 문자를 공백기준으로 splist에 스플릿
print(mylist) #문자열 mylist 출력
print(splist)            #스필릿한 splist출력
print('_______________________')
print(' ')
print('for문으로 출력')
for result in splist: print(result) #splist를 for 문으로 출력