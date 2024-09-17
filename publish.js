/*
 * Google analytics
 */
const script1 = document.createElement('script');
script1.async = true;
script1.src = 'https://www.googletagmanager.com/gtag/js?id=G-B4K0W89D88';

const script2 = document.createElement('script');
script2.textContent = `
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-B4K0W89D88');
`;

document.body.appendChild(script1);
document.body.appendChild(script2);

/*
 * Accent Color
 */
// #5e8d59
document.body.style.setProperty('--accent-h', '114', "important");
document.body.style.setProperty('--accent-s', '23%', "important");
document.body.style.setProperty('--accent-l', '45%', "important");

/*
 * Resize SVG
 */
const attempt = (selector, loop, max_wait, sleep, success) => {
    var i = 0;
    var interval = setInterval(() => { i++;
        var elements = document.querySelectorAll(selector);
        if (elements.length == 0 && i < max_wait/sleep) return;
        
        clearInterval(interval);
        if (success) success()

        elements.forEach(loop);

    }, sleep);
}

let resizing = false;
const autoResize = () => {
    if (resizing) return;
    resizing = true;
    attempt('img[src*="excalidraw"]', element => {
        const alt = element.getAttribute('alt');
        var pieces = alt.split('|');

        for (const piece of pieces) {
            if (isNaN(piece)) continue; // not a number

            const width = Number(piece);
            element.setAttribute('width', width);
            break;
        }
    }, 2000, 10, () => {resizing = false});
}

attempt('.tree-item', element =>
    element.addEventListener('click', autoResize)
, 1000, 5);
autoResize();
