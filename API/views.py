from django.shortcuts import render
from  API import models
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import datetime
import xlwt

# Create your views here.

def listUsers(request):
	

	response=HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename=Usuários' + \
	str(datetime.datetime.now())+ '.xls'
	
	wb= xlwt.Workbook(encoding='utf-8')
	ws=wb.add_sheet('Usuarios')
	
	row_num=0  
	font_style=xlwt.XFStyle()
	font_style.font.bold=True
	
	columns=['Nome']
	
	for cols in  range( len(columns) ):
		ws.write(row_num, cols, columns[cols], font_style)		


	font_style=xlwt.XFStyle()
	
	rows=models.User.objects.values_list('login')
	
	for row in rows:
		row_num +=1
		
		for cols in range( len(row) ):
			ws.write(row_num, cols, str(row[cols]), font_style)
	
	
	wb.save(response)
	
	
	return response
	
	
	
	
	
