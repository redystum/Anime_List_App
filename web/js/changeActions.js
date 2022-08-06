function changeActions(element, id, AnimeId, option, fav = 0) {
    closeToolTips();
    if (option == "view") {
        console.log("view");
        console.log(element)
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
        if (fav == 0) {
            console.log("not fav");
            span_umBr.setAttribute(`data-icon`, `heart_plus`);
            span_umBr.setAttribute(`data-tooltip`, `Add to favorites`);
            span_umBr.setAttribute(`onclick`, `addFav(${id}, ${AnimeId})`);
        } else {
            console.log(" fav");
            span_umBr.setAttribute(`data-icon`, `favorite`);
            span_umBr.setAttribute(`data-tooltip`, `In favorites List`);
            span_umBr.setAttribute(`onclick`, `removeFav(${id}, ${AnimeId})`);
        }
        element.appendChild(span_umBr);
    } else if (option == "unview") {
        const span_tIvWc = document.createElement('span');
        span_tIvWc.classList.add('iconElement');
        span_tIvWc.setAttribute(`data-icon`, `done`);
        span_tIvWc.setAttribute(`data-tooltip`, `Viewed`);
        span_tIvWc.setAttribute(`onclick`, `setViewed(${id}, ${AnimeId})`);
        element.appendChild(span_tIvWc);
        const span_umBrx = document.createElement('span');
        span_umBrx.classList.add('iconElement');
        span_umBrx.setAttribute(`data-icon`, `delete`);
        span_umBrx.setAttribute(`data-tooltip`, `Delete`);
        span_umBrx.setAttribute(`onclick`, `deleteAnime(${id}, ${AnimeId}, 0)`);
        element.appendChild(span_umBrx);
    }
}