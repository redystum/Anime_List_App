function changeActions(element, id, AnimeId) {
    const span_tIvWc = document.createElement('span');
    span_tIvWc.classList.add('iconElement');
    span_tIvWc.setAttribute(`data-icon`, `remove_done`);
    span_tIvWc.setAttribute(`data-tooltip`, `Unview`);
    span_tIvWc.setAttribute(`onclick`, `setUnview(${id}, ${AnimeId})`);
    element.appendChild(span_tIvWc);
    const span_umBrx = document.createElement('span');
    span_umBrx.classList.add('iconElement');
    span_umBrx.setAttribute(`data-icon`, `delete`);
    span_umBrx.setAttribute(`data-tooltip`, `Delete`);
    span_umBrx.setAttribute(`onclick`, `deleteAnime(${id}, ${AnimeId},1)`);
    element.appendChild(span_umBrx);
    const span_umBr = document.createElement('span');
    span_umBr.classList.add('iconElement');
    span_umBr.setAttribute(`data-icon`, `heart_plus`);
    span_umBr.setAttribute(`data-tooltip`, `Add to favorites`);
    span_umBr.setAttribute(`onclick`, `addFav(${id}, ${AnimeId})`);
    element.appendChild(span_umBr);
}