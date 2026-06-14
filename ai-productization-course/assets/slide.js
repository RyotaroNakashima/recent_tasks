(function () {
  const slides = Array.from(document.querySelectorAll('.slide'));
  let current = Number(window.location.hash.replace('#', '')) || 0;

  function show(index) {
    if (!slides.length) return;
    current = Math.max(0, Math.min(index, slides.length - 1));

    slides.forEach((slide, slideIndex) => {
      slide.classList.toggle('active', slideIndex === current);
    });

    const fill = document.querySelector('.bar span');
    const count = document.querySelector('#count');
    if (fill) fill.style.width = `${((current + 1) / slides.length) * 100}%`;
    if (count) count.textContent = `${current + 1} / ${slides.length}`;

    window.history.replaceState(null, '', `#${current}`);
    window.scrollTo(0, 0);
  }

  document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' || event.key === 'PageDown') show(current + 1);
    if (event.key === 'ArrowLeft' || event.key === 'PageUp') show(current - 1);
  });

  document.querySelectorAll('[data-next]').forEach((button) => {
    button.addEventListener('click', () => show(current + 1));
  });
  document.querySelectorAll('[data-prev]').forEach((button) => {
    button.addEventListener('click', () => show(current - 1));
  });

  show(current);
}());
