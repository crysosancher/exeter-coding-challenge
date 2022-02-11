import csv
import time
import os, psutil

text=open('french_dictionary.csv')
text_csv=csv.reader(text)

time1=time.time()
dictionary=dict()

#dictionary with word and meanings
for row in text_csv:
    dictionary[row[0]]=row[1]

#dictionary to store frequency of words
freq_dict=dict()

with open('t8.shakespeare.txt','r') as f , open('t8.shakespeare.translated.txt','w') as out:

    for line in f:
            temp=""
            fin=""
            for chr in line:


                #if character is alphanumeric adding it temporary word
                if chr.isalnum():
                    temp+=chr
                else:
                    #when special character came cutting and taking the temp word to check it in dictionary
                    if temp.lower() in dictionary:
                        #updating the frequency of word
                        if temp.lower() in freq_dict:
                            freq_dict[temp.lower()]+=1
                        else:
                            freq_dict[temp.lower()]=1

                        #maintaining the case scenerio
                        dic_word=dictionary[temp.lower()]
                        if temp.isupper():
                            dic_word=dic_word.upper()
                        elif temp.islower():
                            dic_word=dic_word.lower()
                        else:
                            dic_word=dic_word.capitalize()
                        fin+=dic_word
                    else:
                        fin+=temp

                    #writing the word in output file
                    out.write(fin)


                    #adding special chr(space , / - ; : ! etc) to output file and reseting the temp variables
                    out.write(chr)
                    fin = ""
                    temp = ""
#creating a csv file for frequency of words
with open('frequency.csv','w',newline="") as file:
    writer=csv.writer(file)

    writer.writerow(["English Word","French Word","Frequency"])
    for key,val in sorted(freq_dict.items()):
        writer.writerow([key,dictionary[key],val])

time2=time.time()
final_time_min=(time2-time1)//60
final_time_sec=(time2-time1)%60
memory_used=(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

#adding the time and space values to txt file
with open('performance.txt','w') as f:
    f.write("Time to process: {} minutes {} seconds \nMemory used: {} MB".format(final_time_min,final_time_sec,memory_used))
