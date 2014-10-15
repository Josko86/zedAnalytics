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
    showAllCat(playerXKeys, appsPlayerX, 4);
    showAllCat(ZWKeys, appsZW, 4);
    showAllCat(ZGPSKeys, appsZGPS, 4);
    showAllCat(AZWKeys, appsAZW, 4);

    miTabla.appendChild(tbBody);
    miCapa = document.getElementById('resultado');
    miCapa.appendChild(miTabla);
    $(".table").tablesorter({
		sortList: [[1,0]]
	});
});

function verEstadisticas(){

    if ($(".table")){
        $(".table").remove();
    }

    time = 4;
    if ( $("#month").is(':checked')){
        time++;
    }else if ( $("#week").is(':checked')){
        time = time + 2;
    }else if ( $("#day").is(':checked')){
        time = time + 3;
    }
    createTable();

    if( $("#allOS").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            showAllCat(playerXKeys, appsPlayerX, time);
            showAllCat(ZWKeys, appsZW, time);
            showAllCat(ZGPSKeys, appsZGPS, time);
            showAllCat(AZWKeys, appsAZW, time);
        }
        else if($("#games").is(':checked')){
            showGames(playerXKeys, appsPlayerX, time);
            showGames(ZWKeys, appsZW, time);
            showGames(ZGPSKeys, appsZGPS, time);
            showGames(AZWKeys, appsAZW, time);
        }
        else{
            showOthers(playerXKeys, appsPlayerX, time);
            showOthers(ZWKeys, appsZW, time);
            showOthers(ZGPSKeys, appsZGPS, time);
            showOthers(AZWKeys, appsAZW, time);
        }
    }

    if( $("#android").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            showAllCat(ZGPSKeys, appsZGPS, time);
            showAllCat(AZWKeys, appsAZW, time);
        }
        else if($("#games").is(':checked')){
            showGames(ZGPSKeys, appsZGPS, time);
            showGames(AZWKeys, appsAZW, time);
        }
        else{
            showOthers(ZGPSKeys, appsZGPS, time);
            showOthers(AZWKeys, appsAZW, time);
        }
    }

    if( $("#ios").is(':checked')) {
        if( $("#allCategories").is(':checked')){
            showAllCat(playerXKeys, appsPlayerX, time);
            showAllCat(ZWKeys, appsZW, time);
        }
        else if($("#games").is(':checked')){
            showGames(playerXKeys, appsPlayerX, time);
            showGames(ZWKeys, appsZW, time);
        }
        else{
            showOthers(playerXKeys, appsPlayerX, time);
            showOthers(ZWKeys, appsZW, time);
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

    miTabla.appendChild(tbBody);
    miCapa = document.getElementById('resultado');
    miCapa.appendChild(miTabla);
    $(".table").tablesorter({
		sortList: [[1,0]]
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
    th5 = document.createElement("th");
    th1.setAttribute("style", "text-align:center");
    th2.setAttribute("style", "text-align:center");
    th3.setAttribute("style", "text-align:center");
    th4.setAttribute("style", "text-align:center");
    th5.setAttribute("style", "text-align:center");
    th1.innerHTML = "Account";
    th2.innerHTML = "Name";
    th3.innerHTML = "Downloads";
    th4.innerHTML = "OS";
    th5.innerHTML = "Revenue";

    tr1.setAttribute("class", "active");
    tr1.appendChild(th1);
    tr1.appendChild(th2);
    tr1.appendChild(th3);
    tr1.appendChild(th4);
    tr1.appendChild(th5);

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
    td5 = document.createElement("td");
    td6 = document.createElement("td");
    td1.setAttribute("align", "center");
    td2.setAttribute("align", "center");
    td3.setAttribute("align", "center");
    td4.setAttribute("align", "center");
    td5.setAttribute("align", "center");

    td1.innerHTML = appsOS[osKey[k]][3];
    td2.innerHTML = appsOS[osKey[k]][0];
    td3.innerHTML = appsOS[osKey[k]][time];
    td4.innerHTML = appsOS[osKey[k]][2];
    td5.innerHTML = '$ ' + appsOS[osKey[k]][time+4];

    tr2.appendChild(td1);
    tr2.appendChild(td2);
    tr2.appendChild(td3);
    tr2.appendChild(td4);
    tr2.appendChild(td5);
    tbBody.appendChild(tr2);
}