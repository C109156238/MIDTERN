a=list("rat,ox,tiger,rabbit,dragon,snake,horse,sheep,monkey,rooster,dog,pig".split(","))
year=int(input("please input year:"))
print(a[year%12-4])
