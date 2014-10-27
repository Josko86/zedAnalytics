# coding=utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Analytics.models import Application, Date
import simplejson
from django.http import HttpResponseRedirect

def index(request):

    aplicacionesBitmonIOS = {}
    aplicacionesBitmonAndroid = {}
    aplicacionesPyroMIOS = {}
    aplicacionesPlayerX = {}
    aplicacionesZW = {}
    aplicacionesAZW = {}
    aplicacionesZGPS = {}
    aplicacionesRUSAndroid = {}
    aplicacionesRUSiOS = {}
    aplicacionesZEDAll = {}
    aplicacionesRUSAll = {}
    aplicacionesBitmonAll = {}
    dates = {}
    # aplicacionesFlurry = {}
    # aplicacionesFlurryAll = {}

    playerXList = Application.objects.filter(account="PlayerX")
    ZWList = Application.objects.filter(account="ZW")
    ZGPSList = Application.objects.filter(account="ZGPS")
    AZWList = Application.objects.filter(account="AZW")
    RUSListAndroid = Application.objects.filter(os="Android", account="RUS")
    RUSListiOS = Application.objects.filter(os="iOS", account="RUS")
    BitmonListIOS = Application.objects.filter(os="iOS", account="Bitmonlab")
    BitmonListAndroid = Application.objects.filter(os="Android", account="Bitmonlab")
    PyroMListIOS = Application.objects.filter(os="iOS", account="PyroM")
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

    for i in range(len(BitmonListIOS)):
        app = BitmonListIOS[i]
        aplicacionesBitmonIOS[app.appKey] = []
        aplicacionesBitmonIOS[app.appKey].append(app.name)
        aplicacionesBitmonIOS[app.appKey].append(app.category)
        aplicacionesBitmonIOS[app.appKey].append(app.os)
        aplicacionesBitmonIOS[app.appKey].append(app.account)
        aplicacionesBitmonIOS[app.appKey].append(app.downloadsA)
        aplicacionesBitmonIOS[app.appKey].append(app.downloadsM)
        aplicacionesBitmonIOS[app.appKey].append(app.downloadsW)
        aplicacionesBitmonIOS[app.appKey].append(app.downloadsT)
        aplicacionesBitmonIOS[app.appKey].append(app.revenueA)
        aplicacionesBitmonIOS[app.appKey].append(app.revenueM)
        aplicacionesBitmonIOS[app.appKey].append(app.revenueW)
        aplicacionesBitmonIOS[app.appKey].append(app.revenueT)

    for i in range(len(BitmonListAndroid)):
        app = BitmonListAndroid[i]
        aplicacionesBitmonAndroid[app.appKey] = []
        aplicacionesBitmonAndroid[app.appKey].append(app.name)
        aplicacionesBitmonAndroid[app.appKey].append(app.category)
        aplicacionesBitmonAndroid[app.appKey].append(app.os)
        aplicacionesBitmonAndroid[app.appKey].append(app.account)
        aplicacionesBitmonAndroid[app.appKey].append(app.downloadsA)
        aplicacionesBitmonAndroid[app.appKey].append(app.downloadsM)
        aplicacionesBitmonAndroid[app.appKey].append(app.downloadsW)
        aplicacionesBitmonAndroid[app.appKey].append(app.downloadsT)
        aplicacionesBitmonAndroid[app.appKey].append(app.revenueA)
        aplicacionesBitmonAndroid[app.appKey].append(app.revenueM)
        aplicacionesBitmonAndroid[app.appKey].append(app.revenueW)
        aplicacionesBitmonAndroid[app.appKey].append(app.revenueT)

    for i in range(len(PyroMListIOS)):
        app = PyroMListIOS[i]
        aplicacionesPyroMIOS[app.appKey] = []
        aplicacionesPyroMIOS[app.appKey].append(app.name)
        aplicacionesPyroMIOS[app.appKey].append(app.category)
        aplicacionesPyroMIOS[app.appKey].append(app.os)
        aplicacionesPyroMIOS[app.appKey].append(app.account)
        aplicacionesPyroMIOS[app.appKey].append(app.downloadsA)
        aplicacionesPyroMIOS[app.appKey].append(app.downloadsM)
        aplicacionesPyroMIOS[app.appKey].append(app.downloadsW)
        aplicacionesPyroMIOS[app.appKey].append(app.downloadsT)
        aplicacionesPyroMIOS[app.appKey].append(app.revenueA)
        aplicacionesPyroMIOS[app.appKey].append(app.revenueM)
        aplicacionesPyroMIOS[app.appKey].append(app.revenueW)
        aplicacionesPyroMIOS[app.appKey].append(app.revenueT)

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

    #  rellenar aplicacionesZEDAll con los datos de descargas y revenue combinados
    for i in range(len(ZWList)):
        appZW = ZWList[i]
        aplicacionesZEDAll[appZW.appKey] = []
        aplicacionesZEDAll[appZW.appKey].append(appZW.name)
        aplicacionesZEDAll[appZW.appKey].append(appZW.category)
        aplicacionesZEDAll[appZW.appKey].append(appZW.os)
        aplicacionesZEDAll[appZW.appKey].append(appZW.account)
        aplicacionesZEDAll[appZW.appKey].append(appZW.downloadsA)
        aplicacionesZEDAll[appZW.appKey].append(appZW.downloadsM)
        aplicacionesZEDAll[appZW.appKey].append(appZW.downloadsW)
        aplicacionesZEDAll[appZW.appKey].append(appZW.downloadsT)
        aplicacionesZEDAll[appZW.appKey].append(appZW.revenueA)
        aplicacionesZEDAll[appZW.appKey].append(appZW.revenueM)
        aplicacionesZEDAll[appZW.appKey].append(appZW.revenueW)
        aplicacionesZEDAll[appZW.appKey].append(appZW.revenueT)

    for i in range(len(ZGPSList)):
        app = ZGPSList[i]
        aplicacionesZEDAll[app.appKey] = []
        aplicacionesZEDAll[app.appKey].append(app.name)
        aplicacionesZEDAll[app.appKey].append(app.category)
        aplicacionesZEDAll[app.appKey].append(app.os)
        aplicacionesZEDAll[app.appKey].append(app.account)
        aplicacionesZEDAll[app.appKey].append(app.downloadsA)
        aplicacionesZEDAll[app.appKey].append(app.downloadsM)
        aplicacionesZEDAll[app.appKey].append(app.downloadsW)
        aplicacionesZEDAll[app.appKey].append(app.downloadsT)
        aplicacionesZEDAll[app.appKey].append(app.revenueA)
        aplicacionesZEDAll[app.appKey].append(app.revenueM)
        aplicacionesZEDAll[app.appKey].append(app.revenueW)
        aplicacionesZEDAll[app.appKey].append(app.revenueT)

        for j in range(len(AZWList)):
            appAZW = AZWList[j]
            if appAZW.name == app.name:
                aplicacionesZEDAll[app.appKey][2] = app.os + '-' + appAZW.os
                aplicacionesZEDAll[app.appKey][4] = app.downloadsA + appAZW.downloadsA
                aplicacionesZEDAll[app.appKey][5] = app.downloadsM + appAZW.downloadsM
                aplicacionesZEDAll[app.appKey][6] = app.downloadsW + appAZW.downloadsW
                aplicacionesZEDAll[app.appKey][7] = app.downloadsT + appAZW.downloadsT
                aplicacionesZEDAll[app.appKey][8] = str(float(app.revenueA) + float(appAZW.revenueA))
                aplicacionesZEDAll[app.appKey][9] = str(float(app.revenueM) + float(appAZW.revenueM))
                aplicacionesZEDAll[app.appKey][10] = str(float(app.revenueW) + float(appAZW.revenueW))
                aplicacionesZEDAll[app.appKey][11] = str(float(app.revenueT) + float(appAZW.revenueT))
            else:
                if appAZW.name == 'Commandos' or appAZW.name == 'Animal Planet: Trivia Challenge_DE':
                    aplicacionesZEDAll[appAZW.appKey] = []
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.name)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.category)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.os)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.account)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.downloadsA)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.downloadsM)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.downloadsW)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.downloadsT)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.revenueA)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.revenueM)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.revenueW)
                    aplicacionesZEDAll[appAZW.appKey].append(appAZW.revenueT)
        for j in range(len(ZWList)):
            appZW = ZWList[j]
            if appZW.name == app.name:
                aplicacionesZEDAll[app.appKey][2] = app.os + '-' + appZW.os
                aplicacionesZEDAll[app.appKey][4] = app.downloadsA + appZW.downloadsA
                aplicacionesZEDAll[app.appKey][5] = app.downloadsM + appZW.downloadsM
                aplicacionesZEDAll[app.appKey][6] = app.downloadsW + appZW.downloadsW
                aplicacionesZEDAll[app.appKey][7] = app.downloadsT + appZW.downloadsT
                aplicacionesZEDAll[app.appKey][8] = str(float(app.revenueA) + float(appZW.revenueA))
                aplicacionesZEDAll[app.appKey][9] = str(float(app.revenueM) + float(appZW.revenueM))
                aplicacionesZEDAll[app.appKey][10] = str(float(app.revenueW) + float(appZW.revenueW))
                aplicacionesZEDAll[app.appKey][11] = str(float(app.revenueT) + float(appZW.revenueT))
                if aplicacionesZEDAll.has_key(appZW.appKey):
                    del aplicacionesZEDAll[appZW.appKey]

            for k in range(len(AZWList)):
                appAZW = AZWList[k]
                if app.name == appZW.name == appAZW.name:
                    aplicacionesZEDAll[app.appKey][2] = app.os + '-' + appZW.os + '-' + appAZW.os
                    aplicacionesZEDAll[app.appKey][4] = app.downloadsA + appZW.downloadsA + appAZW.downloadsA
                    aplicacionesZEDAll[app.appKey][5] = app.downloadsM + appZW.downloadsM + appAZW.downloadsM
                    aplicacionesZEDAll[app.appKey][6] = app.downloadsW + appZW.downloadsW + appAZW.downloadsW
                    aplicacionesZEDAll[app.appKey][7] = app.downloadsT + appZW.downloadsT + appAZW.downloadsT
                    aplicacionesZEDAll[app.appKey][8] = str(float(app.revenueA) + float(appZW.revenueA) + float(appAZW.revenueA))
                    aplicacionesZEDAll[app.appKey][9] = str(float(app.revenueM) + float(appZW.revenueM) + float(appAZW.revenueM))
                    aplicacionesZEDAll[app.appKey][10] = str(float(app.revenueW) + float(appZW.revenueW) + float(appAZW.revenueW))
                    aplicacionesZEDAll[app.appKey][11] = str(float(app.revenueT) + float(appZW.revenueT) + float(appAZW.revenueT))

    # Rellenar aplicacionesRUSALL con los datos combinados
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

    # rellenar BitmonAll con los datos combinados
    for i in range(len(BitmonListAndroid)):
        appAnd = BitmonListAndroid[i]
        aplicacionesBitmonAll[appAnd.appKey] = []
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.name)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.category)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.os)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.account)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.downloadsA)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.downloadsM)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.downloadsW)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.downloadsT)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.revenueA)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.revenueM)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.revenueW)
        aplicacionesBitmonAll[appAnd.appKey].append(appAnd.revenueT)

        for j in range(len(BitmonListIOS)):
            appIOS = BitmonListIOS[j]
            if appAnd.name == appIOS.name:
                aplicacionesBitmonAll[appAnd.appKey][2] = appAnd.os + '-' + appIOS.os
                aplicacionesBitmonAll[appAnd.appKey][4] = appAnd.downloadsA + appIOS.downloadsA
                aplicacionesBitmonAll[appAnd.appKey][5] = appAnd.downloadsM + appIOS.downloadsM
                aplicacionesBitmonAll[appAnd.appKey][6] = appAnd.downloadsW + appIOS.downloadsW
                aplicacionesBitmonAll[appAnd.appKey][7] = appAnd.downloadsT + appIOS.downloadsT
                aplicacionesBitmonAll[appAnd.appKey][8] = str(float(appAnd.revenueA) + float(appIOS.revenueA))
                aplicacionesBitmonAll[appAnd.appKey][9] = str(float(appAnd.revenueM) + float(appIOS.revenueM))
                aplicacionesBitmonAll[appAnd.appKey][10] = str(float(appAnd.revenueW) + float(appIOS.revenueW))
                aplicacionesBitmonAll[appAnd.appKey][11] = str(float(appAnd.revenueT) + float(appIOS.revenueT))

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
        "aplicacionesZEDAll": simplejson.dumps(aplicacionesZEDAll),
        "aplicacionesRUSAll": simplejson.dumps(aplicacionesRUSAll),
        "aplicacionesBitmonIOS": simplejson.dumps(aplicacionesBitmonIOS),
        "aplicacionesBitmonAndroid": simplejson.dumps(aplicacionesBitmonAndroid),
        "aplicacionesBitmonAll": simplejson.dumps(aplicacionesBitmonAll),
        "aplicacionesPyroMIOS": simplejson.dumps(aplicacionesPyroMIOS),
        "dateExcel": dates["excel"],
        "dateAppannie": dates["appannie"]
        # "aplicacionesFlurry": simplejson.dumps(aplicacionesFlurry),
        # "aplicacionesFlurryAll": simplejson.dumps(aplicacionesFlurryAll)
    }

    return render_to_response('analytics/index.html', ctx, context_instance=RequestContext(request))

def save_file(request):
    import os
    from django.core.urlresolvers import reverse

    exists = False
    file_path = os.path.join('rusia.xlsx')
    if os.path.isfile(file_path):
        os.remove(os.path.join('rusia.xlsx'))

    input_file = request.FILES['file'].file

    temp_file_path = file_path + '~'
    output_file = open(temp_file_path, 'wb')

    input_file.seek(0)
    while True:
        data = input_file.read(2<<16)
        if not data:
            break
        output_file.write(data)

    output_file.close()
    os.rename(temp_file_path, file_path)

    if os.path.isfile(file_path):
        exists = True

    url = reverse('index')

    return HttpResponseRedirect(url)

