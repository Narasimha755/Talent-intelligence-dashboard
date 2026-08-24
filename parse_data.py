import json
import re

raw_data = """1	Chandini K Jain	CDM	Clinical Programmer	14th July		Rejected		Rejected				CDM	
2	Himabindu Gunikuntla	CDM	External Data Manager	14th July	Completed	Offer shortlisted	INR 9,80,000	Offered	1250000	01-09-2026	YTO	CDM	
3	Trayambica Acharya	CDM	Data Reviewer	15th July		Rejected		Rejected				CDM	
4	Kavya Shree R	CDM	Clinical Programmer	14th July	Completed	Offer Shortlisted	INR 7,50,000	Offered	1320000	01-09-2026	YTO	CDM	
5	Sai kumar mahidar	CDM	Data Reviewer	16th July	Completed	Offer Shortlisted	INR 6,50,000	Offered	770000	01-09-2026	YTO	CDM	
6	Karan Marathe	CDM	Data Reviewer	14th July	Completed	Offer Shortlisted	INR 8,00,000	Offered	1050000	01-09-2026	YTO	CDM	
7	Rohini Singamaneni	CDM	UAT Tester	15th July		Rejected		Rejected				CDM	
8	K Sangeeta	CDM	UAT Tester	14th July		Offer Shortlisted	INR 5,30,000	Offered	770000	01-09-2026	YTO	CDM	
9	Hemavantha patil	CDM	UAT Tester	16th July		Rejected		Rejected				CDM	
10	Shivani Attri	CDM	UAT Tester	16th July	Completed	Offer Shortlisted	INR 11,50,000	Offered	1250000	01-09-2026	YTO	CDM	
11	Bharath kumar	CDM	Lab Data Manager	16th July	Completed	Offer Shortlisted	INR 9,00,000	Offered	1320000	01-09-2026	YTO	CDM	
12	Sudipta Chakraborty	CDM	Lab Data Manager	15th July	Completed	Offer Shortlisted	INR 16,90,000	Offered	1850000	03-08-2026	Onboarded	CDM	
13	Madan kumar	CDM	Vendor Data Manager	15TH JULY		Rejected		Rejected				CDM	
14	Pavithra	CDM	Vendor Data Manager	20th July	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
15	Kiranmai	CDM	Data Reviewer	20th July	Completed	Offer Shortlisted	850000	Offered	1000000	01-09-2026		CDM	
16	Omkar	CDM	Lab Data Manager	20th July		Rejected		Rejected				CDM	
17	shiwangi	CDM	Lab Data Manager	20th July		Rejected		Rejected				CDM	
18	Ritu Jois	CDM	Vendor Data Manager	21st July	Completed	Offer Shortlisted	INR 8,30,000	Offered	924000	01-09-2026	YTO	CDM	
19	Abhishek Suresh Vishwasrao	CDM	Lab Data Manager	19th July		Int No Show						CDM	
20	Nidhi Nayan	CDM	UAT Tester	 				rejected				CDM	
21	Sk samdhani	CDM	External Data Manager	 				rejected				CDM	
22	Lavanya Guntur	CDM	External Data Manager	 				rejected				CDM	
23	Rajeswari	CDM	Clinical Programmer	 				rejected				CDM	
24	Kavitha Perumal	CDM	Data Reviewer	22nd July	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
25	Anvith Ullal	CDM	Lab Data Manager	22nd July	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
26	Archana kothireddy	CDM	UAT Tester	22nd July	Completed	Candidate Drop		rejected				CDM	
27	Sridevi Huli	CDM	UAT Tester	22nd July	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
28	Dr. Yagni Patel	CDM	Data Reviewer	23rd July	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
29	Vrushabh Kondalkar	CDM	Data Reviewer	23rd July	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
30	Sompalli Padmavathi	CDM	Data Reviewer	23rd July	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
31	Dr. Aniket Somnath Deore	CDM	Medical Coder	24TH JULY	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
32	Dr. Jamuna Konapalli	CDM	Medical Coder	23rd July	Completed	Offer Shortlisted		Offer Shortlisted				CDM	
33	Jitendra Chauhan	CDM	RAVE Programmer	27th July	Completed	Offer shortlisted		Offer Shortlisted				CDM	
34	Meghana	CDM	RAVE Programmer	28th July	Completed	Rejected		Rejected				CDM	
35	Premsai	CDM	RAVE Programmer	27th July		Rejected		Rejected				CDM	
36	Ankit Goyal	CDM	RAVE Programmer	24th July		Drop		Candidate No Show				CDM	
37	Sirisha GA	CDM	RAVE Programmer	28th July	Completed	Offer shortlisted		Offer Shortlisted				CDM	
38	Ranjeeta Sinha	CDM	RAVE Programmer	30th March 	Completed	Offer shortlisted	INR 10,00,000	Offered	1250000	03-08-2026	Onboarded	CDM	
39	Sita Ratnam Nunna	CDM	RAVE Programmer	30th March 	Completed	Rejected		Rejected				CDM	
40	Shubhangi Kale	CDM	RAVE Programmer	2nd April 	Completed	Offer shortlisted	INR 21,00,000	Offered	2280000	03-08-2026	Onboarded	CDM	
41	Arpit Chitransh	CDM	RAVE Programmer	30th March 	Completed	Offer Shortlisted		Candidate No Show				CDM	
42	Sathish Kumar H	CDM	RAVE Programmer	30th March 	Completed	Rejected		Rejected				CDM	
43	Dr. Kumar Mahesh	CDM	RAVE Programmer	2nd April 	Completed	Offer Shortlisted	INR 31,00,000	Offered	2700000	03-08-2026	Onboarded	CDM	
44	Saurav Sinha	CDM	RAVE Programmer	9th April 		Rejected		Rejected				CDM	
45	Katam Veera Nagendra	CDM	RAVE Programmer	9th April 		Rejected		Rejected				CDM	
46	Agalya Rajendran	CDM	RAVE Programmer	9th April 		Rejected		Rejected				CDM	
47	Chakali Gowtham Kumar	CDM	RAVE Programmer	31st March 		Rejected		Rejected				CDM	
48	Ansar Shaik	CDM	RAVE Programmer	 		 		 				CDM	
49	Satish Halappanavar	CDM	RAVE Programmer	 		 		 				CDM	
50	Anusha B Bhaskar	CDM	RAVE Programmer	 		 		 				CDM	
51	Vinay Kumar	CDM	RAVE Programmer	 		 		 				CDM	
52	Akshay Sanjay Karne	CDM	RAVE Programmer	 		 		 				CDM	
53	Manikannan Kannusamy	CDM	RAVE Programmer	 		 		 				CDM	
54	Vasuki Natarajan	CDM	RAVE Programmer	 		 		 				CDM	
55	Saiki Volvoikar	CDM	RAVE Programmer	 		 		 				CDM	
56	Rajashekar Hachadad	CDM	RAVE Programmer	 		 		 				CDM	
57	Rohit Bhandarakavate 	CDM	RAVE Programmer	 		 		 				CDM	
59	Avinash Belure	CDM	UAT Tester			 		 				CDM	
60	Parmeshwar Madke,	CDM	Data Reviewer			 	 	 				CDM	
61	Usha	CDM	Data Reviewer									CDM	
62	Gayatri Gireesh,	CDM	Data Reviewer									CDM	
63	Chaitail Khandelwal	CDM	Data Reviewer									CDM	
64	Dr Aayesha 	CDM	UAT Tester									CDM	
65	Minal Mangesh Jadhav	CDM	Data Reviewer									CDM	
66	Pravin	CDM	Data Reviewer									CDM	
67	Abhilash Varma	CDM	Rave Programmer									RAVE Programmer	
68	Siddhesh Chalke	CDM	Rave Programmer									RAVE Programmer	
69	Ansari Aishabanu,	CDM	Vendor Data Manager									CDM	
70	Aakansha Murekar,	CDM	Lab Data Manager									CDM	
71	HARSHADA KHANDGE	CDM	Lab Data Manager									CDM	
72	Shahin Jawle,	CDM	Data Reviewer									CDM	
73	Nikita Awate,	CDM	Data Reviewer									CDM	
74	Avinash Urhekar	CDM	Lab Data Manager									CDM	
75	Vijay Halde	CDM	Vendor Data Manager									CDM	
76	Greeshma Jadhav,	CDM	Vendor Data Manager									CDM	
77	Jenish Evana Nvss	CDM	Data Reviewer									CDM	
78	Medara Akhil Babu	CDM	Data Reviewer									CDM	
79	Shravani Somayajula	CDM	UAT Tester									CDM	
80	Lavanya Krishna	CDM	Vendor Data Manager									CDM	
81	Lavanya Gunda	CDM	Vendor Data Manager									CDM	
82	Vijitha Kumar	CDM	UAT Tester									CDM	
83	Devyani Supe	CDM	UAT Tester									CDM	
84	Anila Balan B	CDM	UAT Tester									CDM	
85	Diksha Khandale	CDM	Vendor Data Manager									CDM	
86	Prajesh Patil	CDM	Lab Data Manager									CDM	
87	Naga Vamsi,	CDM	Lab Data Manager									CDM	
88	Arunachaleswari Panneerselvam 	CDM	Lab Data Manager									CDM	
89	Alka Devvanshi,	CDM	Data Reviewer									CDM	
90	Prajakta Kashalikar,	CDM	Data Reviewer									CDM	
91	M Rangaswamy,	CDM	Lab Data Manager									CDM	
92	Sauradeep Mitra,	CDM	Lab Data Manager									CDM	
93	Jay Bhalerao 	CDM	Data Reviewer									CDM	
94	Nupur Shimpi,	CDM	UAT Tester									CDM	
95	SHWETHA H	CDM	UAT Tester									CDM	
96	Heena Kausar	CDM	UAT Tester									CDM	
97	Jigyansha Sandha	CDM	Vendor Data Manager									CDM	
98	Meher Taj	CDM	Data Reviewer									CDM	
99	Swetha Somalaraju	CDM	UAT Tester									CDM	
100	Yashwanth D	CDM	External Data Manager									CDM	
101	Pranjali Patil	CDM	External Data Manager									CDM	
102	Rishil Shah,	CDM	External Data Manager									CDM	
103	Shweta Shinde	CDM	External Data Manager									CDM	
104	Sushmita Malik	CDM	Vendor Data Manager									CDM	
105	Megha Shasrei,	CDM	External Data Manager									CDM	
106	Nikesh kumar 	CDM	UAT Tester									CDM	
107	Shraddha Mandale	CDM	UAT Tester									CDM	
108	Harini D	CDM	Lab Data Manager									CDM	
109	Sadaf Faizan	CDM	External Data Manager									CDM	
110	karthik jain	CDM	Lab Data Manager									CDM	
111	Hemanth jadhav	CDM	Data Reviewer									CDM	
112	Aditya Grada	CDM	Vendor Data Manager									CDM	
113	Harish 	CDM	Vendor Data Manager									CDM	
114	Yadavalli Santhosh Krishna Chaitanya, 	CDM	External Data Manager									CDM	
115	Rashimi K J	CDM	External Data Manager	07-08-2026		Waiting for feedback		Waiting for feedback				CDM	
116	Naresh Kumar	CDM	Report Programmer	04-08-2026		Waiting for feedback		Waiting for feedback				Report Programmer	
117	Shai Lakshmi	CDM	Report Programmer					rejected				Report Programmer	
118	Himanshu Kumar Singh V	CDM	Report Programmer	04-08-2026	Completed	Offer Shortlisted		Offer Shortlisted				Report Programmer	
119	Shayeestha Sheik	CDM	Report Programmer	12-08-2026		Scheduled		Waiting for feedback				Report Programmer	
120	Sandeep Gonela	CDM	Report Programmer	11-08-2026	 	Waiting for feedback		Waiting for feedback				Report Programmer	
121	Pranaya Pandharinath	CDM	Report Programmer	11-08-2026	 	Waiting for feedback		Waiting for feedback				Report Programmer	
122	Nourin  Fakruddin Mullannava	CDM	Report Programmer	11-08-2026	 	Waiting for feedback		Waiting for feedback				Report Programmer	
123	Ameer Basha Valluri	CDM	Report Programmer	07-08-2026								Report Programmer	"""

lines = raw_data.strip().split('\n')
parsed = []
for line in lines:
    parts = line.split('\t')
    if len(parts) >= 14:
        sno = parts[0].strip()
        name = parts[1].strip().rstrip(',')
        function = parts[2].strip()
        role = parts[3].strip()
        int_date = parts[4].strip()
        int2 = parts[5].strip()
        client_fb = parts[6].strip()
        present_ctc = parts[7].strip()
        status = parts[8].strip()
        offered_ctc = parts[9].strip()
        doj = parts[10].strip()
        onboard = parts[11].strip()
        skill_group = parts[12].strip()
        role_selected = parts[13].strip() if len(parts) > 13 else ""
        
        parsed.append({
            "sno": int(sno) if sno.isdigit() else len(parsed)+1,
            "name": name,
            "function": function,
            "role": role,
            "interviewDate": int_date,
            "interview2": int2,
            "clientFeedback": client_fb,
            "presentCtcRaw": present_ctc,
            "status": status,
            "offeredCtcRaw": offered_ctc,
            "doj": doj,
            "onboard": onboard,
            "skillGroup": skill_group,
            "roleSelected": role_selected
        })

print(f"Parsed {len(parsed)} records.")
with open('C:\\Users\\lucky\\.gemini\\antigravity\\scratch\\cdm_recruitment_dashboard\\data.json', 'w') as f:
    json.dump(parsed, f, indent=2)
