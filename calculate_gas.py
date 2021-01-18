gas_price = input("gas cost: ")
gas = input("gas used: ")
eth_price = input("eth price: $")

print("$" + str(int(gas_price) * int(gas) * int(eth_price) * 0.000000001))
