
# coding: utf-8

# In[22]:

#Function that takes a file.txt as entry and returns a list(k1,v1) corresponding to each number of the line and its text
#input=fichier_texte--> output=list(ki,vi) where i from 0 to nb of lines of fichier texte
def Input_reader(fichier_texte):
    list_k1=[]
    index_ligne=1
    for i in fichier_texte:
        list_k1.append([index_ligne,i.rstrip('\n\r')])
        index_ligne=index_ligne+1
    return(list_k1)
    
#Test of Input_reader on the chosen file    
test_Input_reader=open("C:/Users/Sophia/Desktop/texte_Sophia.txt","r")
print(Input_reader(test_Input_reader))


# In[23]:

#Function that split a line v1 into words and returns a list of tuples (word present in line v1,1)
#input= (k1,v1)-->output= list(k2,v2)
def my_map(k1,v1):
    list_map=[]
    list_split=v1.split()
    for j in range(len(list_split)):
        list_map.append((list_split[j],1))
    return(list_map) 

#Test of the map function on the second line of the chosen file
k_test=2
v_test="are able to live in peace and progressive harmony above all creeds and all"
print(my_map(k_test,v_test))


# In[24]:

#Intermediate function that removes elements of indexes in index from a given list ma_liste
def supprimer_from_liste(ma_liste=[],mon_index=[]):
    compt=0
    for l in mon_index:
        ma_liste.remove(ma_liste[l-compt])
        compt=compt+1
    return (ma_liste)

#Test of the function supprimer_from_liste --> removes words in position 0 and 3 from the second line of the chosen file
suppression=[('are', 1), ('able', 1), ('to', 1), ('live', 1), ('in', 1), ('peace', 1), ('and', 1), ('progressive', 1), ('harmony', 1), ('above', 1), ('all', 1), ('creeds', 1), ('and', 1), ('all', 1)]
print(supprimer_from_liste(suppression,[0,3]))


# In[25]:

#Function sort_shuffle that is implemented when every node_mapper has finished its task
#input=list containing the result of all mappers-->output=(word,[1,1,...]) for every word in the input_file
def shuffle_sort(all_mappers=[]):
    temp_size=len(all_mappers)
    list_ss=[]
    while temp_size >0:
        counter=0
        index_supp=[]
        for j in range(temp_size):
            if (all_mappers[0])[0]==(all_mappers[j])[0]:
                counter=counter+1
                index_supp.append(j)
        list_ss.append(((all_mappers[0])[0],[1]*counter))
        supprimer_from_liste(all_mappers,index_supp) 
        temp_size=len(all_mappers)
    return(list_ss)

#Test of the function shuffle_sort on line 2 in this example but actually it takes all the lines when mapped
test_ss=[('are', 1), ('able', 1), ('to', 1), ('live', 1), ('in', 1), ('peace', 1), ('and', 1), ('progressive', 1), ('harmony', 1), ('above', 1), ('all', 1), ('creeds', 1), ('and', 1), ('all', 1)]
print(shuffle_sort(test_ss))


# In[27]:

#Function that ,in this particular case,sums the numbers in a given list
#input=(k2,v2)-->output=list(k3,v3)
def my_reduce(k2,v2):
    list_reduced=()
    compt=0
    for h in v2:
        compt=compt+1
        list_reduced=(k2,compt)
    return(list_reduced)

k2_test="Auroville"
v2_test=[1,1,1,1]
print(my_reduce(k2_test,v2_test))


# In[47]:

#Function Output writer
def Output_writer(all_reducers=[]):
    long=len(all_reducers)
    for w in range(long):
        print(all_reducers[w][0],all_reducers[w][1])

#Test of Output writer on 3 reducers        
test_all_reducers=[("Auroville",4),("India",2),("Peace",1)]
Output_writer(test_all_reducers)


# In[ ]:

#MON MAIN

