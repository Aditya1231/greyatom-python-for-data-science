# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

data_file = path
data=np.genfromtxt(data_file,delimiter=",", skip_header=1)
census = np.concatenate((data,new_record),axis=0)
print(census)


# --------------
#Code starts here
age = census[:,0] #row and column
max_age = max(age)
print(max_age)
min_age = min(age)
print(min_age)
age_mean = age.mean()
print(age_mean)
age_std = age.std()
print(age_std)
print('Country with max age is old country with max age as ',max_age)
print('Country with min age is young country with min age as',min_age)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

l1 = [len_0,len_1,len_2,len_3,len_4]
minority_race = l1.index(min(l1))
print(minority_race)
#print(l1)

#print('Store',min(l1),'in minority race')



# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
print(senior_citizens)


working_hours_sum = float(sum(senior_citizens[:,6]))
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)



# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
print(high)
print(low)

avg_pay_high = high[:,7].mean()
print(avg_pay_high)

avg_pay_low = low[:,7].mean()
print(avg_pay_low)


