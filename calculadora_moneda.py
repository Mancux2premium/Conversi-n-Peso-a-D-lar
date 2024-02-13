informacion = "El precio de compra del Dolar es  de $"
peso = 1145
dolar = 1145
dolar_compra = 1145
dolar_venta =1125
Dolar = " Dolares"
Pesos = " Pesos"
venta_completada = "Felicidades compraste $"
peso= int(input("¿Cuantos pesos quieres vender?"))
dolar= input("¿Cuantos dolares quieres vender?")

peso_to_dolar_buy = peso / dolar_compra
dolar_to_peso_buy = float(dolar)* dolar_venta 

print(informacion,dolar_compra,sep="")


print(venta_completada,round(peso_to_dolar_buy, 2),Dolar,sep="")
print(venta_completada,dolar_to_peso_buy,Pesos,sep="")
