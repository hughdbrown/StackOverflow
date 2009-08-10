
import operator 

def test_1252481():
	d = {'file_name':'thisfile.flt', 'item_name':'box', 'item_height':'8.7', 'item_width':'10.5', 'item_depth':'2.2', 'texture_file': 'red.jpg'}
	elem = [ 'file_name', 'item_name', 'item_height', 'item_width', 'item_depth', 'texture_file'] 
	order = dict( (name, i) for i, name in enumerate(elem) )
	return [d[k] for k,v in sorted(order.items(), key=operator.itemgetter(1))] 
	

if __name__ == '__main__':
	print test_1252481()
	print "Expect: ", ['thisfile.flt', 'box', '8.7', '10.5', '2.2', 'red.jpg']