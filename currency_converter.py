def usd_to_pkr(usd):
    rate = 278.5  # example rate
    return usd * rate

dollars = float(input("Enter amount in USD: "))
print(f"{dollars} USD = {usd_to_pkr(dollars)} PKR")
