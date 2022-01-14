import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")

mathematics = df["math score"].to_list()
reading = df["reading score"].to_list()
#Mean for Mathematics and Reading
Mathematics_mean = statistics.mean(mathematics)
Reading_mean = statistics.mean(reading)
#Median for Mathematics and Reading
Mathematics_median = statistics.median(mathematics)
Reading_median = statistics.median(reading)
#Mode for Mathematics and Reading
Mathematics_mode = statistics.mode(mathematics)
Reading_mode = statistics.mode(reading)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of Mathematics is {}, {} and {} respectively".format(Mathematics_mean, Mathematics_median, Mathematics_mode))
print("Mean, Median and Mode of Reading is {}, {} and {} respectively".format(Reading_mean, Reading_median, Reading_mode))
#Standard deviation for Mathematics and Reading
Mathematics_std_deviation = statistics.stdev(mathematics)
Reading_std_deviation = statistics.stdev(reading)
#1, 2 and 3 Standard Deviations for Mathematics
Mathematics_first_std_deviation_start, Mathematics_first_std_deviation_end = Mathematics_mean-Mathematics_std_deviation, Mathematics_mean+Mathematics_std_deviation
Mathematics_second_std_deviation_start, Mathematics_second_std_deviation_end = Mathematics_mean-(2*Mathematics_std_deviation), Mathematics_mean+(2*Mathematics_std_deviation)
Mathematics_third_std_deviation_start, Mathematics_third_std_deviation_end = Mathematics_mean-(3*Mathematics_std_deviation), Mathematics_mean+(3*Mathematics_std_deviation)
#1, 2 and 3 Standard Deviations for Reading
Reading_first_std_deviation_start, Reading_first_std_deviation_end = Reading_mean-Reading_std_deviation, Reading_mean+Reading_std_deviation
Reading_second_std_deviation_start, Reading_second_std_deviation_end = Reading_mean-(2*Reading_std_deviation), Reading_mean+(2*Reading_std_deviation)
Reading_third_std_deviation_start, Reading_third_std_deviation_end = Reading_mean-(3*Reading_std_deviation), Reading_mean+(3*Reading_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for Mathematics
mathematics_of_data_within_1_std_deviation = [result for result in mathematics if result > Mathematics_first_std_deviation_start and result < Mathematics_first_std_deviation_end]
mathematics_of_data_within_2_std_deviation = [result for result in mathematics if result > Mathematics_second_std_deviation_start and result < Mathematics_second_std_deviation_end]
mathematics_of_data_within_3_std_deviation = [result for result in mathematics if result > Mathematics_third_std_deviation_start and result < Mathematics_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for Reading
reading_of_data_within_1_std_deviation = [result for result in reading if result > Reading_first_std_deviation_start and result < Reading_first_std_deviation_end]
reading_of_data_within_2_std_deviation = [result for result in reading if result > Reading_second_std_deviation_start and result < Reading_second_std_deviation_end]
reading_of_data_within_3_std_deviation = [result for result in reading if result > Reading_third_std_deviation_start and result < Reading_third_std_deviation_end]
#Printing data for Mathematics and Reading (Standard Deviation)
print("{}% of data for Mathematics lies within 1 standard deviation".format(len(mathematics_of_data_within_1_std_deviation)*100.0/len(mathematics)))
print("{}% of data for Mathematics lies within 2 standard deviations".format(len(mathematics_of_data_within_2_std_deviation)*100.0/len(mathematics)))
print("{}% of data for Mathematics lies within 3 standard deviations".format(len(mathematics_of_data_within_3_std_deviation)*100.0/len(mathematics)))
print("{}% of data for Reading lies within 1 standard deviation".format(len(reading_of_data_within_1_std_deviation)*100.0/len(reading)))
print("{}% of data for Reading lies within 2 standard deviations".format(len(reading_of_data_within_2_std_deviation)*100.0/len(reading)))
print("{}% of data for Reading lies within 3 standard deviations".format(len(reading_of_data_within_3_std_deviation)*100.0/len(reading)))
