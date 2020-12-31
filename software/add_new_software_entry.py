import os
import json
with open('entryDict.json', 'r') as file:
	entryDict = json.load(file)
with open('index.html', 'r') as html:
	htmlExistingContent = html.readlines()
	newEntryPoint = htmlExistingContent.index('			<!-- @@@NEW-ENTRY-POINT -->\n')
with open('index.html', 'w') as html:
	html.writelines(htmlExistingContent[:newEntryPoint])
	html.write('			<br/>\n')
	html.write('			<article>\n')
	html.write('				<section>\n')
	html.write('					<h1 style="color:white;">\n')
	html.write('						{}\n'.format(entryDict['header']))
	html.write('					</h1>\n')
	html.write('				</section>\n')
	html.write('				<section>\n')
	for i in entryDict['content']:
		html.write('					<p style="color:white;">\n')
		html.write('						{}\n'.format(i))
		html.write('					</p>\n')
	html.write('				</section>\n')
	html.write('				<section>\n')
	html.write('					<a href="{}" style="color:red;">\n'.format(entryDict['page-path']))
	html.write('						Read More >>\n')
	html.write('					</a>\n')
	html.write('				</section>\n')
	html.write('			</article>\n')
	html.writelines(htmlExistingContent[newEntryPoint:])