var confirmed = sessionStorage.getItem('confirmed');
days = ['Sunday','Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday'];
if(!confirmed){
   let date = prompt('enter your birth date yyyy-mm-dd', '2003-11-21');
   let ms = Date.parse(date);
   let day = days[(new Date(date)).getDay()]
   let nowms = Date.now();
   let gap = nowms-ms;
   years = Math.floor(gap/1000/3600/24/365.25);
   if(years>=18){
        alert("Age:\t"+years+"\nDay of birth:" + day);
        sessionStorage.setItem('confirmed','true');
   }
   else{
        alert('You need an adult to use the site!')
   }

}