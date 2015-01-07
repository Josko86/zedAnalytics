/**
 * Created with PyCharm.
 * User: Josko
 * Date: 17/09/14
 * Time: 14:48
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function(){
    //busca las aplicaciones con el mismo nombre y suma las descargas
    playerXKeys = Object.keys(appsPlayerX);
    ZWKeys = Object.keys(appsZW);
    ZGPSKeys = Object.keys(appsZGPS);
    AZWKeys = Object.keys(appsAZW);
    RUSAndroidKeys = Object.keys(appsRUSAndroid);
    RUSiOSKeys = Object.keys(appsRUSiOS);
    ZEDAllKeys = Object.keys(appsZEDAll);
    RUSAllKeys = Object.keys(appsRUSAll);
    BitmoniOSKeys = Object.keys(appsBitmonIOS);
    BitmonAndroidKeys = Object.keys(appsBitmonAndroid);
    BitmonAllKeys = Object.keys(appsBitmonAll);
    PyroMIOSKeys = Object.keys(appsPyroMIOS);
//    flurryKeys = Object.keys(appsFlurry);
//    flurryAllKeys = Object.keys(appsFlurryAll);
//    for (var k in androidKeys){
//        if (androidKeys.hasOwnProperty(k)) {
//            for (var j in iosKeys){
//                if (iosKeys.hasOwnProperty(j)) {
//                    if (appsIOS[iosKeys[j]][0].toLowerCase().indexOf(appsAndroid[androidKeys[k]][0].toLowerCase())> -1){
//                        appsAll[androidKeys[k]][2] = appsIOS[iosKeys[j]][2] + appsAndroid[androidKeys[k]][2];
//                    }
//                }
//            }
//        }
//    }
    createTable();
    totalDownloads = 0;
    totalRevenue = 0;
    totalDownloadIOS = 0;
    totalDownloadAndroid = 0;
    totalRevenueIOS = 0;
    totalRevenueAndroid = 0;
    totalRevenuesArray = [];
    totalDownloadsArray = [];
    before = 0;

    showAllCat(ZEDAllKeys,appsZEDAll, 4);
    showAllCat(RUSAllKeys,appsRUSAll, 4);
    showAllCat(playerXKeys, appsPlayerX, 4);
    showAllCat(BitmonAllKeys,appsBitmonAll, 4);
    showAllCat(PyroMIOSKeys,appsPyroMIOS, 4);

    addTotal();

    $('#canvas1').hide();
    $('#canvas2').hide();
    $('#canvas3').hide();
    $('#canvas4').hide();
    miTabla.appendChild(tbBody);
    miCapa = document.getElementById('resultado');
    miCapa.appendChild(miTabla);
//    crear parser para ordenar la tabla sin tener en cuenta puntos y comas
    $.tablesorter.addParser({
        id: 'downloads',
        is: function(s){
            s = s.replace('.','');
            return parseInt(s)
        },
        format: function(s){
            s = s.replace('.','');
            return parseInt(s)
        },
        type: 'numeric'
    });
    $.tablesorter.addParser({
        id: 'revenue',
        is: function(s){
            s = s.replace('.','');
            s = s.replace(',','.');
            return parseFloat(s)
        },
        format: function(s){
            s = s.replace('.','');
            s = s.replace(',','.');
            return parseFloat(s)
        },
        type: 'numeric'
    });
    $(".table").tablesorter({
        headers: {
            2: {
                sorter: 'downloads'
            },
            3: {
                sorter: 'revenue'
            }
        },
        widgets: ['staticRow']
	});
    totalRevenuesArray.sort(function(a,b) { return b.value - a.value;});
    totalDownloadsArray.sort(function(a,b) { return b.value - a.value;});
    crearGraficos(totalDownloadIOS, totalDownloadAndroid, totalRevenueIOS, totalRevenueAndroid, totalRevenuesArray, totalDownloadsArray);

});

function verEstadisticas(){

//    Reiniciamos la tabla y los valores de los totales
    if ($(".table")){
        $(".table").remove();
    }
    totalDownloads = 0;
    totalRevenue = 0;
    totalDownloadIOS = 0;
    totalDownloadAndroid = 0;
    totalRevenueIOS = 0;
    totalRevenueAndroid = 0;
    totalRevenuesArray = [];
    totalDownloadsArray = [];
    before = 0;

    allAccount= $("#allAccount").is(':checked');
    playerX= $("#playerX").is(':checked');
    bitmon= $("#bitmon").is(':checked');
    pyro= $("#pyro").is(':checked');
    zed= $("#zed").is(':checked');
    rus= $("#RUS").is(':checked');

    time = 4;
    if ( $("#month").is(':checked')){
        time++;
        before = 30;
    }else if ( $("#week").is(':checked')){
        time = time + 2;
        before = 7;
    }else if ( $("#day").is(':checked')){
        time = time + 3;
        before = 1;
    }
    createTable();

    if( $("#combined").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if (allAccount){
                showAllCat(playerXKeys,appsPlayerX, time);
                showAllCat(ZEDAllKeys,appsZEDAll, time);
                showAllCat(RUSAllKeys,appsRUSAll, time);
                showAllCat(BitmonAllKeys,appsBitmonAll, time);
                showAllCat(PyroMIOSKeys,appsPyroMIOS, time);
            }
            if (playerX) showAllCat(playerXKeys, appsPlayerX, time);
            if (bitmon) showAllCat(BitmonAllKeys,appsBitmonAll, time);
            if (pyro) showAllCat(PyroMIOSKeys,appsPyroMIOS, time);
            if (zed) showAllCat(ZEDAllKeys,appsZEDAll, time);
            if (rus) showAllCat(RUSAllKeys,appsRUSAll, time);
        }
        else if($("#games").is(':checked')){
            if (allAccount){
                showGames(playerXKeys,appsPlayerX, time);
                showGames(ZEDAllKeys,appsZEDAll, time);
                showGames(RUSAllKeys,appsRUSAll, time);
                showGames(BitmonAllKeys,appsBitmonAll, time);
                showGames(PyroMIOSKeys,appsPyroMIOS, time);
            }
            if (playerX) showGames(playerXKeys, appsPlayerX, time);
            if (bitmon) showGames(BitmonAllKeys,appsBitmonAll, time);
            if (pyro) showGames(PyroMIOSKeys,appsPyroMIOS, time);
            if (zed) showGames(ZEDAllKeys,appsZEDAll, time);
            if (rus) showGames(RUSAllKeys,appsRUSAll, time);
        }
        else{
            if (allAccount){
                showOthers(playerXKeys,appsPlayerX, time);
                showOthers(ZEDAllKeys,appsZEDAll, time);
                showOthers(RUSAllKeys,appsRUSAll, time);
                showOthers(BitmonAllKeys,appsBitmonAll, time);
                showOthers(PyroMIOSKeys,appsPyroMIOS, time);
            }
            if (playerX) showOthers(playerXKeys, appsPlayerX, time);
            if (bitmon) showOthers(BitmonAllKeys,appsBitmonAll, time);
            if (pyro) showOthers(PyroMIOSKeys,appsPyroMIOS, time);
            if (zed) showOthers(ZEDAllKeys,appsZEDAll, time);
            if (rus) showOthers(RUSAllKeys,appsRUSAll, time);
        }
    }

    if( $("#allOS").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if(allAccount || playerX) showAllCat(playerXKeys, appsPlayerX, time);
            if(allAccount || bitmon){
                showAllCat(BitmoniOSKeys, appsBitmonIOS, time);
                showAllCat(BitmonAndroidKeys, appsBitmonAndroid, time);
            }
            if(allAccount || pyro) showAllCat(PyroMIOSKeys, appsPyroMIOS, time);
            if(allAccount || zed){
                showAllCat(ZWKeys, appsZW, time);
                showAllCat(AZWKeys, appsAZW, time);
                showAllCat(ZGPSKeys, appsZGPS, time);
            }
            if(allAccount || rus) {
                showAllCat(RUSAndroidKeys, appsRUSAndroid, time);
                showAllCat(RUSiOSKeys, appsRUSiOS, time);
            }
        }
        else if($("#games").is(':checked')){
            if(allAccount || playerX) showGames(playerXKeys, appsPlayerX, time);
            if(allAccount || bitmon){
                showGames(BitmoniOSKeys, appsBitmonIOS, time);
                showGames(BitmonAndroidKeys, appsBitmonAndroid, time);
            }
            if(allAccount || pyro) showGames(PyroMIOSKeys, appsPyroMIOS, time);
            if(allAccount || zed){
                showGames(ZWKeys, appsZW, time);
                showGames(AZWKeys, appsAZW, time);
                showGames(ZGPSKeys, appsZGPS, time);
            }
            if(allAccount || rus) {
                showGames(RUSAndroidKeys, appsRUSAndroid, time);
                showGames(RUSiOSKeys, appsRUSiOS, time);
            }
        }
        else{
            if(allAccount || playerX) showOthers(playerXKeys, appsPlayerX, time);
            if(allAccount || bitmon){
                showOthers(BitmoniOSKeys, appsBitmonIOS, time);
                showOthers(BitmonAndroidKeys, appsBitmonAndroid, time);
            }
            if(allAccount || pyro) showOthers(PyroMIOSKeys, appsPyroMIOS, time);
            if(allAccount || zed){
                showOthers(ZWKeys, appsZW, time);
                showOthers(AZWKeys, appsAZW, time);
                showOthers(ZGPSKeys, appsZGPS, time);
            }
            if(allAccount || rus) {
                showOthers(RUSAndroidKeys, appsRUSAndroid, time);
                showOthers(RUSiOSKeys, appsRUSiOS, time);
            }
        }
    }

    if( $("#android").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if(allAccount || zed) showAllCat(ZGPSKeys, appsZGPS, time);
            if(allAccount || rus) showAllCat(RUSAndroidKeys, appsRUSAndroid, time);
            if(allAccount || bitmon) showAllCat(BitmonAndroidKeys, appsBitmonAndroid, time);
        }
        else if($("#games").is(':checked')){
            if(allAccount || zed) showGames(ZGPSKeys, appsZGPS, time);
            if(allAccount || rus) showGames(RUSAndroidKeys, appsRUSAndroid, time);
            if(allAccount || bitmon) showGames(BitmonAndroidKeys, appsBitmonAndroid, time);
        }
        else{
            if(allAccount || zed) showOthers(ZGPSKeys, appsZGPS, time);
            if(allAccount || rus) showOthers(RUSAndroidKeys, appsRUSAndroid, time);
            if(allAccount || bitmon) showOthers(BitmonAndroidKeys, appsBitmonAndroid, time);
        }
    }

    if( $("#ios").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if(allAccount || playerX) showAllCat(playerXKeys, appsPlayerX, time);
            if(allAccount || bitmon) showAllCat(BitmoniOSKeys, appsBitmonIOS, time);
            if(allAccount || rus) showAllCat(RUSiOSKeys, appsRUSiOS, time);
            if(allAccount || pyro) showAllCat(PyroMIOSKeys, appsPyroMIOS, time);
            if(allAccount || zed) showAllCat(ZWKeys, appsZW, time);
        }
        else if($("#games").is(':checked')){
            if(allAccount || playerX) showGames(playerXKeys, appsPlayerX, time);
            if(allAccount || bitmon) showGames(BitmoniOSKeys, appsBitmonIOS, time);
            if(allAccount || rus) showGames(RUSiOSKeys, appsRUSiOS, time);
            if(allAccount || pyro) showGames(PyroMIOSKeys, appsPyroMIOS, time);
            if(allAccount || zed) showGames(ZWKeys, appsZW, time);
        }
        else{
            if(allAccount || playerX) showOthers(playerXKeys, appsPlayerX, time);
            if(allAccount || bitmon) showOthers(BitmoniOSKeys, appsBitmonIOS, time);
            if(allAccount || rus) showOthers(RUSiOSKeys, appsRUSiOS, time);
            if(allAccount || pyro) showOthers(PyroMIOSKeys, appsPyroMIOS, time);
            if(allAccount || zed) showOthers(ZWKeys, appsZW, time);
        }
    }

    if( $("#amazon").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if(allAccount || zed) showAllCat(AZWKeys, appsAZW, time);
        }
        else if($("#games").is(':checked')){
            if(allAccount || zed) showGames(AZWKeys, appsAZW, time);
        }
        else{
            if(allAccount || zed) showOthers(AZWKeys, appsAZW, time);
        }
    }
//    }else if($("#flurry").is(':checked')){
//        if( $("#allOS").is(':checked')) {
//            if( $("#allCategories").is(':checked')){showAllCat(flurryAllKeys, appsFlurryAll)}
//            else if($("#games").is(':checked')){showGames(flurryAllKeys, appsFlurryAll)}
//            else showOthers(flurryAllKeys, appsFlurryAll);
//        }
//
//        if( $("#android").is(':checked')) {
//            if( $("#allCategories").is(':checked')){showAllCat(flurryKeys, appsFlurry, "android")}
//            else if($("#games").is(':checked')){showGames(flurryKeys, appsFlurry, "android")}
//            else showOthers(flurryKeys, appsFlurry, "android");
//        }
//
//        if( $("#ios").is(':checked')) {
//            if( $("#allCategories").is(':checked')){showAllCat(flurryKeys, appsFlurry, "ios")}
//            else if($("#games").is(':checked')){showGames(flurryKeys, appsFlurry, "ios")}
//            else showOthers(flurryKeys, appsFlurry, "ios");
//        }
//    }

    addTotal();
    miTabla.appendChild(tbBody);
    miCapa = document.getElementById('resultado');
    miCapa.appendChild(miTabla);
    $(".table").tablesorter({
        widgets: ['staticRow']
	});
    totalRevenuesArray.sort(function(a,b) { return b.value - a.value;});
    totalDownloadsArray.sort(function(a,b) { return b.value - a.value;});
    crearGraficos(totalDownloadIOS, totalDownloadAndroid, totalRevenueIOS, totalRevenueAndroid, totalRevenuesArray, totalDownloadsArray);

}

//switch (appsOS[osKeys[k]][3]){case "PlayerX": a = 1; break; case "Bizmonlab": a = 2; break;} pa las sumas de muvis
function showAllCat(osKeys, appsOS, time){
    for (var k in osKeys){
        if (osKeys.hasOwnProperty(k)) {
            addRow(appsOS, osKeys, k, time);
        }
    }
}

function showGames(osKeys, appsOS, time){
    for (var k in osKeys){
        if (osKeys.hasOwnProperty(k)) {
            if(appsOS[osKeys[k]][1].toLowerCase().indexOf("game") > -1){
                addRow(appsOS, osKeys, k, time);
            }
        }
    }
}

function showOthers(osKeys, appsOS, time){
    for (var k in osKeys){
        if (osKeys.hasOwnProperty(k)) {
            if(appsOS[osKeys[k]][1].toLowerCase().indexOf("game") == -1){
                addRow(appsOS, osKeys, k, time);
            }
        }
    }
}

function createTable(){
    miTabla = document.createElement("table");
    tbHead = document.createElement("thead");
    tbBody = document.createElement("tbody");
    tr1 = document.createElement("tr");
    th1 = document.createElement("th");
    th2 = document.createElement("th");
    th3 = document.createElement("th");
    th4 = document.createElement("th");
    th1.setAttribute("style", "text-align:center");
    th2.setAttribute("style", "text-align:center");
    th3.setAttribute("style", "text-align:center");
    th4.setAttribute("style", "text-align:center");
    th1.innerHTML = "OS";
    th2.innerHTML = "Name";
    th3.innerHTML = "Downloads";
    th4.innerHTML = "Revenue ($)";

    tr1.setAttribute("class", "active");
    tr1.appendChild(th1);
    tr1.appendChild(th2);
    tr1.appendChild(th3);
    tr1.appendChild(th4);

    tbHead.appendChild(tr1);

    miTabla.appendChild(tbHead);
    miTabla.setAttribute("class", "table table-bordered");
//    miTabla.style.width = '855px';
}

function addRow(appsOS, osKey, k, time){
    if ((appsOS[osKey[k]][time] != 0) || ((appsOS[osKey[k]][time+4] != '0.00') && (appsOS[osKey[k]][time+4] != '0.0'))){
        tr2 = document.createElement("tr");
        td1 = document.createElement("td");
        td2 = document.createElement("td");
        td3 = document.createElement("td");
        td4 = document.createElement("td");
        td1.setAttribute("align", "center");
        td2.setAttribute("align", "center");
        td3.setAttribute("align", "right");
        td4.setAttribute("align", "rigth");
        td4.setAttribute("style", 'text-align: right');
        td3.setAttribute("class", 'derecha');
        td4.setAttribute("class", 'derecha');

        td1.innerHTML = appsOS[osKey[k]][2];
        td2.innerHTML = appsOS[osKey[k]][0];
        td3.innerHTML = appsOS[osKey[k]][time].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        if (appsOS[osKey[k]][time+4] == '0.00'){
            td4.innerHTML = '0,0';
        }else{
            revenue_with_comma = appsOS[osKey[k]][time+4].replace('.',',');
            td4.innerHTML = revenue_with_comma.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        }
        totalDownloads += appsOS[osKey[k]][time];
        totalRevenue += parseFloat(appsOS[osKey[k]][time+4]);
        tr2.appendChild(td1);
        tr2.appendChild(td2);
        tr2.appendChild(td3);
        tr2.appendChild(td4);
        tbBody.appendChild(tr2);
    }

    dict = {"label": "", "value": 0};
    dictAux = {"label": "", "value": 0};
    dictD = {"label": "", "value": 0};
    dictAuxD = {"label": "", "value": 0};


//    Añadir el total de android y de ios para porcentajes
    switch (appsOS[osKey[k]][3]){
        case "PlayerX":
            totalDownloadIOS += appsOS[osKey[k]][time];
            totalRevenueIOS += parseFloat(appsOS[osKey[k]][time+4]);
            dict.label = appsOS[osKey[k]][0].substring(0,14);
            dict.value = parseFloat(appsOS[osKey[k]][time+4]);
            totalRevenuesArray.push(dict);
            dictD.label = appsOS[osKey[k]][0].substring(0,14);
            dictD.value = parseFloat(appsOS[osKey[k]][time]);
            totalDownloadsArray.push(dictD);
            break;
        case "PyroM":
            totalDownloadIOS += appsOS[osKey[k]][time];
            totalRevenueIOS += parseFloat(appsOS[osKey[k]][time+4]);
            dict.label = appsOS[osKey[k]][0].substring(0,14);
            dict.value = parseFloat(appsOS[osKey[k]][time+4]);
            totalRevenuesArray.push(dict);
            dictD.label = appsOS[osKey[k]][0].substring(0,14);
            dictD.value = parseFloat(appsOS[osKey[k]][time]);
            totalDownloadsArray.push(dictD);
            break;
        case "Bitmonlab":
            if (appsOS[osKey[k]][2] == "Android-iOS"){
                for (var j in BitmonAndroidKeys){
                    if (BitmonAndroidKeys.hasOwnProperty(j)) {
                        if (appsBitmonAndroid[BitmonAndroidKeys[j]][0] == appsOS[osKey[k]][0]){
                            totalDownloadAndroid += appsBitmonAndroid[BitmonAndroidKeys[j]][time];
                            totalRevenueAndroid +=  parseFloat(appsBitmonAndroid[BitmonAndroidKeys[j]][time+4]);
                            dict.label = appsBitmonAndroid[BitmonAndroidKeys[j]][0].substring(0,9) +
                                "-" + appsBitmonAndroid[BitmonAndroidKeys[j]][2].substring(0,3);
                            dict.value = parseFloat(appsBitmonAndroid[BitmonAndroidKeys[j]][time+4]);
                            totalRevenuesArray.push(dict);
                            dictD.label = appsBitmonAndroid[BitmonAndroidKeys[j]][0].substring(0,9) +
                                "-" + appsBitmonAndroid[BitmonAndroidKeys[j]][2].substring(0,3);
                            dictD.value = parseFloat(appsBitmonAndroid[BitmonAndroidKeys[j]][time]);
                            totalDownloadsArray.push(dictD);
                        }
                    }
                }
                for (var l in BitmoniOSKeys){
                    if (BitmoniOSKeys.hasOwnProperty(l)) {
                        if (appsBitmonIOS[BitmoniOSKeys[l]][0] == appsOS[osKey[k]][0]){
                            totalDownloadIOS += appsBitmonIOS[BitmoniOSKeys[l]][time];
                            totalRevenueIOS +=  parseFloat(appsBitmonIOS[BitmoniOSKeys[l]][time+4]);
                            dictAux.label = appsBitmonIOS[BitmoniOSKeys[l]][0].substring(0,9) +
                                "-" + appsBitmonIOS[BitmoniOSKeys[l]][2];
                            dictAux.value = parseFloat(appsBitmonIOS[BitmoniOSKeys[l]][time+4]);
                            totalRevenuesArray.push(dictAux);
                            dictAuxD.label = appsBitmonIOS[BitmoniOSKeys[l]][0].substring(0,9) +
                                "-" + appsBitmonIOS[BitmoniOSKeys[l]][2];
                            dictAuxD.value = parseFloat(appsBitmonIOS[BitmoniOSKeys[l]][time]);
                            totalDownloadsArray.push(dictAuxD);
                        }
                    }
                }
            }
            if (appsOS[osKey[k]][2] == "Android"){
                totalDownloadAndroid += appsOS[osKey[k]][time];
                totalRevenueAndroid +=  parseFloat(appsOS[osKey[k]][time+4]);
                dict.label = appsOS[osKey[k]][0].substring(0,14)+ "-" + appsOS[osKey[k]][2];
                dict.value = parseFloat(appsOS[osKey[k]][time+4]);
                totalRevenuesArray.push(dict);
                dictD.label = appsOS[osKey[k]][0].substring(0,14)+ "-" + appsOS[osKey[k]][2];
                dictD.value = parseFloat(appsOS[osKey[k]][time]);
                totalDownloadsArray.push(dictD);
            }
            if (appsOS[osKey[k]][2] == "iOS"){
                totalDownloadIOS += appsOS[osKey[k]][time];
                totalRevenueIOS +=  parseFloat(appsOS[osKey[k]][time+4]);
                dict.label = appsOS[osKey[k]][0].substring(0,14)+ "-" + appsOS[osKey[k]][2];
                dict.value = parseFloat(appsOS[osKey[k]][time+4]);
                totalRevenuesArray.push(dict);
                dictD.label = appsOS[osKey[k]][0].substring(0,14)+ "-" + appsOS[osKey[k]][2];
                dictD.value = parseFloat(appsOS[osKey[k]][time]);
                totalDownloadsArray.push(dictD);
            }
            break;
        case "ZW":
            totalDownloadIOS += appsOS[osKey[k]][time];
            totalRevenueIOS += parseFloat(appsOS[osKey[k]][time+4]);
            dict.label = appsOS[osKey[k]][0].substring(0,13);
            dict.value = parseFloat(appsOS[osKey[k]][time+4]);
            totalRevenuesArray.push(dict);
            dictD.label = appsOS[osKey[k]][0].substring(0,13);
            dictD.value = parseFloat(appsOS[osKey[k]][time]);
            totalDownloadsArray.push(dictD);
            break;
        case "ZGPS":
            if (appsOS[osKey[k]][2] == "Android-Fire/Android"){
                for (var j in ZGPSKeys){
                    if (ZGPSKeys.hasOwnProperty(j)) {
                        if (appsZGPS[ZGPSKeys[j]][0] == appsOS[osKey[k]][0]){
                            totalDownloadAndroid += appsZGPS[ZGPSKeys[j]][time];
                            totalRevenueAndroid +=  parseFloat(appsZGPS[ZGPSKeys[j]][time+4]);
                            dict.label = appsZGPS[ZGPSKeys[j]][0].substring(0,9)+ "-" + appsZGPS[ZGPSKeys[j]][2].substring(0,3);
                            dict.value = parseFloat(appsZGPS[ZGPSKeys[j]][time+4]);
                            totalRevenuesArray.push(dict);
                            dictD.label = appsZGPS[ZGPSKeys[j]][0].substring(0,9)+ "-" + appsZGPS[ZGPSKeys[j]][2].substring(0,3);
                            dictD.value = parseFloat(appsZGPS[ZGPSKeys[j]][time]);
                            totalDownloadsArray.push(dictD);
                        }
                    }
                }
            }
            if (appsOS[osKey[k]][2] == "Android-iOS-Fire/Android" || appsOS[osKey[k]][2] == "Android-iOS"){
                for (var j in ZGPSKeys){
                    if (ZGPSKeys.hasOwnProperty(j)) {
                        if (appsZGPS[ZGPSKeys[j]][0] == appsOS[osKey[k]][0]){
                            totalDownloadAndroid += appsZGPS[ZGPSKeys[j]][time];
                            totalRevenueAndroid +=  parseFloat(appsZGPS[ZGPSKeys[j]][time+4]);
                            dict.label = appsZGPS[ZGPSKeys[j]][0].substring(0,9)+ "-" + appsZGPS[ZGPSKeys[j]][2].substring(0,3);
                            dict.value = parseFloat(appsZGPS[ZGPSKeys[j]][time+4]);
                            totalRevenuesArray.push(dict);
                            dictD.label = appsZGPS[ZGPSKeys[j]][0].substring(0,9)+ "-" + appsZGPS[ZGPSKeys[j]][2].substring(0,3);
                            dictD.value = parseFloat(appsZGPS[ZGPSKeys[j]][time]);
                            totalDownloadsArray.push(dictD);
                        }
                    }
                }
                for (var j in ZWKeys){
                    if (ZGPSKeys.hasOwnProperty(j)) {
                        if (appsZW[ZWKeys[j]][0] == appsOS[osKey[k]][0]){
                            totalDownloadIOS += appsZW[ZWKeys[j]][time];
                            totalRevenueIOS +=  parseFloat(appsZW[ZWKeys[j]][time+4]);
                            dictAux.label = appsZW[ZWKeys[j]][0].substring(0,9)+ "-" + appsZW[ZWKeys[j]][2];
                            dictAux.value = parseFloat(appsZW[ZWKeys[j]][time+4]);
                            totalRevenuesArray.push(dictAux);
                            dictAuxD.label = appsZW[ZWKeys[j]][0].substring(0,9)+ "-" + appsZW[ZWKeys[j]][2];
                            dictAuxD.value = parseFloat(appsZW[ZWKeys[j]][time]);
                            totalDownloadsArray.push(dictAuxD);
                        }
                    }
                }
            }
            if (appsOS[osKey[k]][2] == "Android"){
                totalDownloadAndroid += appsOS[osKey[k]][time];
                totalRevenueAndroid +=  parseFloat(appsOS[osKey[k]][time+4]);
                dict.label = appsOS[osKey[k]][0].substring(0,14);
                dict.value = parseFloat(appsOS[osKey[k]][time+4]);
                totalRevenuesArray.push(dict);
                dictD.label = appsOS[osKey[k]][0].substring(0,14);
                dictD.value = parseFloat(appsOS[osKey[k]][time]);
                totalDownloadsArray.push(dictD);
            }
            break;
        case "RUS":
            if (appsOS[osKey[k]][2] == "Android-iOS"){
                for (var j in RUSiOSKeys){
                    if (RUSiOSKeys.hasOwnProperty(j)) {
                        if (appsRUSiOS[RUSiOSKeys[j]][0] == appsOS[osKey[k]][0]){
                            totalDownloadIOS += appsRUSiOS[RUSiOSKeys[j]][time];
                            totalRevenueIOS +=  parseFloat(appsRUSiOS[RUSiOSKeys[j]][time+4]);
                            dict.label = appsRUSiOS[RUSiOSKeys[j]][0].substring(0,9)+ "-" + appsRUSiOS[RUSiOSKeys[j]][2];
                            dict.value = parseFloat(appsRUSiOS[RUSiOSKeys[j]][time+4]);
                            totalRevenuesArray.push(dict);
                            dictD.label = appsRUSiOS[RUSiOSKeys[j]][0].substring(0,9)+ "-" + appsRUSiOS[RUSiOSKeys[j]][2];
                            dictD.value = parseFloat(appsRUSiOS[RUSiOSKeys[j]][time]);
                            totalDownloadsArray.push(dictD);
                        }
                    }
                }
                for (var j in RUSAndroidKeys){
                    if (RUSAndroidKeys.hasOwnProperty(j)) {
                        if (appsRUSAndroid[RUSAndroidKeys[j]][0] == appsOS[osKey[k]][0]){
                            totalDownloadAndroid += appsRUSAndroid[RUSAndroidKeys[j]][time];
                            totalRevenueAndroid +=  parseFloat(appsRUSAndroid[RUSAndroidKeys[j]][time+4]);
                            dictAux.label = appsRUSAndroid[RUSAndroidKeys[j]][0].substring(0,9)+ "-" +
                                appsRUSAndroid[RUSAndroidKeys[j]][2].substring(0,3);
                            dictAux.value = parseFloat(appsRUSAndroid[RUSAndroidKeys[j]][time+4]);
                            totalRevenuesArray.push(dictAux);
                            dictAuxD.label = appsRUSAndroid[RUSAndroidKeys[j]][0].substring(0,9)+ "-" +
                                appsRUSAndroid[RUSAndroidKeys[j]][2].substring(0,3);
                            dictAuxD.value = parseFloat(appsRUSAndroid[RUSAndroidKeys[j]][time]);
                            totalDownloadsArray.push(dictAuxD);
                        }
                    }
                }
            }
            if (appsOS[osKey[k]][2] == "Android"){
                totalDownloadAndroid += appsOS[osKey[k]][time];
                totalRevenueAndroid +=  parseFloat(appsOS[osKey[k]][time+4]);
                dict.label = appsOS[osKey[k]][0].substring(0,14);
                dict.value = parseFloat(appsOS[osKey[k]][time+4]);
                totalRevenuesArray.push(dict);
                dictD.label = appsOS[osKey[k]][0].substring(0,14);
                dictD.value = parseFloat(appsOS[osKey[k]][time]);
                totalDownloadsArray.push(dictD);
            }
            if (appsOS[osKey[k]][2] == "iOS"){
                for (var j in RUSiOSKeys){
                    if (RUSiOSKeys.hasOwnProperty(j)) {
                        if (appsRUSiOS[RUSiOSKeys[j]][0] == appsOS[osKey[k]][0]){
                            totalDownloadIOS += appsRUSiOS[RUSiOSKeys[j]][time];
                            totalRevenueIOS +=  parseFloat(appsRUSiOS[RUSiOSKeys[j]][time+4]);
                            dict.label = appsRUSiOS[RUSiOSKeys[j]][0].substring(0,14);
                            dict.value = parseFloat(appsRUSiOS[RUSiOSKeys[j]][time+4]);
                            totalRevenuesArray.push(dict);
                            dictD.label = appsRUSiOS[RUSiOSKeys[j]][0].substring(0,14);
                            dictD.value = parseFloat(appsRUSiOS[RUSiOSKeys[j]][time]);
                            totalDownloadsArray.push(dictD);
                        }
                    }
                }
            }
    }

}

function addTotal(){
    tr2 = document.createElement("tr");
    tr2.setAttribute("class", "static");
    td1 = document.createElement("td");
    td2 = document.createElement("td");
    td3 = document.createElement("td");
    td4 = document.createElement("td");
    td1.setAttribute("align", "center");
    td2.setAttribute("align", "center");
    td3.setAttribute("align", "right");
    td4.setAttribute("align", "right");
    td3.setAttribute("class", "derecha");
    td4.setAttribute("class", "derecha");
    td1.innerHTML = "";
    td2.innerHTML = "TOTAL";
    td3.innerHTML = totalDownloads.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    totalRevenueFixed = totalRevenue.toFixed(2);
    total_revenue_with_comma = totalRevenueFixed.replace('.',',');
    td4.innerHTML = total_revenue_with_comma.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    tr2.appendChild(td1);
    tr2.appendChild(td2);
    tr2.appendChild(td3);
    tr2.appendChild(td4);
    tbBody.appendChild(tr2);
}


function crearGraficos(DIOS, DA, RIOS, RA, TRA, TDA){
    nv.addGraph(function() {
    var chart = nv.models.pieChart()
       .x(function(d) { return d.label })
       .y(function(d) { return d.value })
       .showLabels(true)
       .labelType("percent");

    d3.select("#chart1 svg")
       .datum(chart1Data(DIOS, DA))
       .transition().duration(1200)
       .call(chart);

    d3.select('#chart1 svg')
      .append("text")
      .attr("x", 150)
      .attr("y", 350)
      .attr("text-anchor", "middle")
      .text("Downloads by OS (%)");

    d3.select("#chart4 svg")
       .datum(chart4Data(TDA))
       .transition().duration(1200)
       .call(chart);

    d3.select('#chart4 svg')
      .append("text")
      .attr("x", 150)
      .attr("y", 370)
      .attr("text-anchor", "middle")
      .text("Downloads (%) by sku");

    d3.select("#chart2 svg")
       .datum(chart2Data(RIOS, RA))
       .transition().duration(1200)
       .call(chart);

    d3.select('#chart2 svg')
      .append("text")
      .attr("x", 150)
      .attr("y", 350)
      .attr("text-anchor", "middle")
      .text("Revenue by OS (%)");

    d3.select("#chart3 svg")
       .datum(chart3Data(TRA))
       .transition().duration(1200)
       .call(chart);

    d3.select('#chart3 svg')
      .append("text")
      .attr("x", 150)
      .attr("y", 370)
      .attr("text-anchor", "middle")
      .text("Revenue Breakdown (%) by sku");
    return chart;
    });
}


function chart1Data(DIOS, DA) {
    data= [];
    dict1 = {"label": "iOS", "value": DIOS};
    dict2 = {"label": "Android", "value": DA};
    data.push(dict1);
    data.push(dict2);

  return data;
}

function chart4Data(TDA){
    data = [];
    others = {"label": "Rest of apps", "value": 0};
    for (i=0;  i < TDA.length; i++){
        if (i<5){
            data.push(TDA[i]);
        }else{
            others.value += TDA[i].value;
        }
    }
    data.push(others);
    return data;
}

function chart2Data(RIOS, RA) {
    data= [];
    dict1 = {"label": "iOS", "value": RIOS};
    dict2 = {"label": "Android", "value": RA};
    data.push(dict1);
    data.push(dict2);

  return data;
}

function chart3Data(TRA){
    data = [];
    others = {"label": "Rest of apps", "value": 0};
    for (i=0;  i < TRA.length; i++){
        if (i<5){
            data.push(TRA[i]);
        }else{
            others.value += TRA[i].value;
        }
    }
    data.push(others);
    return data;
}

function descargarPDF(){
    canvas();
    var pdf = new jsPDF('p', 'pt', 'a3');
    source = $('#resultado')[0];
    source.style.width = '885px';
    specialElementHandlers = {
        '#bypassme': function (element, renderer) {
            return true
        }
    };
    pdf.setFontSize(10);

    var today = $('#dateExcel').first().text().substring(7,17);

    var dayBefore = new Date(today);
    if (before!=0){
        dayBefore.setDate(dayBefore.getDate()-(before));
        var ddb = dayBefore.getDate();
        var mmb = dayBefore.getMonth()+1; //January is 0!

        var yyyyb = dayBefore.getFullYear();
        if(ddb<10){
            ddb='0'+ddb
        }
        if(mmb<10){
            mmb='0'+mmb
        }
        var dayBefore = yyyyb+'-'+mmb+'-'+ddb;
        pdf.text(530, 50, dayBefore + " / " + today);
    }else{
        pdf.text(582, 50, "~ / " + today);
    }

    pdf.text(18, 50, "Apps and games downloads and revenue");


    var canvas1 = $("#canvas1")[0];
    var imgData1 = canvas1.toDataURL("", 1.0);
    pdf.addImage(imgData1, 'JPEG', 655, 70, 620, 370);
    pdf.text(700, 290, 'Downloads by OS (%)');

    var canvas4 = $("#canvas4")[0];
    var imgData4 = canvas4.toDataURL("", 1.0);
    pdf.addImage(imgData4, 'JPEG', 655, 340, 620, 370);
    pdf.text(699, 570, 'Downloads (%) by sku');

    var canvas2 = $("#canvas2")[0];
    var imgData2 = canvas2.toDataURL("", 1.0);
    pdf.addImage(imgData2, 'JPEG', 655, 610, 620, 370);
    pdf.text(708, 840, 'Revenue by OS (%)');

    var canvas3 = $("#canvas3")[0];
    var imgData3 = canvas3.toDataURL("", 1.0);
    pdf.addImage(imgData3, 'JPEG', 655, 880, 620, 370);
    pdf.text(675, 1120, 'Revenue Breakdown (%) by sku');

//    margins = {
//        top: 50,
//        bottom: 40,
//        left: 20,
//        right: 350,
//        width: 522
//    };

//    var divider = 1;
//    // clone table one to create table two
//    var $tableOne = $('table').attr('id','newTable1');
//    $tableOne.appendTo('#table1');
//    var $tableTwo = $tableOne.clone().attr('id','newTable2').appendTo('#table2');
//
//    // number of rows in table
//    var numOfRows = $tableOne.find('tr').length;
//
//    // select rows of each table
//    var $tableOneRows = $tableOne.find('tr');
//    var $tableTwoRows = $tableTwo.find('tr');
//
//    // loop through each row in table one.
//    // since table two is a clone of table one,
//    // we will also manipulate table two at the same time.
//    $tableOneRows.each(function(index){
//          // save row for each table
//          var $trOne = $(this);
//          var $trTwo = $tableTwoRows.eq(index);
//
//          // remove columns greater than divider from table one
//          $trOne.children(':gt('+divider+')').remove();
//          $trTwo.children(':lt('+(divider+1)+')').remove();
//    });
    pdf.htmlTable(10, 57, source);
//    pdf.htmlTable(470, -557, $tableTwo, options2);
    pdf.save('ZED_Analytics.pdf');
    source.style.width = '100%';
    $('#resultado').attr('style', 'width: 66.66666667%');
    verEstadisticas();
//    pdf.fromHTML(
//    source,
//    margins.left,
//    margins.top, {
//        'width': margins.width,
//        'elementHandlers': specialElementHandlers
//    },
//
//    function (dispose) {
//        setTimeout(function() {
//            pdf.save('ZED_Analytics.pdf');
//        }, 2);
//    }, margins);
}

function canvas(){
    canvg(document.getElementById('canvas1'),$("#chart1 svg")[0].innerHTML, { ignoreMouse: true, ignoreAnimation: true });
    canvg(document.getElementById('canvas2'),$("#chart2 svg")[0].innerHTML, { ignoreMouse: true, ignoreAnimation: true });
    canvg(document.getElementById('canvas3'),$("#chart3 svg")[0].innerHTML, { ignoreMouse: true, ignoreAnimation: true });
    canvg(document.getElementById('canvas4'),$("#chart4 svg")[0].innerHTML, { ignoreMouse: true, ignoreAnimation: true });
}
