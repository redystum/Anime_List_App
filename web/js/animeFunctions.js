cl = console.log;

function startSearch() {
    // ez understand peace of code
    anime = document.getElementById('animeNameAdd').value;
    if (anime == "" || anime == " ") {
        showToast("Error", "Please enter an anime name", "red", "soft-black")
    } else {
        // remove field content
        document.getElementById('animeNameAdd').value = ""
        // activate verification to close the window
        window.running = true;

        // activate loading animation
        addLoadingElementTable();

        // call python function
        if (anime.startsWith("id:")) { // if anime is an id
            getAnimeData(anime.replace("id:", ""));
        } else {
            eel.getAnime(anime)
        }
    }
}

function showToast(title, msg, colorH, colorT) {
    // set toast colors and text
    document.getElementById("toastHeader").style.backgroundColor = `var(--${colorH})`;
    document.getElementById("toastBodyText").style.backgroundColor = `var(--${colorT})`;
    document.getElementById("toastBodyText").innerHTML = msg;
    document.getElementById("toastTitle").innerHTML = title;
    // show toast
    toast = document.getElementById('toast');
    var bsToast = new bootstrap.Toast(toast)
    bsToast.show()
}

// expose function to be called from python
eel.expose(chooseAnime);
function chooseAnime(animeList) {
    //remove all children (including loading animation)
    removeAllChildren('chooseAnimeBody');

    let e = document.getElementById("chooseAnimeBody");
    // Create Table
    // code generated from www.htmltojs.com (Its normal to have random var names)
    const table_AuwCe = document.createElement('table');
    table_AuwCe.classList.add('table', 'tableHover');
    e.appendChild(table_AuwCe);
    const thead_JZGJr = document.createElement('thead');
    table_AuwCe.appendChild(thead_JZGJr);
    const tr_WzGul = document.createElement('tr');
    thead_JZGJr.appendChild(tr_WzGul);
    const th_wSlfO = document.createElement('th');
    th_wSlfO.classList.add('text-center');
    th_wSlfO.setAttribute(`scope`, `col`);
    tr_WzGul.appendChild(th_wSlfO);
    th_wSlfO.textContent += `Image`;
    const th_bdiDy = document.createElement('th');
    th_bdiDy.setAttribute(`scope`, `col`);
    tr_WzGul.appendChild(th_bdiDy);
    th_bdiDy.textContent += `Name`;
    const tbody_eutXG = document.createElement('tbody');

    // insert data on table
    for (let i = 0; i < animeList.length; i++) {
        table_AuwCe.appendChild(tbody_eutXG);
        const tr_pFSpQ = document.createElement('tr');
        tbody_eutXG.appendChild(tr_pFSpQ);
        const td_ZEsLC = document.createElement('td');
        tr_pFSpQ.appendChild(td_ZEsLC);
        const img_blHfy = new Image();
        img_blHfy.src = animeList[i].node.main_picture.large;
        img_blHfy.setAttribute(`width`, `50px`);
        img_blHfy.setAttribute(`onclick`, `getAnimeData(${animeList[i].node.id})`);
        img_blHfy.classList.add('animeNameChooseTable');
        td_ZEsLC.appendChild(img_blHfy);
        const td_MgHCv = document.createElement('td');
        td_MgHCv.classList.add('tableName');
        td_MgHCv.id = 'chooseNameTable';
        tr_pFSpQ.appendChild(td_MgHCv);
        const a_KgCmV = document.createElement('a');
        a_KgCmV.classList.add('animeNameChooseTable');
        a_KgCmV.setAttribute(`onclick`, `getAnimeData(${animeList[i].node.id})`);
        td_MgHCv.appendChild(a_KgCmV);
        a_KgCmV.textContent += animeList[i].node.title;
    }

    table_AuwCe.appendChild(tbody_eutXG);
    const tr_pFSpQ = document.createElement('tr');
    tbody_eutXG.appendChild(tr_pFSpQ);
    const td_MgHCv = document.createElement('td');
    td_MgHCv.setAttribute(`colspan`, `2`);
    td_MgHCv.classList.add('tableName');
    td_MgHCv.id = 'chooseNameTable';
    tr_pFSpQ.appendChild(td_MgHCv);
    const p_KgCmV = document.createElement('p');
    td_MgHCv.appendChild(p_KgCmV);
    p_KgCmV.textContent += "if you can't find the anime you want:";
    const ul = document.createElement('ul');
    td_MgHCv.appendChild(ul);
    const li = document.createElement('li');
    ul.appendChild(li);
    li.textContent += "Check if you wrote it correctly or try to write another title of the same anime";
    const li_1 = document.createElement('li');
    ul.appendChild(li_1);
    li_1.textContent += "Write the id of myanimelist.net like this: ";
    const code = document.createElement('code');
    li_1.appendChild(code);
    code.textContent += "id:30";

    // launch modal
    const myModal = new bootstrap.Modal(document.getElementById('chooseAnimeModal'))
    myModal.show()

}

function addLoadingElementTable() {
    // block "add anime" fields
    changeSearchDisableStatus(true);
    // stop glow animation
    for (let i = 0; i < document.querySelectorAll(".glowActivator").length; i++) {
        let el = document.querySelectorAll(".glowActivator")[i]
        target = el.dataset.target;
        document.querySelector("#" + target).classList.remove("glowShadow");
    }

    // create loading element
    // basically add a table row with a loading animation instead anime data
    // code generated from www.htmltojs.com (Its normal to have random var names)
    let e = document.getElementById("animeListTable")
    const tr_qnPyJ = document.createElement('tr');
    tr_qnPyJ.classList.add('loadingTr');
    tr_qnPyJ.classList.add('placeholder-glow');
    tr_qnPyJ.setAttribute(`aria-hidden`, `true`);
    e.appendChild(tr_qnPyJ);
    const th_pzBZb = document.createElement('th');
    th_pzBZb.setAttribute(`scope`, `row`);
    tr_qnPyJ.appendChild(th_pzBZb);
    const span_BlbSw = document.createElement('span');
    span_BlbSw.classList.add('iconElement', 'placeholder');
    span_BlbSw.setAttribute(`data-icon`, `done`);
    span_BlbSw.setAttribute(`data-tooltip`, `Viewed`);
    th_pzBZb.appendChild(span_BlbSw);
    const span_GMNDn = document.createElement('span');
    span_GMNDn.classList.add('iconElement', 'placeholder');
    span_GMNDn.setAttribute(`data-icon`, `delete`);
    span_GMNDn.setAttribute(`data-tooltip`, `delete`);
    th_pzBZb.appendChild(span_GMNDn);
    const td_KuaCl = document.createElement('td');
    tr_qnPyJ.appendChild(td_KuaCl);
    const img_PWaZk = new Image();
    img_PWaZk.classList.add('placeholder');
    img_PWaZk.setAttribute(`width`, `50px`);
    img_PWaZk.setAttribute(`height`, `75px`);
    td_KuaCl.appendChild(img_PWaZk);
    const td_PlKlG = document.createElement('td');
    td_PlKlG.classList.add('tableName');
    tr_qnPyJ.appendChild(td_PlKlG);
    const td_xmaE = document.createElement('td');
    tr_qnPyJ.appendChild(td_xmaE);
    const span_dnHCe = document.createElement('span');
    span_dnHCe.classList.add('placeholder', 'col-7');
    td_PlKlG.appendChild(span_dnHCe);
    const td_rVKtA = document.createElement('td');
    td_rVKtA.classList.add('text-center');
    tr_qnPyJ.appendChild(td_rVKtA);
    const span_WJhWT = document.createElement('span');
    span_WJhWT.classList.add('placeholder', 'col-12');
    td_rVKtA.appendChild(span_WJhWT);
    const td_xmaEo = document.createElement('td');
    td_xmaEo.classList.add('text-center');
    tr_qnPyJ.appendChild(td_xmaEo);
    const span_eHXfe = document.createElement('span');
    span_eHXfe.classList.add('placeholder', 'col-7');
    td_xmaEo.appendChild(span_eHXfe);
    const td_eoLpi = document.createElement('td');
    td_eoLpi.classList.add('tableStars');
    tr_qnPyJ.appendChild(td_eoLpi);
    const span_aZHlj = document.createElement('span');
    span_aZHlj.classList.add('placeholder', 'col-11');
    td_eoLpi.appendChild(span_aZHlj);
    // call function to add icons to respective elements
    putIcon();
}

async function getAnimeData(AnimeId) {
    // hide modal
    document.getElementById('closeModal').click();

    // call python function
    data = await eel.AnimeData(AnimeId)();
    if (data == "not_found") {
        // if error, show error message
        showToast("Error", `Anime with id ${AnimeId} was not found! Try again with some existing id.`, 'red', 'soft-black')
        // remove loading element
        removeLoading_NoAnime('animeListTable');
        // enable search fields
        changeSearchDisableStatus(false);
        // permit the window be closed without warns
        window.running = false;
        return
    }
    // data processing
    animeID = data.id;
    title = data.title;
    img = data.main_picture.large;
    episodes = ((data.num_episodes != 0) ? data.num_episodes : "Unknown");
    score = data.mean;

    // insert data on table
    addAnimeToTable(animeID, title, img, episodes, score, "", 0, "\"Processing...\"", "p");

    // call function to add icons to respective elements
    putIcon();
    // permit the window be closed without warns
    window.running = false;

    // remove loading animation and no anime message
    removeLoading_NoAnime('animeListTable');
    // activate "add anime" fields
    changeSearchDisableStatus(false);
}

async function getAnimeList(order = 0) {
    // remove all children (including loading animation)
    removeAllChildren('animeListTable');
    // add loading animation
    addLoadingElementTable();

    // call python function
    data = await eel.getAnimeList(order)();
    if (data.length == 0) {
        appendNoAnime();
        changeSearchDisableStatus(true);
        changeSearchDisableStatus(false);
        return;
    }
    for (let i = 0; i < data.length; i++) {
        // call function to add anime to table
        addAnimeToTable(data[i].animeID, data[i].title, data[i].image, data[i].episodes, data[i].globalScore, data[i].notes, data[i].viewed, data[i].id);
    }
    // permit the window be closed without warns
    putIcon();
    // remove loading animation and no anime message
    removeLoading_NoAnime('animeListTable');
    // activate "add anime" fields
    changeSearchDisableStatus(false);
}

function appendNoAnime() {
    // add a no anime message
    const e = document.getElementById("animeListTable");
    const tr = document.createElement('th');
    tr.classList.add('text-center');
    tr.colSpan = 6;
    tr.textContent += "No Anime yet";
    tr.classList.add("noAnime");
    e.appendChild(tr);
}

function addAnimeToTable(AnimeId, AnimeTitle, AnimeImg, AnimeEpisodes, AnimeScore, AnimeNotes, AnimeViewed, id, AnimeStatus = "complete") {
    if (AnimeViewed == false || AnimeViewed == "False") {
        let e = document.getElementById("animeListTable") // table for non viewed anime
    } else {
        let e = document.getElementById("ViewedAnimeListTable") // table for viewed anime (coming soon)
        e = document.getElementById("animeListTable")
    }

    // define some vars to the recommended icon
    let scoreText = ""
    let cssClass = ""
    if (AnimeScore < 5) {
        scoreText = "not highly recommended"
        cssClass = "negativeScore"
    } else if (AnimeScore > 5) {
        scoreText = "highly recommended"
        cssClass = "positiveScore"
    } else {
        scoreText = "recommended"
        cssClass = "middleScore"
    }

    // add the anime to the table
    let e = document.getElementById("animeListTable")
    // code generated from www.htmltojs.com (Its normal to have random var names)
    const tr_pyFdT = document.createElement('tr');
    tr_pyFdT.id = `Anime${AnimeId}_` + ((id == "\"Processing...\"") ? "" : id);
    e.appendChild(tr_pyFdT);
    const th_umBZQ = document.createElement('th');
    th_umBZQ.setAttribute(`scope`, `row`);
    tr_pyFdT.appendChild(th_umBZQ);
    const span_tIvWc = document.createElement('span');
    span_tIvWc.classList.add('iconElement');
    span_tIvWc.setAttribute(`data-icon`, `done`);
    span_tIvWc.setAttribute(`data-tooltip`, `Viewed`);
    span_tIvWc.setAttribute(`onclick`, `setViewed(${id}, ${AnimeId})`);
    if (AnimeStatus === "p") { // if the anime is being processed, don't allow to change her state
        span_tIvWc.classList.add(`processing`);
    }
    th_umBZQ.appendChild(span_tIvWc);
    const span_umBrx = document.createElement('span');
    span_umBrx.classList.add('iconElement');
    span_umBrx.setAttribute(`data-icon`, `delete`);
    span_umBrx.setAttribute(`data-tooltip`, `Delete`);
    span_umBrx.setAttribute(`onclick`, `deleteAnime(${id}, ${AnimeId})`);
    if (AnimeStatus === "p") { // if the anime is being processed, don't allow to delete it
        span_umBrx.classList.add(`processing`);
    }
    th_umBZQ.appendChild(span_umBrx);
    const td_XRgDI = document.createElement('td');
    tr_pyFdT.appendChild(td_XRgDI);
    const img_QdMhX = new Image();
    img_QdMhX.src = AnimeImg;
    img_QdMhX.setAttribute(`width`, `50px`);
    td_XRgDI.appendChild(img_QdMhX);
    const td_qzEBp = document.createElement('td');
    const a_QZqZ = document.createElement('span');
    a_QZqZ.classList.add(`AnimeName`);
    a_QZqZ.textContent += AnimeTitle;
    td_qzEBp.classList.add('tableName');
    td_qzEBp.appendChild(a_QZqZ);
    tr_pyFdT.appendChild(td_qzEBp);
    const td_info = document.createElement('td');
    tr_pyFdT.appendChild(td_info);
    const span_info = document.createElement('span');
    span_info.classList.add('iconElement', 'infoBtn');
    span_info.setAttribute(`data-icon`, `info`);
    span_info.setAttribute(`data-tooltip`, `More Info`);
    span_info.setAttribute(`onclick`, `showMoreInfo(${AnimeId})`);
    td_info.appendChild(span_info);
    const td_JAGvf = document.createElement('td');
    td_JAGvf.classList.add('text-center', 'animeNotesTd');
    tr_pyFdT.appendChild(td_JAGvf);
    if (AnimeNotes != "") {
        const span_tIvW = document.createElement('span');
        span_tIvW.classList.add('iconElement', 'notesIcon');
        span_tIvW.setAttribute(`data-icon`, `description`);
        span_tIvW.setAttribute(`data-tooltip`, `Show Notes`);
        span_tIvW.setAttribute(`data-popover-text`, AnimeNotes);
        span_tIvW.setAttribute(`data-popover-title`, "Notes");
        span_tIvW.setAttribute(`data-type`, 'popover');
        td_JAGvf.appendChild(span_tIvW);
    }
    const td_jqFGF = document.createElement('td');
    td_jqFGF.classList.add('text-center');
    tr_pyFdT.appendChild(td_jqFGF);
    td_jqFGF.textContent += AnimeEpisodes;
    const td_aobBl = document.createElement('td');
    const span_VfUf = document.createElement('span');
    span_VfUf.classList.add('iconElement', cssClass);
    span_VfUf.setAttribute(`data-icon`, `recommend`);
    span_VfUf.setAttribute(`data-tooltip`, scoreText);
    td_aobBl.classList.add('tableStars');
    td_aobBl.appendChild(span_VfUf);
    const p_qzEBp = document.createElement('p');
    p_qzEBp.textContent = AnimeScore;
    td_aobBl.appendChild(p_qzEBp);
    tr_pyFdT.appendChild(td_aobBl);
}

function cancelAddAnime() {
    // activate "add anime" fields
    changeSearchDisableStatus(false);
    // remove loading animation and no anime message
    removeLoading_NoAnime('animeListTable');
    // permit the window be closed without warns
    window.running = false;
}

async function setViewed(id, AnimeId) {
    // if the anime are being processed, don't allow to change her state
    if (id == "Processing...") {
        showToast("Error", "The anime is still processing, please try again later (30s max) ", "red", "soft-black")
        return;
    }
    // call python function
    eel.setViewed(id)();
    // remove anime from table
    await removeTableElement('animeListTable', id, AnimeId)
    ifEmptyList('animeListTable')
}

async function deleteAnime(id, AnimeId) {
    // if the anime are being processed, don't allow to delete it
    if (id == "Processing...") {
        showToast("Error", "The anime is still processing, please try again later (30s max) ", "red", "soft-black")
        return;
    }
    // call python function
    eel.deleteAnime(id)();
    // remove anime from table
    await removeTableElement('animeListTable', id, AnimeId)
    ifEmptyList('animeListTable')
}

function pickRandom(table) {
    // choose a random anime from the not viewed list
    let e = document.getElementById(table).childNodes
    let animeList = []
    e.forEach(element => {
        if (element.id == undefined) { }
        else if (element.id == "") { }
        else if (element.id == null) { }
        else {
            animeList.push(element.id)
        }
    });
    cl(animeList)
    let randomAnime = animeList[Math.floor(Math.random() * animeList.length)]
    let el = document.getElementById(`${randomAnime}`).getElementsByClassName("infoBtn")[0]
    el.click()
}

// expose function to be called from python
eel.expose(changeBtnId);
function changeBtnId(id) {
    // when called from python, change the delete/viewed button onclick function to the right id
    for (let i = 0; i < document.getElementsByClassName("processing").length; i++) {
        document.getElementsByClassName("processing")[i].classList.remove("processing");
        func = document.getElementsByClassName("processing")[i].getAttribute("onclick");
        document.getElementsByClassName("processing")[i].removeAttribute("onclick");
        document.getElementsByClassName("processing")[i].setAttribute("onclick", func.replace("\"Processing...\"", id));
        document.getElementsByClassName("processing")[i].parentElement.parentElement.id += id;
    }
}

function saveScoreAndNotes() {
    notes = document.getElementById("inpNotesModal").value;
    score = document.getElementById("localScoreInp").value;
    id = document.getElementById("moreInfoModalAnimeId").textContent;
    animeId = document.getElementById("moreInfoModalAnimeIdMAL").textContent;
    eel.updateNotesAndScore(notes, score, id);
    if (notes == "") {
        document.getElementById(`Anime${animeId}_${id}`).getElementsByClassName("notesIcon")[0].remove()
    } else {
        try {
            document.getElementById(`Anime${animeId}_${id}`).getElementsByClassName("notesIcon")[0].setAttribute("data-popover-text", notes);
        } catch (e) {
            let el = document.getElementById(`Anime${animeId}_${id}`).getElementsByClassName("animeNotesTd")[0]
            const span_tIvW = document.createElement('span');
            span_tIvW.classList.add('iconElement', 'notesIcon');
            span_tIvW.setAttribute(`data-icon`, `description`);
            span_tIvW.setAttribute(`data-tooltip`, `Show Notes`);
            span_tIvW.setAttribute(`data-popover-text`, notes);
            span_tIvW.setAttribute(`data-popover-title`, "Notes");
            span_tIvW.setAttribute(`data-type`, 'popover');
            el.appendChild(span_tIvW);
        }
    }
    putIcon();
}

//! Auxiliary functions (these functions are not really necessary, they only save code lines)

function changeSearchDisableStatus(status) {
    // change the disable status of the buttons and inputs
    document.getElementById("addAnimeBtn").disabled = status;
    document.getElementById("animeNameAdd").disabled = status;
}
function closeToolTips() {
    // close all tooltips, because they are not disappear when the element is removed
    let tooltips = document.querySelectorAll('.tooltip-inner');
    for (let i = 0; i < tooltips.length; i++) {
        tooltips[i].remove();
    }
    tooltips = document.querySelectorAll('.tooltip');
    for (let i = 0; i < tooltips.length; i++) {
        tooltips[i].remove();
    }
}
function removeTableElement(table, id, AnimeId) {
    // remove a specific element from the table
    let tb = document.getElementById(table);
    tb.querySelectorAll(`#Anime${AnimeId}_${id}`)[0].remove();
}
function ifEmptyList(table) {
    // if the table is empty, show a message
    let e = document.getElementById(table);
    cl(e)
    var child = e.lastElementChild;
    cl(child)
    if (child == null) {
        addLoadingElementTable();
        appendNoAnime();
        changeSearchDisableStatus(false);
    }
}
function removeLoading_NoAnime(table) {
    // remove loading animation and no anime message
    let e = document.getElementById(table);
    for (let i = e.getElementsByClassName("loadingTr").length; i > 0; i--) {
        e.getElementsByClassName("loadingTr")[i - 1].remove();
    }
    for (let i = e.getElementsByClassName("noAnime").length; i > 0; i--) {
        e.getElementsByClassName("noAnime")[i - 1].remove();
    }
}
function removeAllChildren(table) {
    // remove all children of an element
    let e = document.getElementById(table);
    var child = e.lastElementChild;
    while (child) {
        e.removeChild(child);
        child = e.lastElementChild;
    }
}