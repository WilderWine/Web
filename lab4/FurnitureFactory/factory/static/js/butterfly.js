const butter1 = document.querySelector('#butterfly');
const butter2 = document.querySelector('#butterfly2');
const butter3 = document.querySelector('#butterfly3');
const butter4 = document.querySelector('#butterfly4');
const butter_div = document.querySelector('#bf');

const a = document.get

start1 = 0;
start2 = -100;
start3 = -200;
start4 = -300;
butter1.style.opacity = 1;
butter2.style.opacity = 0;
butter3.style.opacity = 0;
butter4.style.opacity = 0;
butter1.style.left = `${start1}px`;
butter2.style.left = `${start2}px`;
butter3.style.left = `${start3}px`;
butter4.style.left = `${start4}px`;
butter4.style.left = `${start4}px`;

document.body.addEventListener('scroll',()=>{
    value = document.body.scrollTop;
    butter1.style.left = `${start1 + value*3.5}px`;
    butter2.style.left = `${start2 + value*2}px`;
    butter3.style.left = `${start3+ value*1.5}px`;
    butter4.style.left = `${start4 + value*0.1}px`;
    butter1.style.bottom = `${-value*1.5}px`;
    butter2.style.bottom = `${-value*2}px`;
    butter3.style.bottom = `${-value*2.5}px`;
    butter4.style.bottom = `${-value*3}px`;
    //alert(butter4.style.bottom)
    butter1.style.opacity = (parseInt(window.innerWidth)/0.7 - parseInt(butter1.style.left))/parseInt(window.innerWidth)/1.7;
    butter2.style.opacity = (parseInt(window.innerWidth) - parseInt(butter2.style.left))/parseInt(window.innerWidth);
    butter3.style.opacity = (parseInt(window.innerWidth)/1.2 - parseInt(butter3.style.left))/parseInt(window.innerWidth)/1.2;
    butter4.style.opacity = (parseInt(window.innerHeight)/1.5 - value)/parseInt(window.innerHeight)*1.5;
    if(-parseInt(butter4.style.bottom) < window.innerHeight){
        bf.style.marginBottom = `${-parseInt(butter4.style.bottom)}px`;
    }
    if(parseInt(butter2.style.left)<=start2){
        butter2.style.opacity=0;
    }
   if(parseInt(butter3.style.left)<=start3){
        butter3.style.opacity=0;
    }
    if(parseInt(butter4.style.left)<=start4){
        butter4.style.opacity=0;
    }
})

