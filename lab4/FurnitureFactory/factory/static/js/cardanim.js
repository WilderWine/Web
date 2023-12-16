const cards = document.querySelectorAll(".contact");

cards.forEach((card) => {
    card.addEventListener('mousemove',()=>{
        const halfHeight = card.offsetHeight / 2;
        const halfWidth = card.offsetWidth / 2;
        card.style.transform = `rotateX(${-(event.offsetY - halfHeight) / 10}deg) rotateY(${(event.offsetX - halfWidth) / 10}deg)`;
    });
    card.addEventListener('mouseout',()=>{
        card.style.transform = 'rotate(0)';
    });

});
