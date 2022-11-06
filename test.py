# import csv
# import pprint as pp

# myDict = {'test':
#         [{'key_a': 'foo_1', 'key_b': 'bar_1'}, 
#          {'key_a': 'foo_2', 'key_b': 'bar_2'}], 
#         'test2':
#         [{'key_c': 'foo_1', 'key_d': 'bar_1'}, 
#          {'key_c': 'foo_2', 'key_d': 'bar_2'}] }

# def generateFieldnames(myDict):
#     # create unique fieldnames from a dictionary containing dictionaries
#     newDict={}
#     fieldnames=[] # DictWriter will create a .csv with these header names
    
#     for k,v in myDict.items():
        
#         # is a dictionary?
#         if (type(v) is dict):
#             for kk,vv in v.items():
#                 print('k={0}, kk={1}, vv={2}'.format(k,kk,vv))
#                 name='{0}_{1}'.format(k,kk)
#                 fieldnames.append(name)
#                 newDict[name]=vv
                
#         elif (type(v) is list):
#             for item in range(len(v)):
#                 listItem=v.pop()
#                 if (type(listItem) is dict):
#                     for kk,vv in listItem.items():
#                         name='{0}_{1}'.format(k,kk)
#                         fieldnames.append(name)
#                         newDict[name]=vv
        
#         else:
#             print('k=[{0}] , v=[{1}]'.format(k,v))
#             fieldnames.append(k)
#             newDict[k]=v
    
#     return fieldnames, newDict


# # create fieldnames from the dictionary with lists and dictionaries
# fieldnames, newDict=generateFieldnames(myDict)
# pp.pprint(fieldnames)
# print('\n')
# pp.pprint(fieldnames)
# print('\n\n')

# # write a sample .csv with fieldnames as headers
# fd = open('mytest.csv','a')
# dw = csv.DictWriter( fd, fieldnames=fieldnames)

# dw.writeheader() # write the header row

# dw.writerow( newDict )
# dw.writerow( newDict )
# dw.writerow( newDict )

# fd.close()

# importing the csv module
import csv
import json

# my data rows as dictionary objects
# mydict =[{'current progress': 0.0, 'max force': 0.2, 'average max force': 0.1}, 
# {'current progress': 0.0, 'max force': 0.2, 'average max force': 0.1}]
def add_element(dict, value):
    dict.append(value)

mydict = {}
add_element(mydict,  {'current progress' : 0})
add_element(mydict ,{'max force' : 0})
add_element(mydict, {'average max force' : 0})

# field names
fields = ['current progress', 'max force', 'average max force']
	
# name of csv file
filename = "test.csv"
print(mydict)
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames = fields)
		
	# writing headers (field names)
	writer.writeheader()
		
	# writing data rows
	writer.writerows(mydict)
