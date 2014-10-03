# coding=utf-8
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from Analytics.models import Application
import simplejson


def index(request):


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
