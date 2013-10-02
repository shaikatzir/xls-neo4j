


from py2neo import neo4j
import ItemsXls
import confFile as conf

import sys

if (len(sys.argv) > 1):
    url = sys.argv[1];
else:
    url = "http://localhost:7474/db/data/"
    
graph_db = neo4j.GraphDatabaseService(url) 

#get the index for searching
Index = graph_db.get_or_create_index(neo4j.Node, conf.searchIndex)


def startXLS ():
    xls = ItemsXls.XlsParams([conf.itemID]+conf.rels)
    xls.WriteXlsHeader()
    return xls


xls = startXLS();
AllItems= Index.get(conf.searchKey, conf.searchName)
count = 0
countFiles = 0
saveName = conf.fileName+".xls"

for it in AllItems:
     
     #xlItem - the record to be written to the excel file
     xlItem={}
     #first enter the 'itemID' - the unique name of the item
     xlItem[conf.itemID] = [it[conf.itemID]]

     #search all relationships - rels    
     for rel in conf.rels:
          #find all related nodes with 'rel' rel_type
          it_rels = it.match(rel);     
          xlItem[rel]=[]
          #fill the column with all values
          for i_rel in it_rels:
              end_node = i_rel.end_node
              node_name = end_node[conf.itemID]
              if node_name not in conf.ignoreList :
                  xlItem[rel].append(node_name)
     
     xls.WriteItemXls(xlItem)
     count +=1
     
     #dump temp result every 'tmpCount' items
     if ((count % conf.tmpCount) == 0) :
        xls.SaveXls(saveName)
   
     
     #add a new 'xls' file every 'maxItems' items
     if (count > conf.maxItems):   
        xls.SaveXls(saveName)
        #start a new 'xls' table
        xls = startXLS();
        #create a new name for the file
        countFiles +=1
        saveName = conf.fileName + "("+str(countFiles)+").xls"
        count = 0

#save last items
xls.SaveXls(saveName)     

