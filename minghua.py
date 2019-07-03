from selenium import webdriver
import time
import re

browser = webdriver.Chrome()

#创业教育
a_4262 = ((994,1216,1112),(1168,1138,1180,1174),
		(1190,1144,(1229,1230,1231,1232)),
		(972,1146,970))

#自我发展
a_4805 = (((3685,3686,3687),(3538,3539,3540),(3562,3563,3564,3565),(3636,3637,3638,3639),(3632,3633,3634,3635)),
(3738,(3648,3649),(3770,3771,3772,3773),3624,(3640,3641,3642,3643)),
(3558,3696),
(3607,(3546,3547,3548,3549),3656,3531,3743),
((3766,3767,3768,3769),(3676,3677,3678,3679),(3550,3551,3552)),
(3660,3590,3585,3710,(3620,3621,3622,3623)),
(3692,3567,(3774,3775,3776,3777),(3652,3653,3654,3655)),
(3791,3628,(3680,3681,3682,),3780,(3760,3762,3763)),
(3668,3618,3782,(3608,3609,3610,3611),3594),
((3554,3557),3779,(3542,3543,3545),(3672,3674),3569),
(3535,3537,(3792,3793),3705,3764),
(3664,(3752,3755),3730,3706,3734))

#目标与计划管理
a_4797 = ((5246,5256,5260,(5247,5248,5249,5250),(5251,5252,5253,5254)),
(5258,))

#创新思维
a_4824 = (((6165,6166,6167),6275,6221,(6069,6071,6072),6231),
((6097,6099),(6057,6058,6059,6060),(6147,6148,6149),6041,(6183,6185,6186)),
((6053,6054,6055,6056),(6157,6158),(6289,6290),(6293,6294,6295),(6191,6192,6193)),
((6091,6094),6255,(6243,6244,6245,6246),6117,(6235,6236,6237)),
(6101,(6077,6078),6199,6239),
((6125,6126),(6161,6162,6163,6164),6063,6121,6267),
((6251,6252,6254),6178,(6173,6174,6175),6107,6152),
(6130,(6045,6046,6048),6096,6230,(6203,6204,6205)),
(6284,(6279,6280,6281,6282),(6113,6114,6115,6116),6037,(6153,6154,6155)),
((6225,6226),6105,(6109,6110,6111,6112),6187,6062),
((6131,6132,6133,6134),(6217,6218,6219,6220),(6073,6074,6075)),
(6141,6135,(6081,6082,6083,6084),6086))

#国学智慧
a_4825 = (((11607,11608,11609,11610),11455,(11435,11436,11437,11438),(11663,11664,11665,11666),11667),
((11391,11392,11393,11394),(11439,11440),(11519,11520,11521,11522),(11367,11368,11369,11370),(11503,11504,11505)),
((11675,11676,11677,11678),(11407,11408,11409,11410),11351,(11631,11633),(11487,11488,11489,11490)),
((11547,11548,11549),(11415,11416,11417),(11383,11384,11385,11386),(11603,11604,11605,11606),(11427,11428,11429)),
((11495,11496,11497,11498),(11411,11412,11413),11479,(11659,11660,11661),(11643,11644,11645,11646)),
((11359,11360,11361,11362),(11555,11556),(11523,11524,11525,11526),(11535,11536)),
((11355,11356),(11335,11336,11337,11338),(11331,11332,11333,11334),(11539,11540,11541,11542),(11615,11616,11618)),
((11647,11648,11649),(11623,11624,11625),(11423,11424,11425,11426),11531,(11451,11452,11453,11454)),
((11587,11588),(11443,11444,11445),(11515,11516,11517,11518),11611,11323,),
((11371,11372),(11447,11448,11449),(11343,11344),(11651,11652,11653),(11375,11376,11377,11378)),
((11527,11528,11529,11530),11511,11567,(11431,11432,11433,11434),(11419,11420)),
((11471,11472,11473),(11591,11592,11593,11594),(11571,11572,11573,11574),(11379,11381),(11507,11509,11510)),
((11395,11396),(11475,11476,11477,11478),(11595,11596,11597),(11655,11656),(11583,11584,11585,11586)),
(11347,(11387,11388,11389),(11679,11680,11681,11682),(11575,11577,11578),(11619,11620,11621,11622)),
((11327,11329,11330),(11599,11600,11601),(11399,11400,11401),(11467,11468)))

#商务礼仪
a_4826 = ((5179,5204,(4957,4958,4959,4960),5037,(4967,4968,4970)),
((5205,5207,5208),5239,5020,(5081,5082,5083)),
((4905,4906,4907),5231,(5023,5024),5091),
(5048,5145,(5169,5171,5172),(5027,5028,5029)),
((5150,5151,5152),5125,(5221,5222,5223,5224),5141,4919))

#创业实战
a_4799 = ((6031,6029,6017),
(6025,6027,(6033,6034,6035,6036)),
(6021,6019,6023))

#恋爱与性健康
a_4807 = ((4616,4266,4408,4396,4542),
(4430,4360,4338,4394,4249),
(4538,4522,4296,4254,4386),
(4566,4419),
(4357,4624,4260,4600,4480),
(4355,4528,4306),
(4508,4286,4240,4524,4582),
(4262,4608,4234,4434,4551),
(4588,4493,4635),
(4236,4264,4552,4554,4372),
(4417,4654,4320,4584,4575),
((4330,4331,4332,4333),4622,(4334,4335,4337),4646,(4494,4495,4496)),
(4250,4426,(4534,4535,4537),4605,(4343,4344,4345)))

#团队建设
a_4819 = ((11043,11294,10771,10927,(10775,10776,10778)),
((10961,10962,10963,10964),(11273,11274),10832,10890),
(10985,(11093,11094,11095,11096),10956,11047,(10969,10971,10972)),
(11034,(10763,10765,10766),(10839,10840),(11261,11262,11263),11164),
((10859,10861,10862),11303,10819,(10903,10904,10905,10906),(10947,10948,10949)),
(10767,(10981,10982),(11249,11250,11251,11252),(11057,11058,11059,11060),(11131,11132,11133)),
((11049,11050,11051,11052),(11229,11230,11231,11232),(11319,11320,11321),(11181,11182,11183,11184)),
((10827,10828,10829,10830),(11061,11062,11063,11064),(11101,11102,11103),(11277,11278,11279,11280)),
((10965,10966,10967,10968),(11147,11148,11149,11150),(11021,11022,11023,11024),(10823,10824,10825,10826)),
((10915,10916,10917),(10957,10958,10959),(11077,11078,11080),(11257,11258),(10791,10792,10793,10794)),
((10989,10990,10991,10992),(11265,11266,11267),11194,(11241,11242,11243),(11233,11234,11235,11236)),
((10847,10848,10849),(10997,10998,10999,11000),(11029,11030,11031,11032),(11197,11198,11199,11200),(10919,10920,10921,10922)),
((10895,10896,10897,10898),(11285,11286,11287),(10871,10873),10867,(10795,10796,10797,10798)),
(11213,(10951,10952),(11139,11140,11141),(11053,11054),(10799,10800,10801)))

#word
a_4809 = ((3287,3290,3270,3354,3346),
(3338,3312,3305,3342,3267),
(3334,3280,3326,3318,3282),
(3292,3301,3341,3310,3308),
(3302,3332,3321,3268,3316),
(3276,3322,3298,3306,3294),
(3314,3350,3288,3336,3329),
(3345,3274,3278,3296,3324))

#office
a_4822 =((2407,2432),
(2509,2552,2422,2527),
(2551,2426,2500,2466),
(2404,2476,2409,2401,2490),
(2576,2546,2564,2484),
(2543,2486,2457,2460,2489),
(2481,2412,2473,2415,2475),
(2537,2497,2557,2541,2431),
(2479,2447,2439,2535,2515),
(2495,2530,2465,2538),
(2518,2548,2493,2483),
(2463,2422,2525),
(2561,2513,2505,2507,2517),
(2443,2562,2569,2455),
(2444,2559,2532,2574,2545),
(2451,2419,2529,2579,2449),
(2403,2421,2523))

#PPT
a_4811 = ((2952,3048,2908,2982,3032),
(2964,(3056,3057),(3044,3045,3046,3047),3052,2970),
(3005,3006,2896,2936,3060),
(2939,2927,2919,2969,(3024,3025,3026)),
(3028,2956,3000,3036,3072),
(3077,2929,2931))

#职业规划
a_4798 = ((10118,10141,10146,10100,10194),
(10028,10043,10057,10154,10192),
(10059,10089,10183,10071,10069),
(10189,10258,10106,10093,(10227,10228,10229,10230)),
(10162,10080,(10241,10242,10243,10244),(10203,10204,10205,10206),(10195,10196,10197,10198)),
(10112,10129,10026),
(10213,(10221,10222,10223),10064,(10137,10138,10140),10166),
((10047,10048,10049,10050),10010,10220,10076,10226),
(10016,(10039,10040,10041,10042),10005,(10231,10232,10233,10234),10252))

#Excel
a_4810 = (((2888,2889),(2742,2743,2744),(2790,2791),(2872,2873),(2634,2635)),
(2608,2860,2604,2722,2660),
(2776,2767,2700,2814,(2804,2805)),
(2762,2642,2708,2647,2746),
((2682,2683,2684),2589,(2754,2755,2756),2796,2595),
(2810,2622,2876,2652,2864),
(2809,2717,2789,2855))

#PS
a_4816 = ((3395,3494,3439,3359,3449),
(3402,3435,3417,3459,3491),
(3427,3517,3519,3513,3392),
(3467,3473,3401,3484,3433),
(3453,3377,3475,3489,3380),
(3363,3399,3451,3379,3441),
(3397,3471,3437,3496,3463),
(3356,3446,3499,3431,3444),
(3407,3469,3423,3525,3529),
(3421,3465,3457,3373,3383),
(3387,3501,3482,3385,3442),
(3375,3478,3523,3425,3461),
(3514,3415,3481,3411,3413))

def isExist(css):
	try:
		browser.find_element_by_css_selector(css)
		return True
	except:
		return False

def main ():

	#登录
	browser.get("http://wuhues.minghuaetc.com/home/login.mooc")
	time.sleep(1)
	username = input("请输入学号:")
	browser.find_element_by_id("loginName").send_keys(username.strip())
	time.sleep(0.5)
	browser.find_element_by_id("password").send_keys("123456")
	code = input("请输入验证码:")
	browser.find_element_by_id("checkCode").send_keys(code.strip())
	time.sleep(0.5)
	browser.find_element_by_id("userLogin").click()
	time.sleep(1)

	#验证验证码
	while browser.current_url == "http://wuhues.minghuaetc.com/home/login.mooc":
		if isExist(".d-button.d-state-highlight"):
			print("账号已经在别处登录，马上把TA挤下去！")
			time.sleep(0.5)
			browser.execute_script("document.querySelector(\".d-button.d-state-highlight\").click()")
			time.sleep(0.5)
			browser.execute_script("document.querySelector(\".d-close\").click()")
			browser.find_element_by_id("checkCode").send_keys(code)
			time.sleep(0.5)
			browser.find_element_by_id("userLogin").click()
			time.sleep(1)
		else:
			code = input("验证码错误请重新输入:")
			code = code.strip()
			clearcode = browser.find_element_by_id("checkCode")
			clearcode.clear()
			browser.find_element_by_id("checkCode").send_keys(code)
			time.sleep(0.5)
			browser.find_element_by_id("userLogin").click()
			time.sleep(0.5)

	print("登录成功，正在刷课中!")
	time.sleep(0.5)

	videonum = input("请输入观看的门数:")
	startnum = input("第几门开始看:")
	time.sleep(1)

	#获取所有课程url
	urls = browser.execute_script("let urls = [];document.querySelectorAll(\".view-shadow\").forEach(s => urls.push(s.getAttribute(\"href\")));return urls;")
	#观看的门数
	time.sleep(2)

	#循环看视频做题
	for i in range(int(videonum)):

		print("正在刷第%s门课"%(i+1))
		time.sleep(1)
		browser.get("http://wuhues.minghuaetc.com" + str(urls[i+int(startnum)-1]))
		time.sleep(1)
		#获取当前url id
		urlid = int(re.sub("\D","",browser.current_url))
		#获取答案元组
		aid = "a_" + str(urlid)
		time.sleep(1)
		#点击课程内容
		browser.find_element_by_css_selector("body > div.content.person-center > div.sidebar > div:nth-child(2) > div > div > ul > li:nth-child(2) > a").click()
		time.sleep(1)
		#获取url的unitid
		unitid = browser.execute_script("return document.querySelector('.lecture-text.substr.unitItem').getAttribute('unitid')")
		unitid = int(unitid)
		
		videoflag = 1
		testflag = 1
		answerflag = 1

		while True:

			browser.get("http://wuhues.minghuaetc.com/study/unit/"+str(unitid)+".mooc")
			time.sleep(1)

			if isExist(".btn-icon.doObjExam") or isExist(".link-action.enter_exam") :

				answer = eval(aid)
				videoflag = 1
				#做题
				if isExist(".btn-icon.doObjExam"):
					#点击开始测试
					browser.find_element_by_css_selector(".btn-icon.doObjExam").click()
				else:
					#继续
					browser.execute_script("document.querySelector(\".link-action.enter_exam\").click()")
				time.sleep(3)

				print("开始第%s章测试"%answerflag)
				time.sleep(2)
				#做题
				for x in range(len(answer[answerflag-1])):

					#点击题号
					aa = "document.querySelector(\"div.content.learning-center > div.main.main-note-scroll > div.main-scroll > div > div:nth-child(2) \
										 > div > div > div.tab-panels.tabPanels > div > div > div > div > div > div.practice-options \
										  > div.practice-process > div.practice-no.clearfix > a:nth-child("+ str(x+1) +")\").click()"
					time.sleep(1)
					browser.execute_script(aa)
					time.sleep(1)

					answerid = answer[answerflag-1][x]
		 
					#判断是否是多选
					if isinstance(answerid,tuple):
						for y in range(len(answerid)):
							time.sleep(1)
							browser.find_element_by_css_selector("div[option_id='"+ str(answerid[y])+"'] a").click()
							time.sleep(1)
					#单选
					else:	
						time.sleep(1)
						browser.find_element_by_css_selector("div[option_id='"+ str(answerid)+"'] a").click()
						time.sleep(1)
				answerflag = answerflag + 1

				#提交
				browser.find_element_by_id("submit_exam").click()
				time.sleep(1)

				#确认提交
				browser.find_element_by_css_selector(".d-button.d-state-highlight").click()
				time.sleep(1)

				testflag = testflag + 1
				#print("测试")
				unitid = unitid + 1

			elif isExist(".btn-public.btn-interest") or isExist(".btn-public.btn-disabled") or isExist(".error-header"):
				time.sleep(1)
				break
			elif isExist(".view-intro") or browser.current_url == "http://wuhues.minghuaetc.com/portal/myCourseIndex/1.mooc":
				unitid = unitid + 1
				time.sleep(1)
			else:
				itemId = browser.execute_script("return document.querySelector('.tab-inner').getAttribute('itemid')")

				time.sleep(1)
				print("正在观看第%s节视频"%videoflag)
				js = "jQuery.ajax({type : \"POST\",url : \"http://wuhues.minghuaetc.com/study/updateDurationVideo.mooc\",\
				dataType:\"json\",async:false,data : {itemId :"+str(itemId)+" ,isOver : 1,duration : 6000000,currentPosition : 6000000},\
				success : function(response) {console.log(\"1\");},error : function() {}});"
				time.sleep(1)
				a = browser.execute_script(js)
				#time.sleep(600)
				time.sleep(2)
				videoflag = videoflag + 1
				unitid = unitid + 1

		print("完成第%s门"%(i+1))
		time.sleep(0.5)
		i = i+1
	print(username)
	input("所有课程都已完成!")
	time.sleep(0.5)


if __name__ == '__main__':
	main()
