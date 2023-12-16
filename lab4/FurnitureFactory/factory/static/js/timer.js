
var timer = document.getElementById("p_timer");


document.addEventListener('DOMContentLoaded', () => {


        let remained = sessionStorage.getItem("remained");
        let last_session = sessionStorage.getItem("last_session");


        if (remained == null || remained == undefined || remained == 0 || remained == NaN){
            remained = 3600;
        }
        else{
            remained = parseInt(remained)
        }

        if (last_session){
                const last_gap = Math.floor((parseInt(Date.now()) - last_session) / 1000);
                remained -= last_gap;
        }
        function update(){
        const minutes = Math.floor(remained / 60);
        const seconds = remained % 60;
        timer.innerHTML=`${minutes}m ${seconds}s`


        if (remained <= 0) {
            clearInterval(timerInterval);
            timer.innerHTML = "Time's up!";
        }

        const countdownStart = Date.now();
        sessionStorage.setItem("last_session", countdownStart);
        sessionStorage.setItem("remained", remained);
    }
    update()
    const timerInterval = setInterval( () => {
        remained--;

        update();

    }, 1000);


});