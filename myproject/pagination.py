# pagination is used to manage pagination data.
# that is data splits across several pages
# all method of pagination use 'Paginator'class. it does all the heavy lifting of actually spliting a query set into page objects.
from django.core.paginator import Paginator
l=["a","b","c","d","e","f","g"]
p=Paginator(l,2)#split
print(p.count)  #to get the no of elements in the list
print(p.num_pages) #to print the no of pages
print(p.page_range)#to get the no of iteration
page1=p.page(1) #to select the page1
print(page1.object_list) #to print the page1
page2=p.page(2)
print(page2.object_list)
page3=p.page(3)
print(page3.object_list)
print(page3.has_next()) #to check next page (t/f)
page4=p.page(4)
print(page4.has_next())
print(page4.has_previous()) #to check previous page(t/f)
print(page1.has_previous())
print(page1.next_page_number()) #to print next page no
print(page2.next_page_number())
print(page4.previous_page_number()) #to print previous page no
print(page2.previous_page_number())
print(page1.start_index()) # to get the starting index of a page
print(page1.end_index()) #to get the ending index of the page
print(page3.start_index())
print(page3.end_index())