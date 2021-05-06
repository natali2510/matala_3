file = open('text_whatssap.txt','r',encoding='utf-8')
finel_file=file.read()
data=dict()
my_list=list()
lines=finel_file.split('\n')
id=0

line=0
for line in lines:
    if ":" in line[line.find('-')+2: ]: 
        if line[line.find('-')+2:line.find(': ')] not in data:
            id=id+1
            data[line[line.find('-')+2:line.find(': ')]]=id    
    data['datetime']=line[:line.find("-")-1]
    data['id']=id
    data['text']= line[line.find(': ')+1: ]
   
    my_list.append({"datetime":data['datetime'],"id":data['id'],"text": data['text']})  
  
metadata=dict()
for line in lines:
     if "נוצרה על ידי" in line:
         metadata['chat name']=line[line.find(' "')+2:line.find('" ')]
         metadata['date_creation']= line[:line.find('-')-1 ]
         metadata['num_of_participants']= id
         metadata['creator']= line[line.find('על ידי ')+9:len(line)-2].rstrip().lstrip()


summary={"matadata":metadata, "messages":my_list}  
import json
new_json=json.dumps(summary,ensure_ascii=False, indent=5) 
  
with open(metadata['chat name']+'.txt' , 'w',encoding='utf-8') as f:
 f.write(new_json)    
    