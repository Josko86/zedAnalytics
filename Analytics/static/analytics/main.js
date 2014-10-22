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
    AllKeys = Object.keys(appsAll);
    RUSAllKeys = Object.keys(appsRUSAll);
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
    showAllCat(AllKeys,appsAll, 4);
    showAllCat(RUSAllKeys,appsRUSAll, 4);

    addTotal();
    miTabla.appendChild(tbBody);
    miCapa = document.getElementById('resultado');
    miCapa.appendChild(miTabla);
    $(".table").tablesorter({
        widgets: ['staticRow']
	});
});

function verEstadisticas(){

    if ($(".table")){
        $(".table").remove();
    }
    totalDownloads = 0;
    totalRevenue = 0;
    allAccount= $("#allAccount").is(':checked');
    playerX= $("#playerX").is(':checked');
    zw= $("#ZW").is(':checked');
    zgps= $("#ZGPS").is(':checked');
    azw= $("#AZW").is(':checked');
    rus= $("#RUS").is(':checked');

    time = 4;
    if ( $("#month").is(':checked')){
        time++;
    }else if ( $("#week").is(':checked')){
        time = time + 2;
    }else if ( $("#day").is(':checked')){
        time = time + 3;
    }
    createTable();

    if( $("#combined").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if (allAccount){
                showAllCat(AllKeys,appsAll, time);
                showAllCat(RUSAllKeys,appsRUSAll, time);
            }
            if (playerX) showAllCat(playerXKeys, appsPlayerX, time);
            if (zw) showAllCat(ZWKeys, appsZW, time);
            if (zgps) showAllCat(ZGPSKeys, appsZGPS, time);
            if (azw) showAllCat(AZWKeys, appsAZW, time);
            if (rus) showAllCat(RUSAllKeys,appsRUSAll, time);
        }
        else if($("#games").is(':checked')){
            if (allAccount){
                showGames(AllKeys,appsAll, time);
                showGames(RUSAllKeys,appsRUSAll, time);
            }
            if (playerX) showGames(playerXKeys, appsPlayerX, time);
            if (zw) showGames(ZWKeys, appsZW, time);
            if (zgps) showGames(ZGPSKeys, appsZGPS, time);
            if (azw) showGames(AZWKeys, appsAZW, time);
            if (rus) showGames(RUSAllKeys,appsRUSAll, time);
        }
        else{
            if (allAccount){
                showOthers(AllKeys,appsAll, time);
                showOthers(RUSAllKeys,appsRUSAll, time);
            }
            if (playerX) showOthers(playerXKeys, appsPlayerX, time);
            if (zw) showOthers(ZWKeys, appsZW, time);
            if (zgps) showOthers(ZGPSKeys, appsZGPS, time);
            if (azw) showOthers(AZWKeys, appsAZW, time);
            if (rus) showOthers(RUSAllKeys,appsRUSAll, time);
        }
    }

    if( $("#allOS").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if(allAccount || playerX) showAllCat(playerXKeys, appsPlayerX, time);
            if(allAccount || zw) showAllCat(ZWKeys, appsZW, time);
            if(allAccount || zgps) showAllCat(ZGPSKeys, appsZGPS, time);
            if(allAccount || azw) showAllCat(AZWKeys, appsAZW, time);
            if(allAccount || rus) {
                showAllCat(RUSAndroidKeys, appsRUSAndroid, time);
                showAllCat(RUSiOSKeys, appsRUSiOS, time);
            }
        }
        else if($("#games").is(':checked')){
            if(allAccount || playerX) showGames(playerXKeys, appsPlayerX, time);
            if(allAccount || zw) showGames(ZWKeys, appsZW, time);
            if(allAccount || zgps) showGames(ZGPSKeys, appsZGPS, time);
            if(allAccount || azw) showGames(AZWKeys, appsAZW, time);
            if(allAccount || rus) {
                showGames(RUSAndroidKeys, appsRUSAndroid, time);
                showGames(RUSiOSKeys, appsRUSiOS, time);
            }
        }
        else{
            if(allAccount || playerX) showOthers(playerXKeys, appsPlayerX, time);
            if(allAccount || zw) showOthers(ZWKeys, appsZW, time);
            if(allAccount || zgps) showOthers(ZGPSKeys, appsZGPS, time);
            if(allAccount || azw) showOthers(AZWKeys, appsAZW, time);
            if(allAccount || rus){
                showOthers(RUSAndroidKeys, appsRUSAndroid, time);
                showOthers(RUSiOSKeys, appsRUSiOS, time);
            }
        }
    }

    if( $("#android").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if(allAccount || zgps) showAllCat(ZGPSKeys, appsZGPS, time);
            if(allAccount || rus) showAllCat(RUSAndroidKeys, appsRUSAndroid, time);
        }
        else if($("#games").is(':checked')){
            if(allAccount || zgps) showGames(ZGPSKeys, appsZGPS, time);
            if(allAccount || rus) showGames(RUSAndroidKeys, appsRUSAndroid, time);
        }
        else{
            if(allAccount || zgps) showOthers(ZGPSKeys, appsZGPS, time);
            if(allAccount || rus) showOthers(RUSAndroidKeys, appsRUSAndroid, time);
        }
    }

    if( $("#ios").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if(allAccount || playerX) showAllCat(playerXKeys, appsPlayerX, time);
            if(allAccount || zw) showAllCat(ZWKeys, appsZW, time);
            if(allAccount || rus) showAllCat(RUSiOSKeys, appsRUSiOS, time);
        }
        else if($("#games").is(':checked')){
            if(allAccount || playerX) showGames(playerXKeys, appsPlayerX, time);
            if(allAccount || zw) showGames(ZWKeys, appsZW, time);
            if(allAccount || rus) showGames(RUSiOSKeys, appsRUSiOS, time);
        }
        else{
            if(allAccount || playerX) showOthers(playerXKeys, appsPlayerX, time);
            if(allAccount || zw) showOthers(ZWKeys, appsZW, time);
            if(allAccount || rus) showOthers(RUSiOSKeys, appsRUSiOS, time);
        }
    }

    if( $("#amazon").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            if(allAccount || azw) showAllCat(AZWKeys, appsAZW, time);
        }
        else if($("#games").is(':checked')){
            if(allAccount || azw) showGames(AZWKeys, appsAZW, time);
        }
        else{
            if(allAccount || azw) showOthers(AZWKeys, appsAZW, time);
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
}

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
}

function addRow(appsOS, osKey, k, time){
    tr2 = document.createElement("tr");
    td1 = document.createElement("td");
    td2 = document.createElement("td");
    td3 = document.createElement("td");
    td4 = document.createElement("td");
    td1.setAttribute("align", "center");
    td2.setAttribute("align", "center");
    td3.setAttribute("align", "center");
    td4.setAttribute("align", "center");

    td1.innerHTML = appsOS[osKey[k]][2];
    td2.innerHTML = appsOS[osKey[k]][0];
    td3.innerHTML = appsOS[osKey[k]][time];
    td4.innerHTML = appsOS[osKey[k]][time+4];
    totalDownloads += appsOS[osKey[k]][time];
    totalRevenue += parseFloat(appsOS[osKey[k]][time+4]);

    tr2.appendChild(td1);
    tr2.appendChild(td2);
    tr2.appendChild(td3);
    tr2.appendChild(td4);
    tbBody.appendChild(tr2);
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
    td3.setAttribute("align", "center");
    td4.setAttribute("align", "center");
    td1.innerHTML = "";
    td2.innerHTML = "TOTAL";
    td3.innerHTML = totalDownloads;
    td4.innerHTML = totalRevenue.toFixed(2);
    tr2.appendChild(td1);
    tr2.appendChild(td2);
    tr2.appendChild(td3);
    tr2.appendChild(td4);
    tbBody.appendChild(tr2);
}

function descargarPDF(){
    var pdf = new jsPDF('p', 'pt', 'letter');
    source = $('#resultado')[0];
    specialElementHandlers = {
        '#bypassme': function (element, renderer) {
            return true
        }
    };
    margins = {
        top: 80,
        bottom: 60,
        left: 40,
        width: 522
    };
    pdf.fromHTML(
    source,
    margins.left,
    margins.top, {
        'width': margins.width,
        'elementHandlers': specialElementHandlers
    },

    function (dispose) {
        pdf.save('ZED_Analytics.pdf');
    }, margins);
}