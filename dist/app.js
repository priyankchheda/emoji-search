let emojiCodepoints;
fetch('emoji_codepoints.json')
  .then(response => response.json())
  .then(data => {
    emojiCodepoints = data;
    drawUl(emojiCodepoints);
  });

const emojiInput = document.querySelector('#emojiInput');
emojiInput.addEventListener('keyup', (e) => {
  e.preventDefault();
  refresh(emojiInput.value);
});

function refresh(searchText) {
  let results = {};
  const emojiDescriptions = Object.keys(emojiCodepoints);
  emojiDescriptions.forEach((emojiDescription) => {
    if (fuzzySearch(emojiDescription, searchText)) {
      results[emojiDescription] = emojiCodepoints[emojiDescription];
    }
  });
  drawUl(results);
}

function fuzzySearch(emojiDescription, searchText) {
  var searchText = searchText.replace(/\ /g, '').toLowerCase();
  var tokens = [];
  var searchPosition = 0;

  for (var n = 0; n < emojiDescription.length; n++) {
    var textChar = emojiDescription[n];
    if (searchPosition < searchText.length &&
      textChar.toLowerCase() == searchText[searchPosition]) {
      searchPosition += 1;
    }
    tokens.push(textChar);
  }
  if (searchPosition != searchText.length) {
    return '';
  }
  return tokens.join('');
}

function drawUl(codepoints) {
  const ul = document.querySelector('#emojiList');
  ul.innerHTML = '';
  Object.keys(codepoints).forEach(codepoint => {
    const li = document.createElement('li');
    li.setAttribute('title', codepoint);
    li.classList = 'emojicode popup';
    li.innerHTML = `${codepoints[codepoint]}<span class="popuptext"></span>`;
    ul.appendChild(li);
  });
}

document.querySelector('#emojiList').addEventListener('click', (e) => {
  var text = e.target.textContent;
  navigator.clipboard.writeText(text).then(function () {
    e.target.children[0].classList.add('fade');
    setTimeout(() => e.target.children[0].classList.remove('fade'), 1000)
  }, function (err) {
    console.error('Async: Could not copy text: ', err);
  });
});