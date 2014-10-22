# coding=utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Analytics.models import Application, Date
import simplejson


def index(request):


    aplicacionesPlayerX = {}
    aplicacionesZW = {}
    aplicacionesAZW = {}
    aplicacionesZGPS = {}
    aplicacionesRUSAndroid = {}
    aplicacionesRUSiOS = {}
    aplicacionesAll = {}
    aplicacionesRUSAll = {}
    dates = {}
    # aplicacionesFlurry = {}
    # aplicacionesFlurryAll = {}

    playerXList = Application.objects.filter(account="PlayerX")
    ZWList = Application.objects.filter(account="ZW")
    ZGPSList = Application.objects.filter(account="ZGPS")
    AZWList = Application.objects.filter(account="AZW")
    RUSListAndroid = Application.objects.filter(os="Android", account="RUS")
    RUSListiOS = Application.objects.filter(os="iOS", account="RUS")
    datesList = Date.objects.filter(id=1)
    # flurryList = Application.objects.filter(account="flurry")

    for i in range(len(datesList)):
        date = datesList[i]
        dates["excel"] = date.dateExcel
        dates["appannie"] = date.dateAppannie

    for i in range(len(playerXList)):
        app = playerXList[i]
        aplicacionesPlayerX[app.appKey] = []
        aplicacionesPlayerX[app.appKey].append(app.name)
        aplicacionesPlayerX[app.appKey].append(app.category)
        aplicacionesPlayerX[app.appKey].append(app.os)
        aplicacionesPlayerX[app.appKey].append(app.account)
        aplicacionesPlayerX[app.appKey].append(app.downloadsA)
        aplicacionesPlayerX[app.appKey].append(app.downloadsM)
        aplicacionesPlayerX[app.appKey].append(app.downloadsW)
        aplicacionesPlayerX[app.appKey].append(app.downloadsT)
        aplicacionesPlayerX[app.appKey].append(app.revenueA)
        aplicacionesPlayerX[app.appKey].append(app.revenueM)
        aplicacionesPlayerX[app.appKey].append(app.revenueW)
        aplicacionesPlayerX[app.appKey].append(app.revenueT)

    for i in range(len(ZWList)):
        app = ZWList[i]
        aplicacionesZW[app.appKey] = []
        aplicacionesZW[app.appKey].append(app.name)
        aplicacionesZW[app.appKey].append(app.category)
        aplicacionesZW[app.appKey].append(app.os)
        aplicacionesZW[app.appKey].append(app.account)
        aplicacionesZW[app.appKey].append(app.downloadsA)
        aplicacionesZW[app.appKey].append(app.downloadsM)
        aplicacionesZW[app.appKey].append(app.downloadsW)
        aplicacionesZW[app.appKey].append(app.downloadsT)
        aplicacionesZW[app.appKey].append(app.revenueA)
        aplicacionesZW[app.appKey].append(app.revenueM)
        aplicacionesZW[app.appKey].append(app.revenueW)
        aplicacionesZW[app.appKey].append(app.revenueT)

    for i in range(len(ZGPSList)):
        app = ZGPSList[i]
        aplicacionesZGPS[app.appKey] = []
        aplicacionesZGPS[app.appKey].append(app.name)
        aplicacionesZGPS[app.appKey].append(app.category)
        aplicacionesZGPS[app.appKey].append(app.os)
        aplicacionesZGPS[app.appKey].append(app.account)
        aplicacionesZGPS[app.appKey].append(app.downloadsA)
        aplicacionesZGPS[app.appKey].append(app.downloadsM)
        aplicacionesZGPS[app.appKey].append(app.downloadsW)
        aplicacionesZGPS[app.appKey].append(app.downloadsT)
        aplicacionesZGPS[app.appKey].append(app.revenueA)
        aplicacionesZGPS[app.appKey].append(app.revenueM)
        aplicacionesZGPS[app.appKey].append(app.revenueW)
        aplicacionesZGPS[app.appKey].append(app.revenueT)

    for i in range(len(AZWList)):
        app = AZWList[i]
        aplicacionesAZW[app.appKey] = []
        aplicacionesAZW[app.appKey].append(app.name)
        aplicacionesAZW[app.appKey].append(app.category)
        aplicacionesAZW[app.appKey].append(app.os)
        aplicacionesAZW[app.appKey].append(app.account)
        aplicacionesAZW[app.appKey].append(app.downloadsA)
        aplicacionesAZW[app.appKey].append(app.downloadsM)
        aplicacionesAZW[app.appKey].append(app.downloadsW)
        aplicacionesAZW[app.appKey].append(app.downloadsT)
        aplicacionesAZW[app.appKey].append(app.revenueA)
        aplicacionesAZW[app.appKey].append(app.revenueM)
        aplicacionesAZW[app.appKey].append(app.revenueW)
        aplicacionesAZW[app.appKey].append(app.revenueT)

    for i in range(len(RUSListAndroid)):
        app = RUSListAndroid[i]
        aplicacionesRUSAndroid[app.appKey] = []
        aplicacionesRUSAndroid[app.appKey].append(app.name)
        aplicacionesRUSAndroid[app.appKey].append(app.category)
        aplicacionesRUSAndroid[app.appKey].append(app.os)
        aplicacionesRUSAndroid[app.appKey].append(app.account)
        aplicacionesRUSAndroid[app.appKey].append(app.downloadsA)
        aplicacionesRUSAndroid[app.appKey].append(app.downloadsM)
        aplicacionesRUSAndroid[app.appKey].append(app.downloadsW)
        aplicacionesRUSAndroid[app.appKey].append(app.downloadsT)
        aplicacionesRUSAndroid[app.appKey].append(app.revenueA)
        aplicacionesRUSAndroid[app.appKey].append(app.revenueM)
        aplicacionesRUSAndroid[app.appKey].append(app.revenueW)
        aplicacionesRUSAndroid[app.appKey].append(app.revenueT)

    for i in range(len(RUSListiOS)):
        app = RUSListiOS[i]
        aplicacionesRUSiOS[app.appKey] = []
        aplicacionesRUSiOS[app.appKey].append(app.name)
        aplicacionesRUSiOS[app.appKey].append(app.category)
        aplicacionesRUSiOS[app.appKey].append(app.os)
        aplicacionesRUSiOS[app.appKey].append(app.account)
        aplicacionesRUSiOS[app.appKey].append(app.downloadsA)
        aplicacionesRUSiOS[app.appKey].append(app.downloadsM)
        aplicacionesRUSiOS[app.appKey].append(app.downloadsW)
        aplicacionesRUSiOS[app.appKey].append(app.downloadsT)
        aplicacionesRUSiOS[app.appKey].append(app.revenueA)
        aplicacionesRUSiOS[app.appKey].append(app.revenueM)
        aplicacionesRUSiOS[app.appKey].append(app.revenueW)
        aplicacionesRUSiOS[app.appKey].append(app.revenueT)

    #  rellenar aplicacionesAll con los datos de descargas y revenue combinados
    for i in range(len(playerXList)):
        app = playerXList[i]
        aplicacionesAll[app.appKey] = []
        aplicacionesAll[app.appKey].append(app.name)
        aplicacionesAll[app.appKey].append(app.category)
        aplicacionesAll[app.appKey].append(app.os)
        aplicacionesAll[app.appKey].append(app.account)
        aplicacionesAll[app.appKey].append(app.downloadsA)
        aplicacionesAll[app.appKey].append(app.downloadsM)
        aplicacionesAll[app.appKey].append(app.downloadsW)
        aplicacionesAll[app.appKey].append(app.downloadsT)
        aplicacionesAll[app.appKey].append(app.revenueA)
        aplicacionesAll[app.appKey].append(app.revenueM)
        aplicacionesAll[app.appKey].append(app.revenueW)
        aplicacionesAll[app.appKey].append(app.revenueT)

    for i in range(len(ZWList)):
        appZW = ZWList[i]
        aplicacionesAll[appZW.appKey] = []
        aplicacionesAll[appZW.appKey].append(appZW.name)
        aplicacionesAll[appZW.appKey].append(appZW.category)
        aplicacionesAll[appZW.appKey].append(appZW.os)
        aplicacionesAll[appZW.appKey].append(appZW.account)
        aplicacionesAll[appZW.appKey].append(appZW.downloadsA)
        aplicacionesAll[appZW.appKey].append(appZW.downloadsM)
        aplicacionesAll[appZW.appKey].append(appZW.downloadsW)
        aplicacionesAll[appZW.appKey].append(appZW.downloadsT)
        aplicacionesAll[appZW.appKey].append(appZW.revenueA)
        aplicacionesAll[appZW.appKey].append(appZW.revenueM)
        aplicacionesAll[appZW.appKey].append(appZW.revenueW)
        aplicacionesAll[appZW.appKey].append(appZW.revenueT)

    for i in range(len(ZGPSList)):
        app = ZGPSList[i]
        aplicacionesAll[app.appKey] = []
        aplicacionesAll[app.appKey].append(app.name)
        aplicacionesAll[app.appKey].append(app.category)
        aplicacionesAll[app.appKey].append(app.os)
        aplicacionesAll[app.appKey].append(app.account)
        aplicacionesAll[app.appKey].append(app.downloadsA)
        aplicacionesAll[app.appKey].append(app.downloadsM)
        aplicacionesAll[app.appKey].append(app.downloadsW)
        aplicacionesAll[app.appKey].append(app.downloadsT)
        aplicacionesAll[app.appKey].append(app.revenueA)
        aplicacionesAll[app.appKey].append(app.revenueM)
        aplicacionesAll[app.appKey].append(app.revenueW)
        aplicacionesAll[app.appKey].append(app.revenueT)

        for j in range(len(AZWList)):
            appAZW = AZWList[j]
            if appAZW.name == app.name:
                aplicacionesAll[app.appKey][2] = app.os + '-' + appAZW.os
                aplicacionesAll[app.appKey][4] = app.downloadsA + appAZW.downloadsA
                aplicacionesAll[app.appKey][5] = app.downloadsM + appAZW.downloadsM
                aplicacionesAll[app.appKey][6] = app.downloadsW + appAZW.downloadsW
                aplicacionesAll[app.appKey][7] = app.downloadsT + appAZW.downloadsT
                aplicacionesAll[app.appKey][8] = str(float(app.revenueA) + float(appAZW.revenueA))
                aplicacionesAll[app.appKey][9] = str(float(app.revenueM) + float(appAZW.revenueM))
                aplicacionesAll[app.appKey][10] = str(float(app.revenueW) + float(appAZW.revenueW))
                aplicacionesAll[app.appKey][11] = str(float(app.revenueT) + float(appAZW.revenueT))
            else:
                if appAZW.name == 'Commandos' or appAZW.name == 'Animal Planet: Trivia Challenge_DE':
                    aplicacionesAll[appAZW.appKey] = []
                    aplicacionesAll[appAZW.appKey].append(appAZW.name)
                    aplicacionesAll[appAZW.appKey].append(appAZW.category)
                    aplicacionesAll[appAZW.appKey].append(appAZW.os)
                    aplicacionesAll[appAZW.appKey].append(appAZW.account)
                    aplicacionesAll[appAZW.appKey].append(appAZW.downloadsA)
                    aplicacionesAll[appAZW.appKey].append(appAZW.downloadsM)
                    aplicacionesAll[appAZW.appKey].append(appAZW.downloadsW)
                    aplicacionesAll[appAZW.appKey].append(appAZW.downloadsT)
                    aplicacionesAll[appAZW.appKey].append(appAZW.revenueA)
                    aplicacionesAll[appAZW.appKey].append(appAZW.revenueM)
                    aplicacionesAll[appAZW.appKey].append(appAZW.revenueW)
                    aplicacionesAll[appAZW.appKey].append(appAZW.revenueT)
        for j in range(len(ZWList)):
            appZW = ZWList[j]
            if appZW.name == app.name:
                aplicacionesAll[app.appKey][2] = app.os + '-' + appZW.os
                aplicacionesAll[app.appKey][4] = app.downloadsA + appZW.downloadsA
                aplicacionesAll[app.appKey][5] = app.downloadsM + appZW.downloadsM
                aplicacionesAll[app.appKey][6] = app.downloadsW + appZW.downloadsW
                aplicacionesAll[app.appKey][7] = app.downloadsT + appZW.downloadsT
                aplicacionesAll[app.appKey][8] = str(float(app.revenueA) + float(appZW.revenueA))
                aplicacionesAll[app.appKey][9] = str(float(app.revenueM) + float(appZW.revenueM))
                aplicacionesAll[app.appKey][10] = str(float(app.revenueW) + float(appZW.revenueW))
                aplicacionesAll[app.appKey][11] = str(float(app.revenueT) + float(appZW.revenueT))
                del aplicacionesAll[appZW.appKey]

            for k in range(len(AZWList)):
                appAZW = AZWList[k]
                if app.name == appZW.name == appAZW.name:
                    aplicacionesAll[app.appKey][2] = app.os + '-' + appZW.os + '-' + appAZW.os
                    aplicacionesAll[app.appKey][4] = app.downloadsA + appZW.downloadsA + appAZW.downloadsA
                    aplicacionesAll[app.appKey][5] = app.downloadsM + appZW.downloadsM + appAZW.downloadsM
                    aplicacionesAll[app.appKey][6] = app.downloadsW + appZW.downloadsW + appAZW.downloadsW
                    aplicacionesAll[app.appKey][7] = app.downloadsT + appZW.downloadsT + appAZW.downloadsT
                    aplicacionesAll[app.appKey][8] = str(float(app.revenueA) + float(appZW.revenueA) + float(appAZW.revenueA))
                    aplicacionesAll[app.appKey][9] = str(float(app.revenueM) + float(appZW.revenueM) + float(appAZW.revenueM))
                    aplicacionesAll[app.appKey][10] = str(float(app.revenueW) + float(appZW.revenueW) + float(appAZW.revenueW))
                    aplicacionesAll[app.appKey][11] = str(float(app.revenueT) + float(appZW.revenueT) + float(appAZW.revenueT))

    for i in range(len(RUSListAndroid)):
        appAnd = RUSListAndroid[i]
        aplicacionesRUSAll[appAnd.appKey] = []
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.name)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.category)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.os)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.account)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.downloadsA)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.downloadsM)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.downloadsW)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.downloadsT)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.revenueA)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.revenueM)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.revenueW)
        aplicacionesRUSAll[appAnd.appKey].append(appAnd.revenueT)

        for j in range(len(RUSListiOS)):
            appIOS = RUSListiOS[j]
            if appAnd.name == appIOS.name:
                aplicacionesRUSAll[appAnd.appKey][2] = appAnd.os + '-' + appIOS.os
                aplicacionesRUSAll[appAnd.appKey][4] = appAnd.downloadsA + appIOS.downloadsA
                aplicacionesRUSAll[appAnd.appKey][5] = appAnd.downloadsM + appIOS.downloadsM
                aplicacionesRUSAll[appAnd.appKey][6] = appAnd.downloadsW + appIOS.downloadsW
                aplicacionesRUSAll[appAnd.appKey][7] = appAnd.downloadsT + appIOS.downloadsT
                aplicacionesRUSAll[appAnd.appKey][8] = str(float(appAnd.revenueA) + float(appIOS.revenueA))
                aplicacionesRUSAll[appAnd.appKey][9] = str(float(appAnd.revenueM) + float(appIOS.revenueM))
                aplicacionesRUSAll[appAnd.appKey][10] = str(float(appAnd.revenueW) + float(appIOS.revenueW))
                aplicacionesRUSAll[appAnd.appKey][11] = str(float(appAnd.revenueT) + float(appIOS.revenueT))


    # for i in range(len(flurryList)):
    #     app = flurryList[i]
    #     aplicacionesFlurry[app.appKey] = []
    #     aplicacionesFlurry[app.appKey].append(app.name)
    #     aplicacionesFlurry[app.appKey].append(app.category)
    #     aplicacionesFlurry[app.appKey].append(app.downloads)
    #     aplicacionesFlurry[app.appKey].append(app.os)
    #
    # for d in aplicacionesFlurry:
    #     for e in aplicacionesFlurry:
    #         if (aplicacionesFlurry[d][0] == aplicacionesFlurry[e][0]) and (aplicacionesFlurry[d] != aplicacionesFlurry[e]):
    #             aplicacionesFlurryAll[d] = []
    #             aplicacionesFlurryAll[d].append(aplicacionesFlurry[d][0])
    #             aplicacionesFlurryAll[d].append(aplicacionesFlurry[d][1])
    #             aplicacionesFlurryAll[d].append(aplicacionesFlurry[d][2] + aplicacionesFlurry[e][2])
    #             if aplicacionesFlurryAll.has_key(d) and aplicacionesFlurryAll.has_key(e):
    #                 del aplicacionesFlurryAll[e]


    # aplicacionesAll = aplicacionesAndroid.copy()


    ctx = {
        "aplicacionesPlayerX": simplejson.dumps(aplicacionesPlayerX),
        "aplicacionesZW": simplejson.dumps(aplicacionesZW),
        "aplicacionesZGPS": simplejson.dumps(aplicacionesZGPS),
        "aplicacionesAZW": simplejson.dumps(aplicacionesAZW),
        "aplicacionesRUSAndroid": simplejson.dumps(aplicacionesRUSAndroid),
        "aplicacionesRUSiOS": simplejson.dumps(aplicacionesRUSiOS),
        "aplicacionesAll": simplejson.dumps(aplicacionesAll),
        "aplicacionesRUSAll": simplejson.dumps(aplicacionesRUSAll),
        "dateExcel": dates["excel"],
        "dateAppannie": dates["appannie"]
        # "aplicacionesFlurry": simplejson.dumps(aplicacionesFlurry),
        # "aplicacionesFlurryAll": simplejson.dumps(aplicacionesFlurryAll)
    }

    return render_to_response('analytics/index.html', ctx, context_instance=RequestContext(request))
