const duration_input = document.querySelector("#duration");
const show_butt = document.querySelector("#show_butt");

duration_input.addEventListener('input', () => {
    if(duration_input.value == 0){
        show_butt.disabled = true;

    }
    else{
        show_butt.disabled = false;
    }
 });

subscribers = [
    new Object({'name':'Aristarh', 'operator':'A1', 'number':'+375291111111', 'amount':14, 'leng':143}),
    new Object({'name':'Barbara', 'operator':'MTS', 'number':'+375441111122', 'amount':7, 'leng':180}),
    new Object({'name':'Artem', 'operator':'MTS', 'number':'+375443311111', 'amount':13, 'leng':84}),
    new Object({'name':'Marina', 'operator':'A1', 'number':'+375291234567', 'amount':25, 'leng':49}),
    new Object({'name':'John', 'operator':'LIB', 'number':'+16458911122244', 'amount':26, 'leng':54})]

var res = document.getElementById('res');

function ShowFiltered() {
    res.innerHTML=''
    let max_length_av = duration_input.value;
    let result = subscribers.filter(abo => abo.leng/abo.amount < max_length_av).sort((abo1,abo2) => abo2.amount - abo1.amount);
    if(result.length > 0){
        result.forEach( subs => {
            res.innerHTML += `<p> Name: ${subs.name}</p><p>Operator: ${subs.operator}</p><p>Phone number: ${subs.number}</p>`
            res.innerHTML += `<p> Total calls: ${subs.amount}</p><p>Total Duration: ${subs.leng}</p><p>Average: ${subs.leng/subs.amount}</p><br>`

        })
    }
    else{
        res.innerHTML = `<p>No matches were found(</p>`;
    }
    }

function ShowAll() {
    res.innerHTML=''
    let result = subscribers.sort((abo1,abo2) => abo2.amount - abo1.amount)
    result.forEach( subs => {
            res.innerHTML += `<p> Name: ${subs.name}</p><p>Operator: ${subs.operator}</p><p>Phone number: ${subs.number}</p>`
            res.innerHTML += `<p> Total calls: ${subs.amount}</p><p>Total Duration: ${subs.leng}</p><p>Average: ${subs.leng/subs.amount}</p><br>`
        })
}