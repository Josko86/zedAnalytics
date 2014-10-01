# coding=utf-8
import time
import datetime
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Analytics.models import Application
import requests
import simplejson


def index(request):

    # fillDataBase()

    aplicacionesIOS = {}
    aplicacionesAndroid = {}
    aplicacionesFlurry = {}
    aplicacionesFlurryAll = {}

    androidList = Application.objects.filter(os="android", source="appannie")
    iosList = Application.objects.filter(os="ios", source="appannie")
    flurryList = Application.objects.filter(source="flurry")

    for i in range(len(androidList)):
        app = androidList[i]
        aplicacionesAndroid[app.appKey] = []
        aplicacionesAndroid[app.appKey].append(app.name)
        aplicacionesAndroid[app.appKey].append(app.category)
        aplicacionesAndroid[app.appKey].append(app.downloads)

    for i in range(len(iosList)):
        app = iosList[i]
        aplicacionesIOS[app.appKey] = []
        aplicacionesIOS[app.appKey].append(app.name)
        aplicacionesIOS[app.appKey].append(app.category)
        aplicacionesIOS[app.appKey].append(app.downloads)

    for i in range(len(flurryList)):
        app = flurryList[i]
        aplicacionesFlurry[app.appKey] = []
        aplicacionesFlurry[app.appKey].append(app.name)
        aplicacionesFlurry[app.appKey].append(app.category)
        aplicacionesFlurry[app.appKey].append(app.downloads)
        aplicacionesFlurry[app.appKey].append(app.os)

    for d in aplicacionesFlurry:
        for e in aplicacionesFlurry:
            if (aplicacionesFlurry[d][0] == aplicacionesFlurry[e][0]) and (aplicacionesFlurry[d] != aplicacionesFlurry[e]):
                aplicacionesFlurryAll[d] = []
                aplicacionesFlurryAll[d].append(aplicacionesFlurry[d][0])
                aplicacionesFlurryAll[d].append(aplicacionesFlurry[d][1])
                aplicacionesFlurryAll[d].append(aplicacionesFlurry[d][2] + aplicacionesFlurry[e][2])
                if aplicacionesFlurryAll.has_key(d) and aplicacionesFlurryAll.has_key(e):
                    del aplicacionesFlurryAll[e]


    aplicacionesAll = aplicacionesAndroid.copy()


    ctx = {
        "aplicacionesAndroid": simplejson.dumps(aplicacionesAndroid),
        "aplicacionesIOS": simplejson.dumps(aplicacionesIOS),
        "aplicacionesAll": simplejson.dumps(aplicacionesAll),
        "aplicacionesFlurry": simplejson.dumps(aplicacionesFlurry),
        "aplicacionesFlurryAll": simplejson.dumps(aplicacionesFlurryAll)
    }

    return render_to_response('analytics/index.html', ctx, context_instance=RequestContext(request))


def fillDataBase():

    ACCOUNT_ID_IOS = "128906"
    ACCOUNT_ID_ANDROID = "128908"
    APIKEY_APPANNIE = "bearer b1df3d393ea2c4c16090f0aec1a34df0c2fb13ff"
    APIFLURRY = "5DP8FCDNCBP3XRCC9NM3"

    app_ids_ios = []
    app_ids_android = []

    aplicacionesIOS = {}
    aplicacionesAndroid = {}
    aplicacionesFlurry = {}

    #rellenar el array de las aplicaciones flurry
    flurryAppList = requests.get('http://api.flurry.com/appInfo/getAllApplications?apiAccessCode=' + APIFLURRY +
                                '&apiKey=2VYRJ826D32Z7TCS5899')
    json = simplejson.loads(flurryAppList.content)
    flurryAppList = json["application"]
    for i in range(len(flurryAppList)):
        time.sleep(1)
        apiKey = flurryAppList[i]["@apiKey"]
        r = requests.get('http://api.flurry.com/appInfo/getApplication?apiAccessCode='  + APIFLURRY +
                         '&apiKey=' + apiKey)
        json = simplejson.loads(r.content)

        createdDate = json["@createdDate"]
        today = datetime.date.today().strftime("%Y-%m-%d")
        startDate = today
        total = 0
        while (startDate>createdDate):
            endDate = startDate
            startDate = (datetime.datetime.strptime(endDate, '%Y-%m-%d') - datetime.timedelta(days=365))
            startDate = startDate.strftime("%Y-%m-%d")
            time.sleep(1)
            s = requests.get('http://api.flurry.com/appMetrics/NewUsers?apiAccessCode='  + APIFLURRY +
                           '&apiKey='+ apiKey + '&startDate=' + startDate + '&endDate=' + endDate + '&groupBy=months')
            json2 = simplejson.loads(s.content)
            for j in range(len(json2["day"])):
                total += int(json2["day"][j]["@value"])


        aplicacionesFlurry[apiKey] = []
        aplicacionesFlurry[apiKey].append(flurryAppList[i]["@name"])
        aplicacionesFlurry[apiKey].append(json["@category"])
        aplicacionesFlurry[apiKey].append(total)
        aplicacionesFlurry[apiKey].append(flurryAppList[i]["@platform"])
        a1 = Application(appKey=apiKey, name=aplicacionesFlurry[apiKey][0], category=aplicacionesFlurry[apiKey][1],
                         downloads=aplicacionesFlurry[apiKey][2], os=aplicacionesFlurry[apiKey][3], source="flurry")
        try:
            a2= Application.objects.get(appKey=apiKey)
            a2.downloads = a1.downloads
            a2.save()
        except Exception as ex:
            a1.save()


    #rellenar array de aplicaciones de cada tienda
    iosAppList = requests.get('https://api.appannie.com/v1/accounts/'+ ACCOUNT_ID_IOS +'/apps',
                         headers={"Authorization": APIKEY_APPANNIE})
    json = simplejson.loads(iosAppList.content)
    iosAppList = json["app_list"]
    for i in range(len(iosAppList)):
        app_ids_ios.append((iosAppList[i]["app_id"]))

    androidAppList = requests.get('https://api.appannie.com/v1/accounts/'+ ACCOUNT_ID_ANDROID +'/apps',
                         headers={"Authorization": APIKEY_APPANNIE})
    json = simplejson.loads(androidAppList.content)
    AndroidAppList = json["app_list"]
    for i in range(len(AndroidAppList)):
        app_ids_android.append((AndroidAppList[i]["app_id"]))

    #Crea un diccionario por cada tienda con id de aplicacion y nombre, categoría y numero de descargas
    for app_id in app_ids_ios:
        r = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_IOS + '/apps/' + app_id + '/sales',
                         headers={"Authorization": APIKEY_APPANNIE})
        json = simplejson.loads(r.content)

        s = requests.get('https://api.appannie.com/v1.1/apps/ios/app/' + app_id + '/details',
                         headers={"Authorization": APIKEY_APPANNIE})
        json2 = simplejson.loads(s.content)

        aplicacionesIOS[app_id] = []
        aplicacionesIOS[app_id].append(json2["app"]["app_name"])
        aplicacionesIOS[app_id].append(json2["app"]["main_category"])
        aplicacionesIOS[app_id].append(json["sales_list"][0]["units"]["app"]["downloads"])
        a1 = Application(appKey=app_id, name=aplicacionesIOS[app_id][0], category=aplicacionesIOS[app_id][1],
                         downloads=aplicacionesIOS[app_id][2], os='ios', source="appannie")
        try:
            a2= Application.objects.get(appKey=app_id)
            a2.downloads = a1.downloads
            a2.save()
        except Exception as ex:
            a1.save()

    for app_id in app_ids_android:
        r = requests.get('https://api.appannie.com/v1/accounts/' + ACCOUNT_ID_ANDROID + '/apps/' + app_id + '/sales',
                         headers={"Authorization": APIKEY_APPANNIE})
        json = simplejson.loads(r.content)

        s = requests.get('https://api.appannie.com/v1.1/apps/google-play/app/' + app_id + '/details',
                         headers={"Authorization": APIKEY_APPANNIE})
        json2 = simplejson.loads(s.content)

        aplicacionesAndroid[app_id] = []
        aplicacionesAndroid[app_id].append(json2["app"]["app_name"])
        aplicacionesAndroid[app_id].append(json2["app"]["main_category"])
        aplicacionesAndroid[app_id].append(json["sales_list"][0]["units"]["app"]["downloads"])
        a1 = Application(appKey=app_id, name=aplicacionesAndroid[app_id][0], category=aplicacionesAndroid[app_id][1],
                         downloads=aplicacionesAndroid[app_id][2], os='android', source="appannie")
        try:
            a2= Application.objects.get(appKey=app_id)
            a2.downloads = a1.downloads
            a2.save()
        except Exception as ex:
            a1.save()
