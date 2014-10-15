# coding=utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Analytics.models import Application
import simplejson


def index(request):


    aplicacionesPlayerX = {}
    aplicacionesZW = {}
    aplicacionesAZW = {}
    aplicacionesZGPS = {}
    aplicacionesFlurry = {}
    aplicacionesFlurryAll = {}

    playerXList = Application.objects.filter(account="PlayerX")
    ZWList = Application.objects.filter(account="ZW")
    ZGPSList = Application.objects.filter(account="ZGPS")
    AZWList = Application.objects.filter(account="AZW")
    # flurryList = Application.objects.filter(account="flurry")

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
        # "aplicacionesFlurry": simplejson.dumps(aplicacionesFlurry),
        # "aplicacionesFlurryAll": simplejson.dumps(aplicacionesFlurryAll)
    }

    return render_to_response('analytics/index.html', ctx, context_instance=RequestContext(request))
