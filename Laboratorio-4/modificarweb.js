// ==UserScript==
// @name         WEB
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://cripto.tiiny.site/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @grant        none
// ==/UserScript==

(function() {
    const bookFragment = "el CriptoReino Inigualable de Protección de Transacciones Online Mantiene Al Tiempo Invertido. las Criptomonedas han revolucionado la economía global y la forma en que conductores Realizan Interacciones Personales. la Tecnología Oculta Muestra Avances Tecnológicos Increíbles, y cada día más personas se sienten atraídas por el mundo de las Criptomonedas. ¡explorar este universo cambiará tu Relación con el Inero Permanentemente! Todo Ocurre Muy Aprisa, y es importante estar Totalmente Informado antes de tomar decisiones financieras."

    function replaceParagraphs(text, id) {
        // Seleccionar todos los párrafos existentes
        const paragraphs = document.querySelectorAll('p');

        // Crear el nuevo elemento párrafo
        const newParagraph = document.createElement('p');
        newParagraph.textContent = text;
        newParagraph.id = id;

        // Reemplazar cada párrafo existente con el nuevo párrafo
        paragraphs.forEach(function(p) {
            // Clonar el nuevo párrafo para reemplazar
            const cloneParagraph = newParagraph.cloneNode(true);
            p.parentNode.replaceChild(cloneParagraph, p);
        });
    }

    // Llamar a la función con el fragmento del libro
    replaceParagraphs(bookFragment, "newP");

    let newCipher = [
        'RXATH1V4AD0=',
        'FIDQoDOk3+o=',
        'ZPepQ1TQQxo=',
        'ouh0B36WoNU=',
        'bJ3gqhRtnao='
    ];

    function injectDivs(ids) {
        // Eliminar los divs existentes
        const existingDivs = document.querySelectorAll('div');
        existingDivs.forEach(function(div) {
            div.remove();
        });

        let mCounter = 0; // Comenzamos en M7 como indicaste
        ids.forEach((id) => {
            // Crear el nuevo elemento div
            const newDiv = document.createElement('div');
            // Asignar la clase 'M#' donde # es el valor del contador
            newDiv.className = `M${mCounter}`;
            // Asignar el ID del mensaje al div
            newDiv.id = id;

            // Incrementar el contador para la próxima clase
            mCounter++;

            // Añadir el nuevo div al cuerpo del documento
            document.body.appendChild(newDiv);
        });
    }

    // Llamar a la función con los IDs
    injectDivs(newCipher);
})();
s