print("Write  a  Program  to  read  the  Selling  Price  and  Cost  Price  of  any  item  and  check the whether the shopkeeper gain Profit or Loss or no Profit no Loss.")
cp = float(input('Enter cost price: '   ))
sp = float(input('Enter selling price: '))
if sp>cp:
    print('Profit of', 100*(sp -cp)/cp, '%')
elif sp<cp:
    print('Loss of',   100*(cp -sp)/cp, '%')
else:
    print('No profit no loss')