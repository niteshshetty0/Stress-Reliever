const audio = document.querySelector("#audio");
const playPauseBtn = document.querySelector("#play-pause");
const nextBtn = document.querySelector("#next");
const prevBtn = document.querySelector("#previous");
const songList = document.querySelector(".song-list");
const title = document.querySelector("#title");
const record = document.querySelector("#record");

let songArray = [];
let songIndex = 0;
let isPlaying = false;

function loadAudio() {
  audio.src = songArray[songIndex].getAttribute("data-src");
  title.innerText = songArray[songIndex].getAttribute("data-name");
  // Highlight the active song in the playlist
  const songListItems = songList.getElementsByTagName("li");
  for (let i = 0; i < songListItems.length; i++) {
    songListItems[i].classList.remove("active");
  }
  songArray[songIndex].classList.add("active");
}

function loadSongs() {
  const songs = songList.getElementsByTagName("li");
  for (let i = 0; i < songs.length; i++) {
    songArray.push(songs[i]);
  }
  loadAudio();
}

function playAudio() {
  audio.play();
  playPauseBtn.querySelector("i.fas").classList.remove("fa-play");
  playPauseBtn.querySelector("i.fas").classList.add("fa-pause");
  isPlaying = true;
  record.classList.add("record-animation");
}

function pauseAudio() {
  audio.pause();
  playPauseBtn.querySelector("i.fas").classList.remove("fa-pause");
  playPauseBtn.querySelector("i.fas").classList.add("fa-play");
  isPlaying = false;
  record.classList.remove("record-animation");
}

function playSong(index) {
  if (index >= 0 && index < songArray.length) {
    songIndex = index;
    loadAudio();
    playAudio();
  }
}

playPauseBtn.addEventListener("click", function () {
  if (isPlaying) {
    pauseAudio();
  } else {
    playAudio();
  }
});

nextBtn.addEventListener("click", function () {
  playSong(songIndex + 1);
});

prevBtn.addEventListener("click", function () {
  playSong(songIndex - 1);
});

songList.addEventListener("click", function (event) {
  const clickedSong = event.target.closest("li");
  if (clickedSong) {
    const clickedIndex = Array.from(songArray).indexOf(clickedSong);
    playSong(clickedIndex);
  }
});

audio.addEventListener("ended", function () {
  playSong(songIndex + 1);
});

loadSongs();
