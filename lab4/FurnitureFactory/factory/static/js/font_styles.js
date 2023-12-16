const colour_picker = document.querySelector("#textColour");
var standart_size = '16px';
const for_colour_change = document.querySelectorAll('h1,h2,h3,h4,h5,h6,h7,label,p,title,small,strong,i,b,table,li');


colour_picker.addEventListener('input', () => {
    for(let elem of for_colour_change){

        elem.style.color = colour_picker.value;

    }
});

function fontUp(){
    let temp = new Array();
    if(parseInt(standart_size) < 30){
        standart_size = parseInt(standart_size) + 2 + 'px';
        for (let elem of for_colour_change){
            elem.style.fontSize = standart_size;
        }
    }
}

function fontDown(){
    let temp = new Array();
    if(parseInt(standart_size) > 8){
        standart_size = parseInt(standart_size) -2 + 'px';
        for (let elem of for_colour_change){
            elem.style.fontSize = standart_size;
        }
    }
}