from datetime import datetime
S = datetime.strptime(input(), "%Y/%m/%d")
print("Heisei" if datetime(2019,4,30) >= S else "TBD")