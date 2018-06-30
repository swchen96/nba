import pandas as pd
import csv

cleandata = []
cleandata.append(["Date", "V", "H", "V1", "V2", "V3", "V4", "VFinal", "H1", "H2", "H3", "H4", "HFinal", "OpenOU", "OpenVHSpd", "CloseOU", "CloseVHSpd", "VML", "HML", "SecondOU","SecondVHSpd"])

year = "1112"

rawdata = pd.read_csv('odds'+year+'.csv')
for i in range(rawdata.shape[0]/2):
	cleandata.append([])
	cleandata[-1].append(int(rawdata["Date"][2*i]))
	cleandata[-1].append(rawdata["Team"][2*i])
	cleandata[-1].append(rawdata["Team"][2*i+1])
	cleandata[-1].append(int(rawdata["1st"][2*i]))
	cleandata[-1].append(int(rawdata["2nd"][2*i]))
	cleandata[-1].append(int(rawdata["3rd"][2*i]))
	cleandata[-1].append(int(rawdata["4th"][2*i]))
	cleandata[-1].append(int(rawdata["Final"][2*i]))
	cleandata[-1].append(int(rawdata["1st"][2*i+1]))
	cleandata[-1].append(int(rawdata["2nd"][2*i+1]))
	cleandata[-1].append(int(rawdata["3rd"][2*i+1]))
	cleandata[-1].append(int(rawdata["4th"][2*i+1]))
	cleandata[-1].append(int(rawdata["Final"][2*i+1]))
	if float(rawdata["Open"][2*i]) > 60.0:
		cleandata[-1].append(float(rawdata["Open"][2*i]))
		cleandata[-1].append(-float(rawdata["Open"][2*i+1]))
	else:
		cleandata[-1].append(float(rawdata["Open"][2*i+1]))
		cleandata[-1].append(float(rawdata["Open"][2*i]))

	if float(rawdata["Close"][2*i]) > 60.0:
		cleandata[-1].append(float(rawdata["Close"][2*i]))
		cleandata[-1].append(-float(rawdata["Close"][2*i+1]))
	else:
		cleandata[-1].append(float(rawdata["Close"][2*i+1]))
		cleandata[-1].append(float(rawdata["Close"][2*i]))
	cleandata[-1].append(int(rawdata["ML"][2*i]))
	cleandata[-1].append(int(rawdata["ML"][2*i+1]))
	if float(rawdata["2H"][2*i]) > 30.0:
		cleandata[-1].append(float(rawdata["2H"][2*i]))
		cleandata[-1].append(-float(rawdata["2H"][2*i+1]))
	else:
		cleandata[-1].append(float(rawdata["2H"][2*i+1]))
		cleandata[-1].append(float(rawdata["2H"][2*i]))

with open("cleanOdds"+year+".csv", "wb") as myfile:
	wr = csv.writer(myfile)
	for row in cleandata:
		wr.writerow(row)
