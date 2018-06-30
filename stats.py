import pandas as pd

#change file for year
cleanOdds = pd.read_csv("cleanOdds1112.csv")
#print cleanOdds

def runCloseSmallSpd(maxSpd):
	#number of games where betting on -3, -2, -1 line was profitable (close)
	pnlSmallSpd = 0
	cntSmallSpd = 0
	for i in range(cleanOdds.shape[0]):
		if cleanOdds["CloseVHSpd"][i] <= maxSpd and cleanOdds["CloseVHSpd"][i] > 0:
			cntSmallSpd = cntSmallSpd + 1
			#print i
			if cleanOdds["VFinal"][i] - cleanOdds["HFinal"][i] > cleanOdds["CloseVHSpd"][i]:
				pnlSmallSpd = pnlSmallSpd + .95
				#print pnlSmallSpd
			if cleanOdds["VFinal"][i] - cleanOdds["HFinal"][i] < cleanOdds["CloseVHSpd"][i]:
				pnlSmallSpd = pnlSmallSpd - 1
				#print pnlSmallSpd
		if cleanOdds["CloseVHSpd"][i] >= -maxSpd and cleanOdds["CloseVHSpd"][i] < 0:
			cntSmallSpd = cntSmallSpd + 1
			#print i
			if cleanOdds["HFinal"][i] - cleanOdds["VFinal"][i] > -cleanOdds["CloseVHSpd"][i]:
				pnlSmallSpd = pnlSmallSpd + .95
				#print pnlSmallSpd
			if cleanOdds["HFinal"][i] - cleanOdds["VFinal"][i] < -cleanOdds["CloseVHSpd"][i]:
				pnlSmallSpd = pnlSmallSpd - 1
				#print pnlSmallSpd

	print "close", str(maxSpd), str(pnlSmallSpd), str(cntSmallSpd), str(pnlSmallSpd/float(cntSmallSpd))

def runOpenSmallSpd(maxSpd):
	#number of games where betting on -3, -2, -1 line was profitable (open)
	pnlSmallSpd = 0
	cntSmallSpd = 0
	for i in range(cleanOdds.shape[0]):
		if cleanOdds["OpenVHSpd"][i] <= maxSpd and cleanOdds["OpenVHSpd"][i] > 0:
			cntSmallSpd = cntSmallSpd + 1
			#print i
			if cleanOdds["VFinal"][i] - cleanOdds["HFinal"][i] > cleanOdds["OpenVHSpd"][i]:
				pnlSmallSpd = pnlSmallSpd + .95
				#print pnlSmallSpd
			if cleanOdds["VFinal"][i] - cleanOdds["HFinal"][i] < cleanOdds["OpenVHSpd"][i]:
				pnlSmallSpd = pnlSmallSpd - 1
				#print pnlSmallSpd
		if cleanOdds["OpenVHSpd"][i] >= -maxSpd and cleanOdds["OpenVHSpd"][i] < 0:
			cntSmallSpd = cntSmallSpd + 1
			#print i
			if cleanOdds["HFinal"][i] - cleanOdds["VFinal"][i] > -cleanOdds["OpenVHSpd"][i]:
				pnlSmallSpd = pnlSmallSpd + .95
				#print pnlSmallSpd
			if cleanOdds["HFinal"][i] - cleanOdds["VFinal"][i] < -cleanOdds["OpenVHSpd"][i]:
				pnlSmallSpd = pnlSmallSpd - 1
				#print pnlSmallSpd

	print "open", str(maxSpd), str(pnlSmallSpd), str(cntSmallSpd), str(pnlSmallSpd/float(cntSmallSpd))

# open vs close spread bets
print "open/close", "max spread", "pnl", "num games", "avg pnl"
for spd in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]:
	runOpenSmallSpd(spd)
	runCloseSmallSpd(spd)

	
