function init_new_item(){
    const category = document.querySelector('input[name="category"]:checked').value;

    if(category != undefined){
        var category_input = document.getElementById('id_category');
        category_input.value = category;

        var category_label = document.getElementById('new_item_category_label');
        category_label.innerHTML = category;

        var new_item_div = document.getElementById('new_item');
        new_item_div.classList.remove('hidden');

        var add_pannel = document.getElementById('add_new_side_effects');
        add_pannel.classList.add('hidden');

        var new_item_input = document.getElementByClass('id_new_item');
        new_item_input.focus();
    }
}

function close_pannel(){
    var add_pannel = document.getElementById('add_new_side_effects');
    add_pannel.classList.add('hidden');
}

function hide_new_item(){
    var new_item_div = document.getElementById('new_item');
    new_item_div.classList.add('hidden');
}

function editing_mode(id){
    var reading_buttons = document.getElementById('reading_buttons_'+id);
    reading_buttons.classList.add('hidden');

    var editing_buttons = document.getElementById('editing_buttons_'+id);
    editing_buttons.classList.remove('hidden');

    var item = document.getElementById("input_"+id);
    item.disabled = false;
    item.classList.add('border');
    item.focus();
}

function reading_mode(id){
    var reading_buttons = document.getElementById('reading_buttons_'+id);
    reading_buttons.classList.remove('hidden');

    var editing_buttons = document.getElementById('editing_buttons_'+id);
    editing_buttons.classList.add('hidden');

    var item = document.getElementById("input_"+id);
    item.disabled = true;
    item.classList.remove('border');
}