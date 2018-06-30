import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import numpy as np

cleanOddsD = {}
#change file for year
cleanOddsD["1718"] = pd.read_csv("cleanOdds1718.csv")
cleanOddsD["1617"] = pd.read_csv("cleanOdds1617.csv")
cleanOddsD["1516"] = pd.read_csv("cleanOdds1516.csv")
cleanOddsD["1415"] = pd.read_csv("cleanOdds1415.csv")
cleanOddsD["1314"] = pd.read_csv("cleanOdds1314.csv")
cleanOddsD["1213"] = pd.read_csv("cleanOdds1213.csv")
cleanOddsD["1112"] = pd.read_csv("cleanOdds1112.csv")

def runCloseSmallSpd(maxSpd, cleanOdds, year):
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
	print year
	print "close", str(maxSpd), str(pnlSmallSpd), str(cntSmallSpd), str(pnlSmallSpd/float(cntSmallSpd))

def runOpenSmallSpd(maxSpd, cleanOdds, year):
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
	print year
	print "open", str(maxSpd), str(pnlSmallSpd), str(cntSmallSpd), str(pnlSmallSpd/float(cntSmallSpd))

'''
# open vs close spread bets
print "open/close", "max spread", "pnl", "num games", "avg pnl"
for spd in [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]:
	runOpenSmallSpd(spd)
	runCloseSmallSpd(spd)
'''

def plotSpdChgVsRlzdSpd(cleanOdds, year):
	#plot change in V-H line on x-axis, actual V-H score on y-axis
	chg = []
	scoreDiff = []
	pairs = []
	counts = []
	for i in range(cleanOdds.shape[0]):
		if abs(cleanOdds["CloseVHSpd"][i] - cleanOdds["OpenVHSpd"][i]) > 5:
			print cleanOdds["Date"][i], cleanOdds["V"][i], cleanOdds["H"][i], cleanOdds["CloseVHSpd"][i] - cleanOdds["OpenVHSpd"][i]
			continue
		chg.append(cleanOdds["CloseVHSpd"][i] - cleanOdds["OpenVHSpd"][i])
		if cleanOdds["VFinal"][i] - cleanOdds["HFinal"][i] >= 10:
			scoreDiff.append(10)
			pairs.append((cleanOdds["CloseVHSpd"][i] - cleanOdds["OpenVHSpd"][i], 10))
		elif cleanOdds["VFinal"][i] - cleanOdds["HFinal"][i] <= -10:
			scoreDiff.append(-10)
			pairs.append((cleanOdds["CloseVHSpd"][i] - cleanOdds["OpenVHSpd"][i], -10))
		else:
			scoreDiff.append(cleanOdds["VFinal"][i] - cleanOdds["HFinal"][i])
			pairs.append((cleanOdds["CloseVHSpd"][i] - cleanOdds["OpenVHSpd"][i], cleanOdds["VFinal"][i] - cleanOdds["HFinal"][i]))
		
	#plt.scatter(np.array(chg), np.array(scoreDiff))
	#plt.xlabel("Change in V-H line")
	#plt.ylabel("Realized V-H score")
	#plt.title(year)
	#plt.show()
	for i in range(len(pairs)):
		counts.append(pairs.count(pairs[i]))

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(np.array(chg), np.array(scoreDiff), np.array(counts))
	ax.set_xlabel('Change in V-H line')
	ax.set_ylabel("Realized V-H score (truncated to 10)")
	ax.set_zlabel("Number of games")
	plt.show()

'''
#for d in sorted(cleanOddsD.keys()):
for d in ["1718"]:
	plotSpdChgVsRlzdSpd(cleanOddsD[d], d)
'''

def plotStratPnlOverSeason(cleanOdds, year):
	for i in range(cleanOdds.shape[0]):
		pass


	
