
function addLoadingElementTable(table) {
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
    let e = document.getElementById(table);
    const tr_qnPyJ = document.createElement('tr');
    tr_qnPyJ.classList.add('loadingTr');
    tr_qnPyJ.classList.add('placeholder-glow');
    tr_qnPyJ.setAttribute(`aria-hidden`, `true`);
    e.appendChild(tr_qnPyJ);
    const th_pzBZb = document.createElement('th');
    th_pzBZb.setAttribute(`scope`, `row`);
    tr_qnPyJ.appendChild(th_pzBZb);
    const span_dnHCee = document.createElement('span');
    span_dnHCee.classList.add('placeholder', 'col-12');
    th_pzBZb.appendChild(span_dnHCee);
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