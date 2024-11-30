document.addEventListener('DOMContentLoaded', () => {
    const menuDropdown = document.querySelector('.menu-dropdown');
    const dropdownContent = menuDropdown.querySelector('.dropdown-content');

    menuDropdown.addEventListener('mouseenter', () => {
        dropdownContent.style.display = 'block';
        setTimeout(() => {
            dropdownContent.classList.add('show');
        }, 10);
    });

    menuDropdown.addEventListener('mouseleave', () => {
        dropdownContent.classList.remove('show');
        setTimeout(() => {
            dropdownContent.style.display = 'none';
        }, 300);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const mainMenu = document.querySelector('.main-menu > ul');
    const menuItems = document.querySelectorAll('.main-menu > ul > li');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            menuToggle.classList.toggle('active');
            mainMenu.classList.toggle('active');
        });
    }

    menuItems.forEach(item => {
        item.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                // Если это пункт с выпадающим меню
                if (item.querySelector('.dropdown-content')) {
                    e.preventDefault();
                    // Закрываем все другие открытые меню
                    menuItems.forEach(otherItem => {
                        if (otherItem !== item) {
                            otherItem.classList.remove('active');
                        }
                    });
                    // Переключаем текущее меню
                    item.classList.toggle('active');
                }
            }
        });
    });

    // Закрытие меню при клике вне его
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 768) {
            if (!e.target.closest('.main-menu')) {
                menuItems.forEach(item => {
                    item.classList.remove('active');
                });
                if (menuToggle) {
                    menuToggle.classList.remove('active');
                }
                if (mainMenu) {
                    mainMenu.classList.remove('active');
                }
            }
        }
    });

    // Обработка изменения размера окна
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            menuItems.forEach(item => {
                item.classList.remove('active');
            });
            if (menuToggle) {
                menuToggle.classList.remove('active');
            }
            if (mainMenu) {
                mainMenu.classList.remove('active');
            }
        }
    });
});
