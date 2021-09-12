(function(){
    const prevPageBtn = document.querySelector('#prev-page-btn');
    const nextPageBtn = document.querySelector('#next-page-btn');
    const urlParams = new URLSearchParams(window.location.search);

    [prevPageBtn, nextPageBtn].forEach(function(pageBtn) {

        if(pageBtn) {
            const pageNum = pageBtn.getAttribute('page-num');
    
            pageBtn.addEventListener('click', function (){
                urlParams.set('page', pageNum);
                window.history.replaceState({}, '', `${location.pathname}?${urlParams.toString()}`);
                location.reload();
            });
        }
    });

})();