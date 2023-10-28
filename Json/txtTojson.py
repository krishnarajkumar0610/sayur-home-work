# krishna_rajkumar 3rd_year B.E_CSD
# priyadharshini 1st_year B.SC_CS
import json

with open("F:\\KRISHNA RAJKUMAR PERSONAL\\SAYUR LEARNING\\Sayur github\\sayur-home-work\\Json\\text.txt",'r') as file:
    outer_dict={}
    inner_dict={}
    j=1
    for words in file:
        i = 1
        
        words = words.strip().split(" ")
        
        fieds=["name","year","degree"]
        for index,word in enumerate(words): # [krishna_rajkumar , 3rd_year , B.E_CSD]
            
            inner_dict[fieds[index]]=word # [priyadharshini , 1st_year , B.SC_CS]    
               
        outer_dict["Student "+str(j)]=inner_dict
        inner_dict={}
        j+=1
        
with open("F:\KRISHNA RAJKUMAR PERSONAL\SAYUR LEARNING\Sayur github\sayur-home-work\Json\student_det.json",'w') as out_file:
    json.dump(outer_dict,out_file,indent=3)
    out_file.close()
    