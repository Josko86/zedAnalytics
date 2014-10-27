# -*- coding: utf-8 -*-
import time
import datetime
from Analytics.models import Application, Date
import requests
import simplejson
import xlrd
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def handle(self, *args, **options):

        try:

            print("updating database")
            ACCOUNT_ID_BITMONLAB_IOS = "179195"
            ACCOUNT_ID_PYROM_IOS = "179354"
            ACCOUNT_ID_PLAYERX = "173012"
            ACCOUNT_ID_ZW = "39230"
            ACCOUNT_ID_BITMONLAB_ANDROID = "179197"
            ACCOUNT_ID_ZGPS = "46490"
            ACCOUNT_ID_AZW = "173002"
            APIKEY_APPANNIE = "bearer 5dba15b181bd108344478ee985a7e0b737562377"

            app_ids_BitmonlabIOS = []
            app_ids_PyroMIOS = []
            app_ids_PlayerX = []
            app_ids_ZW = []
            app_ids_BitmonlabAndroid = []
            app_ids_ZGPS = []
            app_ids_AZW = []
            lastDateExcel = "unknown"

            # Recoger datos del excel rusia xlsx
            try:
                book = xlrd.open_workbook('rusia.xlsx')
                sheet = book.sheet_by_name('Android market overall')
                num_cells = sheet.ncols - 1
                curr_row = 1

                num_cellsAux = num_cells
                badDays = 0
                while sheet.cell_value(7, num_cellsAux) == '':
                    num_cellsAux = num_cellsAux -1
                    badDays += 1


                lastDateExcel = (datetime.datetime.strptime('1899-12-30', '%Y-%m-%d') +
                                     datetime.timedelta(days=sheet.cell_value(1, num_cells) - badDays)).strftime("%Y-%m-%d")

                while sheet.cell_value(curr_row,0) != 'Daily installs by device':
                    curr_row += 1

                while sheet.cell_value(curr_row,0) != 'Total':
                    curr_row += 1
                    name = sheet.cell_value(curr_row, 0)
                    if '(' in name:
                        name = name[:name.find('(')-1]
                    totalA = 0
                    totalM = 0
                    totalW = 0
                    totalT = 0
                    curr_cell = 0
                    while curr_cell < num_cells:
                        curr_cell += 1
                        cell_type = sheet.cell_type(curr_row, curr_cell - badDays)
                        cell_value = sheet.cell_value(curr_row, curr_cell - badDays)
                        if cell_type == 2:
                            if curr_cell > num_cells - 30:
                                totalM += cell_value
                                if curr_cell > num_cells - 7:
                                    totalW += cell_value
                                    if curr_cell > num_cells - 1:
                                        totalT += cell_value
                            totalA += cell_value
                    if name!='Total':
                        a1 = Application(appKey=name+'A', name=cleanName(name), category='unknown', downloadsA=totalA, os='Android',
                                         account="RUS", downloadsM=totalM, downloadsW=totalW, downloadsT=totalT,
                                         revenueA=0.00, revenueM=0.00, revenueW=0.00, revenueT=0.00)
                        try:
                            a2= Application.objects.get(appKey=name+'A')
                            a2.downloadsA = a1.downloadsA
                            a2.downloadsT = a1.downloadsT
                            a2.downloadsW = a1.downloadsW
                            a2.downloadsM = a1.downloadsM
                            a2.revenueA = a1.revenueA
                            a2.revenueT = a1.revenueT
                            a2.revenueW = a1.revenueW
                            a2.revenueM = a1.revenueM
                            a2.save()
                        except Exception as ex:
                            a1.save()

                while sheet.cell_value(curr_row,0) != 'Daily installs by device from AppStore':
                    curr_row += 1

                while sheet.cell_value(curr_row,0) != '':
                    curr_row += 1
                    name = sheet.cell_value(curr_row, 0)
                    if '(' in name:
                        name = name[:name.find('(')-1]
                    totalA = 0
                    totalM = 0
                    totalW = 0
                    totalT = 0
                    curr_cell = 0
                    while curr_cell < num_cells:
                        curr_cell += 1
                        cell_type = sheet.cell_type(curr_row, curr_cell - badDays)
                        cell_value = sheet.cell_value(curr_row, curr_cell - badDays)
                        if cell_type == 2:
                            if curr_cell > num_cells - 30:
                                totalM += cell_value
                                if curr_cell > num_cells - 7:
                                    totalW += cell_value
                                    if curr_cell > num_cells - 1:
                                        totalT += cell_value
                            totalA += cell_value
                    if name!='':
                        a1 = Application(appKey=name+'I', name=cleanName(name), category='unknown', downloadsA=totalA, os='iOS',
                                         account="RUS", downloadsM=totalM, downloadsW=totalW, downloadsT=totalT,
                                         revenueA=0.00, revenueM=0.00, revenueW=0.00, revenueT=0.00)
                        try:
                            a2= Application.objects.get(appKey=name+'I')
                            a2.downloadsA = a1.downloadsA
                            a2.downloadsT = a1.downloadsT
                            a2.downloadsW = a1.downloadsW
                            a2.downloadsM = a1.downloadsM
                            a2.revenueA = a1.revenueA
                            a2.revenueT = a1.revenueT
                            a2.revenueW = a1.revenueW
                            a2.revenueM = a1.revenueM
                            a2.save()
                        except Exception as ex:
                            a1.save()

                print('Database updated from excel')
            except Exception as ex:
                print(ex)

            today = datetime.date.today().strftime("%Y-%m-%d")
            yesterday = (datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.timedelta(days=2)).strftime("%Y-%m-%d")
            lastWeek = (datetime.datetime.strptime(yesterday, '%Y-%m-%d') - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
            lastMonth = (datetime.datetime.strptime(yesterday, '%Y-%m-%d') - datetime.timedelta(days=30)).strftime("%Y-%m-%d")

            a1 = Date(dateAppannie=yesterday, dateExcel=lastDateExcel)
            try:
                a2= Date.objects.get(id=1)
                a2.dateAppannie = a1.dateAppannie
                a2.dateExcel = a1.dateExcel
                a2.save()
            except Exception as ex:
                a1.save()

            #rellenar el array de las aplicaciones flurry
            # flurryAppList = requests.get('http://api.flurry.com/appInfo/getAllApplications?apiAccessCode=' + APIFLURRY +
            #                             '&apiKey=2VYRJ826D32Z7TCS5899')
            # json = simplejson.loads(flurryAppList.content)
            # flurryAppList = json["application"]
            # for i in range(len(flurryAppList)):
            #     time.sleep(1)
            #     apiKey = flurryAppList[i]["@apiKey"]
            #     r = requests.get('http://api.flurry.com/appInfo/getApplication?apiAccessCode='  + APIFLURRY +
            #                      '&apiKey=' + apiKey)
            #     json = simplejson.loads(r.content)
            #
            #     createdDate = json["@createdDate"]
            #
            #     startDate = today
            #     total = 0
            #     while (startDate>createdDate):
            #         endDate = startDate
            #         startDate = (datetime.datetime.strptime(endDate, '%Y-%m-%d') - datetime.timedelta(days=365))
            #         startDate = startDate.strftime("%Y-%m-%d")
            #         time.sleep(1)
            #         s = requests.get('http://api.flurry.com/appMetrics/NewUsers?apiAccessCode='  + APIFLURRY +
            #                        '&apiKey='+ apiKey + '&startDate=' + startDate + '&endDate=' + endDate + '&groupBy=months')
            #         json2 = simplejson.loads(s.content)
            #         for j in range(len(json2["day"])):
            #             total += int(json2["day"][j]["@value"])
            #
            #
            #     aplicacionesFlurry[apiKey] = []
            #     aplicacionesFlurry[apiKey].append(flurryAppList[i]["@name"])
            #     aplicacionesFlurry[apiKey].append(json["@category"])
            #     aplicacionesFlurry[apiKey].append(total)
            #     aplicacionesFlurry[apiKey].append(flurryAppList[i]["@platform"])
            #     a1 = Application(appKey=apiKey, name=aplicacionesFlurry[apiKey][0], category=aplicacionesFlurry[apiKey][1],
            #                      downloads=aplicacionesFlurry[apiKey][2], os=aplicacionesFlurry[apiKey][3], source="flurry")
            #     try:
            #         a2= Application.objects.get(appKey=apiKey)
            #         a2.downloads = a1.downloads
            #         a2.save()
            #     except Exception as ex:
            #         a1.save()


            #rellenar array de ids de aplicaciones de cada tienda
            BitmonlabIOSAppList = requests.get('https://api.appannie.com/v1.2/accounts/'+ ACCOUNT_ID_BITMONLAB_IOS +'/products',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(BitmonlabIOSAppList.content)
            BitmonlabIOSAppList = json["products"]
            for i in range(len(BitmonlabIOSAppList)):
                if BitmonlabIOSAppList[i]['status']:
                    app_ids_BitmonlabIOS.append((BitmonlabIOSAppList[i]["product_id"]))

            PyroMIOSAppList = requests.get('https://api.appannie.com/v1.2/accounts/'+ ACCOUNT_ID_PYROM_IOS +'/products',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(PyroMIOSAppList.content)
            PyroMIOSAppList = json["products"]
            for i in range(len(PyroMIOSAppList)):
                if PyroMIOSAppList[i]['status']:
                    app_ids_PyroMIOS.append((PyroMIOSAppList[i]["product_id"]))

            PlayerXAppList = requests.get('https://api.appannie.com/v1.2/accounts/'+ ACCOUNT_ID_PLAYERX +'/products',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(PlayerXAppList.content)
            PlayerXAppList = json["products"]
            for i in range(len(PlayerXAppList)):
                if PlayerXAppList[i]['status']:
                    app_ids_PlayerX.append((PlayerXAppList[i]["product_id"]))

            ZWAppList = requests.get('https://api.appannie.com/v1.2/accounts/'+ ACCOUNT_ID_ZW +'/products',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(ZWAppList.content)
            ZWAppList = json["products"]
            for i in range(len(ZWAppList)):
                try:
                    if ZWAppList[i]['status'] and (len(ZWAppList[i]['devices'])>0):
                        app_ids_ZW.append((ZWAppList[i]["product_id"]))
                except:
                    pass

            BitmonlabAndroidAppList = requests.get('https://api.appannie.com/v1.2/accounts/'+ ACCOUNT_ID_BITMONLAB_ANDROID +'/products',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(BitmonlabAndroidAppList.content)
            BitmonlabAndroidAppList = json["products"]
            for i in range(len(BitmonlabAndroidAppList)):
                if BitmonlabAndroidAppList[i]['status']:
                    app_ids_BitmonlabAndroid.append((BitmonlabAndroidAppList[i]["product_id"]))

            ZGPSAppList = requests.get('https://api.appannie.com/v1.2/accounts/'+ ACCOUNT_ID_ZGPS +'/products',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(ZGPSAppList.content)
            ZGPSAppList = json["products"]
            for i in range(len(ZGPSAppList)):
                if ZGPSAppList[i]['status']:
                    app_ids_ZGPS.append((ZGPSAppList[i]["product_id"]))

            AZWAppList = requests.get('https://api.appannie.com/v1.2/accounts/'+ ACCOUNT_ID_AZW +'/products',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(AZWAppList.content)
            AZWAppList = json["products"]
            for i in range(len(AZWAppList)):
                if AZWAppList[i]['status']:
                    app_ids_AZW.append((AZWAppList[i]["product_id"]))

            time.sleep(14)

            #Crea un diccionario por cada tienda con id de aplicacion y nombre, categoria y numero de descargas, y revenues
            for app_id in app_ids_BitmonlabIOS:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.2/apps/ios/app/' + str(app_id) + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_BITMONLAB_IOS + '/products/' +
                                 str(app_id) + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_BITMONLAB_IOS + '/products/' +
                                 str(app_id) + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_BITMONLAB_IOS + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_BITMONLAB_IOS + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["product"]["product_name"]
                category = json["product"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["product"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["product"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["product"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["product"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["product"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='iOS',
                                 account="Bitmonlab", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
                    a2.name = a1.name
                    a2.downloadsA = a1.downloadsA
                    a2.downloadsT = a1.downloadsT
                    a2.downloadsW = a1.downloadsW
                    a2.downloadsM = a1.downloadsM
                    a2.revenueA = a1.revenueA
                    a2.revenueT = a1.revenueT
                    a2.revenueW = a1.revenueW
                    a2.revenueM = a1.revenueM
                    a2.save()
                except Exception as ex:
                    a1.save()

            print('Bitmonlab iTunes updated')


            for app_id in app_ids_PyroMIOS:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.2/apps/ios/app/' + str(app_id) + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_PYROM_IOS + '/products/' +
                                 str(app_id) + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_PYROM_IOS + '/products/' +
                                 str(app_id) + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_PYROM_IOS + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_PYROM_IOS + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["product"]["product_name"]
                category = json["product"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["product"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["product"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["product"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["product"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["product"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='iOS',
                                 account="PyroM", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
                    a2.name = a1.name
                    a2.downloadsA = a1.downloadsA
                    a2.downloadsT = a1.downloadsT
                    a2.downloadsW = a1.downloadsW
                    a2.downloadsM = a1.downloadsM
                    a2.revenueA = a1.revenueA
                    a2.revenueT = a1.revenueT
                    a2.revenueW = a1.revenueW
                    a2.revenueM = a1.revenueM
                    a2.save()
                except Exception as ex:
                    a1.save()

            print('PyroM iTunes updated')


            for app_id in app_ids_PlayerX:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.2/apps/ios/app/' + str(app_id) + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_PLAYERX + '/products/' +
                                 str(app_id) + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_PLAYERX + '/products/' +
                                 str(app_id) + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_PLAYERX + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_PLAYERX + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["product"]["product_name"]
                category = json["product"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["product"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["product"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["product"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["product"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["product"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='iOS',
                                 account="PlayerX", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
                    a2.name = a1.name
                    a2.downloadsA = a1.downloadsA
                    a2.downloadsT = a1.downloadsT
                    a2.downloadsW = a1.downloadsW
                    a2.downloadsM = a1.downloadsM
                    a2.revenueA = a1.revenueA
                    a2.revenueT = a1.revenueT
                    a2.revenueW = a1.revenueW
                    a2.revenueM = a1.revenueM
                    a2.save()
                except Exception as ex:
                    a1.save()

            print('PlayerX updated')


            for app_id in app_ids_ZW:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.2/apps/ios/app/' + str(app_id) + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_ZW + '/products/' +
                                 str(app_id) + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_ZW + '/products/' +
                                 str(app_id) + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_ZW + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_ZW + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["product"]["product_name"]
                category = json["product"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["product"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["product"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["product"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["product"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["product"]["downloads"]

                if name!=None:
                    a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='iOS',
                                     account="ZW", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                     revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                    try:
                        a2= Application.objects.get(appKey=app_id)
                        a2.name = a1.name
                        a2.downloadsA = a1.downloadsA
                        a2.downloadsT = a1.downloadsT
                        a2.downloadsW = a1.downloadsW
                        a2.downloadsM = a1.downloadsM
                        a2.revenueA = a1.revenueA
                        a2.revenueT = a1.revenueT
                        a2.revenueW = a1.revenueW
                        a2.revenueM = a1.revenueM
                        a2.save()
                    except Exception as ex:
                        a1.save()

            print('ZW updated')


            for app_id in app_ids_BitmonlabAndroid:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.2/apps/google-play/app/' + str(app_id) + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_BITMONLAB_ANDROID + '/products/' +
                                 str(app_id) + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_BITMONLAB_ANDROID + '/products/' +
                                 str(app_id) + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_BITMONLAB_ANDROID + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_BITMONLAB_ANDROID + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["product"]["product_name"]
                category = json["product"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["product"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["product"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["product"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["product"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["product"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='Android',
                                 account="Bitmonlab", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
                    a2.name = a1.name
                    a2.downloadsA = a1.downloadsA
                    a2.downloadsT = a1.downloadsT
                    a2.downloadsW = a1.downloadsW
                    a2.downloadsM = a1.downloadsM
                    a2.revenueA = a1.revenueA
                    a2.revenueT = a1.revenueT
                    a2.revenueW = a1.revenueW
                    a2.revenueM = a1.revenueM
                    a2.save()
                except Exception as ex:
                    a1.save()

            print('Bitmonlab Android updated')


            for app_id in app_ids_ZGPS:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.2/apps/google-play/app/' + str(app_id) + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_ZGPS + '/products/' +
                                 str(app_id) + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_ZGPS + '/products/' +
                                 str(app_id) + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_ZGPS + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_ZGPS + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["product"]["product_name"]
                category = json["product"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["product"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["product"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["product"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["product"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["product"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='Android',
                                 account="ZGPS", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
                    a2.name = a1.name
                    a2.downloadsA = a1.downloadsA
                    a2.downloadsT = a1.downloadsT
                    a2.downloadsW = a1.downloadsW
                    a2.downloadsM = a1.downloadsM
                    a2.revenueA = a1.revenueA
                    a2.revenueT = a1.revenueT
                    a2.revenueW = a1.revenueW
                    a2.revenueM = a1.revenueM
                    a2.save()
                except Exception as ex:
                    a1.save()

            print('ZGPS updated')

            for app_id in app_ids_AZW:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.2/apps/amazon-appstore/app/' + str(app_id) + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_AZW + '/products/' +
                                 str(app_id) + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_AZW + '/products/' +
                                 str(app_id) + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_AZW + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1.2/accounts/' + ACCOUNT_ID_AZW + '/products/' +
                                 str(app_id) + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["product"]["product_name"]
                downloadsA = jsonA["sales_list"][0]["units"]["product"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["product"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["product"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["product"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["product"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["product"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category='Game', downloadsA=downloadsA, os='Fire/Android',
                                 account="AZW", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
                    a2.name = a1.name
                    a2.downloadsA = a1.downloadsA
                    a2.downloadsT = a1.downloadsT
                    a2.downloadsW = a1.downloadsW
                    a2.downloadsM = a1.downloadsM
                    a2.revenueA = a1.revenueA
                    a2.revenueT = a1.revenueT
                    a2.revenueW = a1.revenueW
                    a2.revenueM = a1.revenueM
                    a2.save()
                except Exception as ex:
                    a1.save()


            print(today + ' ' + time.strftime("%H:%M:%S") + 'Database updated from appannie')

        except Exception as ex:
            print(datetime.date.today().strftime("%Y-%m-%d") + ' ' + time.strftime("%H:%M:%S"))
            print(ex)

        finally:
            time.sleep(84800)

def cleanName(name):
    appNames = {
        '2in1 Bubble Blaster': '2 in 1 Bubble Blaster',
        'beeline music': 'Beeline Music',
        'Bubble Boom Challenge 3 Free': 'Bubble Boom Challenge 3 - Free',
        'Candies City : The Battle. Join the Candy SupeFreers Troop !': 'Candies City : The Battle',
        'Candies City : The Battle. Join the Candy Supers Troop !': 'Candies City : The Battle',
        'Candies City: The Battle. Join the Candy Supers troop !': 'Candies City : The Battle',
        'Hollywood Hospital 3 - Cure your VIP patients and stay away from gossip and scandal !': 'Hollywood Hospital 3',
        'Hollywood Hospital 3 - Cure your VIP patients and stay away from gossip and scandal!': 'Hollywood Hospital 3',
        'MOBILE TV ': 'Mobile TV',
        'Zed Aywant': 'AYWANT, tu monedero en tu móvil',
        'Track Nest - Keep your family safe through your mobile and act in case your loved ones need help.': 'Track Nest',
        '2 in 1 Dragons & Demons': '2 in 1 Dragons And Demons',
        'beeinfo': 'Beeinfo'
    }

    if name in appNames:
        nameCleaned = appNames[name]
    else:
        nameCleaned = name
    return nameCleaned