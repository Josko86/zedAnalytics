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

            ACCOUNT_ID_PLAYERX = "173012"
            ACCOUNT_ID_ZW = "39230"
            ACCOUNT_ID_ZGPS = "46490"
            ACCOUNT_ID_AZW = "173002"
            APIKEY_APPANNIE = "bearer 5dba15b181bd108344478ee985a7e0b737562377"

            app_ids_PlayerX = []
            app_ids_ZW = []
            app_ids_ZGPS = []
            app_ids_AZW = []
            lastDateExcel = "unknown"

            # Recoger datos del excel rusia xlsx
            try:
                book = xlrd.open_workbook('rusia.xlsx')
                sheet = book.sheet_by_name('Android market overall')
                num_cells = sheet.ncols - 1
                curr_row = 1

                lastDateExcel = (datetime.datetime.strptime('1899-12-30', '%Y-%m-%d') +
                                     datetime.timedelta(days=sheet.cell_value(1, num_cells))).strftime("%Y-%m-%d")

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
                        cell_type = sheet.cell_type(curr_row, curr_cell)
                        cell_value = sheet.cell_value(curr_row, curr_cell)
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
                        cell_type = sheet.cell_type(curr_row, curr_cell)
                        cell_value = sheet.cell_value(curr_row, curr_cell)
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
            PlayerXAppList = requests.get('https://api.appannie.com/v1/accounts/'+ ACCOUNT_ID_PLAYERX +'/apps',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(PlayerXAppList.content)
            PlayerXAppList = json["app_list"]
            for i in range(len(PlayerXAppList)):
                if PlayerXAppList[i]['status']:
                    app_ids_PlayerX.append((PlayerXAppList[i]["app_id"]))

            ZWAppList = requests.get('https://api.appannie.com/v1/accounts/'+ ACCOUNT_ID_ZW +'/apps',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(ZWAppList.content)
            ZWAppList = json["app_list"]
            for i in range(len(ZWAppList)):
                if ZWAppList[i]['status'] and (len(ZWAppList[i]['devices'])>0):
                    app_ids_ZW.append((ZWAppList[i]["app_id"]))

            ZGPSAppList = requests.get('https://api.appannie.com/v1/accounts/'+ ACCOUNT_ID_ZGPS +'/apps',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(ZGPSAppList.content)
            ZGPSAppList = json["app_list"]
            for i in range(len(ZGPSAppList)):
                if ZGPSAppList[i]['status']:
                    app_ids_ZGPS.append((ZGPSAppList[i]["app_id"]))

            AZWAppList = requests.get('https://api.appannie.com/v1/accounts/'+ ACCOUNT_ID_AZW +'/apps',
                                 headers={"Authorization": APIKEY_APPANNIE})
            json = simplejson.loads(AZWAppList.content)
            AZWAppList = json["app_list"]
            for i in range(len(AZWAppList)):
                if AZWAppList[i]['status']:
                    app_ids_AZW.append((AZWAppList[i]["app_id"]))

            time.sleep(8)

            #Crea un diccionario por cada tienda con id de aplicacion y nombre, categoria y numero de descargas, y revenues
            for app_id in app_ids_PlayerX:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.1/apps/ios/app/' + app_id + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_PLAYERX + '/apps/' +
                                 app_id + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_PLAYERX + '/apps/' +
                                 app_id + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_PLAYERX + '/apps/' +
                                 app_id + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_PLAYERX + '/apps/' +
                                 app_id + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["app"]["app_name"]
                category = json["app"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["app"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["app"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["app"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["app"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["app"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='iOS',
                                 account="PlayerX", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
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

            for app_id in app_ids_ZW:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.1/apps/ios/app/' + app_id + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ZW + '/apps/' +
                                 app_id + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ZW + '/apps/' +
                                 app_id + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ZW + '/apps/' +
                                 app_id + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ZW + '/apps/' +
                                 app_id + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["app"]["app_name"]
                category = json["app"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["app"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["app"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["app"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["app"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["app"]["downloads"]

                if name!=None:
                    a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='iOS',
                                     account="ZW", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                     revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                    try:
                        a2= Application.objects.get(appKey=app_id)
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

            for app_id in app_ids_ZGPS:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.1/apps/google-play/app/' + app_id + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ZGPS + '/apps/' +
                                 app_id + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ZGPS + '/apps/' +
                                 app_id + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ZGPS + '/apps/' +
                                 app_id + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ZGPS + '/apps/' +
                                 app_id + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["app"]["app_name"]
                category = json["app"]["main_category"]
                downloadsA = jsonA["sales_list"][0]["units"]["app"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["app"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["app"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["app"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["app"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category=category, downloadsA=downloadsA, os='Android',
                                 account="ZGPS", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
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

            for app_id in app_ids_AZW:

                time.sleep(10)
                r = requests.get('https://api.appannie.com/v1.1/apps/amazon-appstore/app/' + app_id + '/details',
                                 headers={"Authorization": APIKEY_APPANNIE})
                json = simplejson.loads(r.content)

                s = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_AZW + '/apps/' +
                                 app_id + '/sales', headers={"Authorization": APIKEY_APPANNIE})
                jsonA = simplejson.loads(s.content)

                t = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_AZW + '/apps/' +
                                 app_id + '/sales?start_date='+yesterday, headers={"Authorization": APIKEY_APPANNIE})
                jsonY = simplejson.loads(t.content)

                u = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_AZW + '/apps/' +
                                 app_id + '/sales?start_date='+lastWeek, headers={"Authorization": APIKEY_APPANNIE})
                jsonW = simplejson.loads(u.content)

                v = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_AZW + '/apps/' +
                                 app_id + '/sales?start_date='+lastMonth, headers={"Authorization": APIKEY_APPANNIE})
                jsonM = simplejson.loads(v.content)

                name = json["app"]["app_name"]
                downloadsA = jsonA["sales_list"][0]["units"]["app"]["downloads"]
                downloadsM = jsonM["sales_list"][0]["units"]["app"]["downloads"]
                downloadsW = jsonW["sales_list"][0]["units"]["app"]["downloads"]
                downloadsY = jsonY["sales_list"][0]["units"]["app"]["downloads"]
                revenueA = jsonA["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueM = jsonM["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueW = jsonW["sales_list"][0]["revenue"]["app"]["downloads"]
                revenueY = jsonY["sales_list"][0]["revenue"]["app"]["downloads"]

                a1 = Application(appKey=app_id, name=cleanName(name), category='Game', downloadsA=downloadsA, os='Fire/Android',
                                 account="AZW", downloadsM=downloadsM, downloadsW=downloadsW, downloadsT=downloadsY,
                                 revenueA=revenueA, revenueM=revenueM, revenueW=revenueW, revenueT=revenueY)
                try:
                    a2= Application.objects.get(appKey=app_id)
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


            print('Database updated from appannie')

        except Exception as ex:
            print(ex)

        finally:
            time.sleep(1)

def cleanName(name):
    appNames = {
        '2in1 Bubble Blaster': '2 in 1 Bubble Blaster',
        'beeline music': 'Beeline Music',
        'Bubble Boom Challenge 3 Free': 'Bubble Boom Challenge 3 - Free',
        'Candies City : The Battle. Join the Candy SupeFreers Troop !': 'Candies City : The Battle',
        'Candies City : The Battle. Join the Candy Supers Troop !': 'Candies City : The Battle',
        'Hollywood Hospital 3 - Cure your VIP patients and stay away from gossip and scandal !': 'Hollywood Hospital 3',
        'Hollywood Hospital 3 - Cure your VIP patients and stay away from gossip and scandal!': 'Hollywood Hospital 3',
        'MOBILE TV ': 'Mobile TV',
        'Track Nest - Keep your family safe through your mobile and act in case your loved ones need help.': 'Track Nest',
        '2 in 1 Dragons & Demons': '2 in 1 Dragons And Demons',
        'beeinfo': 'Beeinfo'
    }

    if name in appNames:
        nameCleaned = appNames[name]
    else:
        nameCleaned = name
    return nameCleaned