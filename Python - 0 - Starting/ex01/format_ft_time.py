import time
import datetime as dt

x = time.time()
print(f"Seconds since January 1, 1970: {x:,.4f} or {x:.2e} in scientific notation")

x = dt.date.today()
print(x.strftime("%b %d %Y"))
