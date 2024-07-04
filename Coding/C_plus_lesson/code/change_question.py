import sys
total_money=0
money=list(map(int,input().split()))
#统计放入钱币总额
for i in money:
    if i!=-1:
        total_money+=i
#商品价格
goods_price={'0':0,'1':1,'2':1,'3':1,'4':2,'5':2,'6':3,'7':3,'8':3,'9':4,'10':4}
#商品名字
goods_name={'0':"",'1':"Table-water",'2':"Table-water",'3':"Table-water",'4':"Coca-Cola",'5':"Milk",'6':"Beer",'7':"Orange_Juice",'8':"Sprite",'9':"Oolong-Tea",'10':"Green-Tea"}
#商品购买数量
goods_number={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0}
#输入要购买的商品序号
goods=list(input().split())
remain=total_money #找零
for i in goods:
    if i!='-1':
        if remain>=goods_price[i]:
            goods_number[i]+=1
            remain-=goods_price[i]
        else: #钱币不够的情况
            print("Insufficient money")
            sys.exit()
    #输出总额和找回
print(f"Total:{total_money}yuan,change:{remain}yuan")
for i in goods_number.keys():
    if goods_number[i]!=0:
        print(f"{goods_name[i]}:{goods_number[i]};",end='')
