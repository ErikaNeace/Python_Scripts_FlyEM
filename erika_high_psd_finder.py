'''

neacee 07/13/2016

parsing json export from export_dvid_synapses

count tbars

count psds for each tbar

print minimum psds for a tbar

print maximum psds for a tbar

'''
#--------------------------imports------------------------------
import json
from pprint import pprint
import numpy
import matplotlib.pyplot as plt
import argparse
#import sys

#-------------------------script start--------------------------


# change username


#--import file--

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="calculates number of minimum and maximum psds for dataset, generates histogram")
	parser.add_argument('--input', 
		dest='input', action='store', required=True, help='File that contains exported synapses from dvid')
	parser.add_argument('--output', 
		dest='output', action='store', required=True, help='Filename for output')

	args = parser.parse_args()

	# with open(inputfilename, 'rt') as data_file:
	with open(args.input) as data_file:
		data = json.load(data_file)
	#--print input data in command line--
	pprint(data)

	#--deal with data--
	synapsedata=data["data"]

	item = synapsedata[0]

	tbarcount = 0
	totalPartners = 0
	parray = []
	for item in synapsedata:
		tbarcount += 1
		tb = item["T-bar"]
		# print("tb len == " + str(len(tb)))
		part = item["partners"]
		if (len(part)) < 12:
				continue
		else:
			print item["T-bar"]	
			print item["partners"]	
			print("parnter len == " + str(len(part)))
		# print("\n\n\n")
		totalPartners += len(part)
		l = len(part)
		parray.append(len(part))
		

	high_tbar = 0

	# if int(len(part)) < 12:
	# 	continue
		# print item["T-bar"]
		# print item["partners"]
		# high_tbar += 1
		# print("parnter len == " + str(len(part)))
		# print high_tbar




	print("================================")
	print("min psds: " + str(min(parray)))
	print("max psds: " + str(max(parray)))
	print("t-bar count: " + str(tbarcount))
	print("total partners: " + str(totalPartners))

	max_psds = max(parray)

	#--histogram--

	plt.hist(parray, bins=max_psds)
	plt.title("PSDs per T-Bar")
	plt.xlabel("PSDs")
	plt.ylabel("Frequency")
	plt.show()

	psd_min = str(min(parray))
	psd_max = str(max(parray))


	#--data for json export--
	# imported_data = {
	# 	"imported data": data
	# }
	# psd_information_export = {
	# 	"description": "synapse annotations psds", "total tbars": " " + str(tbarcount),"psd minimum": psd_min,
	# 	"psd maximum": psd_max,

	# }
	psd_information_export = {}

	psd_information_export["username"] = "cx_production"
	psd_information_export["description"] = "synapse annotations psds"
	psd_information_export["total tbars"] = " " + str(tbarcount)
	psd_information_export["psd minimim"] = psd_min
	psd_information_export["psd maximum"] = psd_max
	psd_information_export["synapse data"] = synapsedata




	#--open file for writing--
	with open(args.output, 'w') as f:
		json.dump(psd_information_export, f, indent=2) 

