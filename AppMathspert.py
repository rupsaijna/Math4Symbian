import appuifw,e32,random

#defining quit
def quit():
	app_lock.signal()
appuifw.app.exit_key_handler=quit
	
#starting level 1
def callback_M1():
	appuifw.app.title=u"Mathspert Level 1"
	score=tot=cor=0
	appuifw.note(u"Each correct answer +10, Each wrong answer -5")
	prompt(score,1,tot,cor)
	
#starting level 2
def callback_M2():
	appuifw.app.title=u"Mathspert Level 2"
	score=tot=cor=0
	appuifw.note(u"Each correct answer +20, Each wrong answer -10")
	prompt(score,2,tot,cor)

#starting level 3
def callback_M3():
	appuifw.app.title=u"Mathspert Level 3"
	score=tot=cor=0
	appuifw.note(u"Each correct answer +30, Each wrong answer -15")
	prompt(score,3,tot,cor)
	
#starting level 4
def callback_M4():
	appuifw.app.title=u"Mathspert Level 4"
	score=tot=cor=0
	appuifw.note(u"Each correct answer +40, Each wrong answer -20")
	prompt(score,4,tot,cor)
	
#prompt user to continue...
def prompt(scr,lev,tot,cor):
	ind="y"
	if(tot!=0):
		ind=appuifw.query(u"Go on? Y/N","text")
	if ind=="y" or ind=="Y":
		useinp(scr,lev,tot,cor)
	else:
		givescore(scr,lev,tot,cor)

#ask question
def useinp(scre,lev,tot,cor):
	str,rs=process(lev)
	use=appuifw.query(str,"number")
	check(use,rs,scre,lev,tot,cor)

#middle process to create equation
def process(lev):
	sign=(u"+",u"-",u"*",u"/")
	sig1=random.randint(1,4)
	if lev<3:
		num1,num2=operand(lev)
		num1,num2,res=lev12(num1,num2,sig1,lev)
		str=num1+sign[sig1-1]+num2
		return str,res
	if lev==3:
		num1,num2,num3=operand(lev)
		sig2=random.randint(1,4)
		num1,num2,num3,res=lev3(num1,num2,num3,sig1,sig2,lev)
		str=num1+sign[sig1-1]+num2+sign[sig2-1]+num3
		return str,res
	if lev==4:
		nop=random.randint(2,3)
		sig2=random.randint(1,4)
		sig3=random.randint(1,4)
		num1,num2,num3,num4=operand(lev)
		if nop==2:
			num1,num2,num3,res=lev4(num1,num2,num3,num4,sig1,sig2,sig3,lev,nop)
			str=num1+sign[sig1-1]+num2+sign[sig2-1]+num3
			return str,res
		else:
			num1,num2,num3,num4,res=lev4(num1,num2,num3,num4,sig1,sig2,sig3,lev,nop)
			str=u"("+num1+sign[sig1-1]+num2+u")"+sign[sig2-1]+u"("+num3+sign[sig3-1]+num4+u")"
			return str,res
	
#operands
def operand(lev):
	if lev==1:
		end=10
	elif lev==2:
		end=100
	elif lev==3:
		end=1000
	else:
		end=5000
	num1=random.randint(1,end)
	num2=random.randint(1,end)
	num3=random.randint(1,end)
	num4=random.randint(1,end)
	if lev<3 or lev==7:
		return num1,num2
	elif lev==3 or lev==6:
		return num1,num2,num3
	elif lev==4:
		return num1,num2,num3,num4

#level one 	and two
def lev12(num1,num2,sig,lev):
	num1=int(num1)
	num2=int(num2)
	if sig==1:
		res=num1+num2
	if sig==2:
		res=num1-num2
		while res<0:
			num1,num2=operand(lev)
			res=num1-num2
	if sig==3:
		res=num1*num2
		while res>200:
			num1,num2=operand(lev)
			res=num1*num2
	if sig==4:
		resf=float(num1)/float(num2)
		while resf-int(resf)!=0 or num1<num2 or (lev>=4 and resf>20) :
			num1,num2=operand(lev)
			resf=float(num1)/float(num2)
		res=resf
	num1=str(num1)
	num2=str(num2)
	return num1,num2,res
	
#level 3
def lev3(num1,num2,num3,sig1,sig2,lev):
	num1=int(num1)
	num2=int(num2)
	num3=int(num3)
	if sig1+sig2==2:
		res=num1+num2+num3
	if sig1==1 and sig2==2:
		res=num1+num2-num3
		while res<0:
			num1,num2,num3=operand(lev)
			res=num1+num2-num3
	if (sig1==1 and sig2==3):
		while num2*num3>300:
			num1,num2,num3=operand(lev)
			res=num2*num3
		res=res+num1
	if(sig1==1 and sig2==4):
		resf=float(num2)/float(num3)
		while resf-int(resf)!=0 or num2<num3:
			num1,num2,num3=operand(lev)
			resf=float(num2)/float(num3)
		res=resf+num1
		
	if (sig1==2 and sig2==1) or (sig1==2 and sig2==2):
		if sig1+sig2==3:	
			res=num1-num2+num3
		else:
			res=num1-num2-num3
		while res<0:
			num1,num2,num3=operand(lev)
			if sig1+sig2==3:	
				res=num1-num2+num3
			else:
				res=num1-num2-num3
	if (sig1==2 and sig2==3):
		while num2*num3> 300 or num2*num3>num1:
			num1,num2,num3=operand(lev)
		res=num1-num2*num3
	if (sig1==2 and sig2==4):
		resf=float(num2)/float(num3)
		while resf-int(resf)!=0 or num2<num3 or (num2/num3)>num1:
			num1,num2,num3=operand(lev)
			resf=float(num2)/float(num3)
		res=num1-resf
	
	if (sig1==3 and sig2==1):
		while num1*num2>300:
			num1,num2,num3=operand(lev)
		res=num1*num2+num3
	if (sig1==3 and sig2==2):
		while num1*num2>300 or (num1*num2)<num3:
			num1,num2,num3=operand(lev)
		res=num1*num2-num3
	if(sig1==3 and sig2==3):
		res=num1*num2*num3
		while res>300:
			num1,num2,num3=operand(lev)
			res=num1*num2*num3
	if sig1==3 and sig2==4:
		resf=float(num2)/float(num3)
		while resf-int(resf)!=0 or num2<num3 or resf*num1>300:
			num1,num2,num3=operand(lev)
			resf=float(num2)/float(num3)
		res=resf*num1
		
	if sig1==4 and sig2==1:
		resf=float(num1)/float(num2)
		while resf-int(resf)!=0 or (num1<num2) or resf>100:
			num1,num2,num3=operand(lev)
			resf=float(num1)/float(num2)
		res=resf+num3
	if sig1==4 and sig2==2:
		resf=float(num1)/float(num2)
		while resf-int(resf)!=0 or (num1<num2) or resf<num3 or resf>100:
			num1,num2,num3=operand(lev)
			resf=float(num1)/float(num2)
		res=resf-num3
	if sig1==4 and sig2==3:
		resf=float(num1)/float(num2)*num3
		while resf-int(resf)!=0 or (num1<num2) or resf>300 or resf/num3>100:
			num1,num2,num3=operand(lev)
			resf=float(num1)/float(num2)*num3
		res=resf
	if sig1==4 and sig2==4:
		resf1=float(num2)/float(num3)
		resf2=float(num1)/resf1
		while resf1-int(resf1)!=0 or resf2-int(resf2)!=0 or (num1<num2) or num2<num3 or resf>100 :
			num1,num2,num3=operand(lev)
			resf1=float(num2)/float(num3)
			resf2=float(num1)/resf1
		res=resf2
	num1=str(num1)
	num2=str(num2)
	num3=str(num3)
	return num1,num2,num3,res
				
#level 4
def lev4(num1,num2,num3,num4,sig1,sig2,sig3,lev,nop):
	num1=int(num1)
	num2=int(num2)
	num3=int(num3)
	num4=int(num4)
	if nop==2:
		num1,num2,num3,res=lev3(num1,num2,num3,sig1,sig2,6)
		return num1,num2,num3,res
	if nop==3:
		num1,num2,res1=lev12(num1,num2,sig1,7)
		num3,num4,res2=lev12(num1,num2,sig3,7)
		res1=int(res1)
		res2=int(res2)
		if sig2==1:
			res=res1+res2
		if sig2==2:
			while res1<res2:
				num1,num2,num3,num4=operand(lev)
				num1,num2,res1=lev12(num1,num2,sig1,7)
				num3,num4,res2=lev12(num1,num2,sig3,7)
			res=res1-res2
		if sig2==3:
			while res1*res2>300:
				num1,num2,num3,num4=operand(lev)
				num1,num2,res1=lev12(num1,num2,sig1,7)
				num3,num4,res2=lev12(num1,num2,sig3,7)
			res=res1*res2
		if sig2==4:
			resf=float(res1)/float(res2)
			while resf-int(resf)!=0 or res1<res2:
				num1,num2,num3,num4=operand(lev)
				num1,num2,res1=lev12(num1,num2,sig1,7)
				num3,num4,res2=lev12(num1,num2,sig3,7)
				resf=float(res1)/float(res2)
			res=resf
		num1=str(num1)
		num2=str(num2)
		num3=str(num3)
		num4=str(num4)
		return num1,num2,num3,num4,res
			
			

				
#check result and input
def check(use,res,scr,lev,tot,cor):
	tot+=1
	if(use==res):
		appuifw.note(u"correct",'conf')
		scr+=10
		cor+=1
	else:
		appuifw.note(u"wrong",'error')
		scr-=5
	prompt(scr,lev,tot,cor)

#final score
def givescore(scr,lev,tot,cor):
	scr=scr*lev
	scr=str(scr)
	tot=str(tot)
	cor=str(cor)
	val=appuifw.query(u"SCORE: "+scr+u"\nQuestions:"+tot+u",Correct:"+cor+u"\nEnter name ","text")
	tot=int(tot)
	cor=int(cor)
	if cor<=tot/3:
		appuifw.note(u"You must practise more "+str(val)+u"!")
	elif cor<tot/2:
		appuifw.note(u"Getting on!Keep practising "+str(val)+u"!")
	elif cor<tot*2/3:
		appuifw.note(u"Good work "+str(val)+u"!Litte more practise please!")
	elif cor<tot:
		appuifw.note(u"This is a fine performance "+str(val)+u"!")
	else:
		appuifw.note(u"You are a genius "+str(val)+u"!")
	appuifw.note(u"THANK YOU FOR PLAYING "+str(val)+"!!")	

#The application's menu
appuifw.app.menu=[(u"Mathspert",((u"Level 1",callback_M1),(u"Level 2",callback_M2),(u"Level 3",callback_M3),(u"Level 4",callback_M4)))]
app_lock=e32.Ao_lock()
app_lock.wait()
