const themeToggle = document.querySelector('#theme-toggle');
const html = document.documentElement;

const savedTheme = localStorage.getItem('theme') || 'light';

html.dataset.theme = savedTheme;
themeToggle.checked = savedTheme === 'dark';

themeToggle.addEventListener('change', () => {
  const theme = themeToggle.checked ? 'dark' : 'light';

  html.dataset.theme = theme;
  localStorage.setItem('theme', theme);
});
