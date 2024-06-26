import os
import sys
import subprocess

ROOT = 'b1.0'
VERSIONS= [
[
ROOT,
'a1.2.6',
'a1.2.5',
'a1.2.4_01',
'a1.2.3_05','a1.2.3_04','a1.2.3_02','a1.2.3_01-0958','a1.2.3',
'a1.2.2-1938','a1.2.2-1624',
'a1.2.1_01',
'a1.2.0_02','a1.2.0_01','a1.2.0',
'a1.1.2_01','a1.1.2',
'a1.1.1',
'a1.1.0-131933',
'a1.0.17_04','a1.0.17_03','a1.0.17_02',
'a1.0.16_02','a1.0.16_01','a1.0.16',
'a1.0.15',
'a1.0.14-1659',
'a1.0.13_01-1444','a1.0.13',
'a1.0.12',
'a1.0.11',
'a1.0.10',
'a1.0.9',
'a1.0.8_01',
'a1.0.7',
'a1.0.6_03','a1.0.6_01','a1.0.6',
'a1.0.5_01','a1.0.5-2149',
'a1.0.4',
'a1.0.3',
'a1.0.2_02','a1.0.2_01',
'a1.0.1_01'
],
[
'a1.0.1_01',
'inf-20100630-1835',
'inf-20100630-1340',
'inf-20100629',
'inf-20100627',
'inf-20100625-1917',
'inf-20100625-0922',
'inf-20100624',
'inf-20100618',
'inf-20100617-1531',
'inf-20100617-1205',
'inf-20100616',
'inf-20100615',
'inf-20100611',
'inf-20100608',
'inf-20100607',
'inf-20100420',
'inf-20100415',
'inf-20100414',
'inf-20100413',
'inf-20100330-1611',
'inf-20100327',
'inf-20100325-1640',
'inf-20100321-1857',
'inf-20100320',
'inf-20100316',
'inf-20100313',
'inf-20100227-1433'
],
[
'inf-20100227-1433',
'in-20100223',
'in-20100219',
'in-20100218',
'in-20100214',
'in-20100213',
'in-20100212-1622',
'in-20100212-1210',
'in-20100207-1703',
'in-20100207-1101',
'in-20100206-2103',
'in-20100202-2330',
'in-20100201-2227',
'in-20100201-0025',
'in-20100131-2244',
'in-20100130',
'in-20100129-1452',
'in-20100128-2304',
'in-20100125',
'in-20100124-2310',
'in-20100110',
'in-20100105',
'in-20091231-2257',
'in-20091223-1459'
],
[
'in-20091223-1459',
'c0.30-c-renew',
'c0.30-c',
'c0.30-s',
'c0.29_02',
'c0.29_01',
'c0.28_01',
'c0.27_st',
'c0.25_05_st',
'c0.24_st_03',
'c0.0.23a_01',
'c0.0.22a_05',
'c0.0.21a',
'c0.0.20a_01',
'c0.0.19a_06-0137',
'c0.0.18a_02',
'c0.0.17a',
'c0.0.16a_02',
'c0.0.14a_08',
'c0.0.13a_03-launcher',
'c0.0.13a-launcher',
'c0.0.12a_03',
'c0.0.11a-launcher'
],
[
'c0.0.11a-launcher',
'rd-161348-launcher',
'rd-160052-launcher',
'rd-132328-launcher',
'rd-132211-launcher'
],
[
ROOT,
'server-a0.2.8',
'server-a0.2.7',
'server-a0.2.6_02','server-a0.2.6_01','server-a0.2.6',
'server-a0.2.5_02','server-a0.2.5_01','server-a0.2.5-1004',
'server-a0.2.4',
'server-a0.2.3',
'server-a0.2.2_01','server-a0.2.2',
'server-a0.2.1',
'server-a0.2.0_01','server-a0.2.0',
'server-a0.1.4',
'server-a0.1.3',
'server-a0.1.2_01',
'server-a0.1.0'
],
[
ROOT,
'b1.0_01',
'b1.0.2'
],
[
'b1.0.2:b1.0_01',
'b1.1-1245',
'b1.1-1255',
'b1.1-1255:b1.1-1245',
'b1.1_01',
'b1.1_02'
],
[
'b1.1_02',
'b1.2',
'b1.2_01',
'b1.2_02'
],
[
'b1.2_02',
'b1.3-1750',
'b1.3_01'
],
[
'b1.2_01',
'b1.3-1731'
],
[
'b1.2_02:b1.2_01',
'b1.4-1507',
'b1.4-1634',
'b1.4-1634:b1.4-1507',
'b1.4_01'
],
[
'b1.4_01',
'b1.5',
'b1.5_01',
'b1.5_02'
],
[
'b1.5_02',
'b1.6-pre-trailer',
'b1.6-pre-trailer:b1.5_01',
'b1.6-tb3',
'b1.6',
'b1.6.1',
'b1.6.2',
'b1.6.3',
'b1.6.4',
'b1.6.5',
'b1.6.6'
],
[
'b1.6.6',
'b1.7',
'b1.7_01',
'b1.7.2',
'b1.7.3'
],
[
'b1.7.3',
'b1.8-pre1-201109081459',
'b1.8-pre1-201109081459:b1.7.3',
'b1.8-pre1-201109091357',
'b1.8-pre2',
'b1.8',
'b1.8.1'
],
[
'b1.8.1',
'b1.9-pre1',
'b1.9-pre2',
'b1.9-pre3-201110061350',
'b1.9-pre3-201110061402',
'b1.9-pre3-201110061402:b1.9-pre3-201110061350',
'b1.9-pre4-201110131434',
'b1.9-pre4-201110131440',
'b1.9-pre4-201110131440:b1.9-pre4-201110131434',
'b1.9-pre5',
'b1.9-pre6'
],
[
'b1.9-pre6',
'1.0.0-rc1',
'1.0.0-rc1:b1.9-pre6',
'1.0.0-rc2-3',
'1.0.0',
'1.0.1'
],
[
'1.0.1:1.0.0',
'11w47a',
'11w48a',
'11w49a',
'11w50a',
'12w01a',
'1.1'
],
[
'1.1',
'12w03a',
'12w04a',
'12w05a-1442','12w05b',
'12w06a',
'12w07a','12w07b',
'12w08a',
'1.2',
'1.2.1',
'1.2.2',
'1.2.3',
'1.2.4',
'1.2.5',
],
[
'1.2.5',
'12w15a',
'12w16a',
'12w17a',
'12w18a',
'12w19a',
'12w21a','12w21b',
'12w22a',
'12w23a','12w23b',
'12w24a',
'12w25a',
'12w26a',
'12w27a',
'12w30a','12w30b','12w30c','12w30d','12w30e',
'1.3-pre-07261249',
'1.3.1',
'1.3.2'
],
[
'1.3.1',
'12w32a',
'12w34a','12w34b',
'12w36a',
'12w37a',
'12w38a','12w38b',
'12w39a','12w39b',
'12w40a','12w40b',
'12w41a','12w41b',
'12w42a','12w42b',
'1.4-pre','1.4.1-pre-10231538',
'1.4.2',
'1.4.3-pre',
'1.4.4',
'1.4.5',
'12w49a',
'12w50a','12w50b',
'1.4.6',
'1.4.7'
],
[
'1.4.7',
'13w01a','13w01b',
'13w02a','13w02b',
'13w03a-1647',
'13w04a',
'13w05a-1538','13w05b',
'13w06a-1636',
'13w07a',
'13w09a','13w09b','13w09c',
'13w10a','13w10b',
'1.5',
'13w11a',
'1.5.1',
'1.5.2',
],
[
'1.5.1',
'13w16a-04192037','13w16b-04232151',
'13w17a',
'13w18a','13w18b','13w18c',
'13w19a',
'13w21a','13w21b',
'13w22a',
'13w23a','13w23b-06080101',
'13w24a','13w24b',
'13w25a','13w25b','13w25c',
'13w26a',
'1.6-pre-06251516',
'1.6.1',
'1.6.2-091847',
'1.6.3-pre-171231',
'1.6.4'
],
[
'1.6.2-091847',
'13w36a-09051446','13w36b-09061310',
'13w37a','13w37b',
'13w38a','13w38b','13w38c',
'13w39a','13w39b',
'13w41a','13w41b-1523',
'13w42a','13w42b',
'13w43a',
'1.7-pre','1.7.1-pre',
'1.7.2',
'13w47a','13w47b','13w47c','13w47d','13w47e',
'13w48a','13w48b',
'13w49a',
'1.7.3-pre',
'1.7.4',
'1.7.5',
'1.7.6-pre1','1.7.6-pre2',
'1.7.6',
'1.7.7-101331',
'1.7.8',
'1.7.9',
'1.7.10-pre1','1.7.10-pre2','1.7.10-pre3','1.7.10-pre4',
'1.7.10',
],
[
'1.7.4',
'14w02a','14w02b','14w02c',
'14w03a','14w03b',
'14w04b-1554',
'14w05a','14w05b',
'14w06a','14w06b',
'14w07a',
'14w08a',
'14w10a','14w10b','14w10c',
'14w11a','14w11b',
'14w17a',
'14w18a','14w18b',
'14w19a',
'14w20a','14w20b',
'14w21a','14w21b',
'14w25a','14w25b',
'14w26a','14w26b','14w26c',
'14w27a','14w27b-07021646',
'14w28a','14w28b',
'14w29a','14w29b',
'14w30a','14w30b','14w30c',
'14w31a',
'14w32a','14w32b','14w32c','14w32d',
'14w33a','14w33b','14w33c',
'14w34a','14w34b','14w34c-08191549','14w34d',
'1.8-pre1','1.8-pre2','1.8-pre3',
'1.8',
'1.8.1-pre1','1.8.1-pre2','1.8.1-pre3','1.8.1-pre4','1.8.1-pre5',
'1.8.1',
'1.8.2-pre1','1.8.2-pre2','1.8.2-pre3','1.8.2-pre4','1.8.2-pre5','1.8.2-pre6','1.8.2-pre7',
'1.8.2',
'1.8.3',
'1.8.4',
'1.8.5',
'1.8.6',
'1.8.7',
'1.8.8',
'1.8.9'
],
[
'1.8.8',
'15w31a','15w31b','15w31c',
'15w32a','15w32b','15w32c',
'15w33a','15w33b','15w33c',
'15w34a','15w34b','15w34c','15w34d',
'15w35a','15w35b','15w35c','15w35d','15w35e',
'15w36a','15w36b','15w36c','15w36d',
'15w37a',
'15w38a','15w38b',
'15w39a','15w39b','15w39c',
'15w40a','15w40b',
'15w41a','15w41b',
'15w42a',
'15w43a','15w43b','15w43c',
'15w44a','15w44b',
'15w45a',
'15w46a',
'15w47a','15w47b','15w47c',
'15w49a','15w49b',
'15w50a',
'15w51a','15w51b',
'16w02a',
'16w03a',
'16w04a',
'16w05a','16w05b',
'16w06a',
'16w07a','16w07b',
'1.9-pre1','1.9-pre2','1.9-pre3','1.9-pre4',
'1.9',
'1.9.1-pre1','1.9.1-pre2','1.9.1-pre3',
'1.9.1',
'1.9.2',
'16w14a',
'16w15a','16w15b',
'1.9.3-pre1','1.9.3-pre2','1.9.3-pre3',
'1.9.3',
'1.9.4'
],
[
'1.9.4',
'16w20a',
'16w21a','16w21b',
'1.10-pre1','1.10-pre2',
'1.10',
'1.10.1',
'1.10.2'
],
[
'1.10.2',
'16w32a','16w32b',
'16w33a',
'16w35a',
'16w36a',
'16w38a',
'16w39a','16w39b','16w39c',
'16w40a',
'16w41a',
'16w42a',
'16w43a',
'16w44a',
'1.11-pre1',
'1.11',
'16w50a-1438',
'1.11.1',
'1.11.2'
],
[
'1.11.2',
'17w06a',
'17w13a','17w13b',
'17w14a',
'17w15a',
'17w16a','17w16b',
'17w17a','17w17b',
'17w18a','17w18b',
'1.12-pre1','1.12-pre2','1.12-pre3-1409','1.12-pre4','1.12-pre5','1.12-pre6','1.12-pre7',
'1.12',
'17w31a',
'1.12.1-pre1',
'1.12.1',
'1.12.2-pre1','1.12.2-pre2',
'1.12.2'
],
[
'1.12.2',
'17w43a','17w43b',
'17w45a','17w45b',
'17w46a',
'17w47a','17w47b',
'17w48a',
'17w49a','17w49b',
'17w50a',
'18w01a',
'18w02a',
'18w03a','18w03b',
'18w05a',
'18w06a',
'18w07a','18w07b','18w07c',
'18w08a','18w08b',
'18w09a',
'18w10a','18w10b','18w10c','18w10d',
'18w11a',
'18w14a','18w14b',
'18w15a',
'18w16a',
'18w19a','18w19b',
'18w20a','18w20b','18w20c',
'18w21a','18w21b',
'18w22a','18w22b','18w22c',
'1.13-pre1','1.13-pre2','1.13-pre3','1.13-pre4','1.13-pre5','1.13-pre6','1.13-pre7','1.13-pre8','1.13-pre9','1.13-pre10',
'1.13',
'18w30a','18w30b',
'18w31a',
'18w32a',
'18w33a',
'1.13.1-pre1','1.13.1-pre2',
'1.13.1',
'1.13.2-pre1','1.13.2-pre2',
'1.13.2'
],
[
'1.13.2',
'18w43a','18w43b','18w43c',
'18w44a',
'18w45a',
'18w46a',
'18w47a','18w47b',
'18w48a','18w48b',
'18w49a',
'18w50a',
'19w02a',
'19w03a','19w03b','19w03c',
'19w04a','19w04b',
'19w05a',
'19w06a',
'19w07a',
'19w08a','19w08b',
'19w09a',
'19w11a','19w11b',
'19w12a','19w12b',
'19w13a','19w13b-1653',
'19w14a','19w14b',
'1.14-pre1','1.14-pre2','1.14-pre3','1.14-pre4','1.14-pre5',
'1.14',
'1.14.1-pre1','1.14.1-pre2',
'1.14.1',
'1.14.2-pre1','1.14.2-pre2','1.14.2-pre3','1.14.2-pre4-270720',
'1.14.2',
'1.14.3-pre1','1.14.3-pre2','1.14.3-pre3','1.14.3-pre4',
'1.14.3',
'1.14.4-pre1','1.14.4-pre2','1.14.4-pre3','1.14.4-pre4','1.14.4-pre5','1.14.4-pre6','1.14.4-pre7',
'1.14.4'
]
]

def main():
	args = sys.argv
	
	if len(args) == 0:
		raise Exception('no command given!')
	
	command = args[1]
	
	if command == 'generate':
		if len(args) == 2:
			generate(ROOT, VERSIONS)
		else:
			root = args[2]
			versions = []
			for i in range(3, len(args)):
				versions.append(args[i])
			
			generate(root, versions)
	elif command == 'extend':
		if len(args) == 4:
			frm = args[2]
			to = args[3]
			
			extend(None, frm, to)
		elif len(args) == 5:
			frm_frm = args[2]
			frm = args[3]
			to = args[4]
			
			extend(frm_frm, frm, to)
		else:
			raise Exception('too many arguments for extend command')
	else:
		raise Exception('unknown command ' + command)

def generate(root, mc_versions):
	os.environ['MC_VERSION'] = root
	subprocess.run("./gradlew resetGraph --stacktrace", shell = True, check = True)
	
	for versions in mc_versions:
		for i in range(1, len(versions)):
			frm = versions[i - 1]
			to = versions[i]
			
			if ':' not in to:
				if ':' in frm:
					parts = frm.split(':', 2)
					
					os.environ['FROM_MC_VERSION'] = parts[0]
					os.environ['FROM_FROM_MC_VERSION'] = parts[1]
				else:
					os.environ['FROM_MC_VERSION'] = frm
					os.environ.pop('FROM_FROM_MC_VERSION', None)
				
				os.environ['MC_VERSION'] = to
			
				subprocess.run("./gradlew extendGraph --stacktrace", shell = True, check = True)

def extend(frm_frm, frm, to):
	if frm_frm is not None:
		os.environ['FROM_FROM_MC_VERSION'] = frm_frm
	os.environ['FROM_MC_VERSION'] = frm
	os.environ['MC_VERSION'] = to
	
	subprocess.run("./gradlew extendGraph --stacktrace", shell = True, check = True)

if __name__ == '__main__':
	main()