function relatedAnimeManga(data, title, type) {
    closeToolTips();
    //remove all children (including loading animation)
    let e
    if (type == "anime") {
        e = document.getElementById("relatedAnimeBody")
        document.getElementById("relatedAnimeTitle").innerHTML = "Related Animes to " + title
        removeAllChildren('relatedAnimeBody');
    } else {
        e = document.getElementById("relatedMangaBody")
        document.getElementById("relatedMangaTitle").innerHTML = "Related Manga to " + title
        removeAllChildren('relatedMangaBody');
    }

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
    const th_bdiD = document.createElement('th');
    th_bdiD.setAttribute(`scope`, `col`);
    tr_WzGul.appendChild(th_bdiD);
    th_bdiD.textContent += `Add`;
    const tbody_eutXG = document.createElement('tbody');

    // insert data on table
    for (let i = 0; i < data.length; i++) {
        table_AuwCe.appendChild(tbody_eutXG);
        const tr_pFSpQ = document.createElement('tr');
        tr_pFSpQ.classList.add('relatedTableElement');
        tbody_eutXG.appendChild(tr_pFSpQ);
        const td_ZEsLC = document.createElement('td');
        tr_pFSpQ.appendChild(td_ZEsLC);
        const img_blHfy = new Image();
        img_blHfy.src = data[i].node.main_picture.large;
        img_blHfy.setAttribute(`width`, `50px`);
        td_ZEsLC.appendChild(img_blHfy);
        const td_MgHCv = document.createElement('td');
        td_MgHCv.classList.add('tableName');
        td_MgHCv.id = 'chooseNameTable';
        tr_pFSpQ.appendChild(td_MgHCv);
        const a_KgCmV = document.createElement('p');
        td_MgHCv.appendChild(a_KgCmV);
        a_KgCmV.textContent += data[i].node.title;
        const td_jTPgx = document.createElement('td');
        tr_pFSpQ.appendChild(td_jTPgx);
        if (type == "anime") {
            const span_umBrx = document.createElement('span');
            span_umBrx.classList.add('iconElement', "addToListBtn");
            span_umBrx.setAttribute(`data-icon`, `library_add`);
            span_umBrx.setAttribute(`data-tooltip`, `Add to list`);
            span_umBrx.setAttribute(`onclick`, `addToList(${data[i].node.id})`);
            td_jTPgx.appendChild(span_umBrx);
        }
    }
}