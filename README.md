xls-neo4j
=======

Documentation
-------------

Export data from your Neo4j Graph DB into a spreadsheet in ONE CLICK.
**xls-neo4j** searches for all nodes of a certain type, and export them, with their related nodes, into a spreadsheet.

Sample output : 

![improved admin interface screenshot](/docs/AllItemsSample.png)

### Requirements
* [py2neo-1.5.1](https://github.com/nigelsmall/py2neo)
* [xlwt-0.7.5](https://pypi.python.org/pypi/xlwt)

### Installation

Well... For now just copy 'xls-neo4j' to your destination.


### Quickstart

First, you'll will need to modify the 'xls-neo4j/conf.py' for your own needs.
The file contains the following configurable parameters:

```python
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
#(can be empty array...)
ignoreList = ["name1","name2"]

#Name for the spreadsheet. The program will create (or run over) "<fileName>.xls"
fileName = "AllItems"

#Every 'tmpCount' nodes, the program will dump the current results into the spreadsheet file
tmpCount = 50

#Every 'maxItems' nodes, the program will close the file and start dumping results into new file - "<fileName>({file-count}).xls"
maxItems = 1000

```

The above default parameters, will result in the following:
* The program will search using "node_auto_index", all nodes where the property 'type' is 'item'. 
* Each node will be written in a new row in the spreadsheet. The name of the node in the spreadsheet, will be the value of the 'name' property of the node.
* For each node, all connected nodes by 'REL_TYPE1' or 'REL_TYPE2' will be written to the item node row in the spreadsheet.
* Connected nodes which their property 'name' is either "name1" or "name2" won't be exported.
* Every 50 exported nodes, the results will be dumped to "AllItems.xls".
* Every 1000 exported nodes will be dumped to a new file - named "AllItems(x).xls"


Then simply run 

```bash
python xls-neo4j\getAllItems.py <url>
```

url - (OPTIONAL) the graph DB url. If empty - "http://localhost:7474/db/data/" will be used.



