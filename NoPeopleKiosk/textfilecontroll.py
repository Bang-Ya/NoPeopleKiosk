from datetime import datetime
#from dominate.tags import keygen


if __name__ == "__main__":
    d = datetime.today().strftime("%Y%m%d")
    intd = int(d)
#try:
    with open("license.txt", mode="r") as file:
        license = file.read()
        print('lin'+license)

    cdkey = license
    keyCheck = False
    print(cdkey)

    if intd >= 20220516 and intd < 20220518 and cdkey=='19as-asw2-wq2d-d2da':
        keyCheck=True
    elif intd >= 20220519 and intd < 20220720 and cdkey=='20as-asw2-wq2d-d2da':
        keyCheck = True
    else:
        print('cdkey 안맞음... ')
        keyCheck=False
#except:
#    print('라이센스 파일 없는듯') =======검증좀 해보자

    if keyCheck == False:
        print("라이센스 통과 못함....")
        exit()


    print('CD Key통과. 프로그램 시작.')
    c = input()
