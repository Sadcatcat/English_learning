import random
import colorama
from colorama import Fore,Style
def English(name_book, start, end):
    Eng_unit_ti_daan_path = [
        # 第一本书的文件(0-7)
        ['eng one 1.txt', 'eng one 1 daan.txt', 'eng one 1t.txt'],
        ['eng one 2.txt', 'eng one 2 daan.txt', 'eng one 2t.txt'],
        ['eng two 1.txt', 'eng two 1 daan.txt', 'eng two 1t.txt'],
        ['eng two 2.txt', 'eng two 2 daan.txt', 'eng two 2t.txt'],
        ['eng four 1.txt', 'eng four 1 daan.txt', 'eng four 1t.txt'],
        ['eng four 2.txt', 'eng four 2 daan.txt', 'eng four 2t.txt'],
        ['eng seven 1.txt', 'eng seven 1 daan.txt', 'eng seven 1t.txt'],
        ['eng seven 2.txt', 'eng seven 2 daan.txt', 'eng seven 2t.txt'],

        # 第二本书的文件(8-17)
        ['eng two 1.txt', 'eng two 1 daan.txt', 'eng two 1t.txt'],
        ['eng two 2.txt', 'eng two 2 daan.txt', 'eng two 2t.txt'],
        ['eng three 1.txt', 'eng three 1 daan.txt', 'eng three 1t.txt'],
        ['eng three 2.txt', 'eng three 2 daan.txt', 'eng three 2t.txt'],
        ['eng four 1.txt', 'eng four 1 daan.txt', 'eng four 1t.txt'],
        ['eng four 2.txt', 'eng four 2 daan.txt', 'eng four 2t.txt'],
        ['eng five 1.txt', 'eng five 1 daan.txt', 'eng five 1t.txt'],
        ['eng five 2.txt', 'eng five 2 daan.txt', 'eng five 2t.txt'],
        ['eng six 1.txt', 'eng six 1 daan.txt', 'eng six 1t.txt'],
        ['eng six 2.txt', 'eng six 2 daan.txt', 'eng six 2t.txt'],

        # 第三本书的文件(18-25)
        ['eng one 1.txt', 'eng one 1 daan.txt', 'eng one 1t.txt'],
        ['eng one 2.txt', 'eng one 2 daan.txt', 'eng one 2t.txt'],
        ['eng two 1.txt', 'eng two 1 daan.txt', 'eng two 1t.txt'],
        ['eng two 2.txt', 'eng two 2 daan.txt', 'eng two 2t.txt'],
        ['eng four 1.txt', 'eng four 1 daan.txt', 'eng four 1t.txt'],
        ['eng four 2.txt', 'eng four 2 daan.txt', 'eng four 2t.txt'],
        ['eng eight 1.txt', 'eng eight 1 daan.txt', 'eng eight 1t.txt'],
        ['eng eight 2.txt', 'eng eight 2 daan.txt', 'eng eight 2t.txt'],


        # 第四本书的文件(26-33)
        ['eng one 1.txt', 'eng one 1 daan.txt', 'eng one 1t.txt'],
        ['eng one 2.txt', 'eng one 2 daan.txt', 'eng one 2t.txt'],
        ['eng three 1.txt', 'eng three 1 daan.txt', 'eng three 1t.txt'],
        ['eng three 2.txt', 'eng three 2 daan.txt', 'eng three 2t.txt'],
        ['eng four 1.txt', 'eng four 1 daan.txt', 'eng four 1t.txt'],
        ['eng four 2.txt', 'eng four 2 daan.txt', 'eng four 2t.txt'],
        ['eng six 1.txt', 'eng six 1 daan.txt', 'eng six 1t.txt'],
        ['eng six 2.txt', 'eng six 2 daan.txt', 'eng six 2t.txt'],
    ]

    ti_list = []
    daan_list = []
    Title_list_one = []
    Title_list_two = []
    Ct = 1
    for unit in Eng_unit_ti_daan_path[start:end + 1]:
        timu = open(f'./c-test/{name_book}/{unit[0]}')
        daan = open(f'./c-test/{name_book}/{unit[1]}')
        if Ct:
            title_one = open(f'./c-test/{name_book}/{unit[2]}')
            title_resule_one = title_one.readlines()
            for tit in title_resule_one:
                Title_list_one.append(tit)
            Ct = 0
        else:
            title_two = open(f'./c-test/{name_book}/{unit[2]}')
            title_resule_two = title_two.readlines()
            for tit in title_resule_two:
                Title_list_two.append(tit)

        timu_result = timu.readlines()
        daan_result = daan.readlines()

        for tr in timu_result:
            ti_list.append(tr)
        for dn in daan_result:
            daan_list.append(dn)

        ti_list.append('789')
        daan_list.append('789')
    count = 1
    true_num = 0
    dex = 1
    while len(ti_list) > 0:
        if ti_list:
            detial = ti_list.pop(0)
            if dex == 1 and count == 1:
                print(Fore.GREEN + f"现在刷的是{name_book}:{Eng_unit_ti_daan_path[start:end + 1][0][0].split('.')[0]}题")
                print(Fore.RED + "词语填空开始了!")
                print(Style.RESET_ALL)
                for tit in Title_list_one:
                    print(tit, end='')
                print(end='\n')
            elif dex == 0 and count == 1:
                print(Fore.GREEN + f"现在刷的是{name_book}:{Eng_unit_ti_daan_path[start:end + 1][1][0].split('.')[0]}题")
                print(Fore.RED+"短语填空开始了!")
                print(Style.RESET_ALL)
                for tit in Title_list_two:
                    print(tit, end='')
                print(end='\n')
            if detial == "789" or detial == '\n':
                if count -1 == 0:
                    pass
                else:
                    print(Fore.RED+f"\n答题种数:{count-1},正确题目:{true_num},正确率:{format(true_num / (count-1) * 100, '.2f')}%\n")
                    print(Style.RESET_ALL)
                    count = 1
                    true_num = 0
                    if dex == 1:
                        dex = 0
                    else:
                        break

                # 用与跳题时候排除789
                for daan in daan_list[::-1]:
                    if daan == '789' or daan == '\n':
                        daan_list.pop(0)
                        if len(daan_list) >=1:
                            if daan_list[0] != '789' and daan_list[0] != '\n':
                                break
                    else:
                        break

                # 用与跳题时候排除789
                continue

            if dex:
                if count % 4 == 0:
                    for tit in Title_list_one:
                        print(tit, end='')
                    print(end='\n')
            else:
                if count % 4 == 0:
                    for tit in Title_list_two:
                        print(tit, end='')
                    print(end='\n')

            print(f'({count}){detial}', end='')
            response = str(input(Fore.BLUE+"请输入你的回答:"))
            print(Style.RESET_ALL)
            count = count + 1


            True_eng = daan_list.pop(0)

            #跳题模块
            if dex == 1 and count == 2:
                if response == 'xc159753':
                    while ti_list.pop(0) != '789':
                        daan_list.pop(0)
                    ti_list.insert(0,'789')
                    print(Fore.GREEN+'你输入了神秘代码，成功跳题!')
                    print(Style.RESET_ALL)
                    continue
            # 跳题模块

            if response + '\n' == True_eng:
                print(Fore.GREEN+'正确！牛牛牛')
                print(Style.RESET_ALL)
                true_num = true_num + 1
            else:
                print(Fore.RED+f'逗我捏?\nTrue:{True_eng}',end='')
                print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + "刷题完成!")
            print(Style.RESET_ALL)


if __name__ == '__main__':
    book_name = 'None'
    colorama.init()

    while book_name != "break":
        book_name = str(input(Fore.BLUE+"请输入书名(English-1,-2,-3,-4)："))
        issame = str(input(Fore.BLUE+"是否随机章节刷题(Y or N):"))
        unit = -1
        start = -1
        end = -1

        if book_name == "English-1":
            if issame == 'Y\n':
                rand_list = [1, 2, 4, 7]
                unit = rand_list[random.randint(0, 3)]
                if unit == 1:
                    start = 0
                    end = 1
                elif unit == 2:
                    start = 2
                    end = 3
                elif unit == 4:
                    start = 4
                    end = 5
                elif unit == 7:
                    start = 6
                    end = 7
            elif issame == 'N\n':
                unit = int(input('请输入章节->unit:1,2,4,7:'))
                if unit == 1:
                    start = 0
                    end = 1
                elif unit == 2:
                    start = 2
                    end = 3
                elif unit == 4:
                    start = 4
                    end = 5
                elif unit == 7:
                    start = 6
                    end = 7
                else:
                    print(Fore.RED + "章节或者书名错误!")
                    start = -1
                    end = -1
            else:
                print(Fore.RED+"章节或者书名错误!")
                start = -1
                end = -1

        elif book_name == "English-2":
            if issame == 'Y':
                rand_list = [2, 3, 4, 5, 6]
                unit = rand_list[random.randint(0, 4)]
                if unit == 2:
                    start = 8
                    end = 9
                elif unit == 3:
                    start = 10
                    end = 11
                elif unit == 4:
                    start = 12
                    end = 13
                elif unit == 5:
                    start = 14
                    end = 15
                elif unit == 6:
                    start = 16
                    end = 17
            elif issame == 'N':
                unit = int(input('请输入章节->unit:2,3,4,5,6:'))
                if unit == 2:
                    start = 8
                    end = 9
                elif unit == 3:
                    start = 10
                    end = 11
                elif unit == 4:
                    start = 12
                    end = 13
                elif unit == 5:
                    start = 14
                    end = 15
                elif unit == 6:
                    start = 16
                    end = 17
                else:
                    print(Fore.RED + "章节或者书名错误!")
                    start = -1
                    end = -1
            else:
                print(Fore.RED+"章节或者书名错误!")
                start = -1
                end = -1

        elif book_name == "English-3":
            if issame == 'Y':
                rand_list = [1, 2, 4, 8]
                unit = rand_list[random.randint(0, 3)]
                if unit == 1:
                    start = 18
                    end = 19
                elif unit == 2:
                    start = 20
                    end = 21
                elif unit == 4:
                    start = 22
                    end = 23
                elif unit == 8:
                    start = 24
                    end = 25
            elif issame == 'N':
                unit = int(input('请输入章节->unit:1,2,4,8:'))
                if unit == 1:
                    start = 18
                    end = 19
                elif unit == 2:
                    start = 20
                    end = 21
                elif unit == 4:
                    start = 22
                    end = 23
                elif unit == 8:
                    start = 24
                    end = 25
                else:
                    print(Fore.RED + "章节或者书名错误!")
                    start = -1
                    end = -1
            else:
                print(Fore.RED + "章节或者书名错误!")
                start = -1
                end = -1

        elif book_name == "English-4":
            if issame == 'Y':
                rand_list = [1, 3,]
                unit = rand_list[random.randint(0, 1)]
                if unit == 1:
                    start = 26
                    end = 27
                elif unit == 3:
                    start = 28
                    end = 29
                elif unit == 4:
                    start = 30
                    end = 31
                elif unit == 6:
                    start = 32
                    end = 33
            elif issame == 'N':
                unit = int(input('请输入章节->unit:1,3,4,6:'))
                if unit == 1:
                    start = 26
                    end = 27
                elif unit == 3:
                    start = 28
                    end = 29
                elif unit == 4:
                    start = 30
                    end = 31
                elif unit == 6:
                    start = 32
                    end = 33
                else:
                    print(Fore.RED + "章节或者书名错误!")
                    start = -1
                    end = -1
            else:
                print(Fore.RED + "章节或者书名错误!")
                start = -1
                end = -1

        else:
            print(Fore.RED+"章节或者书名错误!")
            start = -1
            end = -1



        if start != -1:
            English(book_name, start, end)
