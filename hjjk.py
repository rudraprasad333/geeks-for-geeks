def accept():
    import csv
    f=open("result.csv","w")
    
    x=csv.writer(f)
    sid=int(input("enter"))
    sname=input("enter")
    game=input("rnmh")
    result=input("enter ")
    head=["stykuj","ggdfrf","hgggu","jjuyh"]
    data=[sid,sname,game,result]
    x.writerow(head)
    x.writerow(data)
accept()
