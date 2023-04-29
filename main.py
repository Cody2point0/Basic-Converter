12#####housekeeping#####
import math
import os
import random
import time
#####special#######################################
def clear():
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')
def loading(amount):
  for i in range(amount):
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                            Loading")
    print("                              .")
    time.sleep(1)
    clear()
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                            Loading")
    print("                              ..")
    time.sleep(1)
    clear()
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                            Loading")
    print("                              ...")
    time.sleep(1)
    clear()
#####imperial#########################################
def inft(inches):
  return inches/12
def ftin(feet):
  return feet*12
def ydft(yards):
  return yards*3
def ftyd(feet):
  return feet/3
def miyd(miles):
  return miles*1760
def ydmi(yards):
  return yards/1760
def miin(miles):
  return miles*63360
def mift(miles):
  return miles*5280
def ftmi(feet):
  return feet/5280
def inmi(inches):
  return inches/63360
def inyd(inches):
  return inches/36
def ydin(yards):
  return yards*36
#####metric###########################################
def mmmm(milimeters):
  return milimeters*1
def mmcm(milimeters):
  return milimeters/10
def mmdim(milimeters):
  return milimeters/100
def mmmet(milimeters):
  return milimeters/1000
def mmdam(milimeters):
  return milimeters/10000
def mmhec(milimeters):
  return milimeters/100000
def mmkm(milimeters):
  return milimeters/1000000
def cmmm(centimeters):
  return centimeters*10
def cmcm(centimeters):
  return centimeters*1
def cmdim(centimeters):
  return centimeters/10
def cmmet(centimeters):
  return centimeters/100
def cmdam(centimeters):
  return centimeters/1000
def cmhec(centimeters):
  return centimeters/10000
def cmkm(centimeters):
  return centimeters/100000
def dimm(decimeters):
  return decimeters*100
def dicm(decimeters):
  return decimeters*10
def didi(decimeters):
  return decimeters*1
def dime(decimeters):
  return decimeters/10
def didam(decimeters):
  return decimeters/100
def dihec(decimeters):
  return decimeters/1000
def dikm(decimeters):
  return decimeters/10000
def metmm(meters):
  return meters*1000
def metcm(meters):
  return meters*100
def metdi(meters):
  return meters*10
def metmet(meters):
  return meters*1
def metdam(meters):
  return meters/10
def methec(meters):
  return meters/100
def metkm(meters):
  return meters/1000
def dammm(decameters):
  return decameters*10000
def damcm(decameters):
  return decameters*1000
def damdi(decameters):
  return decameters*100
def dammet(decameters):
  return decameters*10
def damdam(decameters):
  return decameters*1
def damhec(decameters):
  return decameters/10
def damkm(decameters):
  return decameters/100
def hecmm(hectometers):
  return hectometers*100000
def heccm(hectometers):
  return hectometers*10000
def hecdi(hectometers):
  return hectometers*1000
def hecmet(hectometers):
  return hectometers*100
def hecdam(hectometers):
  return hectometers*10
def hechec(hectometers):
  return hectometers*1
def heckm(hectometers):
  return hectometers/10
def kmmm(kilometers):
  return kilometers*1000000
def kmcm(kilometers):
  return kilometers*100000
def kmdi(kilometers):
  return kilometers*10000
def kmmet(kilometers):
  return kilometers*1000
def kmdam(kilometers):
  return kilometers*100
def kmhec(kilometers):
  return kilometers*10
def kmkm(kilometers):
  return kilometers*1
#####metric-imperial and imperial-metric conversions##
def mmin(milimeters):
  return milimeters/25.4
def mmft(milimeters):
  return milimeters/305
def mmyd(milimeters):
  return milimeters/914
def mmmi(milimeters):
  return milimeters/1609344
def cmin(centimeters):
  return centimeters/2.54
def cmft(centimeters):
  return centimeters/30.48
def cmyd(centimeters):
  return centimeters/91.44
def cmmi(centimeters):
  return centimeters/160934.4
def diin(decimeter):
  return decimeter*3.397
def dift(decimeter):
  return decimeter/3.048
def diyd(decimeter):
  return decimeter/9.144
def dimi(decimeter):
  return decimeter/16093.44
def metin(meter):
  return meter*39.37
def metft(meter):
  return meter*3.281
def metyd(meter):
  return meter*1.094
def metmi(meter):
  return meter/1609
def damin(decameters):
  return decameters*393.701
def damft(decameters):
  return decameters*32.8084
def damyd(decameters):
  return decameters*10.9361
def dammi(decameters):
  return decameters*0.00621371
def hecin(hectometers):
  return hectometers*3937.01
def hecft(hectometers):
  return hectometers*3937
def hecyd(hectometers):
  return hectometers*109.361
def hecmi(hectometer):
  return hectometer/16.093
def kmin(kilometers):
  return kilometers*39370.1
def kmft(kilometers):
  return kilometers*3280.84
def kmyd(kilometers):
  return kilometers*1093.61
def kmmi(kilometers):
  return kilometers*0.621371
def inmm(inches):
  return inches*25.4
def incm(inches):
  return inches*2.54
def indi(inches):
  return  inches*0.254
def inmet(inches):
  return inches*0.0254
def indam(inches):
  return inches*0.00254
def inhec(inches):
  return inches*0.000254
def inkm(inches):
  return inches/39370
def ftmm(feet):
  return feet*304.8
def ftcm(feet):
  return feet*30.48
def ftdi(feet):
  return feet*3.048
def ftmet(feet):
  return feet*0.3048
def ftdam(feet):
  return feet*0.03048
def fthec(feet):
  return feet*0.003048
def ftkm(feet):
  return feet*0.0003048
def ydmm(yards):
  return yards*914.4
def ydcm(yards):
  return yards*91.44
def yddi(yards):
  return yards*9.144
def ydmet(yards):
  return yards*0.9144
def yddam(yards):
  return yards*0.09144
def ydhec(yards):
  return yards*0.009144
def ydkm(yards):
  return yards*0.0009144
def mimm(miles):
  return miles*1609340
def micm(miles):
  return miles*160934.0
def midi(miles):
  return miles*16093.40
def mimet(miles):
  return miles*1609.340
def midac(miles):
  return miles*160.9340
def mihec(miles):
  return miles*16.09340
def mikm(miles):
  return miles*1.609340
#####tempature#####
def CF(celceius):
  c = celceius * (9/5)
  cc = c + 32
  return cc
def FC(farinhight):
  f = farinhight-32
  ff = 5/9
  return f*ff
def FK(farinhight):
  fff = farinhight-32
  ffff = 5/9
  return ffff+273.15
def KF(farinhight):
  fff = farinhight-32
  ffff = 5/9
  return ffff-273.15
def CK(celsius):
  return celsius+273.15
def KC(kelvin):
  return kelvin-273.15
#####time#############################################
def msms(miliseconds):
  return miliseconds*1
def mssec(miliseconds):
  return miliseconds/1000
def msmin(miliseconds):
  return miliseconds/60000
def msh(miliseconds):
  return miliseconds/3600000
def msday(miliseconds):
  return miliseconds/86400000
def msw(miliseconds):
  return miliseconds/604800000
def msm(miliseconds):
  return miliseconds/2628000000
def msy(miliseconds):
  return miliseconds/31540000000
def msdy(miliseconds):
  return miliseconds/315400000000
def mscy(miliseconds):
  return miliseconds/3154000000000
def msmy(miliseconds):
  return miliseconds/31540000000000
def secms(seconds):
  return seconds*1000
def secsec(seconds):
  return seconds*1
def secmin(seconds):
  return seconds/60
def sech(seconds):
  return seconds/3600
def secd(seconds):
  return seconds/86400
def secwk(seconds):
  return seconds/604800
def secmo(seconds):
  return seconds/2628000
def secy(seconds):
  return seconds/31540000
def secdy(seconds):
  return seconds/315400000
def seccy(seconds):
  return seconds/3154000000
def secmy(seconds):
  return seconds/31540000000
def minms(minutes):
  return minutes*60000
def minsec(minutes):
  return minutes*60
def minmin(minutes):
  return minutes*1
def minh(minutes):
  return minutes/60
def mind(minutes):
  return minutes/1440
def minw(minutes):
  return minutes/10080
def minm(minutes):
  return minutes/43800
def miny(minutes):
  return minutes/525600
def mindy(minutes):
  return minutes/5256000
def mincy(minutes):
  return minutes/52560000
def minmy(minutes):
  return minutes/525600000
def hms(hours):
  return hours*3600000
def hsec(hours):
  return hours*3600
def hmin(hours):
  return hours*60
def hh(hours):
  return hours*1 
def hd(hours):
  return hours/24 
def hwk(hours):
  return hours/168
def hm(hours):
  return hours/730
def hy(hours):
  return hours/8760
def hdy(hours):
  return hours/87600
def hcy(hours):
  return hours/876000
def hmy(hours):
  return hours/8760000
def dms(days):
  return days*86400000
def dsec(days):
  return days*86400
def dmin(days):
  return days*1440
def dh(days):
  return days*24
def dd(days):
  return days*1
def dw(days):
  return days/7
def dm(days):
  return days/30.417
def dy(days):
  return days/365.25
def ddy(days):
  return days*3652.5
def dcy(days):
  return days*36525
def dmy(days):
  return days*365250
def wms(weeks):
  return weeks*604800000
def wsec(weeks):
  return weeks*604800
def wmin(weeks):
  return weeks*10080
def wh(weeks):
  return weeks*168
def wd(weeks):
  return weeks*7
def ww(weeks):
  return weeks*1
def wm(weeks):
  return weeks/4.345
def wy(weeks):
  return weeks/52.143
def wdy(weeks):
  return weeks/521
def wcy(weeks):
  return weeks/5214
def wmy(weeks):
  return weeks/52143
def mms(months):
  return months*2628000000
def msec(months):
  return months*2628000
def mmin(months):
  return months*43800
def mh(months):
  return months*730
def md(months):
  return months*30.417
def mw(months):
  return months*4.345
def mm(months):
  return months*1
def my(months):
  return months/12
def mdy(months):
  return months/120
def mcy(months):
  return months/1200
def mmy(months):
  return months/12000
def yms(years):
  return years*31540000000
def ysec(years):
  return years*31540000
def ymin(years):
  return years*525600
def yh(years):
  return years*8760
def yd(years):
  return years*365.25
def yw(years):
  return years*52.143
def ym(years):
  return years*12
def yy(years):
  return years*1
def ydy(years):
  return years/10
def ycy(years):
  return years/100
def ymy(years):
  return years/1000
def dyms(decades):
  return decades*315400000000
def dysec(decades):
  return decades*315400000
def dymin(decades):
  return decades*5256000
def dyh(decades):
  return decades*87600
def dyd(decades):
  return decades*3652.5
def dyw(decades):
  return decades*521.429
def dym(decades):
  return decades*120
def dyy(decades):
  return decades*10
def dydy(decades):
  return decades*1
def dycy(decades):
  return decades/10
def dymy(decades):
  return decades/100
def cyms(centries):
  return centries*3154000000000
def cysec(centries):
  return centries*315000000
def cymin(centries):
  return centries*52560000
def cyh(centries):
  return centries*876000
def cyd(centries):
  return centries*36525
def cyw(centries):
  return centries*5214.29
def cym(centries):
  return centries*1200
def cyy(centries):
  return centries*100
def cydy(centries):
  return centries*10
def cycy(centries):
  return centries*1
def cymy(centries):
  return centries/10
def myms(millenium):
  return millenium*31540000000000
def mysec(millenium):
  return millenium*31540000000
def mymin(millenium):
  return millenium*525600000
def myh(millenium):
  return millenium*8760000
def myd(millenium):
  return millenium*365250
def myw(millenium):
  return millenium*52124.9
def mym(millenium):
  return millenium*12000
def myy(millenium):
  return millenium*1000
def mydy(millenium):
  return millenium*100
def mycy(millenium):
  return millenium*10
def mymy(millenium):
  return millenium*1
#####Liquid metric and imperial#######################
def mlml(mililiters):
  return mililiters*1
def mlcl(mililiters):
  return mililiters/10
def mldil(mililiters):
  return mililiters/100
def mll(mililiters):
  return mililiters/1000
def mldal(mililiters):
  return mililiters/10000
def mlhecl(mililiters):
  return mililiters/100000
def mlkl(mililiters):
  return mililiters/1000000
def clml(centiliters):
  return centiliters*10
def clcl(centiliters):
  return centiliters*1
def cldil(centiliters):
  return centiliters/10
def cll(centiliters):
  return centiliters/100
def cldal(centiliters):
  return centiliters/1000
def clhecl(centiliters):
  return centiliters/10000
def clkl(centiliters):
  return centiliters/100000
def dilml(deciliters):
  return deciliters*100
def dilcl(deciliters):
  return deciliters*10
def dildil(deciliters):
  return deciliters*1
def dill(deciliters):
  return deciliters/10
def dildal(deciliters):
  return deciliters/100
def dilhecl(deciliters):
  return deciliters/1000
def dilkl(deciliters):
  return deciliters/10000
def lml(liters):
  return liters*1000
def lcl(liters):
  return liters*100
def ldil(liters):
  return liters*10
def ll(liters):
  return liters*1
def ldal(liters):
  return liters/10
def lhecl(liters):
  return liters/100
def lkl(liters):
  return liters/1000
def dalml(decaliters):
  return decaliters*10000
def dalcl(decaliters):
  return decaliters*1000
def daldil(decaliters):
  return decaliters*100
def dall(decaliters):
  return decaliters*10
def daldal(decaliters):
  return decaliters*1
def dalhecl(decaliters):
  return decaliters/10
def dalkl(decaliters):
  return decaliters/100
def heclml(hectoliters):
  return hectoliters*100000
def heclcl(hectoliters):
  return hectoliters*10000
def hecldil(hectoliters):
  return hectoliters*1000
def hecll(hectoliters):
  return hectoliters*100
def hecldal(hectoliters):
  return hectoliters*10
def heclhecl(hectoliters):
  return hectoliters*1
def heclkl(hectoliters):
  return hectoliters/10
def klml(kiloliters):
  return kiloliters*1000000
def klcl(kiloliters):
  return kiloliters*100000
def kldil(kiloliters):
  return kiloliters*10000
def kll(kiloliters):
  return kiloliters*1000
def kldal(kiloliters):
  return kiloliters*100
def klhecl(kiloliters):
  return kiloliters*10
def klkl(kiloliters):
  return kiloliters*1
#####imperial#########################################
def gg(gallons):
  return gallons*1
def gq(gallons):
  return gallons*4
def gp(gallons):
  return gallons*8
def gcu(gallons):
  return gallons*16
def go(gallons):
  return gallons*128
def qg(quarts):
  return quarts/4
def qq(quarts):
  return quarts*1
def qp(quarts):
  return quarts*2
def qcu(quarts):
  return quarts*4
def qo(quarts):
  return quarts*32
def pg(pints):
  return pints/8
def pq(pints):
  return pints/4
def pp(pints):
  return pints*1
def pcu(pints):
  return pints*2
def po(pints):
  return pints*16
def cug(cups):
  return cups/16
def cuq(cups):
  return cups/4
def cup(cups):
  return cups/2
def cucu(cups):
  return cups*1
def cuo(cups):
  return cups*8
def og(ounces):
  return ounces/128
def oq(ounces):
  return ounces/32
def op(ounces):
  return ounces/16
def ocu(ounces):
  return ounces/8
def oo(ounces):
  return ounces*1
#####metric to imperial and back conversions for lquid measurement#####
def mlo(mililiters):
  return mililiters/29.574
def mlcu(mililiters):
  return mililiters/240
def mlp(mililiters):
  return mililiters/473
def mlq(mililiters):
  return mililiters/964
def mlg(mililiters):
  return mililiters/3785
def clo(centiliters):
  return centiliters/2.957
def clcu(centiliters):
  return centiliters/24
def clp(centiliters):
  return centiliters/47.318
def clq(centiliters):
  return centiliters/94.365
def clg(centiliters):
  return centiliters/379
def dilo(deciliters):
  return deciliters*3.831
def dilcu(deciliters):
  return deciliters/2.4
def dilp(deciliters):
  return deciliters/4.732
def dilq(deciliters):
  return deciliters/9.464
def dilg(deciliters):
  return deciliters/37.854
def lo(liters):
  return liters*33.814
def lcu(liters):
  return liters*4.16667
def lp(liters):
  return liters*2.11338
def lq(liters):
  return liters*1.05669
def lg(liters):
  return liters*0.264172
def dalo(decaliters):
  return decaliters*338.14
def dalcu(decaliters):
  return decaliters*41.6667
def dalp(decaliters):
  return decaliters*21.1338
def dalq(decaliters):
  return decaliters*10.5669
def dalg(decaliters):
  return decaliters*2.64172
def heclo(hectoliters):
  return hectoliters*3381.4
def heclcu(hectoliters):
  return hectoliters*416.667
def heclp(hectoliters):
  return hectoliters*211.338
def heclq(hectoliters):
  return hectoliters*105.669
def heclg(hectoliters):
  return hectoliters*26.4172
def klo(kiloliters):
  return kiloliters*33814
def klcu(kiloliters):
  return kiloliters*4166.67
def klp(kiloliters):
  return kiloliters*2113.38
def klq(kiloliters):
  return kiloliters*1056.69
def klg(kiloliters):
  return kiloliters*264.172
def gml(gallons):
  return gallons*3785.41
def gcl(gallons):
  return gallons*378.541
def gdil(gallons):
  return gallons*37.8541
def gl(gallons):
  return gallons*3.78541
def gdal(gallons):
  return gallons*0.378541
def ghecl(gallons):
  return gallons*0.0378541
def gkl(gallons):
  return gallons*0.00378541
def ql(quarts):
  return quarts*946.353
def qcl(quarts):
  return quarts*94.6353
def qdil(quarts):
  return quarts*9.46353
def ql(quarts):
  return quarts*0.946353
def qdal(quarts):
  return quarts*0.0946353
def qhecl(quarts):
  return quarts*0.00946353
def qkl(quarts):
  return quarts*0.000946353
def pml(pints):
  return pints*473.176
def pcl(pints):
  return pints*47.3176
def pdil(pints):
  return pints*4.73176
def pl(pints):
  return pints*0.473176
def pdal(pints):
  return pints*0.0473176
def phecl(pints):
  return pints*0.00473176
def pkl(pints):
  return pints*0.000473176
def cuml(cups):
  return cups*240
def cucl(cups):
  return cups*24
def cudil(cups):
  return cups*2.4
def cul(cups):
  return cups*0.24
def cudal(cups):
  return cups*0.024
def cuhecl(cups):
  return cups*0.0024
def cukl(cups):
  return cups*0.00024
def oml(ounces):
  return ounces*29.5735
def ocl(ounces):
  return ounces*2.95735
def odil(ounces):
  return ounces*0.295735
def ol(ounces):
  return ounces*0.0295735
def odal(ounces):
  return ounces*0.00295735
def ohecl(ounces):
  return ounces*0.000295735
def okl(ounces):
  return ounces*0.0000295735


def inF(inches):
  abcd = inches*55.9275
  abc = abcd-459.67
  return abc
def Fin(farinheight):
  farinheight55 = farinheight+459.67
  done = farinheight55/55.9275
  return done
#####weight metric to metric conversions##############
def mgmg(miligrams):
  return miligrams*1
def mgcg(miligrams):
  return miligrams/10
def mgdig(miligrams):
  return miligrams/100
def mgg(miligrams):
  return miligrams/1000
def mgdag(miligrams):
  return miligrams/10000
def mgheg(miligrams):
  return miligrams/100000
def mgkg(miligrams):
  return miligrams/1000000
def cgmg(centigrams):
  return centigrams*10
def cgcg(centigrams):
  return centigrams*1
def cgdig(centigrams):
  return centigrams/10
def cgg(centigrams):
  return centigrams/100
def cgdag(centigrams):
  return centigrams/1000
def cgheg(centigrams):
  return centigrams/10000
def cgkg(centigrams):
  return centigrams/100000
def digmg(decigrams):
  return decigrams*100
def digcg(decigrams):
  return decigrams*10
def digdig(decigrams):
  return decigrams*1
def digg(decigrams):
  return decigrams/10
def digdag(decigrams):
  return decigrams/100
def digheg(decigrams):
  return decigrams/1000
def digkg(decigrams):
  return decigrams/10000
def gmg(grams):
  return grams*1000
def gcg(grams):
  return grams*100
def gdig(grams):
  return grams*10
def gg(grams):
  return grams*1
def gdag(grams):
  return grams/10
def gheg(grams):
  return grams/100
def gkg(grams):
  return grams/1000
def dagmg(decagrams):
  return decagrams*10000
def dagcg(decagrams):
  return decagrams*1000
def dagdig(decagrams):
  return decagrams*100
def dagg(decagrams):
  return decagrams*10
def dagdag(decagrams):
  return decagrams*1
def dagheg(decagrams):
  return decagrams/10
def dagkg(decagrams):
  return decagrams/100
def hegmg(hectograms):
  return hectograms*100000
def hegcg(hectograms):
  return hectograms*10000
def hegdig(hectograms):
  return hectograms*1000
def hegg(hectograms):
  return hectograms*100
def hegdag(hectograms):
  return hectograms*10
def hegheg(hectograms):
  return hectograms*1
def hegkg(hectograms):
  return hectograms/10
def kgmg(kilograms):
  return kilograms*1000000
def kgcg(kilograms):
  return kilograms*100000
def kgdig(kilograms):
  return kilograms*10000
def kgg(kilograms):
  return kilograms*1000
def kgdag(kilograms):
  return kilograms*100
def kgheg(kilograms):
  return kilograms*10
def kgkg(kilograms):
  return kilograms*1
#####imperial-imperial weight comversions##############
def opop(ounces):
  return ounces
def oplbs(ounces):
  return ounces/16
def opton(ounces):
  return ounces/32000
def opcton(ounces):
  return ounces/32000000
def lbsop(pounds):
  return pounds*16
def lbslbs(pounds):
  return pounds
def lbston(pounds):
  return pounds/2000
def lbscton(pounds):
  return pounds/2000000
def tonop(tons):
  return tons*32000
def tonlbs(tons):
  return tons*2000
def tonton(tons):
  return tons
def toncton(tons):
  return tons/1000
def ctonop(craptons):
  return craptons*32000000000
def ctonlbs(craptons):
  return craptons*2000000
def ctonton(craptons):
  return craptons*1000
def ctoncton(craptons):
  return craptons
#####metric-imperial/imperial-metric weight conversions
def opmg(ounces):
  return ounces*28350
def opcg(ounces):
  return ounces*2835
def opdig(ounces):
  return ounces*283.495
def opg(ounces):
  return ounces*28.35
def opdag(ounces):
  return ounces*2.835
def opheg(ounces):
  return ounces*.28350
def opkg(ounces):
  return ounces*.028350
def lbsmg(pounds):
  return pounds*453592
def lbscg(pounds):
  return pounds*45359.2
def lbsdig(pounds):
  return pounds*4535.92
def lbsg(pounds):
  return pounds*453.592
def lbsdag(pounds):
  return pounds*45.3592
def lbshg(pounds):
  return pounds*4.53592
def lbskg(pounds):
  return pounds*.453592
def tonmg(tons):
  return tons*907200000
def toncg(tons):
  return tons*90720000
def tondig(tons):
  return tons*9072000
def tong(tons):
  return tons*907200
def tondag(tons):
  return tons*90720
def tonheg(tons):
  return tons*9072
def tonkg(tons):
  return tons*907.2
def ctonmg(tons):
  return tons*907200000000
def ctoncg(tons):
  return tons*90720000000
def ctondig(tons):
  return tons*9072000000
def ctong(tons):
  return tons*907200000
def ctondag(tons):
  return tons*90720000
def ctonheg(tons):
  return tons*9072000
def ctonkg(tons):
  return tons*907200
def mgop(ounces):
  return ounces/28350
def cgop(ounces):
  return ounces/2835
def digop(ounces):
  return ounces/283.495
def gop(ounces):
  return ounces/28.35
def dagop(ounces):
  return ounces/2.835
def hegop(ounces):
  return ounces/.28350
def kgop(ounces):
  return ounces/.028350
def mglbs(pounds):
  return pounds/453592
def cglbs(pounds):
  return pounds/45359.2
def diglbs(pounds):
  return pounds/4535.92
def glbs(pounds):
  return pounds/453.592
def daglbs(pounds):
  return pounds/45.3592
def heglbs(pounds):
  return pounds/4.53592
def kglbs(pounds):
  return pounds/.453592
def mgton(tons):
  return tons/907200000
def cgton(tons):
  return tons/90720000
def digton(tons):
  return tons/9072000
def gton(tons):
  return tons/907200
def dagton(tons):
  return tons/90720
def hegton(tons):
  return tons/9072
def kgton(tons):
  return tons/907.2
def mgcton(tons):
  return tons/907200000000
def cgcton(tons):
  return tons/90720000000
def digcton(tons):
  return tons/9072000000
def gcton(tons):
  return tons/907200000
def dagcton(tons):
  return tons/90720000
def hegcton(tons):
  return tons/9072000
def kgcton(tons):
  return tons/907200
#####all raidation conversions########################
def mcsmcs(microseiverts):
  return microseiverts/1
def mcsmis(microseiverts):
  return microseiverts/1000
def mcss(microseiverts):
  return microseiverts/1000000
def mcsmcr(microseiverts):
  return microseiverts*107.185
def mcsmir(microseiverts):
  return microseiverts*0.107185
def mcsr(miliseiverts):
  return miliseiverts*0.000107185
def mismcs(miliseiverts):
  return miliseiverts/1000
def mismis(miliseiverts):
  return miliseiverts*1
def miss(miliseiverts):
  return miliseiverts*1000
def mismcr(miliseiverts):
  return miliseiverts*107185
def mismir(miliseiverts):
  return miliseiverts*107.185
def misr(miliseiverts):
  return miliseiverts*0.107185
def smcs(seiverts):
  return seiverts*1000000
def smis(seiverts):
  return seiverts*1000
def ss(seiverts):
  return seiverts*1
def smcr(seiverts):
  return seiverts*107185000
def smir(seiverts):
  return seiverts*107185
def sr(seiverts):
  return seiverts*107.185
#####Focus helper################################
def rs(rem):
  return rem/100
def rmis(rem):
  return rem*10
def rmcs(rem):
  return rem*10000
def rr(rem):
  return rem*1
def rmis(rem):
  return rem*1000
def rmcs(rem):
  return rem*1000000
def mirs(milirem):
  return milirem*.00001
def mirmis(rem):
  return rem*.01
def mirmcs(rem):
  return rem*10
def mirr(rem):
  return rem*.001
def mirmir(rem):
  return rem*1
def mirmcr(rem):
  return rem*1000
def mcrs(microrem):
  return microrem*.00000001
def mcrmis(microrem):
  return microrem*.00001
def mcrmcs(microrem):
  return microrem*.01
def mcrr(microrem):
  return microrem*.000001
def mcrmir(microrem):
  return microrem*.001
def mcrmcr(microrem):
  return microrem*1
#####data measurement#################################
def bibi(bit):
  return bit*1
def bibt(bit):
  return bit/8
def bikb(bit):
  return bit/1000
def bikB(bit):
  return bit/8000
def bimb(bit):
  return bit/1000000
def bimB(bit):
  return bit/8000000
def bigb(bit):
  return bit/1000000000
def bigB(bit):
  return bit/8000000000
def bitb(bit):
  return bit/1000000000000
def bitB(bit):
  return bit/8000000000000
def bipb(bit):
  return bit/1000000000000000
def bipB(bit):
  return bit/8000000000000000
def kbbi(kilobit):
  return kilobit*1000
def kbbt(kilobit):
  return kilobit*125
def kbkb(kilobit):
  return kilobit*1
def kbkB(kilobit):
  return kilobit/8
def kbmb(kilobit):
  return kilobit/1000
def kbmB(kilobit):
  return kilobit/8000
def kbgb(kilobit):
  return kilobit/1000000
def kbgB(kilobit):
  return kilobit/8000000
def kbtb(kilobit):
  return kilobit/1000000000
def kbtB(kilobit):
  return kilobit/8000000000
def kbpb(kilobit):
  return kilobit/1000000000000
def kbpB(kilobit):
  return kilobit/8000000000000
def mbbi(megabit):
  return megabit*1000000
def mbbt(megabit):
  return megabit*125000
def mbkb(megabit):
  return megabit*1000
def mbkB(megabit):
  return megabit*125
def mbmb(megabit):
  return megabit*1
def mbmB(megabit):
  return megabit/8
def mbgb(megabit):
  return megabit/1000
def mbgB(megabit):
  return megabit/8000
def mbtb(megabit):
  return megabit/1000000
def mbtB(megabit):
  return megabit/8000000
def mbpb(megabit):
  return megabit/1000000000
def mbpB(megabit):
  return megabit/8000000000
def gbbi(gigabit):
  return gigabit*1000000000
def gbbt(gigabit):
  return gigabit*125000000
def gbkb(gigabit):
  return gigabit*1000000
def gbkB(gigabit):
  return gigabit*125000
def gbmb(gigabit):
  return gigabit*1000
def gbmB(gigabit):
  return gigabit*125
def gbgb(gigabit):
  return gigabit*1
def gbgB(gigabit):
  return gigabit/8
def gbtb(gigabit):
  return gigabit/1000
def gbtB(gigabit):
  return gigabit/8000
def gbpb(gigabit):
  return gigabit/1000000
def gbpB(gigabit):
  return gigabit/8000000
def tbbi(terabit):
  return terabit*1000000000000
def tbbt(terabit):
  return terabit*125000000000
def tbkb(terabit):
  return terabit*1000000000
def tbkB(terabit):
  return terabit*125000000
def tbmb(terabit):
  return terabit*1000000
def tbmB(terabit):
  return terabit*125000
def tbgb(terabit):
  return terabit*1000
def tbgB(terabit):
  return terabit*125
def tbtb(terabit):
  return terabit*1
def tbtB(terabit):
  return terabit/8
def tbpb(terabit):
  return terabit/1000
def tbpB(terabit):
  return terabit/8000
def btbi(byte):
  return byte*8
def btbt(byte):
  return byte*1
def btkb(byte):
  return byte/1000
def btkB(byte):
  return byte/8000
def btmb(byte):
  return byte/1000000
def btmB(byte):
  return byte/8000000
def btgb(byte):
  return byte/1000000000
def btgB(byte):
  return byte/8000000000
def bttb(byte):
  return byte/1000000000000
def bttB(byte):
  return byte/8000000000000
def btpb(byte):
  return byte/1000000000000000
def btpB(byte):
  return byte/8000000000000000
def kBbi(kilobyte):
  return kilobyte*8000
def kBbt(kilobyte):
  return kilobyte*1000
def kBkb(kilobyte):
  return kilobyte*8
def kBkB(kilobyte):
  return kilobyte*1
def kBmb(kilobyte):
  return kilobyte/8000
def kBmB(kilobyte):
  return kilobyte/1000
def kBkb(kilobyte):
  return kilobyte/8000000
def kBkB(kilobyte):
  return kilobyte/1000000
def kBgb(kilobyte):
  return kilobyte/8000000000
def kBgB(kilobyte):
  return kilobyte/1000000000
def kBtb(kilobyte):
  return kilobyte/8000000000000
def kBtB(kilobyte):
  return kilobyte/1000000000000
def kBpb(kilobyte):
  return kilobyte/8000000000000000
def kBpB(kilobyte):
  return kilobyte/1000000000000000
def mBbi(megabyte):
  return megabyte*8000000
def mBbt(megabyte):
  return megabyte*1000000
def mBkb(megabyte):
  return megabyte*8000
def mBkB(megabyte):
  return megabyte*1000
def mBmb(megabyte):
  return megabyte*8
def mBmB(megabyte):
  return megabyte*1
def mBgb(megabyte):
  return megabyte/125
def mBgB(megabyte):
  return megabyte/1000
def mBtb(megabyte):
  return megabyte/125000
def mBtB(megabyte):
  return megabyte/1000000
def mBpb(megabyte):
  return megabyte/125000000
def mBpB(megabyte):
  return megabyte/1000000000
def gBbi(gigabyte):
  return gigabyte*8000000000
def gBbt(gigabyte):
  return gigabyte*1000000000
def gBkb(gigabyte):
  return gigabyte*80000000
def gBkB(gigabyte):
  return gigabyte*10000000
def gBmb(gigabyte):
  return gigabyte*8000
def gBmB(gigabyte):
  return gigabyte*1000
def gBgb(gigabyte):
  return gigabyte*8
def gBgB(gigabyte):
  return gigabyte*1
def gBtb(gigabyte):
  return gigabyte/125
def gBtB(gigabyte):
  return gigabyte/1000
def gBpb(gigabyte):
  return gigabyte/125000
def gBpB(gigabyte):
  return gigabyte/1000000
def tBbi(terabyte):
  return terabyte*8000000000000
def tBbt(terabyte):
  return terabyte*1000000000000
def tBkb(terabyte):
  return terabyte*8000000000
def tBkB(terabyte):
  return terabyte*1000000000
def tBmb(terabyte):
  return terabyte*8000000
def tBmB(terabyte):
  return terabyte*1000000
def tBgb(terabyte):
  return terabyte*8000
def tBgB(terabyte):
  return terabyte*1000
def tBtb(terabyte):
  return terabyte*8
def tBtB(terabyte):
  return terabyte*1
def tBpb(terabyte):
  return terabyte/125
def tBpB(terabyte):
  return terabyte/1000
def pBbi(petabyte):
  return petabyte*800000000000000
def pBbt(petabyte):
  return petabyte*100000000000000
def pBkb(petabyte):
  return petabyte*8000000000000
def pBkB(petabyte):
  return petabyte*1000000000000
def pBmb(petabyte):
  return petabyte*8000000000
def pBmB(petabyte):
  return petabyte*1000000000
def pBgb(petabyte):
  return petabyte*8000000
def pBgB(petabyte):
  return petabyte*1000000
def pBtb(petabyte):
  return petabyte*8000
def pBtB(petabyte):
  return petabyte*1000
def pBpb(petabyte):
  return petabyte*8
def pBpB(petabyte):
  return petabyte*1
#####sorting##########################################
'''
mm = milimeters
cm = centimeters
di = decimeters
met = meters
dam = decameters
hec = hectometers
km = kilometers
in = inches
ft = feet
yd = yards
mi = miles
F = farinhight
C = celcius
K = kelvin
ms = miliseconds
sec = seconds
min = munites
h = hours
d = days
w = weeks
m = months
y = years
dy = decades
cy = centuries
my = millinia
ml = mililiters
cl = centliters
dil = deciliters
l = liters
dal = decaliters
hecl = hectoliters
kl = kiloliters
g = gallon
q = quart
p = pint
cu = cup
o = lquid ounces
mg = miligrams
cg = centigrams
dig = decigrams
g = grams
dag = decagrams
heg = hectograms
kg = kilograms
op = weight ounces
lbs = pounds
ton = tons (2000 pounds)
cton = imperial crapton (1000 tons)
r = rem
s = sieverts
mcs = microsieverts
mis = milisieverts
mir = milirotogen
mcr = microrotogen
bt = byte
bi = bit
kB = kilabyte
kb = kilabit
mB = megabyte
mb = megabit
gB = gigabyte
gb = gigabit
tb = terabit
tB = terabyte
pb = petabit
pB = petabyte
'''

#####selector#########################################
print("there are many choices, pick one")
print("1.  Lenght Measurement")
print("2.  Tempature Measurement")
print("3.  Time Measurement")
print("4.  Lquid Measurment")
print("5.  Weight Measurement")
print("6.  Raidation Measurement Beteween Sci and Non-Sci Radians/Rotogens")
print("7.  Digital Storage measurment")
selec = int(input("enter choice: "))
if selec == 0:
  print("Congrats! you found the hidden choice")
  clear()
  loading(3)
  print("1. inches to farinhight")
  print("2. farinheight to inches")
  select = int(input("select one: "))
  num1 = float(input("enter first number: "))
  if select == 1:
    print(inF(num1))
  elif select == 2:
    print(Fin(num1))
elif selec == 1:
  print("1.  milimeters to")
  print("2.  centimeters to")
  print("3.  decimeters to")
  print("4.  meters to")
  print("5.  decameters to")
  print("6.  hectometers to")
  print("7.  kilometers to")
  print("8.  inches to")
  print("9.  feet to")
  print("10. yards to")
  print("11. miles to")
  select = int(input("enter choice: "))
  if select == 1:
    
    print("1. milimeters to milimeters")
    print("2. milimeters to centimeters")
    print("3. milimeters to decimeters")
    print("4. milimeters to meters")
    print("5. milimeters to decameters")
    print("6. milimeters to hectometers")
    print("7. milimeters to kilometers")
    print("8. milimeters to inches")
    print("9. milimeters to feet")
    print("10. milimeters to yards")
    print("11. milimeters to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(mmmm(num1))
    elif select2 == 2:
      print(mmcm(num1))
    elif select2 == 3:
      print(mmdi(num1))
    elif select2 == 4:
      print(mmmet(num1))
    elif select2 == 5:
      print(mmdam(num1))
    elif select2 == 6:
      print(mmhec(num1))
    elif select2 == 7:
      print(mmkm(num1))
    elif select2 == 8:
      print(mmin(num1))
    elif select2 == 9:
      print(mmft(num1))
    elif select2 == 10:
      print(mmyd(num1))
    elif select2 == 11:
      print(mmmi(num1))
  elif select == 2:
    
    print("1. centimeters to milimeters")
    print("2. centimeters to centimeters")
    print("3. centimeters to decimeters")
    print("4. centimeters to meters")
    print("5. centimeters to decameters")
    print("6. centimeters to hectometers")
    print("7. centimeters to kilometers")
    print("8. centimeters to inches")
    print("9. centimeters to feet")
    print("10. centimeters to yards")
    print("11. centimeters to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(cmmm(num1))
    elif select2 == 2:
      print(cmcm(num1))
    elif select2 == 3:
      print(cmdi(num1))
    elif select2 == 4:
      print(cmmet(num1))
    elif select2 == 5:
      print(cmdam(num1))
    elif select2 == 6:
      print(cmhec(num1))
    elif select2 == 7:
      print(cmkm(num1))
    elif select2 == 8:
      print(cmin(num1))
    elif select2 == 9:
      print(cmft(num1))
    elif select2 == 10:
      print(cmyd(num1))
    elif select2 == 11:
      print(cmmi(num1))
  elif select == 3:
    
    print("1. decimeters to milimeters")
    print("2. decimeters to centimeters")
    print("3. decimeters to decimeters")
    print("4. decimeters to meters")
    print("5. decimeters to decameters")
    print("6. decimeters to hectometers")
    print("7. decimeters to kilometers")
    print("8. decimeters to inches")
    print("9. decimeters to feet")
    print("10. decimeters to yards")
    print("11. decimeters to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(dimm(num1))
    elif select2 == 2:
      print(dicm(num1))
    elif select2 == 3:
      print(didi(num1))
    elif select2 == 4:
      print(dimet(num1))
    elif select2 == 5:
      print(didam(num1))
    elif select2 == 6:
      print(dihec(num1))
    elif select2 == 7:
      print(dikm(num1))
    elif select2 == 8:
      print(diin(num1))
    elif select2 == 9:
      print(dift(num1))
    elif select2 == 10:
      print(diyd(num1))
    elif select2 == 11:
      print(dimi(num1))
  elif select == 4 :
    
    print("1. meters to milimeters")
    print("2. meters to centimeters")
    print("3. meters to decimeters")
    print("4. meters to meters")
    print("5. meters to decameters")
    print("6. meters to hectometers")
    print("7. meters to kilometers")
    print("8. meters to inches")
    print("9. meters to feet")
    print("10. meters to yards")
    print("11. meters to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(metmm(num1))
    elif select2 == 2:
      print(metcm(num1))
    elif select2 == 3:
      print(metdi(num1))
    elif select2 == 4:
      print(metmet(num1))
    elif select2 == 5:
      print(metdam(num1))
    elif select2 == 6:
      print(methec(num1))
    elif select2 == 7:
      print(metkm(num1))
    elif select2 == 8:
      print(metin(num1))
    elif select2 == 9:
      print(metft(num1))
    elif select2 == 10:
      print(metyd(num1))
    elif select2 == 11:
      print(metmi(num1))
  elif select == 5:
    
    print("1. decameters to milimeters")
    print("2. decameters to centimeters")
    print("3. decameters to decimeters")
    print("4. decameters to meters")
    print("5. decameters to decameters")
    print("6. decameters to hectometers")
    print("7. decameters to kilometers")
    print("8. decameters to inches")
    print("9. decameters to feet")
    print("10. decameters to yards")
    print("11. decameters to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(dammm(num1))
    elif select2 == 2:
      print(damcm(num1))
    elif select2 == 3:
      print(damdi(num1))
    elif select2 == 4:
      print(dammmet(num1))
    elif select2 == 5:
      print(damdam(num1))
    elif select2 == 6:
      print(damhec(num1))
    elif select2 == 7:
      print(damkm(num1))
    elif select2 == 8:
      print(damin(num1))
    elif select2 == 9:
      print(damft(num1))
    elif select2 == 10:
      print(damyd(num1))
    elif select2 == 11:
      print(dammi(num1))
  elif select == 6:
    
    print("1. hectometers to milimeters")
    print("2. hectometers to centimeters")
    print("3. hectometers to decimeters")
    print("4. hectometers to meters")
    print("5. hectometers to decameters")
    print("6. hectometers to hectometers")
    print("7. hectometers to kilometers")
    print("8. hectometers to inches")
    print("9. hectometers to feet")
    print("10. hectometers to yards")
    print("11. hectometers to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(hecmm(num1))
    elif select2 == 2:
      print(heccm(num1))
    elif select2 == 3:
      print(hecdi(num1))
    elif select2 == 4:
      print(hecmet(num1))
    elif select2 == 5:
      print(hecdam(num1))
    elif select2 == 6:
      print(hechec(num1))
    elif select2 == 7:
      print(heckm(num1))
    elif select2 == 8:
      print(hecin(num1))
    elif select2 == 9:
      print(hecft(num1))
    elif select2 == 10:
      print(hecyd(num1))
    elif select2 == 11:
      print(hecmi(num1))
  elif select == 7:
    
    print("1. kilometers to milimeters")
    print("2. kilometers to centimeters")
    print("3. kilometers to decimeters")
    print("4. kilometers to meters")
    print("5. kilometers to decameters")
    print("6. kilometers to hectometers")
    print("7. kilometers to kilometers")
    print("8. kilometers to inches")
    print("9. kilometers to feet")
    print("10. kilometers to yards")
    print("11. kilometers to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(kmmm(num1))
    elif select2 == 2:
      print(kmcm(num1))
    elif select2 == 3:
      print(kmdi(num1))
    elif select2 == 4:
      print(kmmet(num1))
    elif select2 == 5:
      print(kmdam(num1))
    elif select2 == 6:
      print(kmhec(num1))
    elif select2 == 7:
      print(kmkm(num1))
    elif select2 == 8:
      print(kmin(num1))
    elif select2 == 9:
      print(kmft(num1))
    elif select2 == 10:
      print(kmyd(num1))
    elif select2 == 11:
      print(kmmi(num1))
  elif select == 8:
    
    print("1. inches to milimeters")
    print("2. inches to centimeters")
    print("3. inches to decimeters")
    print("4. inches to meters")
    print("5. inches to decameters")
    print("6. inches to hectometers")
    print("7. inches to kilometers")
    print("8. inches to inches")
    print("9. inches to feet")
    print("10. inches to yards")
    print("11. inches to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(inmm(num1))
    elif select2 == 2:
      print(incm(num1))
    elif select2 == 3:
      print(indi(num1))
    elif select2 == 4:
      print(inmet(num1))
    elif select2 == 5:
      print(indam(num1))
    elif select2 == 6:
      print(inhec(num1))
    elif select2 == 7:
      print(inkm(num1))
    elif select2 == 8:
      print(inin(num1))
    elif select2 == 9:
      print(inft(num1))
    elif select2 == 10:
      print(inyd(num1))
    elif select2 == 11:
      print(inmi(num1))
  elif select == 9:
    
    print("1. feet to milimeters")
    print("2. feet to centimeters")
    print("3. feet to decimeters")
    print("4. feet to meters")
    print("5. feet to decameters")
    print("6. feet to hectometers")
    print("7. feet to kilometers")
    print("8. feet to inches")
    print("9. feet to feet")
    print("10. feet to yards")
    print("11. feet to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(ftmm(num1))
    elif select2 == 2:
      print(ftcm(num1))
    elif select2 == 3:
      print(ftdi(num1))  
    elif select2 == 4:
      print(ftmet(num1))
    elif select2 == 5:
      print(ftdam(num1))
    elif select2 == 6:
      print(fthec(num1))
    elif select2 == 7:
      print(ftkm(num1))
    elif select2 == 8:
      print(ftin(num1))
    elif select2 == 9:
      print(ftft(num1))
    elif select2 == 10:
      print(ftyd(num1))
    elif select2 == 11:
      print(ftmi(num1))
  elif select == 10:
    
    print("1. yards to milimeters")
    print("2. yards to centimeters")
    print("3. yards to decimeters")
    print("4. yards to meters")
    print("5. yards to decameters")
    print("6. yards to hectometers")
    print("7. yards to kilometers")
    print("8. yards to inches")
    print("9. yards to feet")
    print("10. yards to yards")
    print("11. yards to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(ydmm(num1))    
    elif select2 == 2:
      print(ydcm(num1))
    elif select2 == 3:
      print(yddi(num1))
    elif select2 == 4:
      print(ydmet(num1))
    elif select2 == 5:
      print(yddam(num1))
    elif select2 == 6:
      print(ydhec(num1))
    elif select2 == 7:
      print(ydkm(num1))
    elif select2 == 8:
      print(ydin(num1))
    elif select2 == 9:
      print(ydft(num1))
    elif select2 == 10:
      print(ydyd(num1))
    elif select2 == 11:
      print(ydmi(num1))
  elif select == 11:
    
    print("1. miles to milimeters")
    print("2. miles to centimeters")
    print("3. miles to decimeters")
    print("4. miles to meters")
    print("5. miles to decameters")
    print("6. miles to hectometers")
    print("7. miles to kilometers")
    print("8. miles to inches")
    print("9. miles to feet")
    print("10. miles to yards")
    print("11. miles to miles")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(mimm(num1))
    elif select2 == 2:
      print(micm(num1))
    elif select2 == 3:
      print(midi(num1))
    elif select2 == 4:
      print(mimet(num1))
    elif select2 == 5:
      print(midam(num1))
    elif select2 == 6:
      print(mihec(num1))
    elif select2 == 7:
      print(mikm(num1))
    elif select2 == 8:
      print(miin(num1))
    elif select2 == 9:
      print(mift(num1))
    elif select2 == 10:
      print(miyd(num1))
    elif select2 == 11:
      print(mimi(num1))
elif selec == 2:
  print("1. farinhight to")
  print("2. celcius to")
  print("3. kelvin to")
  select = int(input("enter choice: "))
  if select == 1:
    
    print("1. fareinhight to celcius")
    print("2. fareinhight to kelvin")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(FC(num1))
    elif select2 == 2:
      print(FK(num1))
  elif select == 2:
    
    print("1. celcius to farinhight")
    print("2. celcius to kelvin")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(CF(num1))
    elif select2 == 2:
      print(CK(num1))
  elif select == 3:
    
    print("1. kelvin to farinhight")
    print("2. kelvin to celcius")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(KF(num1))
    elif select2 == 2:
      print(KC(num1))
  
elif selec == 3:  
  print("1. miliseconds to")
  print("2. seconds to")
  print("3. minuites to")
  print("4. hours to")
  print("5. days to")
  print("6. weeks to")
  print("7. months to")
  print("8. years to")
  print("9. decades to")
  print("10. centuries to")
  print("11. millinia to")
  select = int(input("enter choice: "))
  if select == 1:
    print("1. miliseconds to miliseconds")
    print("2. miliseconds to seconds")
    print("3. miliseconds to minutes")
    print("4. miliseconds to hours")
    print("5. miliseconds to days")
    print("6. miliseconds to weeks")
    print("7. miliseconds to months")
    print("8. miliseconds to years")
    print("9. miliseconds to decades")
    print("10. miliseconds to centries")
    print("11. miliseconds to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(msms(num1))
    elif select2 == 2:
      print(mssec(num1))
    elif select2 == 3:
      print(msmin(num1))
    elif select2 == 4:
      print(msh(num1))
    elif select2 == 5:
      print(msd(num1))
    elif select2 == 6:
      print(msw(num1))
    elif select2 == 7:
      print(msm(num1))
    elif select2 == 8:
      print(msy(num1))
    elif select2 == 9:
      print(msdy(num1))
    elif select2 == 10:
      print(mscy(num1))
    elif select2 == 11:
      print(msmy(num1))
  elif select == 2:
    print("1. seconds to miliseconds")
    print("2. seconds to seconds")
    print("3. seconds to minutes")
    print("4. seconds to hours")
    print("5. seconds to days")
    print("6. seconds to weeks")
    print("7. seconds to months")
    print("8. seconds to years")
    print("9. seconds to decades")
    print("10.seconds to centries")
    print("11.seconds to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(secms(num1))
    elif select2 == 2:
      print(secsec(num1))
    elif select2 == 3:
      print(secmin(num1))
    elif select2 == 4:
      print(sech(num1))
    elif select2 == 5:
      print(secd(num1))
    elif select2 == 6:
      print(secw(num1))
    elif select2 == 7:
      print(secm(num1))
    elif select2 == 8:
      print(secy(num1))
    elif select2 == 9:
      print(secdy(num1))
    elif select2 == 10:
      print(seccy(num1))
    elif select2 == 11:
      print(secmy(num1))
  elif select == 3:
    print("1. minutes to miliseconds")
    print("2. minutes to seconds")
    print("3. minutes to minutes")
    print("4. minutes to hours")
    print("5. minutes to days")
    print("6. minutes to weeks")
    print("7. minutes to months")
    print("8. minutes to years")
    print("9. minutes to decades")
    print("10. minutes to centries")
    print("11. minutes to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(minms(num1))
    elif select2 == 2:
      print(minsec(num1))
    elif select2 == 3:
      print(minmin(num1))
    elif select2 == 4:
      print(minh(num1))
    elif select2 == 5:
      print(mind(num1))
    elif select2 == 6:
      print(minw(num1))
    elif select2 == 7:
      print(minm(num1))
    elif select2 == 8:
      print(miny(num1))
    elif select2 == 9:
      print(mindy(num1))
    elif select2 == 10:
      print(mincy(num1))
    elif select2 == 11:
      print(minmy(num1))
  elif select == 4:
    print("1. hours to miliseconds")
    print("2. hours to seconds")
    print("3. hours to minutes")
    print("4. hours to hours")
    print("5. hours to days")
    print("6. hours to weeks")
    print("7. hours to months")
    print("8. hours to years")
    print("9. hours to decades")
    print("10. hours to centries")
    print("11. hours to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(hms(num1))
    elif select2 == 2:
      print(hsec(num1))
    elif select2 == 3:
      print(hmin(num1))
    elif select2 == 4:
      print(hh(num1))
    elif select2 == 5:
      print(hd(num1))
    elif select2 == 6:
      print(hw(num1))
    elif select2 == 7:
      print(hm(num1))
    elif select2 == 8:
      print(hy(num1))
    elif select2 == 9:
      print(hdy(num1))
    elif select2 == 10:
      print(hcy(num1))
    elif select2 == 11:
      print(hmy(num1))
  elif select == 5:
    print("1. days to miliseconds")
    print("2. days to seconds")
    print("3. days to minutes")
    print("4. days to hours")
    print("5. days to days")
    print("6. days to weeks")
    print("7. days to months")
    print("8. days to years")
    print("9. days to decades")
    print("10. days to centries")
    print("11. days to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(dms(num1))
    elif select2 == 2:
      print(dsec(num1))
    elif select2 == 3:
      print(dmin(num1))
    elif select2 == 4:
      print(dh(num1))
    elif select2 == 5:
      print(dd(num1))
    elif select2 == 6:
      print(dw(num1))
    elif select2 == 7:
      print(dm(num1))
    elif select2 == 8:
      print(dy(num1))
    elif select2 == 9:
      print(ddy(num1))
    elif select2 == 10:
      print(dcy(num1))
    elif select2 == 11:
      print(dmy(num1))
  elif select == 6:
    print("1. weeks to miliseconds")
    print("2. weeks to seconds")
    print("3. weeks to minutes")
    print("4. weeks to hours")
    print("5. weeks to days")
    print("6. weeks to weeks")
    print("7. weeks to months")
    print("8. weeks to years")
    print("9. weeks to decades")
    print("10. weeks to centries")
    print("11. weeks to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(wms(num1))
    elif select2 == 2:
      print(wsec(num1))
    elif select2 == 3:
      print(wmin(num1))
    elif select2 == 4:
      print(wh(num1))
    elif select2 == 5:
      print(wd(num1))
    elif select2 == 6:
      print(ww(num1))
    elif select2 == 7:
      print(wm(num1))
    elif select2 == 8:
      print(wy(num1))
    elif select2 == 9:
      print(wdy(num1))
    elif select2 == 10:
      print(wcy(num1))
    elif select2 == 11:
      print(wmy(num1))
  elif select == 7:
    print("1. months to miliseconds")
    print("2. months to seconds")
    print("3. months to minutes")
    print("4. months to hours")
    print("5. months to days")
    print("6. months to weeks")
    print("7. months to months")
    print("8. months to years")
    print("9. months to decades")
    print("10. months to centries")
    print("11. months to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(mms(num1))
    elif select2 == 2:
      print(msec(num1))
    elif select2 == 3:
      print(mmin(num1))
    elif select2 == 4:
      print(mh(num1))
    elif select2 == 5:
      print(md(num1))
    elif select2 == 6:
      print(mw(num1))
    elif select2 == 7:
      print(mm(num1))
    elif select2 == 8:
      print(my(num1))
    elif select2 == 9:
      print(mdy(num1))
    elif select2 == 10:
      print(mcy(num1))
    elif select2 == 11:
      print(mmy(num1))
  elif select == 8:
    print("1. years to miliseconds")
    print("2. years to seconds")
    print("3. years to minutes")
    print("4. years to hours")
    print("5. years to days")
    print("6. years to weeks")
    print("7. years to months")
    print("8. years to years")
    print("9. years to decades")
    print("10. years to centries")
    print("11. years to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(yms(num1))
    elif select2 == 2:
      print(ysec(num1))
    elif select2 == 3:
      print(ymin(num1))
    elif select2 == 4:
      print(yh(num1))
    elif select2 == 5:
      print(yd(num1))
    elif select2 == 6:
      print(yw(num1))
    elif select2 == 7:
      print(ym(num1))
    elif select2 == 8:
      print(yy(num1))
    elif select2 == 9:
      print(ydy(num1))
    elif select2 == 10:
      print(ycy(num1))
    elif select2 == 11:
      print(ymy(num1))
  elif select == 9:
    print("1. decades to miliseconds")
    print("2. decades to seconds")
    print("3. decades to minutes")
    print("4. decades to hours")
    print("5. decades to days")
    print("6. decades to weeks")
    print("7. decades to months")
    print("8. decades to years")
    print("9. decades to decades")
    print("10. decades to centries")
    print("11. decades to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(dyms(num1))
    elif select2 == 2:
      print(dysec(num1))
    elif select2 == 3:
      print(dymin(num1))
    elif select2 == 4:
      print(dyh(num1))
    elif select2 == 5:
      print(dyd(num1))
    elif select2 == 6:
      print(dyw(num1))
    elif select2 == 7:
      print(dym(num1))
    elif select2 == 8:
      print(dyy(num1))
    elif select2 == 9:
      print(dydy(num1))
    elif select2 == 10:
      print(dycy(num1))
    elif select2 == 11:
      print(dymy(num1))
  elif select == 10:
    print("1. centuries to miliseconds")
    print("2. centuries to seconds")
    print("3. centuries to minutes")
    print("4. centuries to hours")
    print("5. centuries to days")
    print("6. centuries to weeks")
    print("7. centuries to months")
    print("8. centuries to years")
    print("9. centuries to decades")
    print("10. centuries to centries")
    print("11. centuries to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(cyms(num1))
    elif select2 == 2:
      print(cysec(num1))
    elif select2 == 3:
      print(cymin(num1))
    elif select2 == 4:
      print(cyh(num1))
    elif select2 == 5:
      print(cyd(num1))
    elif select2 == 6:
      print(cyw(num1))
    elif select2 == 7:
      print(cym(num1))
    elif select2 == 8:
      print(cyy(num1))
    elif select2 == 9:
      print(cydy(num1))
    elif select2 == 10:
      print(cycy(num1))
    elif select2 == 11:
      print(cymy(num1))
  elif select == 11:
    print("1. millinia to miliseconds")
    print("2. millinia to seconds")
    print("3. millinia to minutes")
    print("4. millinia to hours")
    print("5. millinia to days")
    print("6. millinia to weeks")
    print("7. millinia to months")
    print("8. millinia to years")
    print("9. millinia to decades")
    print("10. millinia to centries")
    print("11. millinia to millinia")
    select2 = int(input("select one: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(myms(num1))
    elif select2 == 2:
      print(mysec(num1))
    elif select2 == 3:
      print(mymin(num1))
    elif select2 == 4:
      print(myh(num1))
    elif select2 == 5:
      print(myd(num1))
    elif select2 == 6:
      print(myw(num1))
    elif select2 == 7:
      print(mym(num1))
    elif select2 == 8:
      print(myy(num1))
    elif select2 == 9:
      print(mydy(num1))
    elif select2 == 10:
      print(mycy(num1))
    elif select2 == 11:
      print(mymy(num1))
elif selec == 4:
  print("1.  mililiters to")
  print("2.  centiliters to")
  print("3.  deciliters to")
  print("4.  liters to")
  print("5. decaliters to")
  print("6.  hectoliters to")
  print("7.  kiloliters to")
  print("8.  ounces to")
  print("9.  cups to")
  print("10. pints to")
  print("11. quarts to")
  print("12. gallons to")
  select = int(input("enter choice: "))
  if select == 1:
    print("1.  mililiters to mililiters")
    print("2.  mililiters to centiliters")
    print("3.  mililiters to deciliters")
    print("4.  mililiters to liters")
    print("5.  mililiters to decaliters")
    print("6.  mililiters to hectoliters")
    print("7.  mililiters to kiloliters")
    print("8.  mililiters to ounces")
    print("9.  mililiters to cups")
    print("10. mililiters to pints")
    print("11. mililiters to quarts")
    print("12. mililiters to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(mlml(num1))
    elif select2 == 2:
      print(mlcl(num1))
    elif select2 == 3:
      print(mldil(num1))
    elif select2 == 4:
      print(mll(num1))
    elif select2 == 5:
      print(mldal(num1))
    elif select2 == 6:
      print(mlhecl(num1))
    elif select2 == 7:
      print(mlkl(num1))
    elif select2 == 8:
      print(mlo(num1))
    elif select2 == 9:
      print(mlcu(num1))
    elif select2 == 10:
      print(mlp(num1))
    elif select2 == 11:
      print(mlq(num1))
    elif select2 == 12:
      print(mlg(num1))
  if select == 2:
    print("1.  centiliters to mililiters")
    print("2.  centiliters to centiliters")
    print("3.  centiliters to deciliters")
    print("4.  centiliters to liters")
    print("5.  centiliters to decaliters")
    print("6.  centiliters to hectoliters")
    print("7.  centiliters to kiloliters")
    print("8.  centiliters to ounces")
    print("9.  centiliters to cups")
    print("10. centiliters to pints")
    print("11. centiliters to quarts")
    print("12. centiliters to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(clml(num1))
    elif select2 == 2:
      print(clcl(num1))
    elif select2 == 3:
      print(cldil(num1))
    elif select2 == 4:
      print(cll(num1))
    elif select2 == 5:
      print(cldal(num1))
    elif select2 == 6:
      print(clhecl(num1))
    elif select2 == 7:
      print(clkl(num1))
    elif select2 == 8:
      print(clo(num1))
    elif select2 == 9:
      print(clcu(num1))
    elif select2 == 10:
      print(clp(num1))
    elif select2 == 11:
      print(clq(num1))
    elif select2 == 12:
      print(clg(num1))
  if select == 3:
    print("1. deciliters to mililiters")
    print("2. deciliters to centiliters")
    print("3. deciliters to deciliters")
    print("4. deciliters to liters")
    print("5. deciliters to decaliters")
    print("6. deciliters to hectoliters")
    print("7. deciliters to kiloliters")
    print("8. deciliters to ounces")
    print("9. deciliters to cups")
    print("10. decaliters to pints")
    print("11. decaliters to quarts")
    print("12. decaliters to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(dilml(num1))
    elif select2 == 2:
      print(dilcl(num1))
    elif select2 == 3:
      print(dildil(num1))
    elif select2 == 4:
      print(dill(num1))
    elif select2 == 5:
      print(dildal(num1))
    elif select2 == 6:
      print(dilhecl(num1))
    elif select2 == 7:
      print(dilkl(num1))
    elif select2 == 8:
      print(dilo(num1))
    elif select2 == 9:
      print(dilcu(num1))
    elif select2 == 10:
      print(dilp(num1))
    elif select2 == 11:
      print(dilq(num1))
    elif select2 == 12:
      print(dilg(num1))
  if select == 4:
    print("1.  liters to mililiters")
    print("2.  liters to centiliters")
    print("3.  liters to deciliters")
    print("4.  liters to liters")
    print("5.  liters to decaliters")
    print("6.  liters to hectoliters")
    print("7.  liters to kiloliters")
    print("8.  liters to ounces")
    print("9.  liters to cups")
    print("10. liters to pints")
    print("11. liters to quarts")
    print("12. liters to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(lml(num1))
    elif select2 == 2:
      print(lcl(num1))
    elif select2 == 3:
      print(ldil(num1))
    elif select2 == 4:
      print(ll(num1))
    elif select2 == 5:
      print(ldal(num1))
    elif select2 == 6:
      print(lhecl(num1))
    elif select2 == 7:
      print(lkl(num1))
    elif select2 == 8:
      print(lo(num1))
    elif select2 == 9:
      print(lcu(num1))
    elif select2 == 10:
      print(lp(num1))
    elif select2 == 11:
      print(lq(num1))
    elif select2 == 12:
      print(lg(num1))
  if select == 5:
    print("1.  decaliters to mililiters")
    print("2.  decaliters to centiliters")
    print("3.  decaliters to deciliters")
    print("4.  decaliters to liters")
    print("5.  decaliters to decaliters")
    print("6.  decaliters to hectoliters")
    print("7.  decaliters to kiloliters")
    print("8.  decaliters to ounces")
    print("9.  decaliters to cups")
    print("10. decaliters to pints")
    print("11. decaliters to quarts")
    print("12. decaliters to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(dalml(num1))
    elif select2 == 2:
      print(dalcl(num1))
    elif select2 == 3:
      print(daldil(num1))
    elif select2 == 4:
      print(dall(num1))
    elif select2 == 5:
      print(daldal(num1))
    elif select2 == 6:
      print(dalhecl(num1))
    elif select2 == 7:
      print(dalkl(num1))
    elif select2 == 8:
      print(dalo(num1))
    elif select2 == 9:
      print(dalcu(num1))
    elif select2 == 10:
      print(dalp(num1))
    elif select2 == 11:
      print(dalq(num1))
    elif select2 == 12:
      print(dalg(num1))
  if select == 6:
    print("1.  hectoliters to mililiters")
    print("2.  hectoliters to centiliters")
    print("3.  hectoliters to deciliters")
    print("4.  hectoliters to liters")
    print("5.  hectoliters to decaliters")
    print("6.  hectoliters to hectoliters")
    print("7.  hectoliters to kiloliters")
    print("8.  hectoliters to ounces")
    print("9.  hectoliters to cups")
    print("10. hectoliters to pints")
    print("11. hectoliters to quarts")
    print("12. hectoliters to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(heclml(num1))
    elif select2 == 2:
      print(heclcl(num1))
    elif select2 == 3:
      print(hecldil(num1))
    elif select2 == 4:
      print(hecll(num1))
    elif select2 == 5:
      print(hecldal(num1))
    elif select2 == 6:
      print(heclhecl(num1))
    elif select2 == 7:
      print(heclkl(num1))
    elif select2 == 8:
      print(heclo(num1))
    elif select2 == 9:
      print(heclcu(num1))
    elif select2 == 10:
      print(heclp(num1))
    elif select2 == 11:
      print(heclq(num1))
    elif select2 == 12:
      print(heclg(num1))
  if select == 7:
    print("1.  kiloliters to mililiters")
    print("2.  kiloliters to centiliters")
    print("3.  kiloliters to deciliters")
    print("4.  kiloliters to liters")
    print("5.  kiloliters to decaliters")
    print("6.  kiloliters to hectoliters")
    print("7.  kiloliters to kiloliters")
    print("8.  kiloliters to ounces")
    print("9.  kiloliters to cups")
    print("10. kiloliters to pints")
    print("11. kiloliters to quarts")
    print("12. kiloliters to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(klml(num1))
    elif select2 == 2:
      print(klcl(num1))
    elif select2 == 3:
      print(kldil(num1))
    elif select2 == 4:
      print(kll(num1))
    elif select2 == 5:
      print(kldal(num1))
    elif select2 == 6:
      print(klhecl(num1))
    elif select2 == 7:
      print(klkl(num1))
    elif select2 == 8:
      print(klo(num1))
    elif select2 == 9:
      print(klcu(num1))
    elif select2 == 10:
      print(klp(num1))
    elif select2 == 11:
      print(klq(num1))
    elif select2 == 12:
      print(klg(num1))
  if select == 8:
    print("1.  ounces to mililiters")
    print("2.  ounces to centiliters")
    print("3.  ounces to deciliters")
    print("4.  ounces to liters")
    print("5.  ounces to decaliters")
    print("6.  ounces to hectoliters")
    print("7.  ounces to kiloliters")
    print("8.  ounces to ounces")
    print("9.  ounces to cups")
    print("10. ounces to pints")
    print("11. ounces to quarts")
    print("12. ounces to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(oml(num1))
    elif select2 == 2:
      print(ocl(num1))
    elif select2 == 3:
      print(odil(num1))
    elif select2 == 4:
      print(ol(num1))
    elif select2 == 5:
      print(odal(num1))
    elif select2 == 6:
      print(ohecl(num1))
    elif select2 == 7:
      print(okl(num1))
    elif select2 == 8:
      print(oo(num1))
    elif select2 == 9:
      print(ocu(num1))
    elif select2 == 10:
      print(op(num1))
    elif select2 == 11:
      print(oq(num1))
    elif select2 == 12:
      print(og(num1))
  if select == 9:
    print("1.  cups to mililiters")
    print("2.  cups to centiliters")
    print("3.  cups to deciliters")
    print("4.  cups to liters")
    print("5.  cups to decaliters")
    print("6.  cups to hectoliters")
    print("7.  cups to kiloliters")
    print("8.  cups to ounces")
    print("9.  cups to cups")
    print("10. cups to pints")
    print("11. cups to quarts")
    print("12. cups to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(cuml(num1))
    elif select2 == 2:
      print(cucl(num1))
    elif select2 == 3:
      print(cudil(num1))
    elif select2 == 4:
      print(cul(num1))
    elif select2 == 5:
      print(cudal(num1))
    elif select2 == 6:
      print(cuhecl(num1))
    elif select2 == 7:
      print(cukl(num1))
    elif select2 == 8:
      print(cuo(num1))
    elif select2 == 9:
      print(cucu(num1))
    elif select2 == 10:
      print(cup(num1))
    elif select2 == 11:
      print(cuq(num1))
    elif select2 == 12:
      print(cug(num1))
  if select == 10:
    print("1.  pints to mililiters")
    print("2.  pints to centiliters")
    print("3.  pints to deciliters")
    print("4.  pints to liters")
    print("5.  pints to decaliters")
    print("6.  pints to hectoliters")
    print("7.  pints to kiloliters")
    print("8.  pints to ounces")
    print("9.  pints to cups")
    print("10. pints to pints")
    print("11. pints to quarts")
    print("12. pints to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(pml(num1))
    elif select2 == 2:
      print(pcl(num1))
    elif select2 == 3:
      print(pdil(num1))
    elif select2 == 4:
      print(pl(num1))
    elif select2 == 5:
      print(pdal(num1))
    elif select2 == 6:
      print(phecl(num1))
    elif select2 == 7:
      print(pkl(num1))
    elif select2 == 8:
      print(po(num1))
    elif select2 == 9:
      print(pcu(num1))
    elif select2 == 10:
      print(pp(num1))
    elif select2 == 11:
      print(pq(num1))
    elif select2 == 12:
      print(pg(num1))
  if select == 11:
    print("1.  quarts to mililiters")
    print("2.  quarts to centiliters")
    print("3.  quarts to deciliters")
    print("4.  quarts to liters")
    print("5.  quarts to decaliters")
    print("6.  quarts to hectoliters")
    print("7.  quarts to kiloliters")
    print("8.  quarts to ounces")
    print("9.  quarts to cups")
    print("10. quarts to pints")
    print("11. quarts to quarts")
    print("12. quarts to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(qml(num1))
    elif select2 == 2:
      print(qcl(num1))
    elif select2 == 3:
      print(qdil(num1))
    elif select2 == 4:
      print(ql(num1))
    elif select2 == 5:
      print(qdal(num1))
    elif select2 == 6:
      print(qhecl(num1))
    elif select2 == 7:
      print(qkl(num1))
    elif select2 == 8:
      print(qo(num1))
    elif select2 == 9:
      print(qcu(num1))
    elif select2 == 10:
      print(qp(num1))
    elif select2 == 11:
      print(qq(num1))
    elif select2 == 12:
      print(qg(num1))
  if select == 12:
    print("1.  gallons to mililiters")
    print("2.  gallons to centiliters")
    print("3.  gallons to deciliters")
    print("4.  gallons to liters")
    print("5.  gallons to decaliters")
    print("6.  gallons to hectoliters")
    print("7.  gallons to kiloliters")
    print("8.  gallons to ounces")
    print("9.  gallons to cups")
    print("10. gallons to pints")
    print("11. gallons to quarts")
    print("12. gallons to gallons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter first number: "))
    if select2 == 1:
      print(gml(num1))
    elif select2 == 2:
      print(gcl(num1))
    elif select2 == 3:
      print(gdil(num1))
    elif select2 == 4:
      print(gl(num1))
    elif select2 == 5:
      print(gdal(num1))
    elif select2 == 6:
      print(ghecl(num1))
    elif select2 == 7:
      print(gkl(num1))
    elif select2 == 8:
      print(go(num1))
    elif select2 == 9:
      print(gcu(num1))
    elif select2 == 10:
      print(gp(num1))
    elif select2 == 11:
      print(gq(num1))
    elif select2 == 12:
      print(gg(num1))
elif selec == 5:
  print("1.  miligrams to")
  print("2.  centigrams to")
  print("3.  decigrams to")
  print("4.  grams to")
  print("5.  decagrams to")
  print("6.  hectogrrams to")
  print("7.  kilograms to")
  print("8.  ounces to")
  print("9.  pounds to")
  print("10. tons to")
  print("11. craptons to")
  select = int(input("enter choice: "))
  if select == 1:
    print("1.  miligrams to miligrams")
    print("2.  miligrams to centigrams")
    print("3.  miligrams to decigrams")
    print("4.  miligrams to grams")
    print("5.  miligrams to decagrams")
    print("6.  miligrams to hectograms")
    print("7.  miligrams to kilograms")
    print("8.  miligrams to weight ounces")
    print("9.  miligrams to pounds")
    print("10. miligrams to imperial tons")
    print("11. miligrams to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(mgmg(num1))
    if select2 == 2:
      print(mgcg(num1))
    if select2 == 3:
      print(mgdig(num1))
    if select2 == 4:
      print(mgg(num1))
    if select2 == 5:
      print(mgdag(num1))
    if select2 == 6:
      print(mgheg(num1))
    if select2 == 7:
      print(mgkg(num1))
    if select2 == 8:
      print(mgop(num1))
    if select2 == 9:
      print(mglbs(num1))
    if select2 == 10:
      print(mgton(num1))
    if select2 == 11:
      print(mgcton(num1))
  if select == 2:
    print("1.  centigrams to miligrams")
    print("2.  centigrams to centigrams")
    print("3.  centigrams to decigrams")
    print("4.  centigrams to grams")
    print("5.  centigrams to decagrams")
    print("6.  centigrams to hectograms")
    print("7.  centigrams to kilograms")
    print("8.  centigrams to weight ounces")
    print("9.  centigrams to pounds")
    print("10. centigrams to imperial tons")
    print("11. centigrams to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(cgmg(num1))
    if select2 == 2:
      print(cgcg(num1))
    if select2 == 3:
      print(cgdig(num1))
    if select2 == 4:
      print(cgg(num1))
    if select2 == 5:
      print(cgdag(num1))
    if select2 == 6:
      print(cgheg(num1))
    if select2 == 7:
      print(cgkg(num1))
    if select2 == 8:
      print(cgop(num1))
    if select2 == 9:
      print(cglbs(num1))
    if select2 == 10:
      print(cgton(num1))
    if select2 == 11:
      print(cgcton(num1))

  if select == 3:
    print("1.  decigrams to miligrams")
    print("2.  decigrams to centigrams")
    print("3.  decigrams to decigrams")
    print("4.  decigrams to grams")
    print("5.  decigrams to decagrams")
    print("6.  decigrams to hectograms")
    print("7.  decigrams to kilograms")
    print("8.  decigrams to weight ounces")
    print("9.  decigrams to pounds")
    print("10. decigrams to imperial tons")
    print("11. decigrams to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(digmg(num1))
    if select2 == 2:
      print(digcg(num1))
    if select2 == 3:
      print(digdig(num1))
    if select2 == 4:
      print(digg(num1))
    if select2 == 5:
      print(digdag(num1))
    if select2 == 6:
      print(digheg(num1))
    if select2 == 7:
      print(digkg(num1))
    if select2 == 8:
      print(digop(num1))
    if select2 == 9:
      print(diglbs(num1))
    if select2 == 10:
      print(digton(num1))
    if select2 == 11:
      print(digcton(num1))
  if select == 4:
    print("1.  grams to miligrams")
    print("2.  grams to centigrams")
    print("3.  grams to decigrams")
    print("4.  grams to grams")
    print("5.  grams to decagrams")
    print("6.  grams to hectograms")
    print("7.  grams to kilograms")
    print("8.  grams to weight ounces")
    print("9.  grams to pounds")
    print("10. grams to imperial tons")
    print("11. grams to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(gmg(num1))
    if select2 == 2:
      print(gcg(num1))
    if select2 == 3:
      print(gdig(num1))
    if select2 == 4:
      print(gg(num1))
    if select2 == 5:
      print(gdag(num1))
    if select2 == 6:
      print(gheg(num1))
    if select2 == 7:
      print(gkg(num1))
    if select2 == 8:
      print(gop(num1))
    if select2 == 9:
      print(glbs(num1))
    if select2 == 10:
      print(gton(num1))
    if select2 == 11:
      print(gcton(num1))
  if select == 5:
    print("1.  decagrams to miligrams")
    print("2.  decagrams to centigrams")
    print("3.  decagrams to decigrams")
    print("4.  decagrams to grams")
    print("5.  decagrams to decagrams")
    print("6.  decagrams to hectograms")
    print("7.  decagrams to kilograms")
    print("8.  decagrams to weight ounces")
    print("9.  decagrams to pounds")
    print("10. decagrams to imperial tons")
    print("11. decagrams to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(dagmg(num1))
    if select2 == 2:
      print(dagcg(num1))
    if select2 == 3:
      print(dagdig(num1))
    if select2 == 4:
      print(dagg(num1))
    if select2 == 5:
      print(dagdag(num1))
    if select2 == 6:
      print(dagheg(num1))
    if select2 == 7:
      print(dagkg(num1))
    if select2 == 8:
      print(dagop(num1))
    if select2 == 9:
      print(daglbs(num1))
    if select2 == 10:
      print(dagton(num1))
    if select2 == 11:
      print(dagcton(num1))
  if select == 6:
    print("1.  hectograms to miligrams")
    print("2.  hectograms to centigrams")
    print("3.  hectograms to decigrams")
    print("4.  hectograms to grams")
    print("5.  hectograms to decagrams")
    print("6.  hectograms to hectograms")
    print("7.  hectograms to kilograms")
    print("8.  hectograms to weight ounces")
    print("9.  hectograms to pounds")
    print("10. hectograms to imperial tons")
    print("11. hectograms to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(hegmg(num1))
    if select2 == 2:
      print(hegcg(num1))
    if select2 == 3:
      print(hegdig(num1))
    if select2 == 4:
      print(hegg(num1))
    if select2 == 5:
      print(hegdag(num1))
    if select2 == 6:
      print(hegheg(num1))
    if select2 == 7:
      print(hegkg(num1))
    if select2 == 8:
      print(hegop(num1))
    if select2 == 9:
      print(heglbs(num1))
    if select2 == 10:
      print(hegton(num1))
    if select2 == 11:
      print(hegcton(num1))
  if select == 7:
    print("1.  kilograms to miligrams")
    print("2.  kilograms to centigrams")
    print("3.  kilograms to decigrams")
    print("4.  kilograms to grams")
    print("5.  kilograms to decagrams")
    print("6.  kilograms to hectograms")
    print("7.  kilograms to kilograms")
    print("8.  kilograms to weight ounces")
    print("9.  kilograms to pounds")
    print("10. kilograms to imperial tons")
    print("11. kilograms to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(kgmg(num1))
    if select2 == 2:
      print(kgcg(num1))
    if select2 == 3:
      print(kgdig(num1))
    if select2 == 4:
      print(kgg(num1))
    if select2 == 5:
      print(kgdag(num1))
    if select2 == 6:
      print(kgheg(num1))
    if select2 == 7:
      print(kgkg(num1))
    if select2 == 8:
      print(kgop(num1))
    if select2 == 9:
      print(kglbs(num1))
    if select2 == 10:
      print(kgton(num1))
    if select2 == 11:
      print(kgcton(num1))
  if select == 8:
    print("1.  weight ounces to miligrams")
    print("2.  weight ounces to centigrams")
    print("3.  weight ounces to decigrams")
    print("4.  weight ounces to grams")
    print("5.  weight ounces to decagrams")
    print("6.  weight ounces to hectograms")
    print("7.  weight ounces to kilograms")
    print("8.  weight ounces to weight ounces")
    print("9.  weight ounces to pounds")
    print("10. weight ounces to imperial tons")
    print("11. weight ounces to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(opmg(num1))
    if select2 == 2:
      print(opcg(num1))
    if select2 == 3:
      print(opdig(num1))
    if select2 == 4:
      print(opg(num1))
    if select2 == 5:
      print(opdag(num1))
    if select2 == 6:
      print(opheg(num1))
    if select2 == 7:
      print(opkg(num1))
    if select2 == 8:
      print(opop(num1))
    if select2 == 9:
      print(oplbs(num1))
    if select2 == 10:
      print(opton(num1))
    if select2 == 11:
      print(opcton(num1))
  if select == 9:
    print("1.  pounds to miligrams")
    print("2.  pounds to centigrams")
    print("3.  pounds to decigrams")
    print("4.  pounds to grams")
    print("5.  pounds to decagrams")
    print("6.  pounds to hectograms")
    print("7.  pounds to kilograms")
    print("8.  pounds to weight ounces")
    print("9.  pounds to pounds")
    print("10. pounds to imperial tons")
    print("11. pounds to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(lbsmg(num1))
    if select2 == 2:
      print(lbscg(num1))
    if select2 == 3:
      print(lbsdig(num1))
    if select2 == 4:
      print(lbsg(num1))
    if select2 == 5:
      print(lbsdag(num1))
    if select2 == 6:
      print(lbsheg(num1))
    if select2 == 7:
      print(lbskg(num1))
    if select2 == 8:
      print(lbsop(num1))
    if select2 == 9:
      print(lbslbs(num1))
    if select2 == 10:
      print(lbston(num1))
    if select2 == 11:
      print(lbscton(num1))
  if select == 10:
    print("1.  imperial tons to miligrams")
    print("2.  imperial tons to centigrams")
    print("3.  imperial tons to decigrams")
    print("4.  imperial tons to grams")
    print("5.  imperial tons to decagrams")
    print("6.  imperial tons to hectograms")
    print("7.  imperial tons to kilograms")
    print("8.  imperial tons to weight ounces")
    print("9.  imperial tons to pounds")
    print("10. imperial tons to imperial tons")
    print("11. imperial tons to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(tonmg(num1))
    if select2 == 2:
      print(toncg(num1))
    if select2 == 3:
      print(tondig(num1))
    if select2 == 4:
      print(tong(num1))
    if select2 == 5:
      print(tondag(num1))
    if select2 == 6:
      print(tonheg(num1))
    if select2 == 7:
      print(tonkg(num1))
    if select2 == 8:
      print(tonop(num1))
    if select2 == 9:
      print(tonlbs(num1))
    if select2 == 10:
      print(tonton(num1))
    if select2 == 11:
      print(toncton(num1))
  if select == 11:
    print("1.  imperial craptons to miligrams")
    print("2.  imperial craptons to centigrams")
    print("3.  imperial craptons to decigrams")
    print("4.  imperial craptons to grams")
    print("5.  imperial craptons to decagrams")
    print("6.  imperial craptons to hectograms")
    print("7.  imperial craptons to kilograms")
    print("8.  imperial craptons to weight ounces")
    print("9.  imperial craptons to pounds")
    print("10. imperial craptons to imperial tons")
    print("11. imperial craptons to imperial craptons")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(ctonmg(num1))
    if select2 == 2:
      print(ctoncg(num1))
    if select2 == 3:
      print(ctondig(num1))
    if select2 == 4:
      print(ctong(num1))
    if select2 == 5:
      print(ctondag(num1))
    if select2 == 6:
      print(ctonheg(num1))
    if select2 == 7:
      print(ctonkg(num1))
    if select2 == 8:
      print(ctonop(num1))
    if select2 == 9:
      print(ctonlbs(num1))
    if select2 == 10:
      print(ctonton(num1))
    if select2 == 11:
      print(ctoncton(num1))

elif selec == 6:
  print("1.  microseiverts to")
  print("2.  miliseiverts to")
  print("3.  sieverts to")
  print("4.  rotogens to")
  print("5.  milirotogens to")
  print("6.  microrotogens")
  select = int(input("enter choice: "))
  if select == 1:
    print("1.  microseiverts to microseiverts")
    print("2.  microseiverts to miliseiverts")
    print("3.  microseiverts to seiverts")
    print("4.  microseiverts to microrotogens")
    print("5.  microseiverts to milirotogens")
    print("6.  microseiverts to rotogens")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(mcsmcs(num1))
    if select2 == 2:
      print(mcsmis(num1))
    if select2 == 3:
      print(mcss(num1))
    if select2 == 4:
      print(mcsmcr(num1))
    if select2 == 5:
      print(mcsmir(num1))
    if select2 == 6:
      print(mcsr(num1))
  if select == 2:
    print("1.  miliseiverts to microseiverts")
    print("2.  miliseiverts to miliseiverts")
    print("3.  miliseiverts to seiverts")
    print("4.  miliseiverts to microrotogens")
    print("5.  miliseiverts to milirotogens")
    print("6.  miliseiverts to rotogens")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(mismcs(num1))
    if select2 == 2:
      print(mismis(num1))
    if select2 == 3:
      print(miss(num1))
    if select2 == 4:
      print(mismcr(num1))
    if select2 == 5:
      print(mismir(num1))
    if select2 == 6:
      print(misr(num1))
  if select == 3:
    print("1.  seiverts to microseiverts")
    print("2.  seiverts to miliseiverts")
    print("3.  seiverts to seiverts")
    print("4.  seiverts to microrotogens")
    print("5.  seiverts to milirotogens")
    print("6.  seiverts to rotogens")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(smcs(num1))
    if select2 == 2:
      print(smis(num1))
    if select2 == 3:
      print(ss(num1))
    if select2 == 4:
      print(smcr(num1))
    if select2 == 5:
      print(smir(num1))
    if select2 == 6:
      print(sr(num1))
  if select == 4:
    print("1.  microrotogens to microseiverts")
    print("2.  microrotogens to miliseiverts")
    print("3.  microrotogens to seiverts")
    print("4.  microrotogens to microrotogens")
    print("5.  microrotogens to milirotogens")
    print("6.  microrotogens to rotogens")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(mcrmcs(num1))
    if select2 == 2:
      print(mcrmis(num1))
    if select2 == 3:
      print(mcrs(num1))
    if select2 == 4:
      print(mcrmcr(num1))
    if select2 == 5:
      print(mcrmir(num1))
    if select2 == 6:
      print(mcrr(num1))
  if select == 5:
    print("1.  milirotogens to microseiverts")
    print("2.  milirotogens to miliseiverts")
    print("3.  milirotogens to seiverts")
    print("4.  milirotogens to microrotogens")
    print("5.  milirotogens to milirotogens")
    print("6.  milirotogens to rotogens")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(mirmcs(num1))
    if select2 == 2:
      print(mirmis(num1))
    if select2 == 3:
      print(mirs(num1))
    if select2 == 4:
      print(mirmcr(num1))
    if select2 == 5:
      print(mirmir(num1))
    if select2 == 6:
      print(mirr(num1))
  if select == 6:
    print("1.  rotogens to microseiverts")
    print("2.  rotogens to miliseiverts")
    print("3.  rotogens to seiverts")
    print("4.  rotogens to microrotogens")
    print("5.  rotogens to milirotogens")
    print("6.  rotogens to rotogens")
    select2 = int(input("enter choice: "))
    num1 = float(input("enter input: "))
    if select2 == 1:
      print(rmcs(num1))
    if select2 == 2:
      print(rmis(num1))
    if select2 == 3:
      print(rs(num1))
    if select2 == 4:
      print(rmcr(num1))
    if select2 == 5:
      print(rmir(num1))
    if select2 == 6:
      print(rr(num1))
elif selec == 7:
  print('1.  bits to')
  print('2.  kilobits to')
  print('3.  megabits to')
  print('4.  gigabits to')
  print('5.  terabits to')
  print('6.  petabits to')
  print('7.  bytes to')
  print('8.  kilobytes to')
  print('9.  megabytes to')
  print('10. gigabytes to')
  print('11. terabytes to')
  print('12. petabytes to')
  select = int(input('enter choice:'))
  if select == 1:
    print("1.  bits to bits")
    print("2.  bits to kilobits")
    print("3.  bits to megbits")
    print("4.  bits to gigabits")
    print("5.  bits to terabits")
    print("6.  bits to petabits")
    print("7.  bits to bytes")
    print("8.  bits to kilobytes")
    print("9.  bits to megabytes")
    print("10. bits to gigabytes")
    print("11. bits to terabytes")
    print("12. bits to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(bibi(num1))
    elif select2 == 2:
      print(bikb(num1))
    elif select2 == 3:
      print(bimb(num1))
    elif select2 == 4:
      print(bigb(num1))
    elif select2 == 5:
      print(bitb(num1))
    elif select2 == 6:
      print(bipb(num1))
    elif select2 == 7:
      print(bibt(num1))
    elif select2 == 8:
      print(bikB(num1))
    elif select2 == 9:
      print(bimB(num1))
    elif select2 == 10:
      print(bigB(num1))
    elif select2 == 11:
      print(bitB(num1))
    elif select2 == 12:
      print(bipB(num1))
  if select == 2:
    print("1.  kilobits to bits")
    print("2.  kilobits to kilobits")
    print("3.  kilobits to megbits")
    print("4.  kilobits to gigabits")
    print("5.  kilobits to terabits")
    print("6.  kilobits to petabits")
    print("7.  kilobits to bytes")
    print("8.  kilobits to kilobytes")
    print("9.  kilobits to megabytes")
    print("10. kilobits to gigabytes")
    print("11. kilobits to terabytes")
    print("12. kilobits to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(kbbi(num1))
    elif select2 == 2:
      print(kbkb(num1))
    elif select2 == 3:
      print(kbmb(num1))
    elif select2 == 4:
      print(kbgb(num1))
    elif select2 == 5:
      print(kbtb(num1))
    elif select2 == 6:
      print(kbpb(num1))
    elif select2 == 7:
      print(kbbt(num1))
    elif select2 == 8:
      print(kbkB(num1))
    elif select2 == 9:
      print(kbmB(num1))
    elif select2 == 10:
      print(kbgB(num1))
    elif select2 == 11:
      print(kbtB(num1))
    elif select2 == 12:
      print(kbpB(num1))
  if select == 3:
    print("1.  megabits to bits")
    print("2.  megabits to kilobits")
    print("3.  megabits to megbits")
    print("4.  megabits to gigabits")
    print("5.  megabits to terabits")
    print("6.  megabits to petabits")
    print("7.  megabits to bytes")
    print("8.  megabits to kilobytes")
    print("9.  megabits to megabytes")
    print("10. megabits to gigabytes")
    print("11. megabits to terabytes")
    print("12. megabits to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(mbbi(num1))
    elif select2 == 2:
      print(mbkb(num1))
    elif select2 == 3:
      print(mbmb(num1))
    elif select2 == 4:
      print(mbgb(num1))
    elif select2 == 5:
      print(mbtb(num1))
    elif select2 == 6:
      print(mbpb(num1))
    elif select2 == 7:
      print(mbbt(num1))
    elif select2 == 8:
      print(mbkB(num1))
    elif select2 == 9:
      print(mbmB(num1))
    elif select2 == 10:
      print(mbgB(num1))
    elif select2 == 11:
      print(mbtB(num1))
    elif select2 == 12:
      print(mbpB(num1))
  if select == 4:
    print("1.  gigabits to bits")
    print("2.  gigabits to kilobits")
    print("3.  gigabits to megbits")
    print("4.  gigabits to gigabits")
    print("5.  gigabits to terabits")
    print("6.  gigabits to petabits")
    print("7.  gigabits to bytes")
    print("8.  gigabits to kilobytes")
    print("9.  gigabits to megabytes")
    print("10. gigabits to gigabytes")
    print("11. gigabits to terabytes")
    print("12. gigabits to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(gbbi(num1))
    elif select2 == 2:
      print(gbkb(num1))
    elif select2 == 3:
      print(gbmb(num1))
    elif select2 == 4:
      print(gbgb(num1))
    elif select2 == 5:
      print(gbtb(num1))
    elif select2 == 6:
      print(gbpb(num1))
    elif select2 == 7:
      print(gbbt(num1))
    elif select2 == 8:
      print(gbkB(num1))
    elif select2 == 9:
      print(gbmB(num1))
    elif select2 == 10:
      print(gbgB(num1))
    elif select2 == 11:
      print(gbtB(num1))
    elif select2 == 12:
      print(gbpB(num1))
  if select == 5:
    print("1.  terabits to bits")
    print("2.  terabits to kilobits")
    print("3.  terabits to megbits")
    print("4.  terabits to gigabits")
    print("5.  terabits to terabits")
    print("6.  terabits to petabits")
    print("7.  terabits to bytes")
    print("8.  terabits to kilobytes")
    print("9.  terabits to megabytes")
    print("10. terabits to gigabytes")
    print("11. terabits to terabytes")
    print("12. terabits to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(tbbi(num1))
    elif select2 == 2:
      print(tbkb(num1))
    elif select2 == 3:
      print(tbmb(num1))
    elif select2 == 4:
      print(tbgb(num1))
    elif select2 == 5:
      print(tbtb(num1))
    elif select2 == 6:
      print(tbpb(num1))
    elif select2 == 7:
      print(tbbt(num1))
    elif select2 == 8:
      print(tbkB(num1))
    elif select2 == 9:
      print(tbmB(num1))
    elif select2 == 10:
      print(tbgB(num1))
    elif select2 == 11:
      print(tbtB(num1))
    elif select2 == 12:
      print(tbpB(num1))
  if select == 6:
    print("1.  petabits to bits")
    print("2.  petabits to kilobits")
    print("3.  petabits to megbits")
    print("4.  petabits to gigabits")
    print("5.  petabits to terabits")
    print("6.  petabits to petabits")
    print("7.  petabits to bytes")
    print("8.  petabits to kilobytes")
    print("9.  petabits to megabytes")
    print("10. petabits to gigabytes")
    print("11. petabits to terabytes")
    print("12. petabits to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(pbbi(num1))
    elif select2 == 2:
      print(pbkb(num1))
    elif select2 == 3:
      print(pBmb(num1))
    elif select2 == 4:
      print(pbgb(num1))
    elif select2 == 5:
      print(pbtb(num1))
    elif select2 == 6:
      print(pbpb(num1))
    elif select2 == 7:
      print(pbbt(num1))
    elif select2 == 8:
      print(pbkB(num1))
    elif select2 == 9:
      print(pbmB(num1))
    elif select2 == 10:
      print(pbgB(num1))
    elif select2 == 11:
      print(pbtB(num1))
    elif select2 == 12:
      print(pbpB(num1))
  if select == 7:
    print("1.  bits to bits")
    print("2.  bits to kilobits")
    print("3.  bits to megbits")
    print("4.  bits to gigabits")
    print("5.  bits to terabits")
    print("6.  bits to petabits")
    print("7.  bits to bytes")
    print("8.  bits to kilobytes")
    print("9.  bits to megabytes")
    print("10. bits to gigabytes")
    print("11. bits to terabytes")
    print("12. bits to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(btbi(num1))
    elif select2 == 2:
      print(btkb(num1))
    elif select2 == 3:
      print(btmb(num1))
    elif select2 == 4:
      print(btgb(num1))
    elif select2 == 5:
      print(bttb(num1))
    elif select2 == 6:
      print(btpb(num1))
    elif select2 == 7:
      print(btbt(num1))
    elif select2 == 8:
      print(btkB(num1))
    elif select2 == 9:
      print(btmB(num1))
    elif select2 == 10:
      print(btgB(num1))
    elif select2 == 11:
      print(bttB(num1))
    elif select2 == 12:
      print(btpB(num1))
  if select == 8:
    print("1.  kilobytes to bits")
    print("2.  kilobytes to kilobits")
    print("3.  kilobytes to megbits")
    print("4.  kilobytes to gigabits")
    print("5.  kilobytes to terabits")
    print("6.  kilobytes to petabits")
    print("7.  kilobytes to bytes")
    print("8.  kilobytes to kilobytes")
    print("9.  kilobytes to megabytes")
    print("10. kilobytes to gigabytes")
    print("11. kilobytes to terabytes")
    print("12. kilobytes to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(kBbi(num1))
    elif select2 == 2:
      print(kBkb(num1))
    elif select2 == 3:
      print(kBmb(num1))
    elif select2 == 4:
      print(kBgb(num1))
    elif select2 == 5:
      print(kBtb(num1))
    elif select2 == 6:
      print(kBpb(num1))
    elif select2 == 7:
      print(kBbt(num1))
    elif select2 == 8:
      print(kBkB(num1))
    elif select2 == 9:
      print(kBmB(num1))
    elif select2 == 10:
      print(kBgB(num1))
    elif select2 == 11:
      print(kBtB(num1))
    elif select2 == 12:
      print(kBpB(num1))
  if select == 9:
    print("1.  megabytes to bits")
    print("2.  megabytes to kilobits")
    print("3.  megabytes to megbits")
    print("4.  megabytes to gigabits")
    print("5.  megabytes to terabits")
    print("6.  megabytes to petabits")
    print("7.  megabytes to bytes")
    print("8.  megabytes to kilobytes")
    print("9.  megabytes to megabytes")
    print("10. megabytes to gigabytes")
    print("11. megabytes to terabytes")
    print("12. megabytes to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(mBbi(num1))
    elif select2 == 2:
      print(mBkb(num1))
    elif select2 == 3:
      print(mBmb(num1))
    elif select2 == 4:
      print(mBgb(num1))
    elif select2 == 5:
      print(mBtb(num1))
    elif select2 == 6:
      print(mBpb(num1))
    elif select2 == 7:
      print(mBbt(num1))
    elif select2 == 8:
      print(mBkB(num1))
    elif select2 == 9:
      print(mBmB(num1))
    elif select2 == 10:
      print(mBgB(num1))
    elif select2 == 11:
      print(mBtB(num1))
    elif select2 == 12:
      print(mBpB(num1))
  if select == 10:
    print("1.  gigabytes to bits")
    print("2.  gigabytes to kilobits")
    print("3.  gigabytes to megbits")
    print("4.  gigabytes to gigabits")
    print("5.  gigabytes to terabits")
    print("6.  gigabytes to petabits")
    print("7.  gigabytes to bytes")
    print("8.  gigabytes to kilobytes")
    print("9.  gigabytes to megabytes")
    print("10. gigabytes to gigabytes")
    print("11. gigabytes to terabytes")
    print("12. gigabytes to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(gBbi(num1))
    elif select2 == 2:
      print(gBkb(num1))
    elif select2 == 3:
      print(gBmb(num1))
    elif select2 == 4:
      print(gBgb(num1))
    elif select2 == 5:
      print(gBtb(num1))
    elif select2 == 6:
      print(gBpb(num1))
    elif select2 == 7:
      print(gBbt(num1))
    elif select2 == 8:
      print(gBkB(num1))
    elif select2 == 9:
      print(gBmB(num1))
    elif select2 == 10:
      print(gBgB(num1))
    elif select2 == 11:
      print(gBtB(num1))
    elif select2 == 12:
      print(gBpB(num1))
  if select == 11:
    print("1.  terabytes to bits")
    print("2.  terabytes to kilobits")
    print("3.  terabytes to megbits")
    print("4.  terabytes to gigabits")
    print("5.  terabytes to terabits")
    print("6.  terabytes to petabits")
    print("7.  terabytes to bytes")
    print("8.  terabytes to kilobytes")
    print("9.  terabytes to megabytes")
    print("10. terabytes to gigabytes")
    print("11. terabytes to terabytes")
    print("12. terabytes to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(tBbi(num1))
    elif select2 == 2:
      print(tBkb(num1))
    elif select2 == 3:
      print(tBmb(num1))
    elif select2 == 4:
      print(tBgb(num1))
    elif select2 == 5:
      print(tBtb(num1))
    elif select2 == 6:
      print(tBpb(num1))
    elif select2 == 7:
      print(tBbt(num1))
    elif select2 == 8:
      print(tBkB(num1))
    elif select2 == 9:
      print(tBmB(num1))
    elif select2 == 10:
      print(tBgB(num1))
    elif select2 == 11:
      print(tBtB(num1))
    elif select2 == 12:
      print(tBpB(num1))
  if select == 12:
    print("1.  petabytes to bits")
    print("2.  petabytes to kilobits")
    print("3.  petabytes to megbits")
    print("4.  petabytes to gigabits")
    print("5.  petabytes to terabits")
    print("6.  petabytes to petabits")
    print("7.  petabytes to bytes")
    print("8.  petabytes to kilobytes")
    print("9.  petabytes to megabytes")
    print("10. petabytes to gigabytes")
    print("11. petabytes to terabytes")
    print("12. petabytes to petabytes")
    select2 = int(input("enter choice"))
    num1 = float(input("enter first number:"))
    if select2 == 1:
      print(pBbi(num1))
    elif select2 == 2:
      print(pBkb(num1))
    elif select2 == 3:
      print(pBmb(num1))
    elif select2 == 4:
      print(pBgb(num1))
    elif select2 == 5:
      print(pBtb(num1))
    elif select2 == 6:
      print(pBpb(num1))
    elif select2 == 7:
      print(pBbt(num1))
    elif select2 == 8:
      print(pBkB(num1))
    elif select2 == 9:
      print(pBmB(num1))
    elif select2 == 10:
      print(pBgB(num1))
    elif select2 == 11:
      ans = pBtB(num1)
    elif select2 == 12:
      ans = (pBpB(num1))
    print('1. yes')
    print('2. no')
    x = int(input('Do you want to round '))
    y = int(input('num of places to round to '))
    if x == 1:
      print(round(ans, y))
    elif x == 2:
      print(ans)
    else:
      print('invalid input')