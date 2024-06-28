document.addEventListener("DOMContentLoaded", function() {
    var sections = document.querySelectorAll('.md-nav__item--nested');
  
    sections.forEach(function(section) {
        var header = section.querySelector('.md-nav__link');
        var subItems = section.querySelector('.md-nav__drop');
  
        if (header && subItems) {
            // Initially hide the sub-items
            subItems.style.display = 'none';
  
            // Toggle the display on header click
            header.addEventListener('click', function(event) {
                event.preventDefault();
                if (subItems.style.display === 'none') {
                    subItems.style.display = 'block';
                } else {
                    subItems.style.display = 'none';
                }
            });
        }
    });
  });
  