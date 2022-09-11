dataset = open('/Users/johnnyc/Desktop/CWTS_csv.csv')

#Aggregate summary 1. The total no. of university publications per country
dict_1 = {}
firstline = True

for row in dataset:
    if firstline:
        field_names = row.rstrip('\n').split(',')
        firstline = False
    else:
        values = row.rstrip('\n').split(',')    
        country = values[1]
        impact_P = values[5] 
        if '–' not in impact_P: #Cleaning step: Through manual inspection, some data have been incorrectly incorporated into the 'impact_P' field with the inclusion of hyphen.
                                #Such values have been omitted for the ensurance of data quality   
            float_impact_P = float(impact_P)
            if country not in dict_1:
                dict_1[country] = 0
            else:
                dict_1[country] += float_impact_P
        
for key in sorted(dict_1):
    print(key,":",dict_1[key])


#Aggregate summary 2. The total no. of university’s collaborative activity with other institutions in a given country 
dict_2 = {}
firstline = True

for row in dataset:
    if firstline:
        field_names = row.rstrip('\n').split(',')
        firstline = False
    else:
        values = row.rstrip('\n').split(',')    
        country = values[1]
        collab_P = values[6]
        if '-' not in collab_P: #Cleaning step: Through manual inspection, some data have been incorrectly incorporated into the 'collab_P' field with the inclusion of unncessary '-' character.
                                #Such values have been omitted for the ensurance of data quality.
            float_collab_P = float(collab_P)
            if country not in dict_2:
                dict_2[country] = 0
            else:
                dict_2[country] += float_collab_P
        
for key in sorted(dict_2):
    print(key,":",dict_2[key])

#Aggregate summary 3. Finding the top 5 countries with the highest open-access publications
dict_3 = {}
firstline = True

for row in dataset:
    if firstline:
        field_names = row.rstrip('\n').split(',')
        firstline = False
    else:
        values = row.rstrip('\n').split(',')    
        country = values[1]
        oa = values[7]
        if '-' not in oa: #Cleaning step: Through manual inspection, some data have been incorrectly incorporated into the 'collab_P' field with the inclusion of unncessary '-' character.
                                #Such values have been omitted for the ensurance of data quality.
            float_oa = float(oa)
            if country not in dict_3:
                dict_3[country] = 0
            else:
                dict_3[country] += float_oa


descendingorder_dict_3 = dict( sorted(dict_3.items(),
                           key=lambda item: item[1],
                           reverse=True))


top5 = {x : descendingorder_dict_3[x] for x in list(descendingorder_dict_3)[:5]}

print(top5)



        




        

        

    



    