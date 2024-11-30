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
