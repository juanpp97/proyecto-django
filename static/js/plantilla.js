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
    image.style.transform = `scale(${1 + scaleAmount * percentageSeen(image)})`;

    // Only fires if IntersectionObserver is intersecting
    window.addEventListener("scroll", () => {
      if (isVisible) {
        scrollPosY = window.pageYOffset;
        image.style.transform = `scale(${1 +
          scaleAmount * percentageSeen(image)})`;
      }
    });
  });

  // Calculates the "percentage seen" based on when the image first enters the screen until the moment it leaves
  // Here, we get the parent node position/height instead of the image since it's in a container that has a border, but
  // if your container has no extra height, you can simply get the image position/height
  function percentageSeen(element) {
    const parent = element.parentNode;
    const viewportHeight = window.innerHeight;
    const scrollY = window.scrollY;
    const elPosY = parent.getBoundingClientRect().top + scrollY;
    const borderHeight = parseFloat(getComputedStyle(parent).getPropertyValue('border-bottom-width')) + parseFloat(getComputedStyle(element).getPropertyValue('border-top-width'));
    const elHeight = parent.offsetHeight + borderHeight;

    if (elPosY > scrollY + viewportHeight) {
      // If we haven't reached the image yet
      return 0;
    } else if (elPosY + elHeight < scrollY) {
      // If we've completely scrolled past the image
      return 100;
    } else {
      // When the image is in the viewport
      const distance = scrollY + viewportHeight - elPosY;
      let percentage = distance / ((viewportHeight + elHeight) / 100);
      percentage = Math.round(percentage);

      return percentage;
    }
  }
}

scrollZoom();




// class TxtRotate {
//     constructor(el, toRotate, period) {
//         this.toRotate = toRotate
//         this.el = el
//         this.loopNum = 0
//         this.period = parseInt(period, 10) || 2000
//         this.txt = ''
//         this.tick()
//         this.isDeleting = false
//     }
//     tick() {
//         var i = this.loopNum % this.toRotate.length
//         var fullTxt = this.toRotate[i]

//         if (this.isDeleting) {
//             this.txt = fullTxt.substring(0, this.txt.length - 1)
//         } else {
//             this.txt = fullTxt.substring(0, this.txt.length + 1)
//         }

//         this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>'

//         var that = this
//         var delta = 300 - Math.random() * 100

//         if (this.isDeleting) { delta /= 2} 

//         if (!this.isDeleting && this.txt === fullTxt) {
//             delta = this.period
//             this.isDeleting = true
//         } else if (this.isDeleting && this.txt === '') {
//             this.isDeleting = false
//             this.loopNum++
//             delta = 500
//         }

//         setTimeout(function () {
//             that.tick()
//         }, delta)
//     }
// }; 
  
  
//   window.onload = function() {
//     var elements = document.getElementsByClassName('txt-rotate');
//     for (var i=0; i<elements.length; i++) {
//       var toRotate = elements[i].getAttribute('data-rotate');
//       var period = elements[i].getAttribute('data-period');
//       if (toRotate) {
//         new TxtRotate(elements[i], JSON.parse(toRotate), period);
//       }
//     }
//     // INJECT CSS
//     var css = document.createElement("style");
//     css.type = "text/css";
//     css.innerHTML = ".txt-rotate > .wrap { border-right: 0.08em solid #666 }";
//     document.body.appendChild(css);
//   };



// class TxtRotate {
//     constructor(el, toRotate, period) {
//       this.toRotate = toRotate;
//       this.el = el;
//       this.loopNum = 0;
//       this.period = parseInt(period, 10) || 2000;
//       this.txt = '';
//       this.isDeleting = false;
//       this.tick();
//     }
  
//     tick = () => {
//       const i = this.loopNum % this.toRotate.length;
//       const fullTxt = this.toRotate[i];
  
//       if (this.isDeleting) {
//         this.txt = fullTxt.substring(0, this.txt.length - 1);
//       } else {
//         this.txt = fullTxt.substring(0, this.txt.length + 1);
//       }
  
//       this.el.innerHTML = `<span class="wrap">${this.txt}</span>`;
  
//       let delta = 300 - Math.random() * 100;
  
//       if (this.isDeleting) {
//         delta /= 2;
//       }
  
//       if (!this.isDeleting && this.txt === fullTxt) {
//         delta = this.period;
//         this.isDeleting = true;
//       } else if (this.isDeleting && this.txt === '') {
//         this.isDeleting = false;
//         this.loopNum++;
//         delta = 500;
//       }
  
//       setTimeout(this.tick, delta);
//     };
//   }
  
//   window.onload = () => {
//     const elements = document.getElementsByClassName('txt-rotate');
//     for (let i = 0; i < elements.length; i++) {
//       const toRotate = elements[i].getAttribute('data-rotate');
//       const period = elements[i].getAttribute('data-period');
//       if (toRotate) {
//         new TxtRotate(elements[i], JSON.parse(toRotate), period);
//       }
//     }
  
//     // INJECT CSS
//     const css = document.createElement('style');
//     css.type = 'text/css';
//     css.innerHTML = '.txt-rotate > .wrap { border-right: 0.08em solid #666; }';
//     document.body.appendChild(css);
//   };
  


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
  
  
  init()
  