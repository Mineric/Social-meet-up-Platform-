// class to create a rounded rectangle

$('document').ready(() => {
    let tags_box = document.getElementsByClassName("tags_box");

    for(let i = 0; i < tags_box.length; i++) {
        tags_box[i].addEventListener('click', (event) => {
            let id = event.target.getAttribute('value');
            console.log(id);
            let checkbox = document.getElementById(`tags_${id}`);
            if(checkbox.checked == false) {
                checkbox.checked = true;
                // let choosen = document.querySelector(`div.choosen[value='${id}']`);
                // choosen.style.display = 'inline-block';
                // let not_choosen = document.querySelector(`div.not_choosen[value='${id}']`);
                // not_choosen.style.display = 'none';
                let tags_box = document.querySelector(`div.tags_box[value='${id}']`);
                tags_box.className = tags_box.className.replace("not_choosen", "choosen");
            }
            else {
                checkbox.checked = false;
                 // let choosen = document.querySelector(`div.choosen[value='${id}']`);
                // choosen.style.display = 'none';
                // let not_choosen = document.querySelector(`div.not_choosen[value='${id}']`);
                // not_choosen.style.display = 'inline-block';
                let tags_box = document.querySelector(`div.tags_box[value='${id}']`);
                tags_box.className = tags_box.className.replace("choosen", "not_choosen");
            }
        });
        tags_box[i].style.display = 'inline-block';
    }

    let choosen = document.getElementsByClassName("choosen");
    for(let i = 0; i < choosen.length; i++) {
        choosen[i].style.display = 'none';
    }

    let checkbox = document.querySelectorAll('[type="checkbox"]');
    for(let i = 0; i < checkbox.length; i++) {
        checkbox[i].style.display = 'none';
    }
})