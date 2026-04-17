/* ============================================
   SCRIPT - Funzioni del sito
   ============================================ */

// Ore totali del corso - MODIFICA questo numero con le ore del tuo corso
let ore = 999;

// Calcola la percentuale di presenze
function assenze() {
    let giorni = parseInt(document.getElementById("progresso").value);
    if (isNaN(giorni) || giorni < 0) {
        giorni = 0;
    }
    
    let oreAssenza = giorni * 6;
    let orePresente = ore - oreAssenza;
    let percentuale = Math.max(0, Math.round((100 * orePresente) / ore));
    
    // Aggiorna la barra
    document.getElementById("barra").style.width = percentuale + "%";
    
    // Aggiorna il testo
    let testo = document.getElementById("percentuale-text");
    if (testo) {
        testo.textContent = "Presenze: " + percentuale + "%";
    }
}
