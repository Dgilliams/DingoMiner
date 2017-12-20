# DingoMiner
GPU mining Cryptos for Linux

To get started:
	Replace the WalletIDs and worker names in each mining script with your own. If you don't, I'll gladly collect a 'dummy tax'
	WalletIDs are found in following:
	
		DingoMiner/Ethereum/mineETC.sh
		DingoMiner/Ethereum/mineETH.sh
		DingoMiner/Monero/mineXMR.sh
		DingoMiner/ZCash/mineZEC.sh

	

may need to set 'init.sh' as executable before starting:
	chmod +x init.sh

Then run:
	./init.sh


Then should be able to run:
	./mineAll.sh
or
	./mineAll.sh <time><unit>
		Ex:
			./mineAll.sh 4h 	(checks rates every 4 hours)
			./mineAll.sh 90m	(checks rates every 90 minutes)

mineAll.sh
	By default, checks exchange rates every hour to determine which is best to mine


alternatively, you can call any of these four from any directory to either mine Ethereum, Ethereum Classic, Monero, ZCash, or cycle through each based on exchange rates:

	mineETH
	mineETC
	mineXMR
	mineZEC
	mineCrypto


	
