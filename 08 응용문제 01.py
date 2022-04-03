inStr, outStr = "", ""
ch = ""
count, i = 0, 0

if __name__=="__main__" :
    inStr = input("문자열을 입력하세요 : ")
    count = len(inStr)

#이름:강문정 학번:2021041040
    for i in range(0, count):
        ch = inStr[i]
        if(ord(ch) >= ord("A") and ord(ch) <= ord("Z")):
            newCh = ch.lower()

        elif(ord(ch) >= ord("a") and ord(ch) <= ord("z")):
            newCh = ch.upper()

        else:
            newCh = ch

        outStr += newCh

    print("대소문자 변환 결과 --> %s" % outStr)

