let botton = document.querySelector('#panel-users-switch')
let panel = document.querySelector('.panel-users-list')
botton.addEventListener('click',()=>{
    if(panel.classList.contains('panel-close')){
        botton.classList.add('rotate-button')
    } else {
        botton.classList.remove('rotate-button')
    }
    panel.classList.toggle('panel-close')

})
function percentageSeen(element) {
  const parent = element.parentNode;
  const viewportHeight = window.innerHeight;
  const scrollY = window.scrollY;
  const elPosY = parent.getBoundingClientRect().top + scrollY;
  const borderHeight = parseFloat(getComputedStyle(parent).getPropertyValue('border-bottom-width')) + parseFloat(getComputedStyle(element).getPropertyValue('border-top-width'));
  const elHeight = parent.offsetHeight + borderHeight;

  if (elPosY > scrollY + viewportHeight) {
    return 0;
  } else if (elPosY + elHeight < scrollY) {
    return 100;
  } else {
    const distance = scrollY + viewportHeight - elPosY;
    let percentage = distance / ((viewportHeight + elHeight) / 100);
    percentage = Math.round(percentage);
    return percentage;
  }
}

let scaleAmount = 0.5;

function scrollZoom() {
  const images = document.querySelectorAll("[data-scroll-zoom]");
  let scrollPosY = 0;
  scaleAmount = scaleAmount / 100;

  const observerConfig = {
    rootMargin: "0% 0% 0% 0%",
    threshold: 0
  };

  // Create separate IntersectionObservers and scroll event listeners for each image so that we can individually apply the scale only if the image is visible
  images.forEach(image => {
    let isVisible = false;
    const observer = new IntersectionObserver((elements, self) => {
      elements.forEach(element => {
        isVisible = element.isIntersecting;
      });
    }, observerConfig);
    observer.observe(image);

    // Set initial image scale on page load
    image.style.transform = `scale(${1.12 })`;

    // Only fires if IntersectionObserver is intersecting
    window.addEventListener("scroll", () => {
      if (isVisible) {
        scrollPosY = window.scrollY;
        // console.log(scrollPosY)

        image.style.transform = `scale(${1+
          scaleAmount * percentageSeen(image)})`;
      }
    });
  });
}
function scrollZoomOut() {
  const imagesOut = document.querySelectorAll("[data-scroll-out]");
  let scrollPosY = 0;
  scaleAmount = scaleAmount/2;

  const observerConfig = {
    rootMargin: "0% 0% 0% 0%",
    threshold: 0
  };

  // Create separate IntersectionObservers and scroll event listeners for each image so that we can individually apply the scale only if the image is visible
  imagesOut.forEach(image_out => {
    let isVisible = false;
    const observer = new IntersectionObserver((elements, self) => {
      elements.forEach(element => {
        isVisible = element.isIntersecting;
      });
    }, observerConfig);
    observer.observe(image_out);
    image_out.style.transform = `scale(${1.3})`;

    window.addEventListener("scroll", () => {
      if (isVisible) {
        scrollPosY = window.scrollY;

        image_out.style.transform = `scale(${1.3 - scaleAmount * percentageSeen(image_out)})`;
      }
    });
  });

}

async function init () {
    const node = document.querySelector("#type-text")
    await sleep(1000)
    // node.innerText = ""
    // await node.type('Hello, ')
    while (true) {
      await node.type('Django!')
      await sleep(2000)
      await node.delete('Django!')
      await node.type('Suites!')
      await sleep(2000)
      await node.delete('Suites!')
    }
  }
  const sleep = time => new Promise(resolve => setTimeout(resolve, time))
  class TypeAsync extends HTMLSpanElement {
    get typeInterval () {
      const randomMs = 200 * Math.random()
      return randomMs < 50 ? 10 : randomMs
        // return 200 + (100 * Math.random())
    }
    async type (text) {
      for (let character of text) {
        this.innerText += character
        await sleep(this.typeInterval)
      }
    }
    async delete (text) {
      for (let character of text) {
        this.innerText = this.innerText.slice(0, this.innerText.length -1)
        await sleep(this.typeInterval)
      }
    }
  }
  customElements.define('type-async', TypeAsync, { extends: 'span' })


window.onload = function (){
scrollZoom();
scrollZoomOut();
init()
}