function addAnimeToTable(AnimeId, AnimeTitle, AnimeImg, AnimeEpisodes, AnimeScore, AnimeNotes, AnimeViewed, id, favorite, AnimeStatus = "complete") {
    let e;
    if (AnimeViewed == true) {
        e = document.getElementById("watchedAnimeListTable") // table for viewed anime
    } else {
        e = document.getElementById("animeListTable") // table for non viewed anime
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
    // code generated from www.htmltojs.com (Its normal to have random var names)
    const tr_pyFdT = document.createElement('tr');
    tr_pyFdT.id = `Anime${AnimeId}_` + ((id == "\"Processing...\"") ? "" : id);
    e.appendChild(tr_pyFdT);
    const th_umBZQ = document.createElement('th');
    th_umBZQ.setAttribute(`scope`, `row`);
    th_umBZQ.classList.add(`actionsBtns`);
    tr_pyFdT.appendChild(th_umBZQ);
    const span_tIvWc = document.createElement('span');
    span_tIvWc.classList.add('iconElement');
    if (AnimeViewed == true) {
        span_tIvWc.setAttribute(`data-icon`, `remove_done`);
        span_tIvWc.setAttribute(`data-tooltip`, `Unview`);
        span_tIvWc.setAttribute(`onclick`, `setUnview(${id}, ${AnimeId})`);
    } else {
        span_tIvWc.setAttribute(`data-icon`, `done`);
        span_tIvWc.setAttribute(`data-tooltip`, `Viewed`);
        span_tIvWc.setAttribute(`onclick`, `setViewed(${id}, ${AnimeId})`);
    }
    if (AnimeStatus === "p") { // if the anime is being processed, don't allow to change her state
        span_tIvWc.classList.add(`processing`);
    }
    th_umBZQ.appendChild(span_tIvWc);
    const span_umBrx = document.createElement('span');
    span_umBrx.classList.add('iconElement');
    span_umBrx.setAttribute(`data-icon`, `delete`);
    span_umBrx.setAttribute(`data-tooltip`, `Delete`);
    span_umBrx.setAttribute(`onclick`, `deleteAnime(${id}, ${AnimeId}, ${+AnimeViewed})`);
    if (AnimeStatus === "p") { // if the anime is being processed, don't allow to delete it
        span_umBrx.classList.add(`processing`);
    }
    th_umBZQ.appendChild(span_umBrx);
    if (AnimeViewed == true) {
        if (favorite == true) {
        const span_umBrx = document.createElement('span');
        span_umBrx.classList.add('iconElement');
        span_umBrx.setAttribute(`data-icon`, `favorite`);
        span_umBrx.setAttribute(`data-tooltip`, `Marked as favorite`);
        span_umBrx.setAttribute(`onclick`, `removeFav(${id}, ${AnimeId})`);
        th_umBZQ.appendChild(span_umBrx);
    } else {
        const span_umBrx = document.createElement('span');
        span_umBrx.classList.add('iconElement');
        span_umBrx.setAttribute(`data-icon`, `heart_plus`);
        span_umBrx.setAttribute(`data-tooltip`, `Add to favorites`);
        span_umBrx.setAttribute(`onclick`, `addFav(${id}, ${AnimeId})`);
        th_umBZQ.appendChild(span_umBrx);
        }
    }
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