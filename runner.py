# coding=utf-8


#I wont write a single comment!
import os

delimiter = "~"

needed_total = 55 #Sinolo
needed_y = 39 #Upoxreotika
needed_br = 4 #Vasika Rois
needed_eu_r = 5 #upoxreotika mathimata epilogis idias rois pou eisai
needed_eu = 7 #eleu8era ma8imata epilogis tis idias rois h kapoias allis


max_gp = 2 #megista genikis paidias

def read_csv(filepath):
	global delimiter
	
	if not os.path.isfile(filepath):
		print("[-] File Not Found")
		return None
	
	f = open(filepath,"r",encoding="utf8")
	first_line = f.readline()
	
	header= first_line.replace("\n","").split(delimiter)
	
	data = {}
	for l in f:
		obj = l.replace("\n","").split(delimiter)
		data[obj[0]] = {}
		
		for i in range(len(header)):
			data[obj[0]][header[i]] = obj[i]
	return data


def get_correlated(tora,prin,perasmena_prin):
	
	perasmena = []
	failed_to_corelate = []
	perasmena_ids = []
	
	for s in perasmena_prin:
		subject = perasmena_prin[s]
		
		if int(subject["Passed"]) == 1:
			if s in prin:
				old_subject = prin[s]
				cid = old_subject["Corralated Id"]
				
				if cid.strip() != "":
					if cid in tora:
						subject["new"] = tora[cid]
						if cid not in perasmena_ids:
							perasmena_ids.append(cid)
						if subject not in perasmena:
							perasmena.append(subject)
					else:
						failed_to_corelate.append(s)
						
				else:
					failed_to_corelate.append(s)
										
				
			else:
				failed_to_corelate.append(s)
	
	return (perasmena,failed_to_corelate,perasmena_ids)
		
		
	
	
def print_perasmena(perasmena):
	s= 0
	for subject in perasmena:
		s += 1
		print(subject["new"]["Subject"])
	print("SUM: ",s)

def print_failed_to_corelate(ftc,prin):
	sm = 0
	for s in ftc:
		print(prin[s]["Subject"])
		sm += 1
	
	print("SUM: ",sm)

def print_stats(stats):
	for stat in stats:
		print(stat,stats[stat])	

def get_stats(perasmena):
	data = {}
	
	for subject in perasmena:
		for stat in subject["new"]["EM"].split(","):
			stat = stat.strip().replace("\n","")
			if stat in data:
				data[stat] += 1
			else:
				data[stat] = 1
	syms = ["Υ","ΒΡ","ΕΥ"]
	for s in syms:
		if not s in data:
			data[s] = 0
	return data

def get_needed_stats(needed,stats,perasmena):
	global needed_y
	
	data ={}
	
	data["Υ"] = len(needed["theloume_sigoura"])
	
	roes_ids = ["1","2","3"]
	
	roes_vasika = {
		"1":4,
		"2":4,
		"3":4
	}
	
	roes_epilogi = {
		"1":5,
		"2":5,
		"3":5,
	}
	
	eleutheri_epilogi = {
		"1":7,
		"2":7,
		"3":7
	}
	
	for subject in perasmena:
		print(subject["new"]["Subject"])
		for stat in subject["new"]["EM"].split(","):
			stat = stat.strip().replace("\n","")
			
			
			
			if stat == "ΒΡ":
				rid = subject["new"]["RID"].strip().replace("\n","")
				roes_vasika[rid] -= 1
				for rrid in roes_ids:
					if rrid == rid:
						continue
					eleutheri_epilogi[rrid] -=1
					
			if stat == "ΕΥ":
				rid = subject["new"]["RID"].strip().replace("\n","")
				#if rid in roes_epilogi:
				#	roes_epilogi[rid] -= 1
					
				for rrid in roes_ids:
					if rrid == rid:
						if roes_epilogi[rid] <= 0:
							eleutheri_epilogi[rrid] -=1
						else:
							roes_epilogi[rid] -= 1
						continue
							
						
					eleutheri_epilogi[rrid] -=1
					
				
	
	data["roes_vasika"] = roes_vasika
	data["roes_epilogi"] = roes_epilogi
	data["eleutheri_epilogi"] = eleutheri_epilogi
		
	return data
	
	
					
	
def get_needed(perasmena,tora,perasmena_ids):
	theloume_sigoura = []
	
	roes = {}
	
	epilogis_upoxreotika = {}
	
	genikis_pedias = []
	
	for s in tora:
		subject = tora[s]
		if s in perasmena_ids:
			continue #Perasmeno Mathima
			
		for em in subject["EM"].split(","):
			em = em.strip().replace("\n","")
			
			if em == "Υ":
				theloume_sigoura.append(s)
				
			elif em == "ΒΡ":
				rid = subject["RID"].strip()
				if rid in roes:
					roes[rid].append(s)
				else:
					roes[rid] = [s]
			elif em == "ΕΥ":
				rid = subject["RID"].strip()
				if rid.strip() == "":
					genikis_pedias.append(s)
					
				else:
					if rid in epilogis_upoxreotika:
						epilogis_upoxreotika[rid].append(s)
					else:
						epilogis_upoxreotika[rid] = [s]
			
				
				
	data = {
		"theloume_sigoura":theloume_sigoura,
		"roes":roes,
		"epilogis_upoxreotika":epilogis_upoxreotika,
		"genikis_pedias":genikis_pedias,
	
	}			
	
	return data

def main():
	tora = read_csv("mathimata.csv")
	prin = read_csv("mathimata_pada.csv")
	perasmena_prin = read_csv("perasmena.csv")
	
	
	if tora == None or prin == None or perasmena_prin == None:
		return None
	
	new_data = get_correlated(tora,prin,perasmena_prin)
	stats = get_stats(new_data[0])

	#Printing Data!
	'''
	print_perasmena(new_data[0])
	print("----------------------------------------")
	print_failed_to_corelate(new_data[1],prin)
	print("----------------------------------------")
	print_stats(stats)
	
	'''
	needed = get_needed(new_data[0],tora,new_data[2])
	needed_stats = get_needed_stats(needed,stats,new_data[0])
	
	results  = {
		"mathimata_pada":tora,
		"proigoumena_mathimata":prin,
		"perasmena_mathimata_pro_antistixisis":perasmena_prin,
		"perasmena_mathimata_meta_antistixisis":new_data[0],
		"mathimata_pou_den_antistixizontai":new_data[1],
		"perasmena_mathimata_ids":new_data[2],
		"statistika":stats,
		"mathimata_pou_xriazomaste":needed,
		"statistika_gia_oti_xiazomaste":needed_stats,
	}
	
	return results

if __name__ == "__main__":
	print("Starting")
	main()	
	
	
	





