
import numpy as np
i=5
while i!=0:
    num=float(input())
    y=(0.587972*(0.0953454+0.340013+num))+(np.tanh(0.836249*np.sqrt(-0.00999988+num))/0.0257725)+abs(np.tan(-0.0468725*num))
    print(np.round(y,decimals=2))