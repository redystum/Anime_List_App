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