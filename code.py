import pywhatkit as kt
from covid import Covid
c=Covid()


a =c.get_status_by_country_id(80) #india
ia=a.get('confirmed')
id=a.get('deaths')
ir=a.get('recovered')
c1="india"


b=c.get_status_by_country_id(86) #italy
ita=b.get('confirmed')
itd=b.get('deaths')
itr=b.get('recovered')
c2="italy"


cc=c.get_status_by_country_id(37) #china
ca=cc.get('confirmed')
cd=cc.get('deaths')
cr=cc.get('recovered')
c3="china"


d=c.get_status_by_country_id(165) #spain
sa=d.get('confirmed')
sd=d.get('deaths')
sr=d.get('recovered')
c4="spain"


e=c.get_status_by_country_id(63) #france
fa=e.get('confirmed')
fd=e.get('deaths')
fr=e.get('recovered')
c5="france"

g=c.get_status_by_country_id(24) #Brazil
ba=g.get('confirmed')
bd=g.get('deaths')
gr=g.get('recovered')
c7="Brazil"


h=c.get_status_by_country_id(145) #Russia
ra=h.get('confirmed')
rd=h.get('deaths')
rr=h.get('recovered')
c8="Russia"


i=c.get_status_by_country_id(181) #turkey
ta=i.get('confirmed')
td=i.get('deaths')
tr=i.get('recovered')
c9="turkey"


j=c.get_status_by_country_id(186) #United Kingdom
uka=j.get('confirmed')
ukd=j.get('deaths')
ukr=j.get('recovered')
c10="United Kingdom"


k=c.get_status_by_country_id(67) #germany
gea=k.get('confirmed')
ged=k.get('deaths')
ger=k.get('recovered')
c11="Germany"


l=c.get_status_by_country_id(82) #iran
ira=l.get('confirmed')
ird=l.get('deaths')
irr=l.get('recovered')
c12="Iran"


m=c.get_status_by_country_id(116) #mexico
ma=m.get('confirmed')
md=m.get('deaths')
mr=m.get('recovered')
c13="Mexico"


n=c.get_status_by_country_id(33) #canada
caa=n.get('confirmed')
cad=n.get('deaths')
car=n.get('recovered')
c14="canada"


o=c.get_status_by_country_id(134) #pakistan
pa=o.get('confirmed')
pd=o.get('deaths')
pr=o.get('recovered')
c15="pakistan"


p=c.get_status_by_country_id(88) #japan
ja=p.get('confirmed')
jd=p.get('deaths')
jr=p.get('recovered')
c16="japan"


q=c.get_status_by_country_id(125) #nepal
na=q.get('confirmed')
nd=q.get('deaths')
nr=q.get('recovered')
c17="nepal"



r=c.get_status_by_country_id(153) #Saudi Arabia
saa=r.get('confirmed')
sad=r.get('deaths')
sar=r.get('recovered')
c18="Saudi Arabia"


s=c.get_status_by_country_id(166) #sri lanka
sra=s.get('confirmed')
srd=s.get('deaths')
srr=s.get('recovered')
c19="Sri lanka"


t=c.get_status_by_country_id(158) #singapur
sia=t.get('confirmed')
sid=t.get('deaths')
sir=t.get('recovered')
c20="singapur"


z=[ia,ita,ca,sa,fa,ba,ra,ta,uka,gea,ira,ma,caa,pa,ja,na,saa,sra,sia]
y=[c1,c2,c3,c4,c5,c7,c8,c9,c10,c12,c13,c14,c15,c16,c17,c18,c19,c20]
x=[id,itd,cd,sd,fd,bd,rd,td,ukd,ged,ird,md,cad,pd,jd,nd,sad,srd,sid]
w=[ir,itr,cr,sr,fr,gr,rr,tr,ukr,ger,irr,mr,car,pr,jr,nr,sar,srr,sir]
confirmed=0
country=""
death=0
recovered=0
for i in range(0,19):
    if confirmed<z[i]:
        confirmed=z[i]
        country=y[i]
        death=x[i]
        recovered=w[i]
choice=input("enterChoice mail_or_whatsapp :")
if(choice=='whatsapp'):
    stri="Hello this is your covid data friend \n"+"Present " +str(country)+ " has the highest no. of active cases in the world as: \n confirmed cases: " +str(confirmed) +"\n Total deaths till now:"+str(death)+"\n Total recovered:"+str(recovered)
    phone=input("enter phone number to send the info(add country code): ")
    hr=int(input("enter hr: "))
    min=int(input("enter min(don't include 0 for single digit): "))
    kt.sendwhatmsg(phone,stri,hr,min)
if(choice=='email'):
    stri = "Hello this is your covid data friend \n" + "Present " + str(country) + " has the highest no. of active cases in the world as: \n confirmed cases: " + str(confirmed) + "\n Total deaths till now:" + str(death) + "\n Total recovered:" + str(recovered)
    email=input("enter-email:")
    password=input("enter-password:")
    tomail=input("enter reciver:")
    kt.send_mail(email,password,"covid data update",stri,tomail)
else:
    print("invalid choice")
