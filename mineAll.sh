x=1

time=1h

if [[ -n "$1" ]]; then
	time=$1
	echo $time
fi

while [ "$x" -eq 1 ] 
do	

	~/DingoMiner/getRates.py

	returnCode=$?

	if [ $returnCode == 1 ]
	then
		~/DingoMiner/Ethereum/mineETH.sh &
		procID=%%	
		sleep $time
		kill $procID

	elif [ $returnCode == 2 ]
	then	
		~/DingoMiner/Ethereum/mineETC.sh &
		procID=%%
		sleep $time
		kill $procID

	elif [ $returnCode == 3 ]
	then
		~/DingoMiner/Monero/mineXMR.sh &
		procID=%%
		sleep $time
		kill $procID		

	else
		~/DingoMiner/ZCash/mineZEC.sh &
		procID=%%
		sleep $time 
		kill $procID		
	fi
done
