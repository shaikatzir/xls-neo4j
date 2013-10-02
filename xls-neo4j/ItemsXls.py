


from xlwt import Workbook
import xlwt




class XlsParams :
    

    def __init__(self, headings):
        self.rowx = 0
        self.book = Workbook()
        self.sheet = self.book.add_sheet('Sheet 1')
        self.headings = headings


    
    def WriteXlsHeader(self):
    

        # Add headings with styling and froszen first row
        heading_xf = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')
    
    
        self.sheet.set_panes_frozen(True) # frozen headings instead of split panes
        self.sheet.set_horz_split_pos(self.rowx+1) # in general, freeze after last heading row
        self.sheet.set_remove_splits(True) # if user does unfreeze, don't leave a split there
        for colx, value in enumerate(self.headings):
            self.sheet.write(self.rowx, colx, value, heading_xf)
            self.sheet.col(colx).width  = 0x0d00 + 1000
        
        self.rowx +=1    
    
    
        
    def WriteItemXls(self,item_xl):
        MaxCount =0
        for i in range(0, len(self.headings)):
           if self.headings[i] in item_xl:
               count = 0
               for pr in item_xl[self.headings[i]]:
                   self.sheet.write(self.rowx+count, i, pr)
                   count+=1
               #check how many rows took for this category    
               if (count > MaxCount):
                   MaxCount = count
        #move to the next item by moving MaxCount rows.  
        self.rowx+= MaxCount
   
    def SaveXls(self,name):
        self.book.save(name)
    
    

