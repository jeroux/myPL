function init_new_item(){
    const category = document.querySelector('input[name="category"]:checked').value;

    if(category != undefined){
        const category_input = document.getElementById('id_category');
        category_input.value = category;

        const category_label = document.getElementById('new_item_category_label');
        category_label.innerHTML = category;

        const new_item_div = document.getElementById('new_item');
        new_item_div.style.display = 'block';

        const add_pannel = document.getElementById('add_new_side_effects');
        add_pannel.classList.add('hidden');
    }
}

function close_pannel(){
    const add_pannel = document.getElementById('add_new_side_effects');
    add_pannel.classList.add('hidden');
}

