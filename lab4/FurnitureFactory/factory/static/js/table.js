const table = document.querySelector('#js_made_table');
const limit_input = document.querySelector('#sel_limit');
const size_input = document.querySelector('#table_size');
const limit_button = document.querySelector('#limit_button');
const create_button = document.querySelector('#create_button');

//limit_button.disabled = true;
//create_button.disabled = true;

const selectedCells = new Set();


limit = 1;
size = 3;

limit_input.addEventListener('input', () => {
    if(limit_input.value <= 0 || limit_input.value > 5){
        limit_button.disabled = true;
    }
    else{
        limit_button.disabled = false;
    }
 });
size_input.addEventListener('input', () => {
    if(size_input.value <= 0 || size_input.value > 20){
        create_button.disabled = true;
    }
    else{
        create_button.disabled = false;
    }
 });
function addRow(){
    const newRow = table.insertRow(table.rows.length);
    for (let i = 0; i < table.rows[0].cells.length; i++) {
        var cell = newRow.insertCell(i);
        cell.innerText = Math.floor(Math.random() * 400) + 1;
        cell.addEventListener('click', () => select(cell));
    }
}
function addColumn(){
    for (let i = 0; i < table.rows.length; i++) {
    const cell = table.rows[i].insertCell(table.rows[i].cells.length);
    cell.innerText = Math.floor(Math.random() * 400) + 1;
    cell.addEventListener('click', () => select(cell));
  }
}
function create(){
    size = parseInt(size_input.value);
    if (size > 0 && size < 21) {
        table.innerHTML = "";
        selectedCells.clear();

        for (let i = 0; i < size; i++) {
            const row = table.insertRow(i);
            for (let j = 0; j < size; j++) {
                const cell = row.insertCell(j);
                cell.innerText = Math.floor(Math.random() * 400) + 1;
                cell.addEventListener("click", () => select(cell));
            }
        }
    }

}
function setLimit(){
    limit = parseInt(limit_input.value);
    unselect();
}
function transpose(){
    const rows = table.rows;
    const columns = [];
    for (let i = 0; i < rows[0].cells.length; i++) {
        columns.push(Array.from({ length: rows.length }, (_, j) => rows[j].cells[i]));
    }
    table.innerHTML = '';
    for (const column of columns) {
        const row = table.insertRow();
        for (const cell of column) {
            row.appendChild(cell.cloneNode(true));
        }
    }
    let rowss = table.getElementsByTagName("tr");

    for (let i = 0; i < rowss.length; i++) {
        let _cells = rowss[i].getElementsByTagName("td");
        for (let j = 0; j < _cells.length; j++) {
            table.getElementsByTagName("tr")[i].getElementsByTagName("td")[j].addEventListener('click', () =>
            select(table.getElementsByTagName("tr")[i].getElementsByTagName("td")[j]));
        }
    }
}

function select(cell){
    const value = parseInt(cell.innerText);
    if (!cell.classList.contains("selected") && !cell.classList.contains("selected-even")) {
        if (selectedCells.size < limit) {

            if (value % 2 == 0) {
                cell.classList.add("selected-even");

            } else {
                cell.classList.add("selected");

            }
            selectedCells.add(cell);

        }
    } else if (cell.classList.contains("selected") || cell.classList.contains("selected-even")) {
        if (value % 2 == 0) {
            cell.classList.remove("selected-even");
        } else {
            cell.classList.remove("selected");
        }
        selectedCells.delete(cell);
    }

}

function unselect(){
    for (const cell of selectedCells) {
        cell.classList.remove("selected");
        let value = parseInt(cell.innerText);
        if (value % 2 == 0) {
            cell.classList.remove("selected-even");
        }
    }
    selectedCells.clear();
}
if (sessionStorage.getItem("is_reloaded")) alert('Reloaded!');