#!/usr/bin/env python3

import sys
import requests


BASE_URL = "https://api.hitbtc.com/api/2/public/ticker/"

ETH = "ETHUSD"
ETC = "ETCUSD"
XMR = "XMRUSD"
ZEC = "ZECUSD"
 
def getExchangeRate(symbol):
	
	resp = requests.get(BASE_URL + symbol)

	print(symbol + " " + resp.json()["last"])
	return resp.json()["last"]


if __name__=='__main__':
	
	ETH = getExchangeRate(ETH)
	ETC = getExchangeRate(ETC)
	XMR = getExchangeRate(XMR)
	ZEC = getExchangeRate(ZEC)

	rates = [ ETH, ETC, XMR, ZEC ] 
	rates.sort()

	if (rates[-1] == ETH):
		sys.exit(1)
	if (rates[-1] == ETC):
		sys.exit(2)
	if (rates[-1] == XMR):
		sys.exit(3)
	if (rates[-1] == ZEC):
		sys.exit(4)

