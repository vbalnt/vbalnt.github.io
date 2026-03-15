// Collapsible code blocks - show first 5 lines with expand button
(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var LINE_HEIGHT = 1.5; // em
    var MAX_LINES = 5;
    var MIN_LINES_TO_COLLAPSE = 8; // only collapse if more than this many lines

    var highlights = document.querySelectorAll('.highlight');

    highlights.forEach(function(highlight) {
      var code = highlight.querySelector('code');
      if (!code) return;

      var lines = code.textContent.split('\n').length;
      if (lines <= MIN_LINES_TO_COLLAPSE) return;

      // Wrap in container
      var wrapper = document.createElement('div');
      wrapper.className = 'code-wrapper collapsed';
      highlight.parentNode.insertBefore(wrapper, highlight);
      wrapper.appendChild(highlight);

      // Add expand button
      var btn = document.createElement('button');
      btn.className = 'code-expand-btn';
      btn.textContent = '+ show ' + (lines - MAX_LINES) + ' more lines';
      wrapper.appendChild(btn);

      btn.addEventListener('click', function() {
        if (wrapper.classList.contains('collapsed')) {
          wrapper.classList.remove('collapsed');
          btn.textContent = '- collapse';
        } else {
          wrapper.classList.add('collapsed');
          btn.textContent = '+ show ' + (lines - MAX_LINES) + ' more lines';
          // Scroll to top of code block so user doesn't get lost
          wrapper.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      });
    });
  });
})();
