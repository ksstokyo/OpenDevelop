# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

#1行目のデータ取得
input_line = int(input())
#2行目のデータ取得
work = input().rstrip().split(' ')
#文字→数字変換
parent = [int(n) for n in work]

parent2 = parent.copy()
num_all = []

#部下の人数をnum_allにまとめる
#添え字は社長から始まる
def num_syain(num):
    for i in range(len(num)):
        if num[i] == 1:
            del num[i]
            num.insert(i,0) #[4, 6, 0, 4, 0, 0, 5, 3, 4]

#社長は0とし、添え字0は上司の番号、添え字1は部下の数だけ数字が入る
def sort_syain(make_new_num):
    for i in range(len(make_new_num)+1):
        num_all.append([0,[]])
    a = 1
    for j in make_new_num:
        num_all[a][0] = j
        a += 1
    #print(num_all) [[0, []], [4, []], [6, []], [0, []], [4, []], [0, []], [0, []], [5, []], [3, []], [4, []]]
    l = 1
    for m in parent2: #上司の添え字1に、上司の値で数字を入れる
        if num_all[l][0] != 0:      
            num_all[m-1][1].append(num_all[m-1][0])
        l += 1
    #print(num_all) #[[0, []], [4, []], [6, [6]], [0, [0, 0]], [4, [4]], [0, [0]], [0, []], [5, []], [3, [3]], [9, []]]

#上司と番号が異なればさらにその上司の番号に移動する
def count_syain(other_num):
    i = 1
    j = 0
    #while i+1 == j:
    while i < 10:
        for j in other_num[i][1]:
            k = other_num[i][0]
            #社長直属の部下k=0になるまで上司のところに数字を追加していく
            while k != 0:
                other_num[k-1][1].append(j)
                k = other_num[k-1][0]
        i += 1
    return other_num

#関数の呼び出し---------------------
count = num_syain(parent2)
sort = sort_syain(parent2)

#count_syainを呼び出し、社長の値の追加と既定の書式に出力する
count = count_syain(num_all)
for x in range(len(parent)):
    num_all[0][1].append(x)
#print(num_all) [[0, [0, 1, 2, 3, 4, 5, 6, 7, 8]], [4, []], [6, [6, 3]], [0, [0, 0, 4]], [4, [4]], [0, [0, 6, 3]], [0, []], [5, []], [3, [3]], [9, []]]
print("各社員の部下の数を出力する")
for n in range(len(num_all)):
    total_num = len(num_all[n][1])
    print(total_num)
