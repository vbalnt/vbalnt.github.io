(function() {
  document.addEventListener('DOMContentLoaded', function() {

    // Reading progress bar (post pages only)
    var progressBar = document.querySelector('.reading-progress');
    if (progressBar) {
      window.addEventListener('scroll', function() {
        var scrollTop = window.scrollY;
        var docHeight = document.documentElement.scrollHeight - window.innerHeight;
        var progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        progressBar.style.width = progress + '%';
      }, { passive: true });
    }

  });
})();
