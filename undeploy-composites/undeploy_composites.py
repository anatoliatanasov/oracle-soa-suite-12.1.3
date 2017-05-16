username = 'weblogic';
password = 'welcome1';

connect(username, password, 't3://localhost:7101');

composite_apps = ['Alfi_Insured_Object_Images_Upload_Process:1.0.0', 
					'Bonus_Home_Integration_Process:2.1.1', 
					'Bonus_Home_Integration_Process:2.1.2', 
					'Bonus_Travel_Integration_Process:1.0.2', 
					'Bonus_Travel_Integration_Process:1.1.0', 
					'Bonus_Travel_Integration_Process:1.1.1', 
					'BST_Alfresco_Intermediary_Reporting_Process:1.0.1', 
					'MotorIns_Integration_Process:2.0.1', 
					'MTPL_Integration_Process:1.0.1', 
					'MTPL_Integration_Process:1.0'];

for composite_app in composite_apps:
	app_data = composite_app.split(':');
	
	sca_undeployComposite('http://localhost:7101', app_data[0], app_data[1], user=username, password=password);
