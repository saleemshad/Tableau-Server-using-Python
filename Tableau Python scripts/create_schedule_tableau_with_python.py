import tableauserverclient as TSC
from datetime import time
''' Successfully installed certifi-2022.5.18.1 charset-normalizer-2.0.12 idna-3.3 requests-2.27.1
 tableauserverclient-0.18.0 urllib3-1.26.9'''

tableau_auth = TSC.TableauAuth('saleems', 'Iphone17s', 'CDKInternal')
server = TSC.Server('https://tableausandbox.cdk.com')
'''
with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])

with server.auth.sign_in(tableau_auth):
  all_workbooks_items, pagination_item = server.workbooks.get()
  # print names of first 100 workbooks
  a= [workbook.name for workbook in all_workbooks_items]
  print(a)

 sign in, etc.
 Create an interval to run every 2 hours between 2:30AM and 11:00PM
'''
with server.auth.sign_in(tableau_auth):
     hourly_interval = TSC.HourlyInterval(start_time=time(2, 30), end_time=time(23, 0), interval_value=2)
     hourly_schedule = TSC.ScheduleItem("Hourly-Schedule2_created_with_python1", 50, TSC.ScheduleItem.Type.Extract,
                                        TSC.ScheduleItem.ExecutionOrder.Parallel, hourly_interval)
     hourly_schedule = server.schedules.create(hourly_schedule)
print("schdule created successfully")
''' Create schedule item '''

''' # Create schedule'''

