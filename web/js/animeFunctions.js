cl = console.log;

function startSearch() {
    // ez understand peace of code
    anime = document.getElementById('animeNameAdd').value;
    closeToolTips();
    if (anime == "" || anime == " ") {
        showToast("Error", "Please enter an anime name", "red", "soft-black")
    } else {
        // remove field content
        document.getElementById('animeNameAdd').value = ""
        // activate verification to close the window
        window.running = true;

        // activate loading animation
        addLoadingElementTable('animeListTable');

        // call python function
        if (anime.startsWith("id:")) { // if anime is an id
            getAnimeData(anime.replace("id:", ""));
        } else {
            eel.getAnime(anime)
        }
    }
}
// expose function to python
eel.expose(showToast);
function showToast(title, msg, colorH, colorT) {
    // set toast colors and text
    document.getElementById("toastHeader").style.backgroundColor = `var(--${colorH})`;
    document.getElementById("toastBodyText").style.backgroundColor = `var(--${colorT})`;
    let color;
    if (colorH == "soft-green") {
        color = "black";
    }
    document.getElementById("toastHeader").style.color = color;
    document.getElementById("toastBodyText").innerHTML = msg;
    document.getElementById("toastTitle").innerHTML = title;
    // show toast
    toast = document.getElementById('toast');
    var bsToast = new bootstrap.Toast(toast)
    bsToast.show()
}

async function getAnimeData(AnimeId) {
    closeToolTips();
    // hide modal
    document.getElementById('closeModal').click();

    // call python function
    data = await eel.AnimeData(AnimeId)();
    if (data == "not_found") {
        // if error, show error message
        showToast("Error", `Anime with id ${AnimeId} was not found! Try again with some existing id.`, 'red', 'soft-black')
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
    fav = data.favorite;

    // insert data on table
    addAnimeToTable(animeID, title, img, episodes, score, "", 0, "\"Processing...\"",fav, "p");

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
    closeToolTips();
    // remove all children (including loading animation)
    removeAllChildren('animeListTable');
    removeAllChildren('watchedAnimeListTable');
    // add loading animation
    addLoadingElementTable('animeListTable');
    addLoadingElementTable('watchedAnimeListTable');

    // call python function
    data = await eel.getAnimeList(order)();
    if (data.length == 0) {
        appendNoAnime('animeListTable');
        appendNoAnime('watchedAnimeListTable');
        changeSearchDisableStatus(true);
        changeSearchDisableStatus(false);
        return;
    }
    for (let i = 0; i < data.length; i++) {
        // call function to add anime to table
        addAnimeToTable(data[i].animeID, data[i].title, data[i].image, data[i].episodes, data[i].globalScore, data[i].notes, data[i].viewed, data[i].id, data[i].favorite);
    }
    // call function to add icons to respective elements
    putIcon();

    // remove loading animation and no anime message
    removeLoading_NoAnime('watchedAnimeListTable');
    removeLoading_NoAnime('animeListTable');
    ifEmptyList('animeListTable');
    ifEmptyList('watchedAnimeListTable');

    // activate "add anime" fields
    changeSearchDisableStatus(false);
}

function appendNoAnime(table) {
    closeToolTips();
    // add a no anime message
    const e = document.getElementById(table);
    const tr = document.createElement('th');
    tr.classList.add('text-center');
    tr.colSpan = 6;
    tr.textContent += "No Anime yet";
    tr.classList.add("noAnime");
    e.appendChild(tr);
}

function cancelAddAnime() {
    closeToolTips();
    // activate "add anime" fields
    changeSearchDisableStatus(false);
    // remove loading animation and no anime message
    removeLoading_NoAnime('animeListTable');
    // permit the window be closed without warns
    window.running = false;
}

async function setViewed(id, AnimeId) {
    closeToolTips();
    // if the anime are being processed, don't allow to change her state
    if (id == "Processing...") {
        showToast("Error", "The anime is still processing, please try again later (30s max) ", "red", "soft-black")
        return;
    }
    // call python function
    eel.setViewed(id)();
    // move anime to the other table
    let el = document.getElementById(`Anime${AnimeId}_${id}`);
    const tr = document.getElementById('watchedAnimeListTable')
    tr.appendChild(el);
    // change actions buttons
    removeLoading_NoAnime('watchedAnimeListTable');
    el = document.getElementById(`Anime${AnimeId}_${id}`);
    actionBtns = el.getElementsByClassName('actionsBtns')[0]
    var child = actionBtns.lastElementChild;
    while (child) {
        actionBtns.removeChild(child);
        child = actionBtns.lastElementChild;
    }
    changeActions(actionBtns, id, AnimeId, "view")

    ifEmptyList('animeListTable')
    putIcon();
}

async function deleteAnime(id, AnimeId, table) {
    closeToolTips();
    // if the anime are being processed, don't allow to delete it
    if (id == "Processing...") {
        showToast("Error", "The anime is still processing, please try again later (30s max) ", "red", "soft-black")
        return;
    }
    // call python function
    eel.deleteAnime(id)();
    // remove anime from table
    let t = table ? 'watchedAnimeListTable' : 'animeListTable';
    await removeTableElement(t, id, AnimeId)
    ifEmptyList(t)
}

function pickRandom(table) {
    // choose a random anime from the not viewed list
    closeToolTips();
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
    if (animeList.length == 0) {
        showToast("Error", "No anime to choose from! The random just takes anime from unwatched table, add some and try again.", "red", "soft-black")
        return;
    }
    if (animeList.length == 1) {
        showToast("Info", "Really? If you only have one anime on the list it's kind of obvious which one you're going to get, right?", "soft-green", "soft-black")
        return;
    }
    let randomAnime = animeList[Math.floor(Math.random() * animeList.length)]
    let el = document.getElementById(`${randomAnime}`).getElementsByClassName("infoBtn")[0]
    el.click()
}

// expose function to be called from python
eel.expose(changeBtnId);
function changeBtnId(row, id) {
    // when called from python, change the delete/viewed button onclick function to the right id
    let e = document.getElementById(`Anime${id}_`).getElementsByClassName("processing")
    for (i = e.length; i > 0; i--) {
        func = e[i - 1].getAttribute("onclick");
        e[i - 1].removeAttribute("onclick");
        e[i - 1].setAttribute("onclick", func.replace("\"Processing...\"", row));
        e[i - 1].classList.remove("processing");
    }
    document.getElementById(`Anime${id}_`).id += row;
}

function saveScoreAndNotes() {
    // get and update notes
    notes = document.getElementById("inpNotesModal").value;
    score = document.getElementById("localScoreInp").value;
    id = document.getElementById("moreInfoModalAnimeId").textContent;
    animeId = document.getElementById("moreInfoModalAnimeIdMAL").textContent;
    eel.updateNotesAndScore(notes, score, id);
    // add/remove notes button
    if (notes == "") {
        try{
            document.getElementById(`Anime${animeId}_${id}`).getElementsByClassName("notesIcon")[0].remove()
        } catch (e) {}
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
    // call function to add icons to respective elements
    putIcon();
}

function setUnview(id, animeId){
    closeToolTips();
    // call python function
    eel.setUnviewed(id)();
    // move anime to the other table
    let el = document.getElementById(`Anime${animeId}_${id}`);
    const tr = document.getElementById('animeListTable')
    tr.appendChild(el);
    // change actions buttons
    removeLoading_NoAnime('animeListTable');
    el = document.getElementById(`Anime${animeId}_${id}`);
    actionBtns = el.getElementsByClassName('actionsBtns')[0]
    var child = actionBtns.lastElementChild;
    while (child) {
        actionBtns.removeChild(child);
        child = actionBtns.lastElementChild;
    }
    changeActions(actionBtns, id, animeId, "unview")

    ifEmptyList('watchedAnimeListTable')
    putIcon();
}

function addFav(id, AnimeId) {
    closeToolTips();
    eel.favAnime(id)
    el = document.getElementById(`Anime${AnimeId}_${id}`);
    actionBtns = el.getElementsByClassName('actionsBtns')[0]
    var child = actionBtns.lastElementChild;
    while (child) {
        actionBtns.removeChild(child);
        child = actionBtns.lastElementChild;
    }
    changeActions(actionBtns, id, AnimeId, "view", 1)
    putIcon();
}
function removeFav(id, AnimeId) {
    closeToolTips();
    eel.unFavAnime(id)
    el = document.getElementById(`Anime${AnimeId}_${id}`);
    actionBtns = el.getElementsByClassName('actionsBtns')[0]
    var child = actionBtns.lastElementChild;
    while (child) {
        actionBtns.removeChild(child);
        child = actionBtns.lastElementChild;
    }
    changeActions(actionBtns, id, AnimeId, "view", 0)
    putIcon();
}

function addToList(AnimeId){
    addLoadingElementTable('animeListTable');
    getAnimeData(AnimeId)
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
    var child = e.lastElementChild;
    if (child == null) {
        addLoadingElementTable(table);
        appendNoAnime(table);
        changeSearchDisableStatus(false);
        return true
    }
    return false
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
function removeAllChildren(element) {
    // remove all children of an element
    let e = document.getElementById(element);
    var child = e.lastElementChild;
    while (child) {
        e.removeChild(child);
        child = e.lastElementChild;
    }
}