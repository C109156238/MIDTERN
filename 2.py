e=float(input("please input your bill:"))
s1=120*2.10
s2=210*3.02
ns2=210*2.68
s3=170*4.39
ns3=170*3.61
s4=200*4.97
ns4=200*4.01
if e<120 :
    s=e*2.10
    ns=e*2.10
if 120<e<331 :
    s=s1+(e-120)*3.02
    ns=s1+(e-120)*2.68

if 330<e<501 :
    s=s1+s2+(e-330)*4.39
    ns=s1+ns2+(e-330)*3.61

if 500<e<701 :
    s=s1+s2+s3+(e-500)*4.97
    ns=s1+ns2+ns3+(e-500)*4.01

if e>700 :
    s=s1+s2+s3+s4+(e-700)*5.63
    ns=s1+ns2+ns3+ns4+(e-700)*4.50
print("Summer months:%0.2f\nNon-Summer Months%0.2f"%(s,ns))