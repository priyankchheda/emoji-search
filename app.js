
fetch('emoji_codepoint.json')
  .then(response => response.json())
  .then(data => {
    const ul = document.querySelector('#emoji_list');
    const codepoints = Object.values(data);
    codepoints.forEach(codepoint => {
      const li = document.createElement('li');
      li.classList = 'emojicode popup';
      li.innerHTML = `${codepoint}<span class="popuptext"></span>`;
      ul.appendChild(li)
    });
  });

document.querySelector('#emoji_list').addEventListener('click', (e) => {
  var text = e.target.textContent;
  navigator.clipboard.writeText(text).then(function () {
    e.target.children[0].classList.add('fade');
    setTimeout(() => e.target.children[0].classList.remove('fade'), 1000)
  }, function (err) {
    console.error('Async: Could not copy text: ', err);
  });
});
