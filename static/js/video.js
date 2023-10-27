let watchBtns = document.querySelectorAll('.watch-btn');

watchBtns.forEach(function(btn) {
  btn.addEventListener('click', function(e) {
    e.preventDefault();
    let videoURL = this.getAttribute("href");

    let video = document.getElementById("video");
    video.removeAttribute("poster");
    let source = document.querySelectorAll("#video_player video source");
    source[0].src = videoURL;

    video.load();
    video.play();
  });
});
