
from atlassian import Confluence
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup


confluence = Confluence(
    url='https://ishar.atlassian.net',
    username="isharanka10@gmail.com",
    password="4LEE3ZBxNzgZmjzobxkOCC4C"
    )
# result="""<table border="1" class="dataframe"> 
#   <thead> 
#     <tr style="text-align: right;">
#       <th>Company</th>
#       <th>Contact</th>
#       <th>Country</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <td>Alfreds Futterkiste</td>
#       <td>Maria Anders</td>
#       <td>Germany</td>
#     </tr>
#     <tr>
#       <td>Centro comercial Moctezuma</td>
#       <td>Francisco Chang</td>
#       <td>Mexico</td>
#     </tr>
#     <tr>
#       <td>consultadd</td>
#       <td>isha</td>
#       <td>india</td>
#     </tr>
#   </tbody>
# </table>"""
# body= "<html><head><title>hii</title></head><body>hi there"+result+"</body></html>"



# confluence.update_page(33131, "title changed again ok yess!!!", body, parent_id=None, type='page', representation='storage', minor_edit=False)








old_content = confluence.get_page_by_id(33131,expand='body.storage')
html_content=old_content["body"]["storage"]["value"]

soup = BeautifulSoup(html_content)

headings = [th.get_text() for th in soup.find("tr").find_all("th")]

datasets = []
for row in soup.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    datasets.append(dataset)
dict={}
for i in datasets:
    i1=list(i)
    for j in range(len(i1)):
        if i1[j][0] in dict:
            dict[i1[j][0]].append(i1[j][1])
        else:
            dict[i1[j][0]]=[i1[j][1]]
df=pd.DataFrame(dict)

df.loc[len(df.index)] = ['google', "gaurav", "india"] 

result=df.to_html(index=False)
result=str(result)
body= "<html><head><title>hii</title></head><body>hi there"+result+"</body></html>"
confluence.update_page(33131, "title changed again badiya!!!", body, parent_id=None, type='page', representation='storage', minor_edit=False)



# page = confluence.get_page_by_id(33131)
# print(page)
# print(confluence.get_page_by_title("start", "title changed!!!", start=None, limit=None))
# print(confluence.get_draft_page_by_id(33131, status='draft'))


#print(confluence.page_exists("start", "start_page1"))
#print(confluence.get_page_id("start", "start_page1"))
#print(confluence.get_page_space(33131))
#confluence.update_page(33131, "title change hogyaaa!!", "nachoooo", parent_id=None, type='page', representation='storage', minor_edit=False)




