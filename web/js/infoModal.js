async function showMoreInfo(AnimeId) {
    closeToolTips();
    // call python function
    data = await eel.getAnimeInfo(AnimeId)();

    // data processing
    id = data.id;
    title = data.title
    titleJp = data.titleJp
    animeID = data.animeID
    notes = data.notes
    startDate = data.startDate
    endDate = data.endDate
    synopsis = data.synopsis
    episodes = data.episodes
    averageEpDuration = data.averageEpDuration
    globalScore = data.globalScore
    localScore = data.localScore
    pictures = data.pictures
    viewed = data.viewed
    Astatus = data.status
    genres = data.genres
    background = data.background
    studio = data.studio
    relatedAnime = data.relatedAnime
    relatedManga = data.relatedManga

    // remove all childrens
    let e = document.getElementById("moreInfoModalBody");
    // remove all children 
    var child = e.lastElementChild;
    while (child) {
        e.removeChild(child);
        child = e.lastElementChild;
    }

    // set modal content
    document.getElementById("moreInfoModalTitle").innerHTML = title
    document.getElementById("moreInfoModalAnimeId").innerHTML = id
    document.getElementById("moreInfoModalAnimeIdMAL").innerHTML = animeID
    // code generated from www.htmltojs.com (Its normal to have random var names)
    const div_fxEUN = document.createElement('div');
    div_fxEUN.classList.add('container-fluid');
    e.appendChild(div_fxEUN);
    const div_oPtRv = document.createElement('div');
    div_oPtRv.classList.add('row');
    div_fxEUN.appendChild(div_oPtRv);
    const div_zgCJM = document.createElement('div');
    div_zgCJM.classList.add('col-md-12');
    div_oPtRv.appendChild(div_zgCJM);
    div_zgCJM.textContent += titleJp;
    const br_kqSYp = document.createElement('br');
    div_fxEUN.appendChild(br_kqSYp);
    const div_fxVnr = document.createElement('div');
    div_fxVnr.classList.add('row');
    div_fxEUN.appendChild(div_fxVnr);
    const div_ZSvAr = document.createElement('div');
    div_ZSvAr.classList.add('col-md-12');
    div_fxVnr.appendChild(div_ZSvAr);
    const input_KviMo = document.createElement('input');
    input_KviMo.setAttribute(`type`, `text`);
    input_KviMo.id = 'inpNotesModal';
    input_KviMo.setAttribute(`autocomplete`, `off`);
    input_KviMo.setAttribute(`placeholder`, `Write a note`);
    if (notes != "") {
        input_KviMo.setAttribute(`value`, notes);
    }
    div_ZSvAr.appendChild(input_KviMo);
    const hr_NVqme = document.createElement('hr');
    hr_NVqme.classList.add('my-2');
    hr_NVqme.style.zIndex = '1';
    div_fxEUN.appendChild(hr_NVqme);
    const div_XmvRG = document.createElement('div');
    div_XmvRG.classList.add('row');
    div_fxEUN.appendChild(div_XmvRG);
    const div_dxixy = document.createElement('div');
    div_dxixy.classList.add('col-md-12', 'text-center');
    for (let i = 0; i < pictures.length; i++) {
        let img_hSdVM = new Image();
        img_hSdVM.src = pictures[i];
        img_hSdVM.setAttribute(`height`, `100px;`);
        img_hSdVM.classList.add('moreInfoModalImages');
        div_dxixy.appendChild(img_hSdVM);
    }
    div_XmvRG.appendChild(div_dxixy);
    const hr_MnAYV = document.createElement('hr');
    hr_MnAYV.classList.add('my-2');
    hr_MnAYV.style.zIndex = '1';
    div_fxEUN.appendChild(hr_MnAYV);
    const div_yIuRk = document.createElement('div');
    div_yIuRk.classList.add('row');
    div_fxEUN.appendChild(div_yIuRk);
    const div_lNOiF = document.createElement('div');
    div_lNOiF.classList.add('col-md-4');
    div_yIuRk.appendChild(div_lNOiF);
    div_lNOiF.textContent += `Start Date:`;
    const br_GLEAx = document.createElement('br');
    div_lNOiF.appendChild(br_GLEAx);
    const span_qXZQe = document.createElement('span');
    span_qXZQe.textContent += startDate;
    div_lNOiF.appendChild(span_qXZQe);
    const div_lkuNJ = document.createElement('div');
    div_lkuNJ.classList.add('col-md-4');
    div_yIuRk.appendChild(div_lkuNJ);
    div_lkuNJ.textContent += `End Date:`;
    const br_rMZuS = document.createElement('br');
    div_lkuNJ.appendChild(br_rMZuS);
    const span_qXZQe2 = document.createElement('span');
    span_qXZQe2.textContent += endDate;
    div_lkuNJ.appendChild(span_qXZQe2);
    const div_Wadqu = document.createElement('div');
    div_Wadqu.classList.add('col-md-4');
    div_yIuRk.appendChild(div_Wadqu);
    div_Wadqu.textContent += `Status:`;
    const br_iXfAR = document.createElement('br');
    div_Wadqu.appendChild(br_iXfAR);
    const span_qXZQe3 = document.createElement('span');
    span_qXZQe3.textContent += Astatus.replace(/_/g, ' ');
    div_Wadqu.appendChild(span_qXZQe3);
    const br_tNpcT = document.createElement('br');
    div_fxEUN.appendChild(br_tNpcT);
    const div_DCnUZ = document.createElement('div');
    div_DCnUZ.classList.add('row');
    div_fxEUN.appendChild(div_DCnUZ);
    const div_LFpzR = document.createElement('div');
    div_LFpzR.classList.add('col-md-4');
    div_DCnUZ.appendChild(div_LFpzR);
    div_LFpzR.textContent += `Genres: ` + genres;
    const div_aZxxL = document.createElement('div');
    div_aZxxL.classList.add('col-md-4');
    div_DCnUZ.appendChild(div_aZxxL);
    div_aZxxL.textContent += `My anime list id: ` + animeID;
    const div_CsRGo = document.createElement('div');
    div_CsRGo.classList.add('col-md-4');
    div_DCnUZ.appendChild(div_CsRGo);
    div_CsRGo.textContent += `Studios: ` + studio;
    const br_jWail = document.createElement('br');
    div_fxEUN.appendChild(br_jWail);
    const div_xhoaA = document.createElement('div');
    div_xhoaA.classList.add('row');
    div_fxEUN.appendChild(div_xhoaA);
    const div_JVbkK = document.createElement('div');
    div_JVbkK.classList.add('col-md-3');
    div_xhoaA.appendChild(div_JVbkK);
    div_JVbkK.textContent += `Total episodes: `;
    const br_XqXxX = document.createElement('br');
    div_JVbkK.appendChild(br_XqXxX);
    const span_XqXxX = document.createElement('span');
    span_XqXxX.textContent += episodes;
    div_JVbkK.appendChild(span_XqXxX);
    const div_DQDgc = document.createElement('div');
    div_DQDgc.classList.add('col-md-3');
    div_xhoaA.appendChild(div_DQDgc);
    div_DQDgc.textContent += `Average Episode Duration: `;
    const br_XqXxX_2 = document.createElement('br');
    div_DQDgc.appendChild(br_XqXxX_2);
    const span_XqXxX_2 = document.createElement('span');
    const date = new Date(averageEpDuration * 1000);
    span_XqXxX_2.textContent += date.getMinutes() + ` minutes`;
    div_DQDgc.appendChild(span_XqXxX_2);
    const div_Ldqno = document.createElement('div');
    div_Ldqno.classList.add('col-md-3');
    div_xhoaA.appendChild(div_Ldqno);
    div_Ldqno.textContent += `Score:`;
    const br_XqXxX_3 = document.createElement('br');
    div_Ldqno.appendChild(br_XqXxX_3);
    const span_XqXxX_3 = document.createElement('span');
    span_XqXxX_3.textContent += globalScore + ` /10`;
    div_Ldqno.appendChild(span_XqXxX_3);
    const div_XPtQK = document.createElement('div');
    div_XPtQK.classList.add('col-md-3');
    div_xhoaA.appendChild(div_XPtQK);
    div_XPtQK.textContent += `Your score:`;
    const br_wtFgi = document.createElement('br');
    div_XPtQK.appendChild(br_wtFgi);
    const input_KviM = document.createElement('input');
    input_KviM.setAttribute(`type`, `number`);
    input_KviM.id = 'localScoreInp';
    input_KviM.setAttribute(`autocomplete`, `off`);
    input_KviM.setAttribute(`placeholder`, `Write a score`);
    if (localScore != 0) {
        input_KviM.setAttribute(`value`, localScore);
    }
    div_XPtQK.appendChild(input_KviM);
    const br_UoTYW = document.createElement('br');
    div_fxEUN.appendChild(br_UoTYW);
    const div_AgTPy = document.createElement('div');
    div_AgTPy.classList.add('row');
    div_fxEUN.appendChild(div_AgTPy);
    const div_csfRP = document.createElement('div');
    div_csfRP.classList.add('col-md-12');
    div_AgTPy.appendChild(div_csfRP);

    const div_Pczhn = document.createElement('div');
    div_Pczhn.classList.add('accordion');
    div_Pczhn.id = 'accordionExample';
    div_csfRP.appendChild(div_Pczhn);
    const div_nIWSp = document.createElement('div');
    div_nIWSp.classList.add('accordion-item');
    div_Pczhn.appendChild(div_nIWSp);
    const h2_KMMzu = document.createElement('h2');
    h2_KMMzu.classList.add('accordion-header');
    h2_KMMzu.id = 'headingOne';
    div_nIWSp.appendChild(h2_KMMzu);
    const button_pKrgr = document.createElement('button');
    button_pKrgr.classList.add('accordion-button', 'collapsed');
    button_pKrgr.setAttribute(`type`, `button`);
    button_pKrgr.setAttribute(`data-bs-toggle`, `collapse`);
    button_pKrgr.setAttribute(`data-bs-target`, `#collapseOne`);
    button_pKrgr.setAttribute(`aria-expanded`, `true`);
    button_pKrgr.setAttribute(`aria-controls`, `collapseOne`);
    button_pKrgr.textContent += `Synopsis`;
    h2_KMMzu.appendChild(button_pKrgr);
    const div_GFvvR = document.createElement('div');
    div_GFvvR.classList.add('accordion-collapse', 'collapse');
    div_GFvvR.id = 'collapseOne';
    div_GFvvR.setAttribute(`aria-labelledby`, `headingOne`);
    div_GFvvR.setAttribute(`ata-bs-parent`, `#accordionExample`);
    div_nIWSp.appendChild(div_GFvvR);
    const div_SprEw = document.createElement('div');
    div_SprEw.classList.add('accordion-body');
    div_GFvvR.appendChild(div_SprEw);
    div_SprEw.textContent += ((synopsis != null) ? synopsis : `This Anime don't have synopsis`);;
    const div_bArPk = document.createElement('div');
    div_bArPk.classList.add('accordion-item');
    div_Pczhn.appendChild(div_bArPk);
    const h2_DMxNG = document.createElement('h2');
    h2_DMxNG.classList.add('accordion-header');
    h2_DMxNG.id = 'headingTwo';
    div_bArPk.appendChild(h2_DMxNG);
    if (background != "") {
        const button_QBzvL = document.createElement('button');
        button_QBzvL.classList.add('accordion-button', 'collapsed');
        button_QBzvL.setAttribute(`type`, `button`);
        h2_DMxNG.appendChild(button_QBzvL);
        button_QBzvL.setAttribute(`data-bs-toggle`, `collapse`);
        button_QBzvL.setAttribute(`data-bs-target`, `#collapseTwo`);
        button_QBzvL.setAttribute(`aria-expanded`, `false`);
        button_QBzvL.setAttribute(`aria-controls`, `collapseTwo`);
        button_QBzvL.textContent += `Background`;
        const div_KQQgG = document.createElement('div');
        div_KQQgG.classList.add('accordion-collapse', 'collapse');
        div_KQQgG.id = 'collapseTwo';
        div_KQQgG.setAttribute(`aria-labelledby`, `headingTwo`);
        div_KQQgG.setAttribute(`data-bs-parent`, `#accordionExample`);
        div_bArPk.appendChild(div_KQQgG);
        const div_WSmgc = document.createElement('div');
        div_WSmgc.classList.add('accordion-body');
        div_KQQgG.appendChild(div_WSmgc);
        div_WSmgc.textContent += ((background != "") ? background : `This Anime don't have background`);
    }
    const br_UoTY = document.createElement('br');
    div_fxEUN.appendChild(br_UoTY);
    const div_IJZTb = document.createElement('div');
    div_IJZTb.classList.add('row');
    div_fxEUN.appendChild(div_IJZTb);
    const div_Gwfbx = document.createElement('div');
    div_Gwfbx.classList.add('col-md-6');
    div_IJZTb.appendChild(div_Gwfbx);
    const button_VrukS = document.createElement('button');
    button_VrukS.classList.add('addAnimeBtn');
    button_VrukS.setAttribute(`type`, `button`);
    button_VrukS.setAttribute(`data-bs-toggle`, `modal`);
    button_VrukS.setAttribute(`data-bs-target`, `#relatedAnimeModal`);
    div_Gwfbx.appendChild(button_VrukS);
    button_VrukS.textContent += `Related Anime`;
    const div_DbZlx = document.createElement('div');
    div_DbZlx.classList.add('col-md-6');
    div_IJZTb.appendChild(div_DbZlx);
    if (relatedManga.length > 0) {
        const button_pRprs = document.createElement('button');
        button_pRprs.classList.add('addAnimeBtn');
        button_pRprs.setAttribute(`type`, `button`);
        button_pRprs.setAttribute(`data-bs-toggle`, `modal`);
        button_pRprs.setAttribute(`data-bs-target`, `#relatedMangaModal`);
        div_DbZlx.appendChild(button_pRprs);
        button_pRprs.textContent += `Related Manga`;
    }

    // show modal
    const myModal = new bootstrap.Modal(document.getElementById('moreInfoModal'))
    myModal.show()

    // listen for close event to save score and notes
    const myModalEl = document.getElementById('moreInfoModal')
    myModalEl.addEventListener('hidden.bs.modal', event => {
        saveScoreAndNotes(); // function on animeFunctions.js
    })

}