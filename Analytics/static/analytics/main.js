/**
 * Created with PyCharm.
 * User: Josko
 * Date: 17/09/14
 * Time: 14:48
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function(){
    //busca las aplicaciones con el mismo nombre y suma las descargas
    androidKeys = Object.keys(appsAndroid);
    iosKeys = Object.keys(appsIOS);
    flurryKeys = Object.keys(appsFlurry);
    flurryAllKeys = Object.keys(appsFlurryAll);
    for (var k in androidKeys){
        if (androidKeys.hasOwnProperty(k)) {
            for (var j in iosKeys){
                if (iosKeys.hasOwnProperty(j)) {
                    if (appsIOS[iosKeys[j]][0].toLowerCase().indexOf(appsAndroid[androidKeys[k]][0].toLowerCase())> -1){
                        appsAll[androidKeys[k]][2] = appsIOS[iosKeys[j]][2] + appsAndroid[androidKeys[k]][2];
                    }
                }
            }
        }
    }
    createTable();
    showAllCat(androidKeys, appsAll);

    miTabla.appendChild(tbBody);
    miCapa = document.getElementById('resultado');
    miCapa.appendChild(miTabla);
    $(".table").tablesorter({
		sortList: [[0,0]]
	});
});

function verEstadisticas(){

    if ($(".table")){
        $(".table").remove();
    }

    createTable();

    if( $("#appannie").is(':checked')){
        if( $("#allOS").is(':checked')) {
            if( $("#allCategories").is(':checked')){showAllCat(androidKeys, appsAll)}
            else if($("#games").is(':checked')){showGames(androidKeys, appsAll)}
            else showOthers(androidKeys, appsAll);
        }

        if( $("#android").is(':checked')) {
            if( $("#allCategories").is(':checked')){showAllCat(androidKeys, appsAndroid)}
            else if($("#games").is(':checked')){showGames(androidKeys, appsAndroid)}
            else showOthers(androidKeys, appsAndroid);
        }

        if( $("#ios").is(':checked')) {
            if( $("#allCategories").is(':checked')){showAllCat(iosKeys, appsIOS)}
            else if($("#games").is(':checked')){showGames(iosKeys, appsIOS)}
            else showOthers(iosKeys, appsIOS);
        }
    }else if($("#flurry").is(':checked')){
        if( $("#allOS").is(':checked')) {
            if( $("#allCategories").is(':checked')){showAllCat(flurryAllKeys, appsFlurryAll)}
            else if($("#games").is(':checked')){showGames(flurryAllKeys, appsFlurryAll)}
            else showOthers(flurryAllKeys, appsFlurryAll);
        }

        if( $("#android").is(':checked')) {
            if( $("#allCategories").is(':checked')){showAllCat(flurryKeys, appsFlurry, "android")}
            else if($("#games").is(':checked')){showGames(flurryKeys, appsFlurry, "android")}
            else showOthers(flurryKeys, appsFlurry, "android");
        }

        if( $("#ios").is(':checked')) {
            if( $("#allCategories").is(':checked')){showAllCat(flurryKeys, appsFlurry, "ios")}
            else if($("#games").is(':checked')){showGames(flurryKeys, appsFlurry, "ios")}
            else showOthers(flurryKeys, appsFlurry, "ios");
        }
    }

    miTabla.appendChild(tbBody);
    miCapa = document.getElementById('resultado');
    miCapa.appendChild(miTabla);
    $(".table").tablesorter({
		sortList: [[0,0]]
	});
}

function showAllCat(osKeys, appsOS, OS){
    for (var k in osKeys){
        if (osKeys.hasOwnProperty(k)) {
            if (OS == "android"){
                if (appsOS[osKeys[k]][3].indexOf("ndroid") > -1){
                    addRow(appsOS,osKeys,k);
                }
            }else if(OS == "ios"){
                if (appsOS[osKeys[k]][3].indexOf("hone") > -1){
                    addRow(appsOS,osKeys,k);
                }
            }else{
                addRow(appsOS, osKeys, k);
            }

        }
    }
}

function showGames(osKeys, appsOS, OS){
    for (var k in osKeys){
        if (osKeys.hasOwnProperty(k)) {
            if(appsOS[osKeys[k]][1].toLowerCase().indexOf("game") > -1){
                if (OS == "android"){
                    if (appsOS[osKeys[k]][3].indexOf("ndroid") > -1){
                        addRow(appsOS,osKeys,k);
                    }
                }else if(OS == "ios"){
                    if (appsOS[osKeys[k]][3].indexOf("hone") > -1){
                        addRow(appsOS,osKeys,k);
                    }
                }else{
                    addRow(appsOS, osKeys, k);
                }
            }
        }
    }
}

function showOthers(osKeys, appsOS, OS){
    for (var k in osKeys){
        if (osKeys.hasOwnProperty(k)) {
            if(appsOS[osKeys[k]][1].toLowerCase().indexOf("game") == -1){
                if (OS == "android"){
                    if (appsOS[osKeys[k]][3].indexOf("ndroid") > -1){
                        addRow(appsOS,osKeys,k);
                    }
                }else if(OS == "ios"){
                    if (appsOS[osKeys[k]][3].indexOf("hone") > -1){
                        addRow(appsOS,osKeys,k);
                    }
                }else{
                addRow(appsOS, osKeys, k);
                }
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
    th1.setAttribute("style", "text-align:center");
    th2.setAttribute("style", "text-align:center");
    th1.innerHTML = "Name";
    th2.innerHTML = "Downloads";

    tr1.setAttribute("class", "active");
    tr1.appendChild(th1);
    tr1.appendChild(th2);

    tbHead.appendChild(tr1);

    miTabla.appendChild(tbHead);
    miTabla.setAttribute("class", "table table-bordered");
}

function addRow(appsOS, osKey, k){
    tr2 = document.createElement("tr");
    td1 = document.createElement("td");
    td2 = document.createElement("td");
    td1.setAttribute("align", "center");
    td2.setAttribute("align", "center");
    if ((appsOS == appsIOS) && (appsOS[osKey[k]][0].indexOf("-") > -1)){
        td1.innerHTML = appsOS[osKey[k]][0].substring(0, appsOS[osKey[k]][0].indexOf("-"));
    }
    else{
        td1.innerHTML = appsOS[osKey[k]][0]
    }
    td2.innerHTML = appsOS[osKey[k]][2];

    tr2.appendChild(td1);
    tr2.appendChild(td2);
    tbBody.appendChild(tr2);
}