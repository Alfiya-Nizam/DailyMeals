from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect,redirect
from django.db import connection
from datetime import *
import datetime
today_date = datetime.date.today()
today = today_date.strftime("%Y-%m-%d")
from datetime import datetime, timedelta
yesterday_date = today_date - timedelta(days=1)
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request,'index.html')
def UserReghome(request):
    return render(request,'UserReghome.html')
def adminhome(request):
    return render(request,'adminhome.html')
def staffhome(request):
    return render(request,'staffhome.html')

def UserReg(request):
    return render(request,'UserReg.html')
def UserRegAct(request):
    cur=connection.cursor()
    nm=request.GET['cn']
    addr=request.GET['ad']
    addr1=request.GET['hd']
    # city=request.GET['ct']
    # dist=request.GET['ds']
    # pin=request.GET['pn']
    ph=request.GET['ph']
    em=request.GET['em']
    pwd=request.GET['pass']

    # s1="insert into user (cname,adr,office,city,dist,pin,phn,em) values('%s','%s','%s','%s','%s','%s','%s','%s')"%(nm,addr,addr1,city,dist,pin,ph,em)
    s1="insert into user (cname,adr,office,phn,em) values('%s','%s','%s','%s','%s')"%(nm,addr,addr1,ph,em)
    cur.execute(s1)
    sq="select max(cid) as cid from user"
    cur.execute(sq)
    cr=cur.fetchall()
    for row in cr:
        q="insert into login(uid,uname,upass,utype)values('%s','%s','%s','user')"%(row[0],em,pwd)
        cur.execute(q)
    msg="<script>alert('Added');window.location='/UserReg/'</script>"
    return HttpResponse(msg)
def login(request):
    return render(request,'login.html')
def LoginAct(request):
    cur = connection.cursor()
    na = request.GET['nm']
    pwd = request.GET['pass']

    s2 = "select * from login where uname='%s' and upass='%s'" % (na, pwd)
    cur.execute(s2)

    if cur.rowcount > 0:
        rs = cur.fetchall()
        for row in rs:
            request.session['uid'] = row[1]
            request.session['utype'] = row[4]
            request.session['status'] = row[5]

        if request.session['utype'] == "admin":
            return render(request, 'adminhome.html')
        elif request.session['utype'] == "canteen" and request.session['status'] == "approved":
            return render(request, 'canteenhome.html')
        elif request.session['utype'] == "staff":
            return render(request, 'staffhome.html')
        elif request.session['utype'] == "user":
            return render(request, 'UserReghome.html')
        else:
            h="<script>alert('Login failed');window.location='/login';</script>"
            return HttpResponse(h)
    else:
        msg = "<script>alert('Login failed');window.location='/login';</script>"
        return HttpResponse(msg)
def userview(request):
    cur=connection.cursor()
    s="select * from user"
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'cid':row[0],'cname':row[1],'adr':row[2],'office':row[3],'phn':row[4],'em':row[5]}
        cr.append(q)
    return render(request,'userview.html',{'cr':cr})
def staff(request):
    cur=connection.cursor()
    uid=request.session['uid']
    s1="select * from staff where cnid='%s' "%(uid)
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'sid':row[0],'sname':row[1],'adr':row[2],'district':row[3],'pin':row[4],'phone':row[5],'email':row[6],'gender':row[7],'dob':row[8],'doj':row[8],'cnid':row[9]}
        cr.append(q)
    return render(request,'staff.html',{'cr':cr})

def StaffAct(request):
    cur=connection.cursor()
    uid=request.session['uid']
    sn=request.GET['sn']
    add=request.GET['add']
    ds=request.GET['ds']
    pin=request.GET['pin']
    phn=request.GET['phn']
    em=request.GET['em']
    gen=request.GET['gen']
    dob=request.GET['dob']
    doj=request.GET['doj']
    pwd=request.GET['pass']

    s3="insert into staff(sname,adr,district,pin,phone,email,gender,dob,doj,cnid) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(sn,add,ds,pin,phn,em,gen,dob,doj,uid)
    cur.execute(s3)
    sql="select max(sid) as sid from staff"
    cur.execute(sql)
    rs=cur.fetchall()
    for row in rs:
        sq="insert into login(uid,uname,upass,utype) values('%s','%s','%s','staff')"%(row[0],em,pwd)
        cur.execute(sq)
    msg="<script>alert('Added');window.location='/staff/'</script>"
    return HttpResponse(msg)
def menu(request):
    cur=connection.cursor()
    id=request.session['uid']
    s1="select * from menu where cnid='%s'"%(id)
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'mid':row[0],'dish':row[2],'dtype':row[3],'category':row[4],'details':row[5],'amt':row[6]}
        cr.append(q)
    return render(request,'menu.html',{'cr':cr})

def MenuAct(request):
    cur=connection.cursor()
    id=request.session['uid']
    im=request.GET['im']
    dt=request.GET['dish']
    ct=request.GET['category']
    det=request.GET['det']
    amt=request.GET['amt']
    s2="insert into menu(cnid,dish,dtype,category,details,amt) values('%s','%s','%s','%s','%s','%s')"%(id,im,dt,ct,det,amt)
    cur.execute(s2)
    msg="<script>alert('Successfully Added');window.location='/menu/'</script>"
    return HttpResponse(msg)

def UVMenu(request):                                                                                       
    cur=connection.cursor()
    s1="select * from menu"
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'mid':row[0],'dish':row[1],'dtype':row[2],'category':row[3],'details':row[4],'amt':row[5]}
        cr.append(q)
    return render(request,'UVMenu.html',{'cr':cr})

def DeleteStaff(request):
    cur=connection.cursor()
    dname=request.GET['id']

    s1="delete from staff where sid='%s'"%(dname)
    cur.execute(s1)
    s2="delete from login where uid='%s'"%(dname)
    cur.execute(s2)
    msg="<script>alert('Deleted');window.location='/staff/'</script>"
    return HttpResponse(msg)

def DeleteMenu(request):
    cur=connection.cursor()
    dname=request.GET['id']
    cur.execute("delete from menu where mid='%s'"%(dname))
    msg="<script>alert('Deleted');window.location='/menu/'</script>"
    return HttpResponse(msg)

def UpdateMenu(request):
    cur=connection.cursor()
    mid=request.GET['id']
    sql="select * from menu where mid='%s'"%(mid)
    cur.execute(sql)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'mid':row[0],'cnid':row[1],'dish':row[2],'dtype':row[3],'category':row[4],'details':row[5],'amt':row[6]}
        cr.append(q)
    return render(request,'UpdateMenu.html',{'a':cr})

def UpdateMenuAct(request):
    cur=connection.cursor()
    mid=request.GET['mid']
    im=request.GET['im']
    dt=request.GET['dt']
    det=request.GET['det']
    amt=request.GET['amt']

    sql="update menu set details='%s',amt='%s' where mid='%s'"%(det,amt,mid)
    cur.execute(sql)
    msg="<script>alert('successfully updated');window.location='/menu/';</script>"
    return HttpResponse(msg)

def recipe(request):
    cur=connection.cursor()
    s="select * from recipe"
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'rid':row[0],'rname':row[2],'rdesp':row[3]}
        cr.append(q)
    return render(request,'recipe.html',{'cr':cr,})
def RecipeAct(request):
    cur=connection.cursor()
    uid=request.session['uid']
    rn=request.GET['rname']
    desp=request.GET['rdesp']
    s1="insert into recipe(cid,rname,rdesp) values('%s','%s','%s')"%(uid,rn,desp)
    cur.execute(s1)
    msg="<script>alert('Added');window.location='/recipe/'</script>"
    return HttpResponse(msg)

def UpdateRecipe(request):
    cur=connection.cursor()
    rid=request.GET['id']
    print(rid)
    s="select * from recipe where rid='%s'"%(rid)
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'rid':row[0],'rname':row[2],'rdesp':row[3]}
        cr.append(q)
    return render(request,'UpdateRecipe.html',{'cr':cr})

def UpdateRecipeAct(request):
    cur=connection.cursor()
    rid=request.GET['rid']
    rn=request.GET['rname']
    rdesp=request.GET['rdesp']
    q="update recipe set rname='%s',rdesp='%s' where rid='%s'"%(rn,rdesp,rid)
    cur.execute(q)
    msg="<script> alert('Updated successfully'); window.location='/recipe/'</script>"
    return HttpResponse(msg)

def DeleteRecipe(request):
    cur=connection.cursor()
    rname=request.GET['id']
    cur.execute("delete from recipe where rid='%s'"%(rname))
    msg="<script>alert('Deleted');window.location='/recipe/'</script>"
    return HttpResponse(msg)

def PreOrder(request):
    # print(today)
    cur=connection.cursor()
    mid=request.GET['mid']
    s1="select * from preorder"
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'pid':row[0],'fdate':row[1],'ldate':row[2],'qty':row[4],'mid':row[5],'status':row[7]}
        cr.append(q)
    return render(request,'PreOrder.html',{'mid':mid,'cr':cr,'today':today})

def PreOrderAct(request):
    cur=connection.cursor()
    uid=request.session['uid']
    id=request.GET['id']
    print(id)
    fd=request.GET['fd']
    ln=request.GET['ln']
    qn=request.GET['qn']
    
    s1="insert into preorder(fdate,ldate,cid,qty,mid,status) values('%s','%s','%s','%s','%s','pending')"%(fd,ln,uid,qn,id)
    cur.execute(s1)
    msg="<script>alert('Added');window.location='/PreOrder?mid="+id+"'</script>"
    return HttpResponse(msg)

def DeletePreOrder(request):
    cur=connection.cursor()
    dname=request.GET['ide']
    mid=request.GET['id']
    s="delete from preorder where pid='%s'"%(dname)
    cur.execute(s)
    msg="<script>alert('Deleted');window.location='/PreOrder?mid="+mid+"'</script>"
    return HttpResponse(msg)

def POview(request):                                                                                       
    cur=connection.cursor()
    s1="select * from preorder"
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'pid':row[0],'fdate':row[1],'ldate':row[2],'qty':row[4],'id':row[5],'tprice':row[6],'status':row[7]}
        cr.append(q)
    return render(request,'POview.html',{'cr':cr})

def AcceptPreOrder(request):
    cur=connection.cursor()
    pid=request.GET['id']
    print(pid)
    q="update preorder set status='Accepted' where pid='%s'"%(pid)
    cur.execute(q)
    msg="<script>alert('Accepted successfully');window.location='/POview/'</script>"
    return HttpResponse(msg)

def RejectPreOrder(request):
    cur=connection.cursor()
    pid=request.GET['id']
    print(pid)
    q="update preorder set status='Rejected' where pid='%s'"%(pid)
    cur.execute(q)
    msg="<script>alert('Rejected successfully');window.location='/POview/'</script>"
    return HttpResponse(msg)

def PayPreOrder(request):
    cur=connection.cursor()
    pid=request.GET['pid']
    mid=request.GET['mid']
    qty=request.GET['qty']
    print(pid)
    print(mid)
    s="Select * from menu where mid='%s'"%(mid)
    cur.execute(s)
    rs=cur.fetchall()
    for row in rs:
        price=row[4]
        print(price)
        tprice=int(qty) * int(price)
        print(tprice)
        s1="update preorder set tprice='%s' where pid='%s'"%(tprice,pid)
        cur.execute(s1)
    s1="select * from preorder where pid='%s'"%(pid)
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'pid':row[0],'fdate':row[1],'ldate':row[2],'qty':row[4],'mid':row[5],'tprice':row[6]}
        cr.append(q)
    return render(request,'PayPreOrder.html',{'pid':pid,'cr':cr})
    



def Order(request):
    cur=connection.cursor()
    id=request.GET['id']
    s1="select * from ordernow"
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'oid':row[0],'odate':row[1],'qty':row[3],'mid':row[4],'status':row[5]}
        cr.append(q)
    return render(request,'Order.html',{'id':id,'cr':cr,'today':today})

def OrderAct(request):
    cur=connection.cursor()
    uid=request.session['uid']
    od=today
    qty=request.GET['qty']
    id=request.GET['id']
    s1="insert into ordernow(odate,cid,qty,mid,status) values('%s','%s','%s','%s','Pending')" %(od,uid,qty,id)
    cur.execute(s1)
    msg="<script>alert('Added');window.location='/Order?id="+id+"'</script>"
    return HttpResponse(msg)

def DeleteOrder(request):
    cur=connection.cursor()
    dname=request.GET['ide']
    id=request.GET['id']
    s="delete from ordernow where oid='%s'"%(dname)
    cur.execute(s)
    msg="<script>alert('Deleted');window.location='/Order?id="+id+"'</script>"
    return HttpResponse(msg)

def Oview(request):                                                                                       
    cur=connection.cursor()
    s1="select * from ordernow"
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'oid':row[0],'odate':row[1],'qty':row[3],'id':row[4],'status':row[5]}
        cr.append(q)
    return render(request,'Oview.html',{'cr':cr})

def AcceptOrder(request):
    cur=connection.cursor()
    oid=request.GET['id']
    # print(oid)
    q="update ordernow set status='Accepted' where oid='%s'"%(oid)
    cur.execute(q)
    msg="<script>alert('Accepted successfully');window.location='/Oview/'</script>"
    return HttpResponse(msg)

def RejectOrder(request):
    cur=connection.cursor()
    oid=request.GET['id']
    # print(oid)
    q="update ordernow set status='Rejected' where oid='%s'"%(oid)
    cur.execute(q)
    msg="<script>alert('Rejected successfully');window.location='/Oview/'</script>"
    return HttpResponse(msg)

def SVMenu(request):                                                                                       
    cur=connection.cursor()
    s1="select * from menu"
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'mid':row[0],'mname':row[1],'dtype':row[2],'det':row[3],'amt':row[4]}
        cr.append(q)
    return render(request,'SVMenu.html',{'cr':cr})

def SPview(request):                                                                                       
    cur=connection.cursor()
    s1="select * from preorder"
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'pid':row[0],'fdate':row[1],'ldate':row[2],'qty':row[4],'id':row[5],'status':row[6]}
        cr.append(q)
    return render(request,'SPview.html',{'cr':cr})

def SOview(request):                                                                                       
    cur=connection.cursor()
    s1="select * from ordernow"
    cur.execute(s1)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'oid':row[0],'odate':row[1],'qty':row[3],'id':row[4],'status':row[5]}
        cr.append(q)
    return render(request,'SOview.html',{'cr':cr})
def canteenhome(request):
    return render(request,'canteenhome.html')   
def canteen(request):
    return render(request,'canteen.html')     
def canteenact(request):
    cur=connection.cursor()
    sn=request.GET['sn']
    add=request.GET['add']
    city=request.GET['city']
    ds=request.GET['ds']
    pin=request.GET['pin']
    phn=request.GET['phn']
    lno=request.GET['lno']
    veg=request.GET['veg']
    amt=request.GET['amt']
    em=request.GET['em']
    pwd=request.GET['pass']
    s3="insert into canteen(cname,addr,city,district,pin,phone,license,type,amt,email) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(sn,add,city,ds,pin,phn,lno,veg,amt,em)
    cur.execute(s3)
    sql="select max(cnid) as sid from canteen"
    cur.execute(sql)
    rs=cur.fetchall()
    for row in rs:
        sq="insert into login(uid,uname,upass,utype,status) values('%s','%s','%s','canteen','pending')"%(row[0],em,pwd)
        cur.execute(sq)
    msg="<script>alert('Added');window.location='/canteen/'</script>"
    return HttpResponse(msg)     
def aviewcanteen(request):
    cur=connection.cursor()
    s="select * from canteen inner join login on canteen.cnid=login.uid where login.utype='canteen'"
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'cnid':row[0],'cname':row[1],'addr':row[2],'city':row[3],'district':row[4],'pin':row[5],'phone':row[6],'license':row[7],'type':row[8],'amt':row[9],'status':row[16]}
        cr.append(q)
    return render(request,'aviewcanteen.html',{'cr':cr}) 
def accept(request):
    cur=connection.cursor()
    id=request.GET['id']
    sql="update login set status='approved' where uid='%s'"%(id)
    cur.execute(sql)
    msg="<script>alert('Status updated');window.location='/aviewcanteen/'</script>"
    return HttpResponse(msg)
def reject(request):
    cur=connection.cursor()
    id=request.GET['rid']
    sql="update login set status='Rejected' where uid='%s'"%(id)
    cur.execute(sql)
    msg="<script>alert('Status updated');window.location='/aviewcanteen/'</script>"
    return HttpResponse(msg)  
# def uvcanteen(request):
#     cur=connection.cursor()
#     uid=request.session['uid']
#     s="select * from canteen inner join request on canteen.cnid=request.cnid where request.cid='%s'"%(uid)
#     cur.execute(s)
#     rs=cur.fetchall()
#     cr=[]
#     for row in rs:
#         q={'cnid':row[0],'cname':row[1],'addr':row[2],'city':row[3],'district':row[4],'pin':row[5],'phone':row[6],'license':row[7],'email':row[8],'rqid':row[9],'rqdate':row[10],'cnid':row[11],'cid':row[12],'status':row[13]}
#         cr.append(q)
#     s1="select * from canteen where cnid not in(select cnid from request where cid='%s')"%(uid)
#     cur.execute(s1)
#     rs=cur.fetchall()
#     cr1=[]
#     for row in rs:
#         q1={'cnid':row[0],'cname':row[1],'addr':row[2],'city':row[3],'district':row[4],'pin':row[5],'phone':row[6],'license':row[7],'email':row[8]}
#         cr1.append(q1)    
#     return render(request,'uvcanteen.html',{'cr':cr,'cr1':cr1}) 


# def uvcanteen(request):
#     cur=connection.cursor()
#     uid=request.session['uid']
#     s="select * from canteen inner join login on canteen.cnid=login.uid where login.status='approved'"
#     cur.execute(s)
#     rs=cur.fetchall()
#     cr=[]
#     for row in rs:
#         q={'cnid':row[0],'cname':row[1],'addr':row[2],'city':row[3],'district':row[4],'pin':row[5],'phone':row[6],'license':row[7],'type':row[8],'amt':row[9],'email':row[10]}
#         cr.append(q)
#     return render(request,'uvcanteen.html',{'cr':cr})    
def uvcanteen(request):
    cur = connection.cursor()
    uid = request.session['uid']

    # Modify the query to exclude canteens with existing requests from the user
    s = """
        SELECT *
        FROM canteen
        INNER JOIN login ON canteen.cnid = login.uid
        WHERE login.status = 'approved'
          AND canteen.cnid NOT IN (
              SELECT cnid
              FROM request
              WHERE cid = %s
          )
    """
    cur.execute(s, [uid])
    rs = cur.fetchall()

    cr = []
    for row in rs:
        q = {
            'cnid': row[0],
            'cname': row[1],
            'addr': row[2],
            'city': row[3],
            'district': row[4],
            'pin': row[5],
            'phone': row[6],
            'license': row[7],
            'type': row[8],
            'amt': row[9],
            'email': row[10]
        }
        cr.append(q)

    return render(request, 'uvcanteen.html', {'cr': cr})



def uvcanteenorder(request):
    cur=connection.cursor()
    uid=request.session['uid']
    myobj = datetime.now()
    my=myobj.hour

    s="select * from canteen inner join request on canteen.cnid=request.cnid where request.cid='%s'"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'cnid':row[0],'cname':row[1],'addr':row[2],'city':row[3],'district':row[4],'pin':row[5],'phone':row[6],'license':row[7],'type':row[8],'amt':row[9],'email':row[10],'rqid':row[11],'rqdate':row[12],'cnid':row[13],'cid':row[14],'status':row[15],'pstatus':row[16]}
        cr.append(q)
 
    return render(request,'uvcanteenorder.html',{'cr':cr,'my':my}) 


def day(request):
    cur = connection.cursor()
    id = request.session['uid']
    sql="select * from timetable where cnid='%s'"%(id)
    cur.execute(sql)
    rs = cur.fetchall()
    list1 = []
    for row in rs:
        qq = {'did': row[0],'cnid': row[1], 'day': row[2], 'breakfast': row[3], 'lunch': row[4], 'dinner': row[5]}
        list1.append(qq)
    return render(request, 'day.html', {'list1': list1})


    # s1 = "select * from menu where cnid='%s'" % (id)
    # cur.execute(s1)
    # rs = cur.fetchall()
    # cr = []
    # for row in rs:
    #     q = {'mid': row[0], 'dish': row[2], 'dtype': row[3], 'category': row[4], 'details': row[5], 'amt': row[6]}
    #     cr.append(q)
    # today = date.today()
    # s = "select day.did, day.dtype, day.tdate, menu.dish from day inner join menu on day.dishid=menu.mid where day.cnid='%s' and day.tdate='%s'" % (id, today)
    # # s="select * from day inner join menu on "
    # cur.execute(s)
    # rs = cur.fetchall()
    # list1 = []
    # for row in rs:
    #     qq = {'did': row[0],'dtype': row[1], 'tdate': row[2], 'dish': row[3]}
    #     list1.append(qq)
    # return render(request, 'day.html', {'cr': cr, 'list1': list1})
def dayact(request):
    cur=connection.cursor()
    id=request.session['uid']
    day=request.GET['day']
    br=request.GET['br']
    ln=request.GET['lun']
    din=request.GET['din']
    # od=today
    s3="insert into timetable(cnid,day,breakfast,lunch,dinner) values('%s','%s','%s','%s','%s')"%(id,day,br,ln,din)
    cur.execute(s3)
    msg="<script>alert('successfully inserted');window.location='/day/'</script>"
    return HttpResponse(msg)
def Deleteday(request):
    cur=connection.cursor()
    # dname=request.GET['ide']
    id=request.GET['id']
    s1="delete from day where did='%s'"%(id)
    cur.execute(s1)
    msg="<script>alert('Deleted successfully');window.location='/day/'</script>"
    return HttpResponse(msg)
def viewmenu(request):
    cursor=connection.cursor()
    id=request.GET['id']
    today = date.today()
    # s="select day.did,day.cnid,day.dtype,day.tdate,menu.dish,menu.category,menu.details,menu.amt from day inner join menu on day.dishid=menu.mid where day.cnid='%s'and day.tdate='%s'" % (id, today)
    s="select  * from timetable where cnid='%s'"%(id)
    cursor.execute(s)
    rs=cursor.fetchall()
    cr=[]
    for row in rs:
        y={'did':row[0],'cnid':row[1],'day':row[2],'breakfast':row[3],'lunch':row[4],'dinner':row[5]}
        cr.append(y)
    return render(request,'viewmenu.html',{'cr':cr})
# def bookfood(request):
#     cursor=connection.cursor()
#     uid=request.session['uid']
#     cn=request.GET['id']
#     dish=request.GET['dis']
#     od=today
#     # qt=request.GET['qty']
#     s="insert into request(rqdate,cnid,cid,status,request)values('%s','%s','%s','%s','%s')"%(od,cn,uid,'pending',dish)
#     cursor.execute(s)
#     msg="<script>alert('successfully inserted');window.location='/confirmbook/'</script>"
#     return HttpResponse(msg)
# def confirmbook(request):
#     cursor=connection.cursor()
#     uid=request.session['uid']
#     s=""
#    
def requestcn(request):
    cn=request.GET['rid']
    return render(request,'requestcn.html',{'rid':cn})
def requestact(request):
    cursor=connection.cursor()
    uid=request.session['uid']
    id=request.GET['rid']
    od=today
    s1 = "SELECT * FROM request WHERE cnid='%s' AND cid='%s'" % (id, uid)
    cursor.execute(s1)
    rs = cursor.fetchall()
    if rs:
        msg = "<script>alert('You have already requested from this canteen');window.location='/uvcanteen/'</script>"
    else:
        s = "INSERT INTO request(rqdate, cnid, cid, status,pstatus) VALUES ('%s', '%s', '%s', '%s','%s')" % (od, id, uid,'pending','pending')
        cursor.execute(s)
        msg = "<script>alert('Successfully inserted');window.location='/uvcanteen/'</script>"

    return HttpResponse(msg)

def corder(request):
    cursor=connection.cursor()
    uid=request.session['uid']
    s ="SELECT request.rqid,request.rqdate,request.status,request.pstatus,request.cnid,request.cid,user.cid,user.cname,user.adr,user.office,user.phn FROM request INNER JOIN user on request.cid = user.cid WHERE request.cnid = '%s'" % (uid)
    cursor.execute(s)
    rs=cursor.fetchall()
    cr=[]
    for row in rs:
        y={'rqid':row[0],'rqdate':row[1],'status':row[2],'pstatus':row[3],'cnid':row[4],'cid':row[5],'cid':row[6],'cname':row[7],'adr':row[8],'office':row[9],'phn':row[10]}
        cr.append(y)
    return render(request,'corder.html',{'cr':cr}) 
def uaccept(request):
    cur=connection.cursor()
    id=request.GET['id']
    sql="update request set status='Approved' where rqid='%s'"%(id)
    cur.execute(sql)
    msg="<script>alert('Status updated');window.location='/corder/'</script>"
    return HttpResponse(msg)
def ureject(request):
    cur=connection.cursor()
    id=request.GET['rid']
    sql="update request set status='Rejected' where rqid='%s'"%(id)
    cur.execute(sql)
    msg="<script>alert('Status updated');window.location='/corder/'</script>"
    return HttpResponse(msg)  
def foodlist(request):
    cur=connection.cursor()
    uid=request.session['uid']
    cn=request.GET['s']
    s1="SELECT * FROM menu"
    # s1="SELECT * FROM menu WHERE mid = (SELECT MAX( mid )FROM menu )"

    cur.execute(s1)
    rs1=cur.fetchall()
    cr1=[]
    for row in rs1:
        # q1={'mid':row[0],'dish':row[2],'dtype':row[3],'category':row[4],'details':row[5]}
        q1={'mid':row[0],'dish':row[2],'dtype':row[3],'category':row[4],'details':row[5],'amt':row[6]}
        cr1.append(q1)
    s="select * from user where cid='%s'"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'cid':row[0],'cname':row[1],'adr':row[2],'city':row[3],'dist':row[4],'pin':row[5],'phn':row[6],'em':row[7]}
        cr.append(q)
    return render(request,'foodlist.html',{'cnid':cn,'cr':cr,'cr1':cr1})
def editaddr(request):
    cur=connection.cursor()
    # uid=request.session['uid']
    # cn=request.GET['tt']
    c=request.GET['qid']
    s="select * from user where cid='%s'"%(c)
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'cid':row[0],'cname':row[1],'adr':row[2],'city':row[3],'dist':row[4],'pin':row[5],'phn':row[6],'em':row[7]}
        cr.append(q)
    return render(request,'editaddr.html',{'cid':c,'cr':cr})
def updateeditaddr(request):
    cur=connection.cursor()
    qid=request.GET['cid']
    ad=request.GET['ad']
    ct=request.GET['ct']
    ds=request.GET['ds']
    pn=request.GET['pn']
    ph=request.GET['ph']
    s="update user set adr='%s' ,city='%s',dist='%s',pin='%s',phn='%s' where cid='%s'"%(ad,ct,ds,pn,ph,qid)
    cur.execute(s)
    msg="<script>alert('updated successfully');window.location='/UserReghome/'</script>"
    return HttpResponse(msg)  

def foodact(request):
    cur = connection.cursor()
    uid = request.session['uid']
    cnid = request.GET['cnid']
    now_utc = timezone.now()
    print(now_utc)
    ad = now_utc.date() - timedelta(days=1)
    ct_list = request.GET.getlist('dish')
    ds = request.GET['name1']
    ds1 = request.GET['name2']
    ds2 = request.GET['name3']
    ct_str = ','.join(ct_list)
    
    s3 = "INSERT INTO orderc(cid, date, cnid, dtype, address1, address2, address3, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (uid, ad, cnid, ct_str, ds, ds1, ds2, 'pending')

    try:
        cur.execute(s3, values)
        msg = "<script>alert('Successfully inserted');window.location='/uvcanteen/'</script>"
        return HttpResponse(msg)
    except Exception as e:
        # Handle the exception, you might want to print or log the error for debugging
        print(f"Error: {e}")
        return HttpResponse("Error occurred while inserting into the database.")
def uorder(request):
    cur=connection.cursor()
    uid=request.session['uid']
    s="select * from orderc inner join user on user.cid=orderc.cid where orderc.cnid='%s'"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'ocid':row[0],'cid':row[1],'date':row[2],'cnid':row[3],'dtype':row[4],'address1':row[5],'address2':row[6],'address3':row[7],'status':row[8],'cid':row[9],'cname':row[10],'adr':row[11],'office':row[12],'phn':row[13]}
        cr.append(q)
    s1="select * from staff where cnid='%s'"%(uid)
    cur.execute(s1)
    rs=cur.fetchall()
    cr1=[]
    for row in rs:
        q={'sid':row[0],'sname':row[1],'adr':row[2],'district':row[3],'pin':row[4],'phone':row[5],'email':row[6],'gender':row[7],'dob':row[8],'doj':row[8]}
        cr1.append(q)    
    return render(request,'uorder.html',{'cr':cr,'cr1':cr1})

def assign(request):
    cursor = connection.cursor()

    oid = request.GET['ocid']
    st= request.GET['st']
    s = "INSERT INTO assign(ocid,sid) VALUES ('%s', '%s')"%(oid,st)
    cursor.execute(s)
    sql="update orderc set status='assigned' where ocid='%s'"%(oid)
    cursor.execute(sql)
    h = "<script>alert('Assigned'); window.location='/canteenhome/'; </script>"
    return HttpResponse(h)
def staffviewassign(request):
    cur=connection.cursor()
    uid = request.session['uid']
    s="select * from assign inner join orderc on assign.ocid=orderc.ocid inner join user on user.cid=orderc.cid where assign.sid='%s'"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        q={'ssid':row[0],'ocid':row[1],'sid':row[2],'ocid':row[3],'cid':row[4],'date':row[5],'cnid':row[6],'dtype':row[7],'address1':row[8],'address2':row[9],'address3':row[10],'status':row[11],'cid':row[12],'cname':row[13],'phn':row[16],'email':row[17]}
        cr.append(q)
    return render(request,'staffviewassign.html',{'cr':cr})
def status(request):
	cursor = connection.cursor()
	oid=request.GET['oid']
	sts=request.GET['s']
	sql="update orderc set status='%s' WHERE ocid='%s'"%(sts,oid)
	cursor.execute(sql)
	h="<script>window.location='/staffviewassign/'; </script>"
	return HttpResponse(h)
def custvieworder(request):
    cur=connection.cursor()
    uid = request.session['uid']
    cnid=request.GET['si']
    # s="select * from user inner join orderc on user.cid=orderc.cid inner join canteen on canteen.cnid=orderc.cnid where user.cid='%s'"%(uid)
    s="select * from user where cid='%s'"%(uid)
    cur.execute(s)
    rs=cur.fetchall()
    cr=[]
    for row in rs:
        # q={'cid':row[0],'ocid':row[8],'date':row[10],'cnid':row[11],'dtype':row[12],'status':row[14],'cname':row[16]}
        q={'cid':row[0],'cname':row[1],'adr':row[2],'office':row[3],'phn':row[4],'em':row[5]}
        cr.append(q)
    return render(request,'custvieworder.html',{'cr':cr,'cnid':cnid})
def deleteorder(request):
    cur=connection.cursor()
    dname=request.GET['id']
    cur.execute("delete from orderc where ocid='%s'"%(dname))
    msg="<script>alert('Deleted');window.location='/menu/'</script>"
    return HttpResponse(msg)
def reports(request):
    cur = connection.cursor()
    cr = []
    sql = None  # Initialize sql outside the if statement

    if request.method == 'GET' and 'd1' in request.GET and 'd2' in request.GET:
        d1 = request.GET['d1']
        d2 = request.GET['d2']
        sql = "SELECT * FROM orderc WHERE date BETWEEN '%s' AND '%s'" % (d1, d2)

    if sql:
        cur.execute(sql)
        rs = cur.fetchall()

        for row in rs:
            q = {'ocid': row[0], 'cid': row[1], 'date': row[2], 'cnid': row[3], 'dtype': row[4], 'address': row[5],'status': row[6]}
            cr.append(q)

    return render(request, 'reports.html', {'cr': cr})

def areports(request):
    cur = connection.cursor()
    cr = []
    sql = None 
    if request.method == 'GET' and 'd1' in request.GET and 'd2' in request.GET:
        d1 = request.GET['d1']
        d2 = request.GET['d2']
        sql = "SELECT * FROM orderc WHERE date BETWEEN '%s' AND '%s' AND status='%s'"%(d1, d2,'assigned')
    if sql:
        cur.execute(sql)
        rs = cur.fetchall()
        for row in rs:
            q = {'ocid': row[0], 'cid': row[1], 'date': row[2], 'cnid': row[3], 'dtype': row[4], 'address': row[5],'status': row[6]}
            cr.append(q)
    return render(request, 'areports.html', {'cr': cr})
 

def dreports(request):
    cursor = connection.cursor()
    cr = []
    sql = None  # Initialize sql variable

    # if request.method == 'GET' and 'd1' in request.GET and 'd2' in request.GET:
    #     d1 = request.GET['d1']
    #     d2 = request.GET['d2']
    # sql = "SELECT * FROM orderc WHERE date BETWEEN '%s' AND '%s' AND status='%s'" % (d1, d2,'Delivered')
    sql = "SELECT * FROM orderc WHERE status='Delivered'"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for row in rs:
        q = {'ocid': row[0], 'cid': row[1], 'date': row[2], 'cnid': row[3], 'dtype': row[4], 'address': row[5], 'status': row[6]}
        cr.append(q)
    return render(request, 'dreports.html', {'cr': cr})
def preports(request):
    cursor = connection.cursor()
    cr = []
    sql = "SELECT * FROM orderc WHERE status='Packed'"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for row in rs:
        q = {'ocid': row[0], 'cid': row[1], 'date': row[2], 'cnid': row[3], 'dtype': row[4], 'address': row[5], 'status': row[6]}
        cr.append(q)
    return render(request, 'preports.html', {'cr': cr})
def dsreports(request):
    cursor = connection.cursor()
    cr = []
    sql = "SELECT * FROM orderc WHERE status='Dispatched'"
    cursor.execute(sql)
    rs = cursor.fetchall()
    for row in rs:
        q = {'ocid': row[0], 'cid': row[1], 'date': row[2], 'cnid': row[3], 'dtype': row[4], 'address': row[5], 'status': row[6]}
        cr.append(q)
    return render(request, 'dsreports.html', {'cr': cr})
def feedback(request):
    uid=request.session['uid']
    # cnid=request.GET['cnid']
    cursor=connection.cursor()
    s="select * from feedback "
    cursor.execute(s)
    cr=[]
    rs=cursor.fetchall()
    for row in rs:
        q1={'fid':row[0],'cid':row[1],'date':row[2],'Feedback':row[3]}
        cr.append(q1)
    return render(request,'feedback.html',{'cr':cr})
def feedact(request):
    cursor=connection.cursor()
    uid=request.session['uid']
    od=today
    # cid=request.GET['cnid']
    fd=request.GET['feed']
    sql="insert into feedback(cid,date,feedback)values('%s','%s','%s')"%(uid,od,fd)
    cursor.execute(sql)
    h = "<script>alert('Added'); window.location='/feedback/'; </script>"
    return HttpResponse(h)
def aviewfeedback(request):
    cursor=connection.cursor()
    s="select * from feedback"
    cursor.execute(s)
    cr=[]
    rs=cursor.fetchall()
    for row in rs:
        q={'fid':row[0],'cid':row[1],'date':row[2],'Feedback':row[3]}
        cr.append(q)
    return render(request,'aviewfeedback.html',{'cr':cr})

def payment(request):
    cnid=request.GET['s']
    rqid=request.GET['rqid']
    return render(request,'payment.html',{'cnid':cnid,'rqid':rqid})
def payact(request):
    cursor=connection.cursor()
    uid=request.session['uid']
    rqid=request.GET['rqid']
    cnid=request.GET['cnid']
    cid=request.GET['nm']
    fd=request.GET['lm']
    da=request.GET['date']
    amt=request.GET['amt']
    sql="insert into payment(uid,cnid,fname,lname,edate,amt)values('%s','%s','%s','%s','%s','%s')"%(uid,cnid,cid,fd,da,amt)
    cursor.execute(sql)
    u="update request set pstatus='advpaid' where rqid='%s'"%(rqid)
    cursor.execute(u)
    h = "<script>alert('Added'); window.location='/uvcanteenorder/'; </script>"
    return HttpResponse(h)
            
def compay(request):
    cid=request.GET['id']
    c=request.GET['cnid']
    r=request.GET['rq']
    return render(request,'compay.html',{'cid':cid,'c':c,'r':r})
    

# def calamt(request):
#     cursor = connection.cursor()
#     query = """
#         SELECT
#             MONTH(date) AS month,
#             SUM(CASE WHEN dtype LIKE '%Breakfast%' THEN 1 ELSE 0 END) AS breakfast_count,
#             SUM(CASE WHEN dtype LIKE '%Lunch%' THEN 1 ELSE 0 END) AS lunch_count,
#             SUM(CASE WHEN dtype LIKE '%Dinner%' THEN 1 ELSE 0 END) AS dinner_count
#         FROM
#             orderc
#         GROUP BY
#             MONTH(date)
#     """
def calamt(request):
    cursor = connection.cursor()
    adv=request.GET['adv']
    rq=request.GET['rqid1']
    uid=request.session['uid']
    sql="SELECT * FROM canteen INNER JOIN orderc ON canteen.cnid = orderc.cnid inner join user on orderc.cid=user.cid WHERE orderc.cid ='%s'"%(uid)
    cursor.execute(sql)
    cr=[]
    rs=cursor.fetchall()
    for row in rs:
        w={'cnid':row[0],'cname':row[1],'addr':row[2],'city':row[3],'district':row[4],'pin':row[5],'phone':row[6],'license':row[7],'type':row[8],'amt':row[9],'email':row[10],'ocid':row[11],'cid':row[12],'date':row[13],'cnid':row[14],'dtype':row[15],'address':row[16],'status':row[17],'cid':row[18],'cname':row[19],'adr':row[20],'office':row[21],'phn':row[22],'em':row[23]}
        cr.append(w)
       

    query = """
        SELECT
            MONTH(oc.date) AS month,
            SUM(CASE WHEN oc.dtype LIKE '%Breakfast%' THEN 1 ELSE 0 END * cn.amt) AS breakfast_amount,
            SUM(CASE WHEN oc.dtype LIKE '%Lunch%' THEN 1 ELSE 0 END * cn.amt) AS lunch_amount,
            SUM(CASE WHEN oc.dtype LIKE '%Dinner%' THEN 1 ELSE 0 END * cn.amt) AS dinner_amount,
            SUM(CASE WHEN oc.dtype LIKE '%Breakfast%' THEN 1 ELSE 0 END) AS breakfast_count,
            SUM(CASE WHEN oc.dtype LIKE '%Lunch%' THEN 1 ELSE 0 END) AS lunch_count,
            SUM(CASE WHEN oc.dtype LIKE '%Dinner%' THEN 1 ELSE 0 END) AS dinner_count,
            SUM((CASE WHEN oc.dtype LIKE '%Breakfast%' THEN 1 ELSE 0 END * cn.amt) +
                (CASE WHEN oc.dtype LIKE '%Lunch%' THEN 1 ELSE 0 END * cn.amt) +
                (CASE WHEN oc.dtype LIKE '%Dinner%' THEN 1 ELSE 0 END * cn.amt)) AS total_amount
        FROM
            orderc oc
        JOIN
            canteen cn ON oc.cnid = cn.cnid
        GROUP BY
            MONTH(oc.date)
    """

    cursor.execute(query)
    cr1=[]
    result = cursor.fetchall()

    # Process the result as needed
    for row in result:
        month = row[0]
        breakfast_amount = row[1]
        lunch_amount = row[2]
        dinner_amount = row[3]
        breakfast_count = row[4]
        lunch_count = row[5]
        dinner_count = row[6]
        total_amount = row[7]
        
        print(f"Month: {month}, Breakfast Amount: {breakfast_amount}, Lunch Amount: {lunch_amount}, Dinner Amount: {dinner_amount}, "
              f"Breakfast Count: {breakfast_count}, Lunch Count: {lunch_count}, Dinner Count: {dinner_count}, Total Amount: {total_amount}")
        if total_amount<1000:
            h = "<script>alert('No need of Payment');window.location='/uvcanteenorder/'; </script>"
            return HttpResponse(h)
            
        else:
            balance=total_amount-1000   
    return render(request,'calamt.html',{'cr':cr,'balance':balance,'adv':adv,'rq':rq}) 

def payact1(request):
    cursor = connection.cursor()
    cn = request.GET['cn']
    uid = request.session['uid']
    od = date.today()  
    month = od.month
    amt = request.GET['amt']

    sql = "insert into payc(cid, cnid, date, month, amount) values ('%s', '%s', '%s', '%s', '%s')" % (uid, cn, od, month, amt)
    cursor.execute(sql)

    h = "<script>alert('Added'); window.location='/uvcanteenorder/'; </script>"
    return HttpResponse(h)

def custmyorder(request):
    cursor=connection.cursor()
    uid = request.session['uid']
    s="select * from orderc inner join canteen on orderc.cnid=canteen.cnid where cid='%s'"%(uid)
    cursor.execute(s)
    cr=[]
    rs=cursor.fetchall()
    for row in rs:
        q={'ocid':row[0],'cid':row[1],'date':row[2],'cnid':row[3],'dtype':row[4],'adddress1':row[5],'adddress2':row[6],'adddress3':row[7],'status':row[8],'cid':row[9],'cname':row[10],'addr':row[11],'city':row[12],'district':row[13],'pin':row[14],'phone':row[15],'license':row[16],'type':row[17]}
        cr.append(q)
    return render(request,'custmyorder.html',{'cr':cr})
def upayhis(request):
    cursor=connection.cursor()
    uid = request.session['uid']
    s="SELECT * FROM payc INNER JOIN user ON payc.cid = user.cid where payc.cnid='%s'"%(uid)
    cursor.execute(s)
    cr=[]
    rs=cursor.fetchall()
    for row in rs:
        q={'pcid':row[0],'cid':row[1],'cnid':row[2],'date':row[3],'month':row[4],'amount':row[5],'cid':row[6],'cname':row[7],'adr':row[8],'office':row[9],'phn':row[10],'em':row[11]}
        cr.append(q)
    return render(request,'upayhis.html',{'cr':cr})
def userpayview(request):
    cursor=connection.cursor()
    uid = request.session['uid']
    s="SELECT * FROM payc where cid='%s'"%(uid)
    cursor.execute(s)
    cr=[]
    rs=cursor.fetchall()
    for row in rs:
        q={'pcid':row[0],'cid':row[1],'cnid':row[2],'date':row[3],'month':row[4],'amount':row[5]}
        cr.append(q)
    return render(request,'userpayview.html',{'cr':cr})






   


    

 



    













    



















 





    






    

