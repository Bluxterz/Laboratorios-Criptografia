// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://cripto.tiiny.site/
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tampermonkey.net
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Función para obtener y mostrar las letras mayúsculas
    function almacenarMayusculas(texto) {
        const mayusculas = texto.match(/[A-Z]/g);
        var key;

        if (mayusculas) {
            key = mayusculas.join('')
            console.log('Letras mayúsculas: ' + mayusculas.join(''));
        } else {
            console.log('No se encontraron letras mayúsculas en el texto.');
        }
        return key;
    }

    // Función para obtener y mostrar los IDs de los elementos <div> y contarlos
    function obtenerIDsDeDivs() {
        const divs = document.querySelectorAll('div');
        const divIDs = Array.from(divs).map(div => div.id);
        var mensajes = [];

        if (divIDs.length > 0) {
            console.log('Los mensajes cifrados son: ' + divIDs.length);
            mensajes.push(divIDs);
        } else {
            console.log('No se encontraron elementos <div> con IDs.');
        }
        return mensajes;
    }

    function descifrar(mensajes, key) {
        mensajes[0].forEach(id => {
            let elementoDiv = document.getElementById(id);
            if (elementoDiv) {
                let mensajeCifrado = id;
                let mensajeDesencriptado = CryptoJS.TripleDES.decrypt(mensajeCifrado, CryptoJS.enc.Utf8.parse(key), { mode: CryptoJS.mode.ECB }).toString(CryptoJS.enc.Utf8);
                console.log(id + ' ' + mensajeDesencriptado);

                let resultadoElemento = document.createElement('p');
                resultadoElemento.textContent = mensajeDesencriptado;
                document.body.appendChild(resultadoElemento);
            }
        });
    }


    const elemento = document.querySelector('p'); // Cambia 'p' por el selector adecuado

    if (elemento) {
        // Aplica la función de almacenar mayúsculas al contenido del elemento
        var clave = almacenarMayusculas(elemento.textContent);
    }

    // Llama a la función para obtener y mostrar los IDs de los elementos <div> y contarlos
    var mensajesCifrados = obtenerIDsDeDivs();
    descifrar(mensajesCifrados, clave); // Pasamos mensajesCifrados como un array

})();
