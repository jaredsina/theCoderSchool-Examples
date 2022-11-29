const scrollElements = document.querySelectorAll('.js-scroll');
const scrollOffset = 100;
const windowHeight=document.getElementById
scrollElements.forEach((element)=>{
    element.style.opacity=0;
})

const elementInView = (element,scrollOffset=0)=>{
    const elementTop= element.getBoundingClientRect().top;

    //return true if elementTop is less than or equal to height of the viewport
    return(elementTop<=(window.innerHeight || document.documentElement.clientHeight)-scrollOffset);
}

const displayScrollElement=(element)=>{
    element.classList.add('scrolled');

}
const hideScrollElement=(element)=>{
    element.classList.remove('scrolled');
}

const handleScrollAnimation=()=>{
    scrollElements.forEach((element)=>{
        if(elementInView(element,100)){
            displayScrollElement(element)
        }else{
            hideScrollElement(element)
        }
    })
}

//add event listener that activates on scroll down
window.addEventListener('scroll',handleScrollAnimation());