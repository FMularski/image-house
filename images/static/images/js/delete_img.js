(function(){
    const deleteBtns = document.querySelectorAll('.delete-btn');
    const dark = document.querySelector('#dark');
    const deletePanel = document.querySelector('#delete-panel');
    const cancelDeleteBtn = document.querySelector('#no-del-btn');
    const confirmDeleteBtn = document.querySelector('#yes-del-btn');

    let deletePK;

    deleteBtns.forEach(function(btn){
        btn.addEventListener('click', function(event){

            // if click on btn or its icon
            if (event.target === this || event.target === this.children[0]) {
                event.preventDefault();
                dark.classList.add('active');
                deletePanel.classList.add('active');
                deletePK = btn.getAttribute('del-pk');
            }

        });
    });

    cancelDeleteBtn.addEventListener('click', function(){
        dark.classList.remove('active');
        deletePanel.classList.remove('active');
    })


    confirmDeleteBtn.addEventListener('click', function(){
        window.location.href = '/delete/' + deletePK;
    })

})();