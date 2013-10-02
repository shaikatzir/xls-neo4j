#Neo4j pre-defind Index. "node_auto_index" - default neo4j indexing. 
searchIndex = "node_auto_index"

#A property of the nodes which is indexed by 'searchIndex'
searchKey = "type"

#The 'searchKey' property value of the nodes which we are looking for exporting
searchName = "item"

#Id property of the node - written at each cell
itemID = "name"

#Relationship types to be searched. All connected nodes with the following relationships, will be exported to the node row in the spreadsheet
rels = ['REL_TYPE1','REL_TYPE2']

#nodes to be ignored. connected nodes with 'itemID' equals to one of this list values - will not be exported to the spreadsheet
ignoreList = ["name1","name2"]

#Name for the spreadsheet. The program will create (or run over) "<fileName>.xls"
fileName = "AllItems"

#Every 'tmpCount' nodes, the program will dump the current results into the spreadsheet file
tmpCount = 50

#Every 'maxItems' nodes, the program will close the file and start dumping results into new file - "<fileName>({file-count}).xls"
maxItems = 1000



