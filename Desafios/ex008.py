#Conversor de distância
m=float(input("Digite a distância em m. "))
km=m/1000
hm=m/100
dam=m/10
dm=m*10
cm=m*100
mm=m*1000

print(" A distância é de {}Km. \n \n A distância é de {}hm. \n".format(km,hm))
print(" A distância é de {}dam. \n \n A distância é de {}dm. \n".format(dam,dm))
print(" A distância é de {}cm. \n \n A distância é de {}mm.".format(cm,mm))